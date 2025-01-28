import repository as rep
import pandas as pd


def pesquisar_extrato(ids_conta):
    lista = ', '.join((map(str, ids_conta)))
    print (lista)
    consulta_sql = f"""
select c.descricao as conta, m.data as data, m.descricao as descricao, m.valor as valor, c2.descricao as categoria, t.descricao as tag 
from movimentacao m
inner join conta c on c.id = m.conta 
inner join Categoria c2 on c2.id = m.categoria 
inner join Tag t on t.id = m.tag 
where c.id in ({lista}) 
order by m.data desc
"""
    con = rep.connect_to_database()
    resultados = rep.query_to_dataframe(con, consulta_sql)
    rep.close_connection(con)
    return resultados


