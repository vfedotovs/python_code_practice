def get_choice():
    """ TODO decription 
    
    """
    chices_list = ['1', '2', '5']
    print("Please choose option :")
    print(" ### MENU ### ")
    print("1. List all records")
    print("2. Crete new record") 
    print("5. Exit application")

    while True:
        choice = str(input(":"))
        if choice in chices_list:
            break
        else:
             print("Please enter valid choice")
        return choice