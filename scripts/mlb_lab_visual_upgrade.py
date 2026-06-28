from pathlib import Path

p = Path("scripts/mlb_lab_runner.py")
s = p.read_text()

# ==========================================================
# NUMBERS SAFE COLORS
# ==========================================================

replacements = {
    "fgColor=\"0D2137\"": "fgColor=\"1F4E79\"",
    "fgColor=\"111827\"": "fgColor=\"1F4E79\"",
    "fgColor=\"0F172A\"": "fgColor=\"1F4E79\"",
    "fgColor=\"000000\"": "fgColor=\"1F4E79\"",
}

for old,new in replacements.items():
    s = s.replace(old,new)

# ==========================================================
# REMOVE DARK BODY FILLS
# ==========================================================

s = s.replace(
    'BODY_FILL = PatternFill("solid", fgColor="1F2937")',
    'BODY_FILL = PatternFill("solid", fgColor="FFFFFF")'
)

s = s.replace(
    'ALT_FILL = PatternFill("solid", fgColor="111827")',
    'ALT_FILL = PatternFill("solid", fgColor="F5F7FA")'
)

# ==========================================================
# REMOVE BLUE TRIANGLES
# ==========================================================

s = s.replace(
    'cell.number_format = "0.000"',
    '''
try:
    cell.value = float(cell.value)
except:
    pass
cell.number_format = "0.000"
'''
)

# ==========================================================
# BETTER GAME FLOW HEADER
# ==========================================================

if "GAME SUMMARY" not in s:
    s += '''

# visual hierarchy marker
GAME_FLOW = [
    "GAME SUMMARY",
    "TOP PLAYS",
    "MATCHUPS",
    "PITCHER ARSENAL",
    "BULLPEN",
    "DETAILS"
]
'''

# ==========================================================
# COMMAND CENTER WIDTHS
# ==========================================================

if "preferred_widths" in s:

    start = s.find("preferred_widths")
    end = s.find("for c in range", start)

    if start > 0 and end > start:
        s = (
            s[:start]
            +
'''
preferred = {
    "Rank":7,
    "Player":22,
    "Team":18,
    "Game":34,
    "Opp SP":20,
    "Best Market":16,
    "Score":10,
    "Tier":8,
    "Why":40,
    "Risk":28
}
'''
            +
            s[end:]
        )

p.write_text(s)

print("✅ workbook visual upgrade applied")
