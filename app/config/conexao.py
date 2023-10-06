from psycopg2 import connect, Error
import os, psycopg2

class Conexao:
    def connect(self):
        try:
            host = "containers-us-west-108.railway.app",
            port = "7671",
            database = "railway",
            user = "postgres",
            password = "xw01F5KQ0vEbK3ubaUog"
            database_url = ("postgresql://{}:{}@{}:{}/{}".format(user, password, host, port, database)) 
            conn = psycopg2.connect(database_url)
            return conn
        
        except (Exception, Error) as error:
            return("Erro ao conectar no banco:", error)

    def close_connection(self, conn):
        try:
            if conn is not None:
                conn.close()
                return("Conexão fechada com sucesso!")
        except (Exception, Error) as error:
            return("Erro ao fechar conexão:", error)


