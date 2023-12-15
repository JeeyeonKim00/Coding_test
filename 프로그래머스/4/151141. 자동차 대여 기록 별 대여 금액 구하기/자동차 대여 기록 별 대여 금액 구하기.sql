# SELECT HISTORY_ID, ROUND(DAILY_FEE*DATE*coalesce(1 - (discount_rate * .01),1),0) as fee
# FROM
#         (SELECT C.CAR_TYPE, C.DAILY_FEE, H.HISTORY_ID,DATEDIFF(END_DATE, START_DATE)+1 AS DATE,
#                 CASE WHEN DATEDIFF(END_DATE, START_DATE)+1 BETWEEN 7 AND 29 
#                                                         THEN '7일 이상'
#                     WHEN DATEDIFF(END_DATE, START_DATE)+1 BETWEEN 30 AND 89 
#                                                         THEN '30일 이상'
#                     WHEN DATEDIFF(END_DATE, START_DATE)+1 >=90 
#                                                         THEN '90일 이상'    
#                     ELSE NULL
#                 END AS DURATION_TYPE
#         FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
#         JOIN CAR_RENTAL_COMPANY_CAR C
#         ON C.car_id = H.car_id) A
# JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON A.DURATION_TYPE = P.DURATION_TYPE
#                                         AND A.CAR_TYPE = P.CAR_TYPE
# WHERE A.CAR_TYPE = '트럭'
# ORDER BY FEE DESC, HISTORY_ID DESC;
Select history_id
     , round(daily_fee  * (datediff(end_date, start_date) + 1) * coalesce(1 - (discount_rate * .01),1),0) as fee

from
(SELECT h.history_id, h.car_id, c.car_type, c.daily_fee, h.end_date, h.start_date,
        case when datediff(h.end_date, h.start_date) + 1 between 7 and 29 then '7일 이상'
             when datediff(h.end_date, h.start_date) + 1 between 30 and 89 then '30일 이상'
             when datediff(h.end_date, h.start_date) + 1 >= 90 then '90일 이상'
             else null end as duration_date
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
join CAR_RENTAL_COMPANY_CAR c on c.car_id = h.car_id) a

left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p on a.car_type = p.car_type and a.duration_date = p.duration_type

where a.car_type = '트럭'

order by fee desc, history_id desc;
