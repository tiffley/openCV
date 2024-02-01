-- combine all data and drop data which can identify individual
SELECT
 organization_name
 , organization_level
 , survey_name
 , submit_date
 , question_1
 , question_2
 , question_x ...
FROM org_comp a
JOIN survey_comp b
ON a.employee_id = b.employee_id