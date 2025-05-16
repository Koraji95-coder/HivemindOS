"""
version_bump.py 🛠️
────────────────────────────────────────────
Auto-bumps version, builds changelog, stages commit, and tags release.
"""

import os
import subprocess
from pathlib import Path

VERSION_FILE = Path("shared/meta/version.py")
CHANGELOG = Path("CHANGELOG.md")

def get_current_version():
    lines = VERSION_FILE.read_text().splitlines()
    for line in lines:
        if line.startswith("__version__"):
            return line.split("=")[1].strip().strip('"')
    raise ValueError("❌ __version__ not found in version.py")


def bump_version(ver: str, level: str) -> str:
    major, minor, patch = map(int, ver.split("."))
    if level == "patch":
        patch += 1
    elif level == "minor":
        minor += 1
        patch = 0
    elif level == "major":
        major += 1
        minor = 0
        patch = 0
    return f"{major}.{minor}.{patch}"

def update_version_file(new_ver: str):
    VERSION_FILE.write_text(f'__version__ = "{new_ver}"\n')

def get_git_changes():
    untracked = subprocess.getoutput("git ls-files --others --exclude-standard").splitlines()
    modified = subprocess.getoutput("git diff --name-only").splitlines()
    return untracked, modified

def git_add_all():
    os.system("git add .")

def git_commit_and_tag(version: str, comment: str):
    os.system(f'git commit -m "🚀 v{version} – {comment}"')
    os.system(f"git tag v{version}")

def update_changelog(version: str, comment: str, untracked, modified):
    header = f"## 🚀 v{version} – {comment}\n"
    body = "\n### 🆕 New Files\n" + "\n".join(f"- {f}" for f in untracked or ["(None)"])
    body += "\n\n### 🔧 Modified Files\n" + "\n".join(f"- {f}" for f in modified or ["(None)"])
    body += "\n\n---\n"

    if CHANGELOG.exists():
        existing = CHANGELOG.read_text(encoding="utf-8")
    else:
        existing = ""

    CHANGELOG.write_text(header + body + existing, encoding="utf-8")


def run():
    print("🛠️  Version Bumper for HivemindOS")
    current = get_current_version()
    print(f"Current version: {current}")

    level = input("Bump level (patch / minor / major)? ").strip().lower()
    assert level in ["patch", "minor", "major"], "Invalid bump level."

    comment = input("What's the changelog title? (e.g. Agent Task Chaining Engine): ").strip()
    new_ver = bump_version(current, level)

    update_version_file(new_ver)
    untracked, modified = get_git_changes()
    update_changelog(new_ver, comment, untracked, modified)
    git_add_all()
    git_commit_and_tag(new_ver, comment)

    print(f"\n✅ Project bumped to v{new_ver} and committed.\n📝 Remember to:")
    print(f"   git push origin main && git push origin v{new_ver}")

if __name__ == "__main__":
    run()
