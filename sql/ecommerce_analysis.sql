create database if not exists ecommerce_sales;
use ecommerce_sales;
show tables;
select * from ecommerce_sales_project_dataset;

 select sum(sales)as Total_sales from ecommerce_sales_project_dataset;
 select sum(profit)as Total_profit from ecommerce_sales_project_dataset;
select count(distinct order_id)as Total_Orders from ecommerce_sales_project_dataset;
select category,sum(sales) as Total_Sales from ecommerce_sales_project_dataset 
group by category 
order by Total_Sales desc;
select category,sum(profit) as Total_Profit  from ecommerce_sales_project_dataset 
group by category 
order by Total_Profit  desc;
select region ,sum(sales) as Total_Sales  from ecommerce_sales_project_dataset 
group by region
order by Total_Sales  desc;
select city ,sum(sales) as Total_Sales  from ecommerce_sales_project_dataset 
group by city
order by Total_Sales  desc;
SELECT YEAR(order_date) AS YEAR,
 MONTH(order_date) AS MONTH,
SUM(sales) AS Total_Sales  FROM ecommerce_sales_project_dataset 
group BY YEAR(order_date), MONTH(order_date)
ORDER BY YEAR , MONTH;
