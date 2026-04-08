create database sales_db;
use sales_db;

create table sales(Row_ID int primary key,
Order_ID varchar(20),
Order_Date date,
Ship_Date date,
Ship_Mode varchar(50),
Customer_ID varchar(20),
Customer_Name varchar(100),
Segment varchar(50),
Country varchar(50),
City varchar(50),
State varchar(50),
Postal_Code varchar(50),
Region varchar(50),
Product_ID varchar(50),
Category varchar(50),
Sub_Category varchar(50),
Product_Name varchar(260),
Sales decimal(10,2));

# Total Sales #
select sum(sales) as Total_Sales from sales;

# Sales By Region #
select region, sum(sales) as Revenue from sales
group by region
order by revenue desc;

# Top 10 Products #
select product_name, sum(sales) as Revenue from sales
group by product_name
order by Revenue desc
limit 10;

# Monthly Sales Trend #
select date_format(order_date,'%Y-%m') as month,
sum(sales) as revenue from sales
group by month
order by month;

# Top Customers #
select customer_name,sum(sales) as Total_Spent from sales
group by customer_name
order by Total_spent desc
limit 10;

select * from sales;


