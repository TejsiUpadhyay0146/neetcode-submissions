-- Write your query below
select name from sales_person where sales_id not in (select sales_id from orders where com_id=1 group by sales_id, com_id);