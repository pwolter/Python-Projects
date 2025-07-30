import os
import sys


def create_file(path, content=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main(project_name):
    # Define structure
    root = f"{os.environ['HOME']}/Projects"
    package_dir = os.path.join(root, project_name)
    tests_dir = os.path.join(package_dir, "tests")

    # Create directories
    os.makedirs(package_dir, exist_ok=True)
    os.makedirs(tests_dir, exist_ok=True)

    # Create files in package directory
    create_file(os.path.join(package_dir, "__init__.py"))

    # You can choose either setup.py or pyproject.toml, here is both:
    create_file(
        os.path.join(package_dir, "setup.py"),
        f"""from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="0.1.0",
    packages=find_packages(),
)
""",
    )

    print(f"Project structure for '{project_name}' created successfully.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_project.py <project_name>")
        sys.exit(1)
    main(sys.argv[1])
