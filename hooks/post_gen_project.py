import shutil
import subprocess
import sys


NEEDED_TOOLS = [
    "git",
    "uv",
]

COMMANDS = [
    ["git", "init", "-b", "main"],
    ["git", "add", "--all"],
    ["git", "commit", "-m", "feat: initial project setup"],
    ["uv", "run", "pre-commit", "install"],
]


def main():
    for tool in NEEDED_TOOLS:
        if shutil.which(tool) is None:
            sys.stderr.write(f"[post_gen] ERROR: '{tool}' not found.\n")
            sys.exit(1)

    for cmd in COMMANDS:
        try:
            subprocess.run(cmd)
        except Exception:
            sys.stderr.write(f"[post_gen] ERROR: '{' '.join(cmd)}' failed.\n")
            sys.exit(1)


if __name__ == "__main__":
    main()
