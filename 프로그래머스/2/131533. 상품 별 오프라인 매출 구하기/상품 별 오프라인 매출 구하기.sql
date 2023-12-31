# SELECT p.product_code, SUM(S.sales_amount)*P.price AS SUMANT
# FROM OFFLINE_SALE S
# JOIN PRODUCT P ON S.product_id = P.product_id
# GROUP BY S.product_id
# ORDER BY 2 DESC, 1 ASC;

SELECT product_code, SALES
FROM (
    SELECT P.product_code, SUM(S.sales_amount * P.price) AS SALES
    FROM OFFLINE_SALE S
    JOIN PRODUCT P ON S.product_id = P.product_id
    GROUP BY S.product_id
) AS SalesData
ORDER BY SALES DESC, product_code ASC;
