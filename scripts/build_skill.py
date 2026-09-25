"""Package the indicator-design/ folder into indicator-design.skill (a zip archive).

Run from the repository root:  python scripts/build_skill.py
"""

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "indicator-design"
OUTPUT = ROOT / "indicator-design.skill"


def main() -> None:
    files = sorted(p for p in SKILL_DIR.rglob("*") if p.is_file())
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, path.relative_to(ROOT).as_posix())
    print(f"Wrote {OUTPUT.name} ({len(files)} files)")


if __name__ == "__main__":
    main()
