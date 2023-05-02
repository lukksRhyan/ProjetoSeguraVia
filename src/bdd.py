import mysql.connector
class Conexao:
  def __init__(self):
    self.conectado = False

  def innitConection(self):
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="Rhyan",
      password="lucasdo2",
      database = "seguravia"
    )
    self.conectado = True
  