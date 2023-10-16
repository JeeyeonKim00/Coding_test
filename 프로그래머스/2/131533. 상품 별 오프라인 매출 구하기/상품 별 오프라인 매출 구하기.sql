SELECT product_code, P.price*O.sales as sales
FROM product p
JOIN (SELECT product_id, sum(sales_amount) as sales
        FROM OFFLINE_SALE
        GROUP BY product_id) O
ON p.product_id = O.product_id
ORDER BY sales desc, product_code asc;