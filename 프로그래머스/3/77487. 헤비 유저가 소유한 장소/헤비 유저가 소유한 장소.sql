select
    ID,
    NAME,
    HOST_ID
from
    places
where
    HOST_ID in (
        select
            HOST_ID
        from
            places
        group by
            HOST_ID
        having
            count(*) >= 2
    )
order by
    ID asc