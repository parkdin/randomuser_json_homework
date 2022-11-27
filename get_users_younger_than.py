from from_json import read_json
def get_users_younger_than(data:dict, age:int)->list:
    """Gets all users younger than a certain age from the data
    Args:
        data (dict): The data from the JSON file
        age (int): The age to filter users by
    Returns:
        list: A list of users
    """
    user = data["users"]
    y_users = []
    for i in user:
        if i["age"] < age:
            y_users.append(i)
    return y_users
data = read_json("users.json")
age = 24
print(get_users_younger_than(data, age))
