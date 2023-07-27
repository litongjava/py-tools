print("start")
# 读取input.txt文件内容
with open('input.txt', 'r') as file:
    lines = file.readlines()

# 生成Java代码
java_code = """
package org.psyduck.constants;

import java.util.LinkedHashMap;
import java.util.Map;

public class TableNames {

  /**
   * 数据表的别名
   */
  public static Map<String, String> tableNameMap = new LinkedHashMap<>();
  static {
%s
  }

  public static String getTableName(String f) {
    return tableNameMap.get(f);
  }

  public static String[] getF() {
    return tableNameMap.keySet().toArray(new String[0]);
  }
}
"""

# 生成tableNameMap.put部分的Java代码
table_name_map_code = ""
for line in lines:
    table_name = line.strip()
    table_name_map_code += f"    tableNameMap.put(\"{table_name}\", \"gz_{table_name}\");\n"

# 合并Java代码
java_code_with_table_names = java_code % table_name_map_code

# 将生成的Java代码写入output.java文件
with open('output.java', 'w') as file:
    file.write(java_code_with_table_names)

print("Java代码已生成并写入output.java文件。")
