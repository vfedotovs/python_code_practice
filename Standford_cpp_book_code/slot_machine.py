import random

s = """
  RULES:
  BAR BAR BAR pays $250
  BELL BELL BELL/BAR pays $20
  PLUM PLUM PLUM/BAR pays $14
  ORANGE ORANGE ORANGE/BAR pays $10
  CHERRY CHERRY CHERRY pays $7
  CHERRY CHERRY — pays $5
  CHERRY — — pays $2
  Each spin costs $1
  """


def get_user_input():
    x = str(input("Would you like play (y)es or (n)o ? "))
    if x == "n":
        return False
    else:
        return True


def generate_spin():
    new_list = [random.randrange(0, 5, 1) for i in range(3)]
    return new_list


def print_spin(mylist):
    fruits_dict = {0: 'CHERRY', 1: 'LEMON',
                   2: 'ORANGE', 3: 'PLUM',
                   4: 'BELL', 5: 'BAR'}
    blist = [fruits_dict[num] for num in mylist]
    return blist


def compare_lists(slist, dlist):

    match = 0
    iter_count = 0
    for idx in range(3):
        # print("debug info: loop #", idx, slist[idx], " = ", dlist[idx])
        if slist[idx] == dlist[idx]:
            match += 1
        iter_count += 1
    if match == iter_count:
        return True
    else:
        return False


def calculate_win(mylist):
    bar_list = [5, 5, 5]  # BAR BAR BAR pays $250
    bell_list1 = [4, 4, 4]  # BELL BELL BELL pays $20
    bell_list2 = [4, 4, 5]  # BELL BELL BAR pays $20
    plum_list1 = [3, 3, 3]  # PLUM PLUM PLUM pays $14
    plum_list2 = [3, 3, 5]  # PLUM PLUM BAR pays $14
    orange_list1 = [2, 2, 2]  # ORANGE ORANGE ORANGE pays $10
    orange_list2 = [2, 2, 5]  # ORANGE ORANGE BAR pays $10
    three_cherry = [0, 0, 0]  # CHERRY CHERRY CHERRY pays $7
    # two_cherry = [0, 0]  # CHERRY CHERRY - pays $5
    # one_cherry = [0]  # CHERRY - -  pays $2

    if compare_lists(mylist, bar_list):
        return 250
    if compare_lists(mylist, bell_list1):
        return 20
    if compare_lists(mylist, bell_list2):
        return 20
    if compare_lists(mylist, plum_list1):
        return 14
    if compare_lists(mylist, plum_list2):
        return 14
    if compare_lists(mylist, orange_list1):
        return 10
    if compare_lists(mylist, orange_list2):
        return 10
    if compare_lists(mylist, three_cherry):
        return 7
    if mylist[0] == 0 and mylist[1] == 0:
        return 5
    if mylist[0] == 0:
        return 2
    else:
        return 0


def main():
    balance = 50
    print(s)
    while balance > 0:
        print("Your balance is: $", balance)
        if get_user_input() is False:
            break
        spin_list = generate_spin()
        # print("debug info:", spin_list)
        print(print_spin(spin_list))
        win = calculate_win(spin_list)
        if win > 0:
            print(" --- You have won $", win, " ---")
        else:
            print(" --- You loose ---")
        balance = balance - 1 + win


if __name__ == '__main__':
    main()
