# 🛒 Product Price Aggregator

A simple Flask web app that helps users compare product prices across Amazon, Flipkart, and eBay. Built with Python and Docker.

## 🚀 Features

- Search for popular products
- View price listings from different websites
- Dockerized and easy to run

## 🔧 Tech Stack

- Python 3
- Flask
- Docker
- HTML & CSS (basic)

## 🐳 Run with Docker

```bash
docker build -t product-aggregator .
docker run -p 5000:5000 product-aggregator

#Using docker compose run 
docker-compose up --build

