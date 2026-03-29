# Write your MySQL query statement below
select c.customer_id ,count(*) as count_no_trans

from Visits c
left join Transactions k
on c.visit_id= k.visit_id
where k.transaction_id is null
group by c.customer_id;
