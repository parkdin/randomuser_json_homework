from from_json import read_json
def get_users(data:dict)->list:
    """Gets a list of users from the data

    Args:
        data (dict): The data from the JSON file

    Returns:
        list: A list of users
    """
    # Get the list of users
    list_user = []
    user = data["users"]
    for i in user:
        list_user.append(i)
    return list_user


data = read_json("users.json")
print(get_users(data))