#!/usr/bin/env python3
"""
schema_audit.py - Phase 0A: Schema Validation for MLB-LAB

This script adapts to the actual pybaseball version installed.
It dynamically discovers the correct schedule function and validates
all data structures needed for Phase 0.
"""

import sys
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import pybaseball

# Safer import: avoid direct import of potentially missing attributes
from pybaseball import statcast, cache

# Get version safely
pybb_version = getattr(pybaseball, "__version__", "unknown")

# Enable caching
cache.enable()

# ------------------------------------------------------------------
# DYNAMICALLY DISCOVER THE SCHEDULE FUNCTION
# ------------------------------------------------------------------
def get_schedule_function():
    """
    Attempt to find the correct schedule function in pybaseball.
    Prefers: schedule -> schedules -> schedule_and_record.
    """
    candidates = ['schedule', 'schedules', 'schedule_and_record']
    for name in candidates:
        if hasattr(pybaseball, name):
            func = getattr(pybaseball, name)
            print(f"Using schedule function: {name}")
            return func
    raise ImportError("No schedule function found in pybaseball. Available: " + 
                      ", ".join([f for f in dir(pybaseball) if not f.startswith('_')]))

schedule = get_schedule_function()

# ------------------------------------------------------------------
# SETUP TEST DATE
# ------------------------------------------------------------------
# Use yesterday, or fallback to a known date with games
TEST_DATE = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
FALLBACK_DATE = "2024-06-01"

def print_section(title):
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)

def safe_pull(func, date, label):
    """Attempt to pull data with error handling and fallback."""
    try:
        print(f"Pulling {label} for {date}...")
        df = func(start_dt=date, end_dt=date)
        if df.empty:
            print(f"WARNING: {label} returned empty for {date}, trying fallback {FALLBACK_DATE}")
            df = func(start_dt=FALLBACK_DATE, end_dt=FALLBACK_DATE)
        return df
    except Exception as e:
        print(f"ERROR pulling {label}: {e}")
        print("Trying fallback date...")
        try:
            df = func(start_dt=FALLBACK_DATE, end_dt=FALLBACK_DATE)
            return df
        except Exception as e2:
            print(f"Fallback also failed: {e2}")
            return pd.DataFrame()

