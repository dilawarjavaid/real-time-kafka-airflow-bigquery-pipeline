# Architecture

## High-Level Design

### 1. Producer Layer
A Python-based producer simulates transaction events and sends them into the streaming pipeline.

### 2. Streaming Layer
Apache Kafka acts as the event backbone for near real-time ingestion.

### 3. Processing Layer
Python processing logic validates events, standardizes fields, and flags suspicious transactions.

### 4. Orchestration Layer
Apache Airflow manages pipeline execution and scheduling for downstream processing and warehouse loading.

### 5. Warehouse Layer
The processed data is modeled in a BigQuery-style analytics schema with fact and dimension patterns.

### 6. Analytics Layer
SQL queries provide metrics for transaction volume, customer behavior, and flagged transaction reporting.

## Cloud Mapping
This architecture can be implemented using:
- Kafka or managed streaming equivalent
- Airflow or Cloud Composer
- BigQuery or warehouse equivalent
- Cloud Storage for raw and staged data
