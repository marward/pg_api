select * from work_schema.products p 
left join work_schema.category c on p.id = c.product_id;

