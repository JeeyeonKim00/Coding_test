-- 코드를 입력하세요
SELECT HOUR(DATETIME) as hour, count(*) as cnt
FROM ANIMAL_OUTS
GROUP BY hour
HAVING hour between 9 and 20
ORDER BY hour;