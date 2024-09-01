def build_message(**info):
    message_parts = []
    
    for key, value in info.items():
        message_parts.append(f"{key.capitalize()}: {value}")
    
    message = ', '.join(message_parts)
    
    return message

message = build_message(name="Laiba", age=18, city="Karachi", occupation="Machine learning Eng")
print(message)
