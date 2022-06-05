import mysql.connector

class Banco:
  mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="aps_agrosafe",
    user="python",
    password="123456",
    auth_plugin='mysql_native_password'
  )

  cursor = mydb.cursor()
  
  def getCursor(self, ):
      return self.cursor

  def commit(self, ):
    self.mydb.commit()
