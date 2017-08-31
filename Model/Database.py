import mysql.connector

'''
the model we'll use for this class methods would be like this :

model = [
    ['username', Database.VARCHAR + "(50)"],
    ['password', Database.INTEGER]
]

'''


class Database:
    __username = None
    __password = None
    __dbname = None
    __host = '127.0.0.1'

    __cnx = None

    '''
    types used in sql
    '''
    INTEGER = "INTEGER"
    VARCHAR = "VARCHAR"
    BOOLEAN = "BOOLEAN"
    # TODO complete this!

    def __init__(self, username, password, dbname):
        self.__username = username
        self.__password = password
        self.__dbname = dbname

    def connect_db(self):
        try:
            self.__cnx = mysql.connector.connect(user=self.__username, password= self.__password, host=self.__host,
                                          database=self.__dbname)
        except mysql.connector.Error as err:
            print("couldn't connect to database : %s" % self.__dbname)

    def close_db(self):
        self.__cnx.close()

    def create_table(self, table_name, model):
        # creating the query!
        query = "CREATE TABLE " + table_name + " ("

        for i in range(0, len(model)):
            query = query + model[i][0] + " " + model[i][1] + ","

        # removing the last character
        query = query[:-1]

        query += ");"

        # executing the query!
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        cursor.close()

    def find(self):
        pass

    def insert(self):
        pass
