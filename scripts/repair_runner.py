from pathlib import Path
import py_compile, re, shutil, sys

p = Path("scripts/mlb_lab_runner.py")
backup = Path("scripts/mlb_lab_runner_auto_repair_backup.py")
shutil.copy2(p, backup)

s = p.read_text()

# Fix corrupted float formatter blocks caused by pasted visual patches
patterns = [
    (
        r'(\s*)if isinstance\(val, float\):\ntry:\n\s*cell\.value = float\(cell\.value\)\nexcept:\n\s*pass\ncell\.number_format = "0\.000"',
        r'\1if isinstance(val, float):\n\1    cell.number_format = "0.000"'
    ),
    (
        r'(\s*)if h in pct_cols and isinstance\(val, \(int, float\)\):\n\s*elif h in dec_cols and isinstance\(val, \(int, float\)\):\n\s*cell\.number_format = "0\.000"',
        r'\1if h in pct_cols and isinstance(val, (int, float)):\n\1    cell.number_format = "0.0%"\n\1elif h in dec_cols and isinstance(val, (int, float)):\n\1    cell.number_format = "0.000"'
    ),
    (
        r'(\s*)elif h in dec_cols and isinstance\(val, \(int, float\)\):\ntry:\n\s*cell\.value = float\(cell\.value\)\nexcept:\n\s*pass\ncell\.number_format = "0\.000"',
        r'\1elif h in dec_cols and isinstance(val, (int, float)):\n\1    cell.number_format = "0.000"'
    ),
]

for old, new in patterns:
    s = re.sub(old, new, s)

p.write_text(s)

try:
    py_compile.compile(str(p), doraise=True)
    print("✅ compile passed")
except Exception as e:
    print("❌ compile still failing")
    print(e)
    sys.exit(1)
