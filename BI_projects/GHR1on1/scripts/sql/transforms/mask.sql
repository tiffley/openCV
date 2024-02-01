SELECT
 organization_level
-- if the team is small and easy to identify individual, then mask
 , CASE
    WHEN COUNT(*) OVER (PARTITION BY organization_id) > 5 THEN organization_name
    ELSE "other"
   END as masked
-- if the org has few teams and easy to guess individual, then mask
 , CASE
    WHEN COUNT(*) OVER (PARTITION BY child_org_id) > 2 AND COUNT(*) OVER (PARTITION BY organization_id) > 5 THEN organization_name
    ELSE parent_org_id
   END as org_masked
-- other complicated calculations for business logics
 , some_other_calcs...
FROM combined_table