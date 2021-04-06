import sqlite3
from datetime import date

# Criando a classe BlocoNotas
class BlocoNotas(object):
  #Criando o banco de dados que vai receber a tabela de notas
  def __init__(self, databaseName, tableName):
    self.databaseName = databaseName
    self.tableName = tableName
  
  # Conectando ao banco de dados que vai receber as notas criadas
  # Criando a tabela que vai receber as notas do BlocoNotas
  def createDatabaseSchema(self):
    conn = sqlite3.connect(self.databaseName)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tableName} (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,note_text TEXT NOT NULL,criado_em DATE NOT NULL, tags TEXT);")

  # Gerando a data em que a nota foi escrita
  def getCurrentDate(self):
    today = date.today()
    return today.strftime("%d-%m-%y")
  
  # Função que cria a nota escrita pelo usuário
  def createNote(self, note, tags=""):
    criadoEm = self.getCurrentDate()
    conn = sqlite3.connect(self.databaseName)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {self.tableName} (note_text, tags, criado_em) VALUES ('{note}', '{tags}', '{criadoEm}')")
    conn.commit()
    conn.close()
    print("Nota criada com sucesso! -> Abra o menu, visualizar notas, para velá")

  # Função que faz uma busca no banco as notas pelas tags
  def searchNotes(self, tags=""):
    conn = sqlite3.connect(self.databaseName)
    cursor = conn.cursor()
    if tags != "":
        cursor.execute(f"SELECT * FROM {self.tableName} WHERE tags LIKE '%{tags}%';")
    else:
        cursor.execute(f"SELECT * FROM {self.tableName};")

    for note in cursor.fetchall():
        print(note)
         
    conn.close()
  
  # Função que faz uma busca no banco as notas pelo ID da nota
  def searchNotesByID(self, noteId):
    conn = sqlite3.connect(self.databaseName)
    conn = sqlite3.connect(self.databaseName)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {self.tableName} WHERE id = {noteId};")

    if cursor.fetchone() is None:
      return False
    else:
      return True

    conn.close()
  
  # Função que pode moficar o ID, as Tags e o texto das notas
  def modifyNote(self, noteId, noteText="", tagNote=""):
    conn = sqlite3.connect(self.databaseName)
    cursor = conn.cursor()
    if noteText != "":
        cursor.execute(f"UPDATE {self.tableName} SET note_text = '{noteText}' WHERE id = {noteId}")
    if tagNote != "":
        cursor.execute(f"UPDATE {self.tableName} SET tags = '{tagNote}' WHERE id = {noteId}")
    conn.commit()
    conn.close()
    print("Nota modificada com sucesso!")
  
  # Função que deleta as notas 
  def deleteNote(self, noteId):
    conn = sqlite3.connect(self.databaseName)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {self.tableName} WHERE id = {noteId}")
    conn.commit()
    print("Nota deletada com sucesso!")
    conn.close()