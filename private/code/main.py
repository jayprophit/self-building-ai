import os

def initialize_environment(base_path):
    folders = ["code", "configs", "logs", "models"]
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
        print(f"Created folder: {folder}")

if __name__ == "__main__":
    base_path = "./private"
    initialize_environment(base_path)