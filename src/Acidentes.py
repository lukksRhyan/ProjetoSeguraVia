import json
import datetime
import mysql.connector

class Local:
    def __init__(self, data: dict):
        self.uf = str(data.get("uf"))
        self.br = str(data.get("br"))
        self.km = str(data.get("km"))
        self.municipio = data.get("municipio")
         
    def __str__(self) -> str:
        return "br " + self.br + " km " + self.km + "\n" + self.municipio + " " + self.uf

def convertToISO(date: str, time: str):
    return (date + "T" + time)

class Acidente:
    def __init__(self, data: dict):
        self.local = Local(data)

        iso = convertToISO(data.get("data_inversa"), data.get("horario"))
        self.horario = datetime.datetime.fromisoformat(iso)

        self.info = data

    def __str__(self) -> str:
        return "Local: " + str(self.local) + " Hora: " + str(self.horario)

    def databaseInsert(self):
        caso = self.info

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="Rhyan",
                password="lucasdo2",
                database="seguravia"
            )

            cursor = conexao.cursor()

            colunas = ", ".join(caso.keys())
            valores = tuple(caso.values())
            placeholders = ", ".join(["%s"] * len(caso))
            sql = f"INSERT INTO Acidentes ({colunas}) VALUES ({placeholders})"

            cursor.execute(sql, valores)
            conexao.commit()

        except mysql.connector.Error as error:
            print(f"Erro ao inserir no banco de dados: {error}")

        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
