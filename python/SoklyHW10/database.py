import mysql.connector
from prettytable import PrettyTable
mydb = mysql.connector.connect(
  host="LOCAL",
  user="root",
  password="1234",
  port="8889"
)

mycursor = mydb.cursor()
sql_query = "select * from customer_tbl"
mycursor.execute(sql_query)

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

  
 