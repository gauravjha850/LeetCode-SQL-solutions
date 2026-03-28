# Write your MySQL query statement below
select s.price ,s.year  ,pr.product_name

from sales s 
left join product pr 
on s.product_id=pr.product_id;