select
    count(*) FISH_COUNT,
    max(f.LENGTH) MAX_LENGTH,
    f.FISH_TYPE
from
    (select 
        ID,
        FISH_TYPE,
        case
            when LENGTH is null then 10
            when LENGTH <= 10 then 10
            else LENGTH
        end as LENGTH,
        TIME
     from
        FISH_INFO) as f
group by
    FISH_TYPE
having
    avg(LENGTH) >= 33
order by
    FISH_TYPE asc