SELECT
    location,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_revenue,
    SUM(CASE WHEN is_flagged THEN 1 ELSE 0 END) AS flagged_transactions
FROM analytics.fact_transactions
GROUP BY location
ORDER BY total_revenue DESC;
