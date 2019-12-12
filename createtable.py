import mysql.connector
conn=mysql.connector.connect(user='root',password='***********',host='localhost',database='project')
cursor=conn.cursor()
cursor.execute("""create table attendance(id int,classes int)""")
cursor.close()
conn.close()



