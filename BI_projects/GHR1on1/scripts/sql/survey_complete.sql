SELECT * FROM SURVEY_DATA x
JOIN (
    SELECT * FROM SURVEY_RESPONSE_META_DATA a
    JOIN SURVEY_MASTER b
    ON a.survey_id = b.survey_id
) y
ON x.response_id = y.response_id