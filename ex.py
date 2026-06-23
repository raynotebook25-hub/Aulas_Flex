import sqlite3

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

# cursor.execute('''CREATE TABLE Alunos2 (
#     id  INTEGER PRIMARY KEY, nome TEXT, email TEXT)''')
# cursor.execute("INSERT INTO Alunos2 VALUES (1, 'Lucas', 'lucas123@gmail.com')")
# cursor.execute("INSERT INTO Alunos2 VALUES (2, 'Ana', 'ANINHA12@gmail.com')")
# cursor.execute("INSERT INTO Alunos2 VALUES (3, 'Julia', 'juju25@gmail.com')")
# conexao.commit()

sql_update = """
UPDATE Alunos2
SET email = ?
WHERE ID = ? 
"""

cursor.execute(sql_update, ('aninha23@gmail.com', 2))
conexao.commit()

def deletar_alunos(nomeId):
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM Alunos2 WHERE id = ?", (nomeId,))

    conexao.commit()
    conexao.close()

    print(f"Aluno do id {nomeId} removido com sucesso!")

deletar_alunos(2)

nomes = ('Marcos')

