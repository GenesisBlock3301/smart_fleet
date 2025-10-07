import os

# Define folder structure
project_structure = {
    "vehicle-service": [
        "app/api/v1/routes",
        "app/api/v1/schemas",
        "app/core",
        "app/grpc",
        "app/db",
        "app/kafka",
        "app/main.py",
        "Dockerfile",
        "requirements.txt",
        "proto"
    ],
    "trip-service": [
        "app/api/v1/routes",
        "app/api/v1/schemas",
        "app/core",
        "app/grpc",
        "app/db",
        "app/kafka",
        "app/main.py",
        "Dockerfile",
        "requirements.txt",
        "proto"
    ]
}

# Function to create directories and placeholder files
def create_structure(base_path, structure):
    for folder in structure:
        path = os.path.join(base_path, folder)
        # If path ends with .py or .txt or Dockerfile, create a file
        if folder.endswith(('.py', '.txt', 'Dockerfile')):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                f.write(f"# Placeholder for {folder}\n")
        else:
            os.makedirs(path, exist_ok=True)
            # Create placeholder __init__.py in Python folders
            if "app" in folder or "routes" in folder or "schemas" in folder or "grpc" in folder or "db" in folder or "kafka" in folder:
                init_file = os.path.join(path, "__init__.py")
                with open(init_file, 'w') as f:
                    f.write("# init\n")

# Generate structure
for service, folders in project_structure.items():
    create_structure(service, folders)

print("Folder structure created successfully!")
