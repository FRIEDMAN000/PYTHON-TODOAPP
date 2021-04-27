import mysql.connector




class User:

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def sign_in(self):
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='5326Lionel@99',
                                       database='TODO_LIST')
        select = "SELECT user_name,password FROM User WHERE user_name = %s AND password = %s "
        mycursor = mydb.cursor()
        mycursor.execute(select, (self.username, self.password))
        data = mycursor.fetchone()
        if data:
            print('welcome', self.username)
            return True
        else:
            print('wrong credentials')
            return False




    def sign_up(self):
        email =  input('Email: ')
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='5326Lionel@99',
                                       database='TODO_LIST')
        insert_data = "Insert into User(user_name,password,email) values(%s,%s,%s)"
        mycursor = mydb.cursor()
        mycursor.execute(insert_data,(self.username,self.password,email))
        mydb.commit()
        return True

class Todo_List:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_todo_list(self,todo_list):
        print('date format  year-month-day')
        print('time format hours-min-sec')
        date = input('Enter the date of your Todo List:  ')
        time = input('Enter the time of your Todo List:  ')
        date_time = date + ' ' + time
        mydb = mysql.connector.connect(host = 'localhost',
                                       user = 'root',
                                       passwd = '5326Lionel@99',
                                       database ='TODO_LIST'

        )
        insert_data = "Insert into Todo_List(todo_list_name,user_name,reminder_date) values(%s,%s,%s)"
        mycusor = mydb.cursor()
        mycusor.execute(insert_data,(todo_list,self.username,date_time))
        mydb.commit()

    def delete_todo_List(self,todo_list):
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='5326Lionel@99',
                                       database='TODO_LIST'
                                       )
        remove_data = "DELETE FROM TODO_LIST WHERE todo_list_name = %s"
        mycusor = mydb.cursor()
        mycusor.execute(remove_data, (todo_list,))
        mydb.commit()

    def update_statut(self,todo_list):
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='5326Lionel@99',
                                       database='TODO_LIST'

                                       )
        insert_data = "Update todo_list SET status = Done WHERE todo_list_name = %s "

        mycusor = mydb.cursor()
        mycusor.execute(insert_data, (todo_list,))
        mydb.commit()

    def view_todo_List(self,array):

        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='5326Lionel@99',
                                       database='TODO_LIST')
        select ="SELECT todo_list_name FROM Todo_List WHERE user_name = %s"
        mycursor = mydb.cursor()
        mycursor.execute(select,(self.username,))
        data = mycursor.fetchall()
        if data:
            a = 1
            for row in data:
                print(str(a) + ')   '+ row[0])
                a = a + 1
                array.append(row[0])







class Todo:
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def add_todo(self,todo):

        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='5326Lionel@99',
                                       database='TODO_LIST'

                                       )
        insert_data = "Insert into Todo(todo_list_name,todo_name) values(%s,%s)"
        mycusor = mydb.cursor()
        mycusor.execute(insert_data, (self.todo_list,todo))
        mydb.commit()

    def delete_todo(self,todo_name):
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='5326Lionel@99',
                                       database='TODO_LIST'

                                       )
        remove_data = "DELETE FROM Todo WHERE todo_name = %s"
        mycusor = mydb.cursor()
        mycusor.execute(remove_data, (todo_name,))
        mydb.commit()

    def view_todo(self,array):

        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='5326Lionel@99',
                                       database='TODO_LIST')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT todo_name FROM Todo")
        data = mycursor.fetchall()
        a = 1
        for row in data:
            print(str(a) + ')   ' + row[0])
            a = a + 1
            array.append(row[0])

def intro(is_online):

    if is_online == False:
        print('1)   SIGN_UP', '\n')
        print('2)   SIGN_IN', '\n')
        print('\n')
    else:
        print("------------------------------SELECT OPTION------------------------------", '\n')
        print("----------------------------OPTION 98 TO DELETE A TODO_LIST OR A TODO ------------------------------")
        print("----------------------------OPTION 99 TO CREATE A TODO_LIST OR A TODO ------------------------------")