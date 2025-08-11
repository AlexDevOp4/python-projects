def format_kwargs(**details):
    name = details.get("name")
    age = details.get("age")
    location = details.get("location")

    return f"Hi I am {name}, I am {age} years old, and I live in {location}"
