with email_rank as (select id,
                           DENSE_RANK() over (PARTITION BY email order by id) as rank
                    from Person)
delete
from Person
where id in (select id
             from email_rank
             where email_rank.rank > 1)
