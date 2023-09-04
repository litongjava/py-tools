import os
import sys


def create_structure(catelog_path):
  with open(catelog_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

  # Base path to create directories and files
  base_path = "./"
  current_dir = None  # To keep track of the current 1st level directory

  for line in lines:
    line = line.strip()
    if '.' not in line:  # It's a 1st level directory
      current_dir = os.path.join(base_path, line)
      os.makedirs(current_dir, exist_ok=True)
    else:  # It's a 2nd level file inside the 1st level directory
      file_path = os.path.join(current_dir, f"{line}.md")
      with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"# {line}")


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script_name.py path_to_catelog.txt")
    sys.exit(1)

  catelog_path = sys.argv[1]
  create_structure(catelog_path)
