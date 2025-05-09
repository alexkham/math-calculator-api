import os

# Load the app summary from file
from app_summary import structure, content

# Create everything from the loaded structure/content
for path, default_content in structure.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.get(path, default_content))

print("✅ Project scaffold recreated from app_summary.py")
