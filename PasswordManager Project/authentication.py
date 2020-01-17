def passw_chek():
    """ TODO decription - seems to short function

    """
    unlock_pass = str(input(": "))
    master_pass = '1234'

    if unlock_pass == master_pass:
        return True
    else:
        return False


def authentication():
        """ Checks if STDIN pasword matches master pasword
		
        Args:
            none: TODO

        Returns:
            unlocled(bool): True or False

        Rises:
            Error: TODO		
		"""
        unlocked = False
        print("To unlock Pasword manager please enter master password: ")
        unlock_attempt_count = 3
        while unlock_attempt_count > 0:
            #print(unlock_attempt_count)  # only for debug
            if passw_chek() == True:
                unlocked = True
                break
            else:
                if unlock_attempt_count > 1:
                    print(
                        "Entered password was incorrect please try again ... ")

            unlock_attempt_count -= 1
        return unlocked