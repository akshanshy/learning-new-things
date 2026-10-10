from events import find_event

events=[
    {"name": "Hackathon", "price": 100},
    {"name": "AI Workshop", "price": 50},
    {"name": "Coding Contest", "price": 0}
]

# filter events by price 

def filter_events_by_price(max_price):
    filtered_events = []
    for event in events:
        if event["price"] <=max_price:
            filtered_events.append(event)
    return filtered_events

# Exercise 3: Calculate total
def calculate_total():
    total = 0
    for event in events:
        total += event["price"]
    return total

# Exercise 4: handle invalid input
def safe_str_to_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"Invalid input: {value}. Please enter a valid integer.")
        return None

if __name__ == "__main__":
    print(filter_events_by_price(50))
    print()

    print("--- 2 & 5. Find Event (Case-Insensitive) ---")
    # Testing match
    print("Finding 'ai workshop':", find_event(events, "ai workshop"))
    # Testing no match
    print("Finding 'Web Dev':", find_event(events, "Web Dev"))
    print() 

    print("--- 3. Calculate Total ---")
    print(f"Total cost of all events: ${calculate_total()}")
    print()

    print("--- 4. Handle Invalid Input ---")
    print("Converting '123':", safe_str_to_int("123"))
    print("Converting 'abc':", safe_str_to_int("abc"))
