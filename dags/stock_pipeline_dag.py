from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append("/opt/airflow/scripts")

from scripts.fetch_and_store import fetch_and_store

default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id="stock_data_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    fetch_store_task = PythonOperator(
        task_id="fetch_and_store_stock_data",
        python_callable=fetch_and_store
    )

    fetch_store_task
