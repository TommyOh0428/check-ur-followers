import json
import os
from user_name import get_user_name, string_file_location, get_date

user_name = get_user_name()
date_string = get_date()
file_name = string_file_location(user_name, date_string)

# file path to followers and following json files
def create_file_path(file_name):
    follower_file_path = os.path.join(file_name, "followers_and_following", "followers_1.json")
    following_file_path = os.path.join(file_name, "followers_and_following", "following.json")
    return follower_file_path, following_file_path

follower_file_path, following_file_path = create_file_path(file_name)
print(follower_file_path)
print(following_file_path)

# Validate if the file exists
def validate_file(file_path):
    if os.path.exists(file_path):
        print("File exists")
    else:
        print("File does not exist")

validate_file(follower_file_path)
validate_file(following_file_path)