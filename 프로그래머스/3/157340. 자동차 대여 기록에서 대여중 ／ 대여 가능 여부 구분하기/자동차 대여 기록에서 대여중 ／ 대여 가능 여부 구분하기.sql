-- 코드를 입력하세요
SELECT CAR_ID,
        
        
        CASE
        
        
        WHEN 
        CAR_ID IN ( SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                   WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE
)
        THEN '대여중'
        ELSE '대여 가능'
     END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC


# -- 코드를 입력하세요
# SELECT car_id,
# case
# when car_id in (
# select car_id from car_rental_company_rental_history
#     where '2022-10-16' BETWEEN start_date and end_date ) then '대여중'
#     else '대여 가능'
#     END "AVAILABILITY"
# from car_rental_company_rental_history
# GROUP BY CAR_ID
# ORDER BY CAR_ID DESC