import MySQLdb as dbOps
import os
      
class createDatabase():
    def __init__(self):
        self.connect()
        self.cursor = self.database.cursor()
        # self.userConfig()
        self.tablesConfig()
    
    def connect(self):
        user = input("Insert your's database user : ")
        password = input("Insert your's database password : ")

        if user == '' and password == '':
            print("at least, you can't leave username empty")
            return self.connect()

        elif user != '' and password == '':
            self.database = dbOps.connect()

        elif user != '' and password != '':
            self.database = dbOps.connect(user=user, host='localhost', password = password)

        else:
            print ('Please insert username and password for database !')
            return  self.connect()
        
    def userConfig(self):
        sqlFolderPath = os.path.dirname(os.path.abspath(__file__))
        sqlFilePath = os.path.join(sqlFolderPath, 'userconfig-1.0.1.sql')
        sqlFileRead = open(sqlFilePath, 'r')
        sqlExecute = sqlFileRead.read()
        self.cursor.execute(sqlExecute)
        self.database.commit()
        
    def tablesConfig(self):
        sqlFolderPath = os.path.dirname(os.path.abspath(__file__))
        sqlFilePath = os.path.join(sqlFolderPath, 'tableconfig-1.0.1.sql')
        sqlFileRead = open(sqlFilePath, 'r')
        sqlExecute = sqlFileRead.read()
        self.cursor.execute(sqlExecute)
        self.database.commit()