CREATE TABLE analytics.fact_transactions (
    event_time TIMESTAMP,
    user_id STRING,
    product STRING,
    payment_method STRING,
    amount NUMERIC,
    currency STRING,
    location STRING,
    is_flagged BOOLEAN,
    flag_reason STRING
);
