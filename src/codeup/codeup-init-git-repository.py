import os
import subprocess


def init_git_repository(base_path):
  listdir = os.listdir(base_path)
  commands = [
    "cp /root/.gitignore .",
    "git init",
    "git add .",
    "git add .gitignore",
    'git commit -am "import codeup init"'
  ]

  for dir in listdir:
    dir_path = os.path.join(base_path, dir)
    if os.path.isdir(dir_path):  # check if it's a directory
      os.chdir(dir_path)  # change the current working directory
      for cmd in commands:
        try:
          subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
          print(f"Error executing command '{cmd}' in directory {dir_path}. Error: {e}")

      print(dir, "git inited")


directory_to_scan = r"/root/workspace/repo/projects"
init_git_repository(directory_to_scan)
