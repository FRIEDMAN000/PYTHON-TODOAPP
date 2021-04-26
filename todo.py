import mysql.connector
import os



class User:

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def sign_in(self):
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='5326Lionel@99',
                                       database='TODO_LIST')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT user_name,password FROM User")
        data = mycursor.fetchall()
        for row in data:
            if row[0] == self.username:
                if row[1] == self.password:
                    print('welcom',self.username)
                    return True
                else:
                    print("wrong password")
                    return False
            else:
                print("wrong username")
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
        mycursor = mydb.cursor()
        mycursor.execute("SELECT todo_list_name FROM Todo_List")
        data = mycursor.fetchall()
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
        print("------------------------------OPTION 0 IS TO GO BACK------------------------------", '\n')
        print("----------------------------OPTION 98 TO DELETE A TODO_LIST OR A TODO ------------------------------")
        print("----------------------------OPTION 99 TO CREATE A TODO_LIST OR A TODO ------------------------------")


array = ['0']
array2 = ['0']
username =''
password = ''
todo_list = ''


if __name__ == '__main__':

    is_online = False
    intro(is_online)
    SELECTION = int(input('Please Choose\n'))
    while True:
        if SELECTION == 1:
            username = input("Username: ")
            password = input("Password: ")
            user1 = User(username, password)
            is_online = user1.sign_up()
            SELECTION = 2 if is_online else 1
            continue
        if SELECTION == 2:
            os.system('clear')
            username = input("Username: ")
            password = input("Password: ")
            user = User(username, password)
            user.sign_in()
            is_online = True
            SELECTION = 3
            continue

        if SELECTION == 3:
            os.system('clear')
            intro(is_online)
            print('\n', '\n', '\n', '\n', '\n')
            print("                               These are your TODO LIST")
            todo_list = Todo_List(username,password)
            todo_list.view_todo_List(array)

            print('\n', '\n')
            SELECTION = int(input('ENTER:   '))
            intro(is_online)
            print('\n', '\n', '\n', '\n', '\n')
            print("                               This are your TODO")
            a = 0
            for row in array:
                if SELECTION == array.index(row):
                    todo = Todo(row)
                    intro(12)
                    todo.view_todo(array2)

                    SELECT = int(input('Enter:   '))
                    print('\n', '\n', '\n', '\n', '\n')
                    if SELECT == 98:
                        array2 = ['0']
                        os.system('clear')
                        print("----------------------------SELECT TO DELETE A TODO ------------------------------")
                        todo.view_todo(array2)
                        print('\n', '\n', '\n', '\n', '\n')

                        SELECTION = int(input('Enter:   '))
                        for row in array2:
                            print(array2.index(row))

                            if SELECTION == array2.index(row):
                                print(row)
                                print('y')
                                todo.delete_todo(row)
                                print('z')
                                SELECTION = 3
                                break
                    if SELECT == 99:
                        os.system('clear')
                        print("----------------------------ADD A TODO ------------------------------")
                        print('\n', '\n', '\n', '\n', '\n')
                        SELECTION = input('Enter:   ')
                        todo.add_todo(SELECTION)
                        SELECTION = 3

        if SELECTION == 98:
            os.system('clear')
            print("----------------------------SELECT TO DELETE A TODO LIST------------------------------")
            todo_list.view_todo_List(array)
            print('\n', '\n', '\n', '\n', '\n')
            SELECTION = input('Enter:   ')
            for row in array:
                if SELECTION == array.index(row):
                    todo_list.delete_todo_List(row)
                    SELECTION = 3


        if SELECTION == 99:
            os.system('clear')
            print("----------------------------ADD A TODO  LIST------------------------------")
            print('\n', '\n', '\n', '\n', '\n')
            SELECTION = input('Enter:   ')
            todo_list.create_todo_list(SELECTION)
            SELECTION = 3


