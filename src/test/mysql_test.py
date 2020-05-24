
import mysql.connector
print("begin")
db = mysql.connector.connect(host="localhost", user="root", passwd="@Dengppx123456")
cursor = db.cursor()


cursor.execute("select 111")


r = cursor.fetchone()
db.close()
print(r)
print("end")


