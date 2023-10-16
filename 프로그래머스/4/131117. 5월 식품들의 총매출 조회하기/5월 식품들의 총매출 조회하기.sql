SELECT P.product_id, P.product_name, sum(amount*price) as total_sales
FROM FOOD_ORDER O
LEFT JOIN FOOD_PRODUCT P ON O.product_id = P.product_id
WHERE PRODUCE_DATE LIKE '%2022-05%' AND price IS NOT NULL
GROUP BY product_id
ORDER BY total_sales desc, product_id asc;