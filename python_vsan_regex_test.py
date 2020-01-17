#!/bin/python

def main():


    import re


    #in_filename = 'hostd.all'
    #pattern  = 'error'  # pattern  = 'Migrate|VMotion'  #  matches is case sensitive and this is OR matche example
    #out_filename = 'python-out-file.txt'
 

    def find_match(word:str, logfile:str, out_file:str):
        pattern = word
        in_filename = logfile
        out_filename = out_file
        new_file = []  # Just empty list which will be populated with regex matxhes
    
        with open(in_filename, 'r') as f:
            lines = f.readlines()
    
        for line in lines:
            match = re.search(pattern, line)  # Regex applied to each line
            if match:
                new_line = match.group()
                new_file.append(line)
    
        with open(out_filename, 'w') as f:  # opening and redirecting output to out_file.txt
            f.seek(0)  # go to start of file
            f.writelines(new_file)  # actually write the lines

    # Main code driver
    #w = 'error'
    #inf = 'hostd.all'
    outf = 'python_parser_out.txt'

    find_match('error', 'hostd.all' , outf) 



if __name__ == '__main__':
    main()


# Call bash script from python 
#from subprocess import call
#rc = call("./sleep.sh")