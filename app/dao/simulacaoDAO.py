from app.config.conexao import Conexao
from psycopg2 import Error

#create simulação
def create_simulacao(datasimulacao, valor, datainicial, retorno, acao, idusuario):
    conexao = Conexao()
    conn = conexao.connect()

    try:
        cursor = conn.cursor()
        query = ("insert into simulacao (data_simulacao, valor_simulacao, data_ini_simulacao, retorno_simulacao, acao_simulacao, id_usuario) values "+
                 "({}, {}, {}, {}, {}, {})".format(datasimulacao, valor, datainicial, retorno, acao, idusuario))
        cursor.execute(query)
        conn.commit()
        return "Simulação adicionada!"
    
    except (Exception, Error) as error:
        return ("Erro ao adicionar Simulação:", error)
    
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update simulação(datasimulacao)
def update_simulacao_datasimulacao(id, inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update simulacao set data_simulacao = {} where id_simulacao = {}".format(id, inform))
        cursor.execute(query)
        conn.commit()
        return "Simulação atualizada com sucesso!"
    
    except (Exception, Error) as error:
        return ("Erro ao atualizar:", error)

#update simulação(valor)
def update_simulacao_valor(id, inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update simulacao set valor_simulacao = {} where id_simulacao = {}".format(id, inform))
        cursor.execute(query)
        conn.commit()
        return "Simulação atualizada com sucesso!"
    
    except (Exception, Error) as error:
        return ("Erro ao atualizar:", error)

#update simulação(datainicial)
def update_simulacao_datainicial(id, inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update simulacao set data_ini_simulacao = {} where id_simulacao = {}".format(id, inform))
        cursor.execute(query)
        conn.commit()
        return "Simulação atualizada com sucesso!"
    
    except (Exception, Error) as error:
        return ("Erro ao atualizar:", error)

#update simulação(retorno)
def update_simulacao_retorno(id, inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update simulacao set retorno_simulacao = {} where id_simulacao = {}".format(id, inform))
        cursor.execute(query)
        conn.commit()
        return "Simulação atualizada com sucesso!"
    
    except (Exception, Error) as error:
        return ("Erro ao atualizar:", error)

#update simulação(acao)
def update_simulacao_acao(id, inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update simulacao set acao_simulacao = {} where id_simulacao = {}".format(id, inform))
        cursor.execute(query)
        conn.commit()
        return "Simulação atualizada com sucesso!"
    
    except (Exception, Error) as error:
        return ("Erro ao atualizar:", error)

#update simulação(idusuario)
def update_simulacao_idusuario(id, inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update simulacao set id_usuario = {} where id_simulacao = {}".format(id, inform))
        cursor.execute(query)
        conn.commit()
        return "Simulação atualizada com sucesso!"
    
    except (Exception, Error) as error:
        return ("Erro ao atualizar:", error)
    
#read simulação
def read_simulacao():
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("select * from simulacao")
        cursor.execute(query)
        results = cursor.fetchall()
        simulacoes = []
        for result in results:
            simulacao = (result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
            simulacoes.append(simulacao)
        return simulacoes
    
    except(Exception, Error) as error:
        return ("Erro ao listar Simulação: ", error)
    
    finally:
        cursor.close()
        conexao.close_connection(conn)
        
#delet simulação
def delet_simulacao(id):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("delete from simulacao where id_simulacao = {}".format(id))
        cursor.execute(query)
        conn.commit()
        return "Simulação excluida com sucesso!"
    except(Exception, Error) as error:
        return ("Erro ao deletar simulação: " , error)
    finally:
        cursor.close()
        conexao.close_connection(conn)