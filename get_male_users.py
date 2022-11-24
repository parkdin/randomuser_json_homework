from from_json import read_json
def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    m_user = []
    user = data["users"]
    for i in user:
        if i["gender"] == "male":
            m_user.append(i)
    return m_user
data = read_json("users.json")
print(get_male_users(data))