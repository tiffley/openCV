SELECT
  name,
  list,
  CASE WHEN FIND_IN_SET('1', list) > 0 THEN 1 ELSE 0 END AS col_1,
  CASE WHEN FIND_IN_SET('2', list) > 0 THEN 1 ELSE 0 END AS col_2,
  CASE WHEN FIND_IN_SET('3', list) > 0 THEN 1 ELSE 0 END AS col_3,
  CASE WHEN FIND_IN_SET('4', list) > 0 THEN 1 ELSE 0 END AS col_4,
  CASE WHEN FIND_IN_SET('5', list) > 0 THEN 1 ELSE 0 END AS col_5
FROM combined_table