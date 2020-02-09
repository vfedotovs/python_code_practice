
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
    

    def iterate_over_records(self, obj_list):
        for object in obj_list:
            print(object)




            

    

    
"""
	record must have 
	- record decsription field (str)
	- URL field (str)
	- username field (str)
	- Aditional notes (list of strings)
"""