users = {
    "user1": {"name": "Alex", "email": "alex@email.com", "status": "active"},
    "user2": {"name": "Sara", "email": "sara@email.com", "status": "inactive"},
}


def add_user():
    name = input("Input user's name: ")
    email = input("Input user's email: ")
    status = "active"

    users_info = {"name": name, "email": email, "status": status}
    key_list = list(users.keys())
    users[f"user{len(key_list) + 1}"] = users_info
    return users


def update_user():
    user_to_replace = input("Which user would you like to update? ")
    status = input("What status would you like to update the user with? ")

    for key, values in users.items():
        if values["name"].lower() == user_to_replace.lower():
            values["status"] = status

    print(users)
    return users


def handle_users():
    choice = input(
        "What would you like to do, add a new user or update a user's status? "
    )

    if "add" in choice.lower():
        return add_user()
    elif "update" in choice.lower():
        return update_user()
    else:
        return "No choice made"


print(handle_users())
