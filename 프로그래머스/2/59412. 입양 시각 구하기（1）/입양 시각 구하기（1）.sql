-- 코드를 입력하세요
SELECT HOUR(DATETIME) as hour, count(*) as cnt
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) between 9 and 20
GROUP BY hour
ORDER BY hour;