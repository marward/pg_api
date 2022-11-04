--категория с продуктами 
select c.category_name, p.product_name from work_schema.category c 
left outer join work_schema.products p 
on c.product_id = p.id