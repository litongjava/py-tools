
package org.psyduck.constants;

import java.util.LinkedHashMap;
import java.util.Map;

public class TableNames {

  public static Map<String, String> tableNameMap = new LinkedHashMap<>();
  static {
    tableNameMap.put("cf_dxf", "gz_cf_dxf");
    tableNameMap.put("gz_alarm_rule", "gz_gz_alarm_rule");
    tableNameMap.put("gz_berth", "gz_gz_berth");
    tableNameMap.put("gz_berthing_record", "gz_gz_berthing_record");
    tableNameMap.put("gz_camera", "gz_gz_camera");
    tableNameMap.put("gz_camera_copy1", "gz_gz_camera_copy1");
    tableNameMap.put("gz_dat", "gz_gz_dat");
    tableNameMap.put("gz_dat_base", "gz_gz_dat_base");
    tableNameMap.put("gz_impact_record", "gz_gz_impact_record");
    tableNameMap.put("gz_impact_shift", "gz_gz_impact_shift");
    tableNameMap.put("gz_plan", "gz_gz_plan");
    tableNameMap.put("gz_recoder_video", "gz_gz_recoder_video");
    tableNameMap.put("gz_rule", "gz_gz_rule");
    tableNameMap.put("gz_sensor_data", "gz_gz_sensor_data");
    tableNameMap.put("gz_sensor_result", "gz_gz_sensor_result");
    tableNameMap.put("gz_sensor_result_copy1", "gz_gz_sensor_result_copy1");
    tableNameMap.put("gz_ship", "gz_gz_ship");
    tableNameMap.put("gz_test_record", "gz_gz_test_record");
    tableNameMap.put("gz_wharf", "gz_gz_wharf");
    tableNameMap.put("gz_wharf_point", "gz_gz_wharf_point");
    tableNameMap.put("magic_api_file", "gz_magic_api_file");
    tableNameMap.put("pdman_db_version", "gz_pdman_db_version");
    tableNameMap.put("sys_dict", "gz_sys_dict");
    tableNameMap.put("sys_dict_items", "gz_sys_dict_items");
    tableNameMap.put("sys_file", "gz_sys_file");
    tableNameMap.put("sys_menu", "gz_sys_menu");
    tableNameMap.put("sys_office", "gz_sys_office");
    tableNameMap.put("sys_oper_log", "gz_sys_oper_log");
    tableNameMap.put("sys_permission_code", "gz_sys_permission_code");
    tableNameMap.put("sys_role", "gz_sys_role");
    tableNameMap.put("sys_role_menu", "gz_sys_role_menu");
    tableNameMap.put("sys_user", "gz_sys_user");
    tableNameMap.put("sys_user_code", "gz_sys_user_code");
    tableNameMap.put("sys_user_office", "gz_sys_user_office");
    tableNameMap.put("sys_user_role", "gz_sys_user_role");
    tableNameMap.put("t_alarm", "gz_t_alarm");
    tableNameMap.put("t_enclosure", "gz_t_enclosure");
  }

  public static String getTableName(String f) {
    return tableNameMap.get(f);
  }

  public static String[] getF() {
    return tableNameMap.keySet().toArray(new String[0]);
  }
}
