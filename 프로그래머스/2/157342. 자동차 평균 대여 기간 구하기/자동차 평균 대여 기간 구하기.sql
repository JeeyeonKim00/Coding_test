SELECT car_id, round(avg(DATEDIFF(end_date, start_date)+1),1) AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY car_id
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, car_id DESC;