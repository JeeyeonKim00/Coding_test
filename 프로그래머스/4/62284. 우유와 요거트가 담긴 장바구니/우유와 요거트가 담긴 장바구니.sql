-- 코드를 입력하세요
# SELECT DISTINCT(CART_ID)
# FROM (SELECT CART_ID, COUNT(*) as cnt
#         FROM CART_PRODUCTS
#         WHERE NAME IN ('Yogurt','Milk')
#         GROUP BY CART_ID
#         HAVING cnt>=2) A
# ORDER BY CART_ID
select cart_id
from (select cart_id, name
     from cart_products
     where name in ('Yogurt', 'Milk')
     group by cart_id,name)
     a
group by cart_id
having count(cart_id)>=2
order by cart_id;