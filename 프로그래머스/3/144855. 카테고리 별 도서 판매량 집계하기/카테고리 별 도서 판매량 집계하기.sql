-- 코드를 입력하세요
SELECT category, sum(sales)
FROM book_sales s, book b
WHERE s.book_id = b.book_id
AND sales_date like '2022-01%'
GROUP BY category
ORDER BY category asc
