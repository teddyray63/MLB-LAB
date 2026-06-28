import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.doctor.doctor import run_doctor
from backend.doctor.repair import suggest_repairs


def main():
    result = run_doctor()
    print("\n================ MLB-LAB DOCTOR ================\n")
    print(f"Database: {'found' if (ROOT / 'database' / 'mlb_lab.db').exists() else 'missing'}")

    if result.get("issues"):
        print("\nIssues:")
        for issue in result["issues"]:
            print(f"- {issue}")
    else:
        print("No issues detected.")

    if result.get("warnings"):
        print("\nWarnings:")
        for warning in result["warnings"]:
            print(f"- {warning}")

    repairs = suggest_repairs(result)
    if repairs:
        print("\nSuggested repairs:")
        for repair in repairs:
            print(f"- {repair}")


if __name__ == "__main__":
    main()
