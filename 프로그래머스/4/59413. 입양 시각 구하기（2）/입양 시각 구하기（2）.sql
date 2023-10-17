WITH RECURSIVE TB AS 
        (SELECT 0 AS NUM
         UNION ALL
        SELECT NUM+1 FROM TB
        WHERE NUM+1 <24)


SELECT NUM, IFNULL(CNT, 0) AS CNT_2
FROM (SELECT HOUR(DATETIME) AS H, COUNT(*) CNT
    FROM ANIMAL_OUTS
    GROUP BY H) A
RIGHT JOIN TB B ON A.H = B.NUM
ORDER BY NUM ASC
;