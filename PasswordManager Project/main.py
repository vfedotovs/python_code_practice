#Password manager


def main():

    from authentication import authentication
    from get_choice import get_choice
    """
	Requirements:
	
	record must have 
	- record decsription field (str)
	- URL field (str)
	- username field (str)
	- Aditional notes (list of strings)

	0. App must have master pasword to be secured
		(-) set master pasword option
		(-) chose file where to save Pasoerd manager database
		(done) authenticate agenst master pass to get in app (unlock app feature)

	1. Print choises - (done)
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

    
    def create_record():
        print("Creating new record now  ..... please wait ....")
        print("New record created with success ")

    def list_records():
        print("Listing all records now ..... please wait ....")
        print("All records listed  with success ")

    ### Main driver code
    auth_result = authentication()

    if auth_result == True:
        while True:
            if get_choice() == '1':
                list_records()
            if get_choice() == '5':
                print("Exiting application from choices menu...")
                break
    if auth_result == False:
        print(
            "Exiting application failed enter valid master password 3 times ..."
        )


if __name__ == '__main__':
    main()
