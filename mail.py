import mysql.connector
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta


Email_Address = 'yourmail'
Email_Password = 'password'
username = ''
email = ''
todo_name = ''

mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='password',
                                       database='database-name')
mycursor = mydb.cursor()
mycursor.execute("SELECT User.user_name,User.email,Todo_List.todo_list_name,Todo_List.reminder_date FROM User INNER JOIN Todo_List ON User.user_name = Todo_List. user_name")
data = mycursor.fetchall()
for row in data:
    username = row[0]
    email = row[1]
    todo_name = row[2]
    date = row[3]

    actual_date = datetime.now()
    date = date - timedelta(hours=24)
    if actual_date >= date:
        Email_Address = str(Email_Address)
        Email_Password = str(Email_Password)
        msg = EmailMessage()
        msg['Subject'] = 'Reminder!!'
        msg['From'] = Email_Address
        msg['To'] = 'sender mail'
        msg.set_content('Hello ' + username + ' in 2hours time you are supposed to finish your list ' + todo_name )

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(Email_Address,Email_Password)
            smtp.send_message(msg)









