import random
import json
import time
from datetime import datetime

users = ["user_101", "user_102", "user_103", "user_104"]
products = ["laptop", "phone", "tablet", "headphones"]
payment_methods = ["credit_card", "paypal", "apple_pay"]

def generate_event():
    return {
        "event_time": datetime.utcnow().isoformat(),
        "user_id": random.choice(users),
        "product": random.choice(products),
        "payment_method": random.choice(payment_methods),
        "amount": random.randint(50, 2500),
        "currency": "CAD",
        "location": random.choice(["Toronto", "Mississauga", "Ottawa", "Montreal"])
    }

if __name__ == "__main__":
    for _ in range(10):
        event = generate_event()
        print(json.dumps(event))
        time.sleep(1)
