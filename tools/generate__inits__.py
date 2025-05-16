"""
generate_inits_.py 🛠️

Walks through project and ensures every Python module folder has __init__.py
Required for proper imports, packaging, and modular integrity.
"""

import os

EXCLUDE_DIRS = {'.git', '__pycache__', '.venv', 'node_modules', 'logs', 'data'}

def should_ignore(dir_name):
    return dir_name in EXCLUDE_DIRS or dir_name.startswith('.')

def create_init_file(folder):
    init_path = os.path.join(folder, '__init__.py')
    if not os.path.exists(init_path):
        with open(init_path, 'w') as f:
            f.write("# Auto-generated for Python module recognition\n")
        print(f"[+] Created: {init_path}")

def walk_and_generate_inits(base_path="."):
    for root, dirs, files in os.walk(base_path):
        dirs[:] = [d for d in dirs if not should_ignore(d)]
        if "__init__.py" not in files:
            create_init_file(root)

if __name__ == "__main__":
    print("🔧 Generating __init__.py files across project...")
    walk_and_generate_inits()
    print("✅ Done.")
