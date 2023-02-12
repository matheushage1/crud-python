# importing the necessary packages
import mysql.connector

# creating connection with mysql db
conexao = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'bdyoutube'
)

# creating the cursor
cursor = conexao.cursor()

# Create
nome_produto = "headset"
valor = 350
comando = f'INSERT INTO vendas (nome_produto, valor_do_produto) VALUES ("{nome_produto}", {3.500})'
cursor.execute(comando)

# editing the db
conexao.commit() 

# Read
comando = 'SELECT * FROM vendas'
cursor.execute(comando)

# read the db
resultado = cursor.fetchall()
print(resultado)

# Update
nome_produto = "notebook"
valor = 6000
comando = 'UPDATE vendas SET {valor} = 6000 WHERE nome_produto = "{notebook}"'
cursor.execute(comando)
conexao.commit()

# Delete
nome_produto = "notebook"
comando = 'DELETE * FROM vendas WHERE idVendas = 1'
cursor.execute(comando)
conexao.commit()

# stopping the usage from cursos and also connection
cursor.close()
conexao.close()