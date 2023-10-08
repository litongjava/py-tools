import os


def generate_directory_structure(base_path, group_name):
  formatted_strings = []

  listdir = os.listdir(base_path)

  for directory in listdir:
    formatted_strings.append(f"{base_path}/{directory},{group_name}/{directory},0")
  return formatted_strings


directory_to_scan = r"/root/workspace/repo/projects"
output = generate_directory_structure(directory_to_scan, "zentaopm_svn_old");
print("\n".join(output))
