# Real-Time Kafka + Airflow + BigQuery Data Pipeline

## Overview
This project demonstrates a real-time data engineering pipeline for ingesting, processing, orchestrating, and storing transaction events for analytics and anomaly detection.

The solution is designed to reflect modern cloud-native data engineering practices relevant to enterprise environments. It uses Kafka for streaming ingestion, Python for event processing, Airflow for orchestration, and a BigQuery-style warehouse layer for analytics-ready reporting.

## Business Use Case
Organizations need reliable pipelines to process high-volume event data in near real time. This project simulates an e-commerce transaction system where incoming events are streamed, validated, transformed, and loaded into analytics-ready storage for reporting and fraud detection.

## Architecture
The pipeline includes the following layers:

1. **Event Producer**
   - Simulates transaction events in real time

2. **Streaming Layer**
   - Kafka ingests event streams from the producer

3. **Processing Layer**
   - Python transforms and validates incoming events
   - Suspicious transactions are flagged using business rules

4. **Orchestration Layer**
   - Airflow coordinates scheduled processing and loading workflows

5. **Warehouse Layer**
   - Data is modeled in a BigQuery-style schema for analytics

6. **Analytics Layer**
   - SQL queries support operational reporting and anomaly analysis

## Tech Stack
- Python
- Apache Kafka
- Apache Airflow
- SQL
- BigQuery-style warehouse modeling
- Cloud-native architecture principles

## Key Features
- Real-time event ingestion
- Streaming transaction simulation
- Rule-based anomaly detection
- Airflow orchestration
- Warehouse-ready SQL transformations
- Analytics-focused schema design

## Project Structure
```text
docs/       -> Architecture and project documentation
python/     -> Event producer and stream processing scripts
airflow/    -> Example DAG for orchestration
sql/        -> Warehouse table design and analytics queries
