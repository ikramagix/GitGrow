# duplicates.py
#!/usr/bin/env python3
import sys
import pathlib
from datetime import datetime

def clean_usernames():
    base_dir = pathlib.Path(__file__).parents[1]

    if base_dir.joinpath(".git") not in base_dir.glob(".git"):
        sys.exit(f"Error: Please run the script from the project root directory.")

    username_path = base_dir / "config" / "usernames.txt"
    log_dir       = base_dir / "logs" / "cleaner"
    log_dir.mkdir(parents=True, exist_ok=True)

    if not username_path.exists():
        sys.exit(f"Error: usernames file not found at {username_path}")

    # Read all lines, strip and ignore blanks
    lines    = [l.strip() for l in username_path.read_text().splitlines() if l.strip()]
    seen     = set()
    unique   = []
    duplicates = []

    # Identify duplicates (case-insensitive)
    for name in lines:
        lower = name.lower()
        if lower in seen:
            duplicates.append(name)
        else:
            seen.add(lower)
            unique.append(name)

    if duplicates:
        # Log duplicates
        ts        = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        dup_file  = log_dir / f"duplicates-{ts}.txt"
        with dup_file.open("w") as f:
            for d in duplicates:
                f.write(d + "\n")
        print(f"[INFO] Logged {len(duplicates)} duplicates to {dup_file}")

        # Rewrite usernames.txt without the extras
        username_path.write_text("\n".join(unique) + "\n")
        print(f"[INFO] Removed {len(duplicates)} duplicates; {len(unique)} remain.")
    else:
        print("[INFO] No duplicates found.")

if __name__ == "__main__":
    clean_usernames()