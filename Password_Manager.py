#Password manager

def main():
	
	"""
	Requirements:
	
	record must have 
	- record decsription field (str)
	- URL field (str)
	- username field (str)
	- Aditional notes (list of strings)

	0. App must have master pasword to be secured
	1. Print choises
	2. List all records
	3. Crete new record
	4. Update existing record
	5. Delete record
	6. Encrypt records that they are not plain text
	7. Save records to file (backup)
	8. Load records from file (restore)
	9. Website GUI

	""" 
	def message():
		print("**********************")
		print("Password Manager v1.0 ")
		print("**********************\n")

	def passw_chek():
		unlock_pass = str(input(": "))		
		master_pass = '1234'

		# Testing if unlock password matches
		if unlock_pass == master_pass:
			return True
		else:
			return False


	def authentication():
		"""
		Description of function:
		if master pasword authentuication is passed
		returns True else False
		"""
		message()
	
		unlocked = False
		print("To unlock Pasword manager please enter master password: ")
		unlock_attempt_count = 3
		while unlock_attempt_count > 0:
			print(unlock_attempt_count)  # only for debug		
			if passw_chek() == True:
				unlocked = True
				break
			else:
				if unlock_attempt_count > 1:
					print("Entered password was incorrect please try again ... ")
					
			unlock_attempt_count -= 1
		return unlocked

	def print_choises():
		message()
		chices_list = ['1','2','5']
		print("Please choose option :")
		print("""			
			1. List all records
			2. Crete new record 
			5. Exit app	""")
		while True:
			choice = str(input(":"))
			if choice in chices_list:
				break
			else:
				print("Please enter valid choice")
		return choice		



	def create_record():
		pass


	def list_records():
		pass


	### Main driver code

	if authentication() == True:
		while True:
			if print_choises() == '1':
				list_records()
			if print_choises() == '5':
				print("Exiting application from choices menu...")
				break
	if authentication() == False:
		print("Exiting application failed enter valid master password 3 times ...")
		 


if __name__ == '__main__':
    main()
