import os
import sys
import json


def generate_json_structure(catelog_path):
  with open(catelog_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

  output = []
  current_item = None

  for line in lines:
    line = line.strip()
    if '.' not in line:  # It's a 1st level directory
      if current_item:
        output.append(current_item)
      current_item = {
        "title": line,
        "collapsable": False,
        "children": []
      }
    else:  # It's a 2nd level file
      current_item["children"].append(f"{current_item['title']}/{line}.md")

  # Append the last item
  if current_item:
    output.append(current_item)

  # Print the JSON structure
  print(json.dumps(output, indent=4, ensure_ascii=False))


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script_name.py path_to_catelog.txt")
    sys.exit(1)

  catelog_path = sys.argv[1]
  generate_json_structure(catelog_path)
