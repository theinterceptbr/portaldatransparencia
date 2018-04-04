import csv
import io
import lzma
import sqlite3

from rows.plugins.utils import ipartition


def import_file(connection, filename, drop_sql, create_sql, batch_size=100):
    cursor = connection.cursor()

    cursor.execute(drop_sql)
    cursor.execute(create_sql)
    connection.commit()

    header = [line.strip().split()[0]
              for line in create_sql.split('(')[1].split(')')[0].splitlines()
              if line.strip()]
    placeholders = ', '.join('?' for _ in header)
    header_names = ', '.join(header)
    table_name = create_sql.split('(')[0].strip().split()[-1]
    insert_sql = f'INSERT INTO {table_name} ({header_names}) VALUES ({placeholders})'

    with lzma.LZMAFile(filename, mode='rb', format=lzma.FORMAT_XZ) as fobj, \
        io.TextIOWrapper(fobj, encoding='utf-8') as fobj2:

        counter = 0
        for batch in ipartition(csv.DictReader(fobj2), batch_size):
            counter += len(batch)
            cursor.executemany(
                insert_sql,
                [[row[field] for field in header] for row in batch],
            )
            if counter % 100000 == 0:
                print(counter)
        if counter % 100000 != 0:
            print(counter)

    connection.commit()


drop_sql_1 = 'DROP TABLE IF EXISTS transferencias'
drop_sql_2 = 'DROP TABLE IF EXISTS gastos_diretos'
create_sql_1 = '''CREATE TABLE IF NOT EXISTS transferencias (
    sigla_unidade_federacao TEXT,
    codigo_siafi_municipio INT,
    nome_municipio TEXT,
    codigo_funcao INT,
    nome_funcao TEXT,
    codigo_sub_funcao INT,
    nome_sub_funcao TEXT,
    codigo_programa INT,
    nome_programa TEXT,
    codigo_acao TEXT,
    nome_acao TEXT,
    linguagem_cidada TEXT,
    codigo_favorecido TEXT,
    nome_favorecido TEXT,
    fonte_finalidade TEXT,
    modalidade_aplicacao TEXT,
    numero_convenio TEXT,
    valor_parcela FLOAT,
    ano INT,
    mes INT
);'''
create_sql_2 = '''CREATE TABLE IF NOT EXISTS gastos_diretos (
    codigo_orgao_superior INT,
    nome_orgao_superior TEXT,
    codigo_orgao INT,
    nome_orgao TEXT,
    codigo_unidade_gestora INT,
    nome_unidade_gestora TEXT,
    codigo_grupo_despesa INT,
    nome_grupo_despesa TEXT,
    codigo_elemento_despesa INT,
    nome_elemento_despesa TEXT,
    codigo_funcao INT,
    nome_funcao TEXT,
    codigo_subfuncao INT,
    nome_subfuncao TEXT,
    codigo_programa INT,
    nome_programa TEXT,
    codigo_acao TEXT,
    nome_acao TEXT,
    linguagem_cidada TEXT,
    codigo_favorecido TEXT,
    nome_favorecido TEXT,
    numero_documento TEXT,
    gestao_pagamento TEXT,
    data_pagamento DATE,
    valor FLOAT,
    data_pagamento_original TEXT,
    ano INT,
    mes INT
);'''

filename = 'portal-transparencia.sqlite'
connection = sqlite3.Connection(filename)
import_file(connection, 'transferencias.csv.xz', drop_sql_1, create_sql_1)
import_file(connection, 'gastos-diretos.csv.xz', drop_sql_2, create_sql_2)

# TODO: automatically create schema from CSV
