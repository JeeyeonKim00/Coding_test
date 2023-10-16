-- 코드를 입력하세요
select CATEGORY,	price,	PRODUCT_NAME
from (SELECT * , rank() over(partition by category order by price desc) as r
        from FOOD_PRODUCT
        where category IN ('과자','국','김치','식용유')) A 
where r = 1
order by price desc;