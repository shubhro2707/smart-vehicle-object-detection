import os

# Define folder structure
folders = [
    "data",
    "notebooks",
    "src",
    "models",
    "outputs"
]

# Create base folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty script files in src
src_files = [
    "src/preprocessing.py",
    "src/classical_ml.py",
    "src/object_detection.py",
    "src/utils.py"
]

for file in src_files:
    with open(file, 'w') as f:
        f.write("# " + os.path.basename(file).replace(".py", "").replace("_", " ").title() + "\n")

# Create top-level files
for file in ["requirements.txt", "README.md", "Dockerfile"]:
    open(file, 'a').close()

print("✅ Project structure created successfully.")
