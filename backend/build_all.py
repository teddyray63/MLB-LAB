import subprocess
import sys

steps = [
    "backend/collectors/warehouse.py",
    "backend/collectors/statcast_hitters.py",
    "backend/features/build_hitter_features.py",
    "backend/features/build_daily_scores.py",
]

for step in steps:
    print(f"\n🚀 RUNNING: {step}")
    result = subprocess.run([sys.executable, step])

    if result.returncode != 0:
        print(f"\n❌ FAILED at: {step}")
        sys.exit(result.returncode)

print("\n✅ ALL DATA BUILT SUCCESSFULLY")
print("Now run: streamlit run frontend/app.py")