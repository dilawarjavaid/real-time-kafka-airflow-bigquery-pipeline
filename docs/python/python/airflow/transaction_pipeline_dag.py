from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def ingest_events():
    print("Ingesting streaming transaction events from Kafka topic...")

def process_events():
    print("Processing and validating streaming events...")

def load_to_bigquery():
    print("Loading curated transaction data into BigQuery-style warehouse tables...")

with DAG(
    dag_id="transaction_pipeline_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    description="Real-time transaction pipeline orchestration example"
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_events",
        python_callable=ingest_events
    )

    process_task = PythonOperator(
        task_id="process_events",
        python_callable=process_events
    )

    load_task = PythonOperator(
        task_id="load_to_bigquery",
        python_callable=load_to_bigquery
    )

    ingest_task >> process_task >> load_task
