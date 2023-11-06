import mysql.connector

# database model
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="game_rec"
)