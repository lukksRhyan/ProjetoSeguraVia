from dataclasses import dataclass
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="kani",
  password="lucasdo2",
  database = "acidentes"
)