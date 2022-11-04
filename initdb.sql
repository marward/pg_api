create database docker; create schema work_schema; create table work_schema.products ( id bigint, product_name text, price numeric(53, 4), is_available bool , last_update 
date ); insert into work_schema.products values (12345,'cucumber', 151.3212, true, '2022-11-04'), (54321, 'pen', 15.0300, false, '2022-11-04'); create table 
work_schema.category ( id int8, category_name text, product_id bigint ); insert into work_schema.category values (1,' vegetables', 12345), (2, 'stationery', 54321); ALTER 
DEFAULT PRIVILEGES IN SCHEMA work_schema GRANT SELECT ON TABLES TO "admin";
