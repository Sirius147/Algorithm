with count_by_car_id as (
    select
        car_id CAR_ID,
        count(*) RECORDS
    from
        car_rental_company_rental_history
    where
        start_date >= '2022-08-01'
        and start_date <= '2022-10-31'
    group by
        car_id
)

select
    month(h.start_date) MONTH,
    h.car_id CAR_ID,
    count(*) RECORDS
from
    car_rental_company_rental_history h
    join count_by_car_id c
        on h.car_id = c.car_id
where
    c.records >= 5
    and start_date >= '2022-08-01'
    and start_date <= '2022-10-31'
group by
    month, car_id
order by
    month asc, car_id desc;
  