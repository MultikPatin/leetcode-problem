with summary as (select account, sum(amount) as balance
                 from Transactions
                 group by account)
select u.name, s.balance
from summary as s
         join Users as u on u.account = s.account
where s.balance > 10000