def main():
    print_section("SCHEMA AUDIT: MLB-LAB PHASE 0A")
    print(f"pybaseball version: {pybb_version}")
    print(f"Available functions in pybaseball (sample):")
    available = [f for f in dir(pybaseball) if not f.startswith('_') and callable(getattr(pybaseball, f))]
    print("  " + ", ".join(available[:20]) + (" ..." if len(available) > 20 else ""))

    # 1. Pull Statcast
    sc = safe_pull(statcast, TEST_DATE, "Statcast")
    if sc.empty:
        print("ERROR: No Statcast data could be pulled. Exiting.")
        sys.exit(1)
    print(f"Statcast rows: {len(sc)}")

    # 2. Pull Schedule using the discovered function
    # Note: schedule functions may have different signatures (e.g., 'start_dt', 'start_date').
    # We'll try to call with 'start_dt' and fallback to 'start_date'.
    try:
        sched = schedule(start_dt=TEST_DATE, end_dt=TEST_DATE)
        if sched.empty:
            sched = schedule(start_dt=FALLBACK_DATE, end_dt=FALLBACK_DATE)
    except TypeError as e:
        print(f"TypeError with start_dt, trying 'start_date'...")
        try:
            sched = schedule(start_date=TEST_DATE, end_date=TEST_DATE)
            if sched.empty:
                sched = schedule(start_date=FALLBACK_DATE, end_date=FALLBACK_DATE)
        except Exception as e2:
            print(f"Error: {e2}")
            sched = pd.DataFrame()
    except Exception as e:
        print(f"Error pulling schedule: {e}")
        sched = pd.DataFrame()

    print(f"Schedule rows: {len(sched)}")

    # 3. Statcast Schema
    print_section("STATCAST DATAFRAME SCHEMA")
    print(f"Columns ({len(sc.columns)}):")
    for col in sc.columns:
        print(f"  {col}: {sc[col].dtype}")
    print("\nFirst 3 rows (selected columns):")
    sample_cols = ['game_date', 'batter', 'pitcher', 'home_team', 'away_team',
                   'events', 'description', 'woba_value', 'xwoba', 'iso',
                   'barrel', 'hard_hit', 'runs_scored', 'rbi']
    available_sample = [c for c in sample_cols if c in sc.columns]
    print(sc[available_sample].head(3).to_string())

    # 4. Verify required Statcast columns
    required_statcast = ['game_date', 'batter', 'pitcher', 'home_team', 'away_team',
                         'events', 'description', 'woba_value', 'xwoba', 'iso',
                         'barrel', 'hard_hit', 'runs_scored', 'rbi']
    missing_statcast = [c for c in required_statcast if c not in sc.columns]
    if missing_statcast:
        print(f"\nWARNING: Missing Statcast columns: {missing_statcast}")
    else:
        print("\nAll required Statcast columns are present.")

    # 5. Check barrel/hard_hit types
    for col in ['barrel', 'hard_hit']:
        if col in sc.columns:
            print(f"\n{col} dtype: {sc[col].dtype}")
            print(f"  Unique values: {sc[col].unique()[:10]}")
            try:
                numeric_vals = pd.to_numeric(sc[col], errors='coerce')
                print(f"  Numeric conversion: {numeric_vals.dtype}, non-null count: {numeric_vals.notna().sum()}")
            except:
                print("  Could not convert to numeric.")

    # 6. Schedule Schema (if available)
    if not sched.empty:
        print_section("SCHEDULE DATAFRAME SCHEMA")
        print(f"Columns ({len(sched.columns)}):")
        for col in sched.columns:
            print(f"  {col}: {sched[col].dtype}")
        print("\nFirst 3 rows:")
        print(sched.head(3).to_string())

        # Check for typical outcome columns
        outcome_candidates = ['home_score', 'home_runs', 'away_score', 'away_runs']
        found = [c for c in outcome_candidates if c in sched.columns]
        if found:
            print(f"\nFound outcome columns: {found}")
        else:
            print("\nWARNING: No obvious outcome columns found. Check schedule structure.")
    else:
        print_section("SCHEDULE DATA NOT AVAILABLE")
        print("Skipping schedule validation.")

    # 7. Memory usage
    print_section("MEMORY USAGE ESTIMATES")
    mem_sc = sc.memory_usage(deep=True).sum() / (1024 * 1024)
    mem_sched = sched.memory_usage(deep=True).sum() / (1024 * 1024) if not sched.empty else 0
    print(f"Statcast DataFrame: {mem_sc:.2f} MB")
    if not sched.empty:
        print(f"Schedule DataFrame: {mem_sched:.2f} MB")
    print(f"Total: {mem_sc + mem_sched:.2f} MB")

    # 8. Sample player data
    print_section("SAMPLE PLAYER RECORDS")
    if not sc.empty:
        sample_batter = sc['batter'].iloc[0]
        sample_pitcher = sc['pitcher'].iloc[0]
        print(f"Sample batter ID: {sample_batter}")
        print(f"Sample pitcher ID: {sample_pitcher}")
        batter_data = sc[sc['batter'] == sample_batter]
        if not batter_data.empty:
            print("\nSample batter game stats (first 5 rows):")
            cols = ['game_date', 'events', 'woba_value', 'xwoba', 'iso', 'barrel', 'hard_hit']
            available = [c for c in cols if c in batter_data.columns]
            print(batter_data[available].head(5).to_string())

    # 9. Final summary
    print_section("AUDIT SUMMARY")
    issues = []
    if missing_statcast:
        issues.append(f"Missing Statcast columns: {missing_statcast}")
    if sched.empty:
        issues.append("Schedule data could not be pulled. This may affect game-level validation.")
    else:
        # Check for outcome columns
        if not any(c in sched.columns for c in outcome_candidates):
            issues.append("No home/away score columns found in schedule.")

    if issues:
        print("ISSUES FOUND:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nPlease resolve these before proceeding with Phase 0 implementation.")
        sys.exit(1)
    else:
        print("All core schema checks passed. Ready to proceed with Phase 0.")
        print("Note: If schedule columns differ, adjust column names in the backtest script.")

if __name__ == "__main__":
    main()
