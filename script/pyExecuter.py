import databaseOps
import sys
import os

openterms = os.path.dirname(os.path.abspath(__file__))
term = open(os.path.join(openterms, 'disclaimer'))
termread = term.read()
print(termread)

def term():
    read = input("\nAccept ? (Y/n) : ")
    if read in ['Y', 'y']:
        databaseOps.createDatabase()
        
    elif read == 'n':
        print('disclaimer not accepted rollback installation !')
        sys.exit(0)
    else:
        print('Please input y or no')
        return term()
    
if __name__=='__main__':
    term()