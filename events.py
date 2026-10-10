
def find_event(events, name):
   
    for event in events:
        if event["name"].lower() == name.lower():
            return event
    return None
