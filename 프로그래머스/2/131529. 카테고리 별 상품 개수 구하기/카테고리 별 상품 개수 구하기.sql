-- 코드를 입력하세요
SELECT SUBSTR(product_code,1,2) AS CODE, COUNT(*)
FROM PRODUCT
GROUP BY CODE
ORDER BY CODE ;