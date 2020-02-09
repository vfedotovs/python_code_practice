#Password manager

class Record:
    def __init__(self, descr, username, url, notes):
        self.descr = descr
        self.username = username
        self.url = url
        self.notes = notes


    def create_record(self):
        """
        collects info from user stdin 
        return record obect
        """
        print("How many records you need to create?: ")
        rlist = []
        rec_count = int(input())
        for i in range(rec_count):
            
            descr = str(input("Description : "))
            username = str(input("Username : "))
            url = str(input("URL : "))
            notes = str(input("Notes : "))
            rlist.append(i(descr,username,url,notes))
        return rlist
    

    #def iterate_over_records(self, obj_list):
    #    for object in obj_list:
    #        print(object)

class Record_list:
    def __init__(self):
        alist = [] 


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
        #print("New record created with success ")
        return Record.create_record(self)


    def list_records(olist):
        print("Listing all records now ..... please wait ....")
        #print("All records listed  with success ")
        #Record.iterate_over_records(olist)

    ### Main driver code
    message()
    auth_result = authentication()
    new_list = Record_list()

    alist = []
    if auth_result == True:
        while True:
            if get_choice() == '1':
                list_records(alist)
            if get_choice() == '2':
                alist  = create_record()
            if get_choice() == '5':
                print("Exiting application from choices menu...")
                break
    if auth_result == False:
        print(
            "Exiting application failed enter valid master password 3 times ..."
        )


if __name__ == '__main__':
    main()
