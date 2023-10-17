SELECT YEAR(SALES_DATE) YEAR, MONTH(SALES_DATE) MON, GENDER, COUNT(DISTINCT(OS.user_id)) USERS
FROM ONLINE_SALE OS
JOIN USER_INFO UI ON OS.USER_ID = UI.USER_ID 
WHERE GENDER IS NOT NULL
GROUP BY 1,2,3
ORDER BY 1,2,3

# SELECT YEAR(sales_date) Y, MONTH(sales_date) M,user_id, count(*)
# FROM ONLINE_SALE
# GROUP BY 1,2,3
# ORDER BY 1,2,3
