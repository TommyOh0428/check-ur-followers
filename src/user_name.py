# get current date
def get_date():
    date_string = input("what day did you download your profile details? (YYYYMMDD): ")
    return date_string

# get user name to locate correct file
def get_user_name():
    while True:
        name = input("Enter the your user name in Instagram: ")

        if name == "":
            print("You did not enter the user name, please try again")
        else:
            print(name)
            break
    return name

# return string that will be used to locate file
def string_file_location(user_name, date_string):
    file_name = user_name + "_" + date_string
    print(file_name)
    return file_name


