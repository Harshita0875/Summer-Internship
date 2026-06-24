# PySpark Sales Analysis using Docker

## Description

This project uses PySpark DataFrame to analyze a sales dataset. 
The application reads a CSV file, sorts products by sales, displays top 3 products, and filters products with sales greater than 80,000.

The project is executed using Docker with Java, Python, and Spark installed.

## Technologies Used

- Python
- PySpark
- Apache Spark
- Docker

## Project Structure

## Operations Performed

- Read CSV file into PySpark DataFrame
- Sort products by sales descending order
- Display top 3 highest sales products
- Filter products with sales > 80,000
- Save output as CSV file

## Docker Commands

Build image:

```bash
docker build -t pyspark-sales-analysis .
docker run pyspark-sales-analysis


#Filtered products are saved in :
output/filtered_products.csv    