SELECT product_code, sum(sales_amount)*P.price as SALES
FROM offline_sale O
JOIN product P ON O.product_id = P.product_id
GROUP BY product_code
ORDER BY sales desc, product_code asc;