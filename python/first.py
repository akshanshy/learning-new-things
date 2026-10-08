events = [
    {"name": "Hackathon", "price": 100},
    {"name": "AI Workshop", "price": 50},
    {"name": "Coding Contest", "price": 0}
]
price=0
for event in events:
    print(event["name"])
    if(event["price"]>50):
        print(event["name"])
    price += event["price"]
print(f"Total price of expensive events: {price}")

def find_event(name):
    for event in events:
        if event["name"] == name:
            return event
    return None
