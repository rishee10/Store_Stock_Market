# Store_Stock_Market

# Dockerized Stock Market Data Pipeline

This project implements a fully Dockerized data pipeline using **Apache Airflow** for orchestration and **PostgreSQL** for storage.

The pipeline automatically:
- Fetches live stock data from Alpha Vantage API
- Parses JSON response
- Stores the data in PostgreSQL
- Handles API and database errors gracefully

---

## Tech Stack
- Python
- Apache Airflow
- PostgreSQL
- Docker & Docker Compose
- Alpha Vantage API

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/rishee10/Store_Stock_Market.git
```

```
cd Store_Stock_Market
```

## API Key to .env

* STOCK_API_KEY=your_api_key_here
* DB_USER=airflow
* DB_PASSWORD=airflow
* DB_NAME=stockdb



## Start the Pipeline

```
docker-compose up --build
```

## Access Airflow UI

```
http://localhost:8080
Username: admin
Password: admin
```

#### Enable and trigger:

stock_data_pipeline


## Database Verification

```
SELECT * FROM stock_data;
```


