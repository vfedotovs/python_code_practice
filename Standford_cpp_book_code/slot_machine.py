"""
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
import random


def main():
	

	def get_user_input():
		print(" Would you like play (y)es or (n)o ? ", end ="" )
		x  = str(input())
		if x == "n":
			return False
		else:
			return True
			

	def generate_spin():
		A = []
		for i in range(3):
			num = random.randrange(0, 5, 1)
			A.append(num)
		return A


	def print_spin(A:list):

		display_list = []
		fruits_dict = {0: 'CHERRY', 1: 'LEMON', 2: 'ORANGE',3: 'PLUM',4:'BELL',5:'BAR'} 
		for number in A:			
			for k, v in fruits_dict.items():
				if number == k:
					display_list.append(v)
		return display_list


	def chek_for_win(A:list):
		my_win = 0
		if A[0] == 5 and  A[1] == 5 and  A[2] == 5:
			my_win = 250
		if A[0] == 0 and  A[1] == 0 and A[2] == 0:
			my_win = 7
		if A[0] == 0 and  A[1] == 0 and A[2] != 0:
			my_win = 5
		if A[0] == 0:
			my_win = 2
		if A[0] == 2 and  A[1] == 2 and A[2] == 2:
			my_win = 10
		if A[0] == 3 and  A[1] == 3 and A[2] == 3:
			my_win = 14
		if A[0] == 4 and  A[1] == 4 and A[2] == 4:
			my_win = 20
		if A[0] == 4 and  A[1] == 4 and A[2] == 5:
			my_win = 20
		if A[0] == 3 and  A[1] == 3 and A[2] == 5:
			my_win = 14
		if A[0] == 2 and  A[1] == 2 and A[2] == 5:
			my_win = 10
		if my_win != None:
			return my_win
		else:
			return 0 


	answer = ""
	balance = 50 
	
	while balance > 0:
		print("Your balance is: $", balance)
		if  get_user_input() == False:
			break
		spin_list = generate_spin()
		#print(spin_list)
		print(print_spin(spin_list))
		win = chek_for_win(spin_list)
		if win > 0:
			print(" --- You have won $",win," ---")
		else:
			print(" --- You loose ---")
		balance = balance - 1 + win 


if __name__ == '__main__':
	main()
