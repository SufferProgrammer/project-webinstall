import MySQLdb as dbOps
import getpass
import sys
import os
      
class createDatabase():
    def __init__(self):
        try:
            if self.connect() == True:
                self.databaseConfig()
                self.userConfig()
                self.tablesConfig()
                print('[*]Database config is done...')
        except (dbOps.DatabaseError) as Error:
            print('[*]Error with value ({0})...'.format(Error))
            if self.connect() == True:
                self.databaseConfig()
                self.tablesConfig()
                self.userConfig()

    def connect(self):
        try:
            username = input("Insert your's database user : ")
            password = getpass.getpass("Insert your's database password : ")
            if username == '' and password == '':
                print("at least, you can't leave username empty")
                return self.connect()
    
            elif username != '' and password == '':
                self.database = dbOps.connect(user=username, password = password)
                self.cursor = self.database.cursor()
                self.commitQuer = self.database.commit()
                return True
    
            elif username != '' and password != '':
                self.database = dbOps.connect(user=username, password = password)
                self.cursor = self.database.cursor()
                self.commitQuer = self.database.commit()
                return True
    
            else:
                print ('Please insert username and password for database !')
                return  self.connect()
        except(dbOps.MySQLError) as Error:
            print('\n[*]Error with value : ({0})...\n[*]Retrying...'.format(Error))
            return self.connect()
        
    def databaseConfig(self):
        try:
            sqlFolderPath = os.path.dirname(os.path.abspath(__file__))
            sqlFilePath = os.path.join(sqlFolderPath, 'databaseconfig-1.0.1.sql')
            sqlFileRead = open(sqlFilePath, 'r')
            sqlExecute = sqlFileRead.read()
            cur = self.cursor
            cur.execute(sqlExecute)
            self.commitQuer
            print('[*]Configuring database...')
        except (dbOps.DatabaseError, dbOps.ProgrammingError, dbOps.MySQLError, KeyboardInterrupt) as Error:
            print('[*]Error writting database configuration with value : {0}...\n[*]Try remove your database and retry again...'.format(Error))
            quest = input('\n[*]Want to retry...?? (Y/n) : ')
            if quest in ['Y','y']:
                return self.connect()
            
            elif quest in ['N','n']:
                print('[*]Exiting configuration...')
                sys.exit(0)
                
            else:
                print('[*]Please insert Y/n...!!')
                return quest
        
    def userConfig(self):
        try:
            sqlFolderPath = os.path.dirname(os.path.abspath(__file__))
            sqlFilePath = os.path.join(sqlFolderPath, 'userconfig-1.0.1.sql')
            sqlFileRead = open(sqlFilePath, 'r')
            sqlExecute = sqlFileRead.read()
            cur = self.cursor
            cur.execute(sqlExecute)
            self.commitQuer
            print('[*]Configuring database...')
        except (dbOps.DatabaseError, dbOps.ProgrammingError, dbOps.MySQLError, KeyboardInterrupt) as Error:
            print(
                '[*]Error writting database configuration with value : {0}...\n[*]Try remove your database and retry again...'.format(
                    Error))
            quest = input('\n[*]Want to retry...?? (Y/n) : ')
            if quest in ['Y', 'y']:
                return self.connect()
        
            elif quest in ['N', 'n']:
                print('[*]Exiting configuration...')
                sys.exit(0)
        
            else:
                print('[*]Please insert Y/n...!!')
                return quest
        
    def tablesConfig(self):
        try:
            sqlFolderPath = os.path.dirname(os.path.abspath(__file__))
            sqlFilePath = os.path.join(sqlFolderPath, 'tableconfig-1.0.1.sql')
            sqlFileRead = open(sqlFilePath, 'r')
            sqlExecute = sqlFileRead.read()
            cur = self.cursor
            cur.execute(sqlExecute)
            self.commitQuer
            print('[*]Configuring database...')
        except (dbOps.DatabaseError, dbOps.ProgrammingError, dbOps.MySQLError, KeyboardInterrupt) as Error:
            print(
                '[*]Error writting database configuration with value : {0}...\n[*]Try remove your database and retry again...'.format(
                    Error))
            quest = input('\n[*]Want to retry...?? (Y/n) : ')
            if quest in ['Y', 'y']:
                return self.connect()
        
            elif quest in ['N', 'n']:
                print('[*]Exiting configuration...')
                sys.exit(0)
        
            else:
                print('[*]Please insert Y/n...!!')
                return quest