def validate_event(event):
    required_fields = [
        "event_time",
        "user_id",
        "product",
        "payment_method",
        "amount",
        "currency",
        "location"
    ]
    return all(field in event for field in required_fields)

def flag_anomaly(event):
    if event["amount"] > 1800:
        event["is_flagged"] = True
        event["flag_reason"] = "high_value_transaction"
    else:
        event["is_flagged"] = False
        event["flag_reason"] = None
    return event

def transform_event(event):
    event["product"] = event["product"].lower()
    event["location"] = event["location"].title()
    return event

def process_event(event):
    if not validate_event(event):
        raise ValueError("Invalid event payload")
    event = transform_event(event)
    event = flag_anomaly(event)
    return event
