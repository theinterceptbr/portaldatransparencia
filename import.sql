CREATE DATABASE federal;
USE federal; 
DROP TABLE IF EXISTS gastos_diretos;
CREATE TABLE gastos_diretos (
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
    data_pagamento TEXT,
    valor DECIMAL (20,2),
    data_pagamento_original TEXT,
    ano INT,
    mes INT
);

load data local infile '../dados/gastos-diretos.csv'
  into table gastos_diretos
    fields terminated by ',' OPTIONALLY ENCLOSED BY '"' 
    lines terminated by '\n'
    ignore 1 lines
    (@codigo_orgao_superior, @nome_orgao_superior, @codigo_orgao, @nome_orgao, @codigo_unidade_gestora, @nome_unidade_gestora, @codigo_grupo_despesa, @nome_grupo_despesa, @codigo_elemento_despesa, @nome_elemento_despesa, @codigo_funcao, @nome_funcao, @codigo_subfuncao, @nome_subfuncao, @codigo_programa, @nome_programa, @codigo_acao, @nome_acao, @linguagem_cidada, @codigo_favorecido, @nome_favorecido, @numero_documento, @gestao_pagamento, @data_pagamento, @valor, @data_pagamento_original, @ano, @mes)
SET
    codigo_orgao_superior=@codigo_orgao_superior,
    nome_orgao_superior=@nome_orgao_superior,
    codigo_orgao=@codigo_orgao,
    nome_orgao=@nome_orgao,
    codigo_unidade_gestora=@codigo_unidade_gestora,
    nome_unidade_gestora=@nome_unidade_gestora,
    codigo_grupo_despesa=@codigo_grupo_despesa,
    nome_grupo_despesa=@nome_grupo_despesa,
    codigo_elemento_despesa=@codigo_elemento_despesa,
    nome_elemento_despesa=@nome_elemento_despesa,
    codigo_funcao=@codigo_funcao,
    nome_funcao=@nome_funcao,
    codigo_subfuncao=@codigo_subfuncao,
    nome_subfuncao=@nome_subfuncao,
    codigo_programa=@codigo_programa,
    nome_programa=@nome_programa,
    codigo_acao=@codigo_acao,
    nome_acao=@nome_acao,
    linguagem_cidada=@linguagem_cidada,
    codigo_favorecido=@codigo_favorecido,
    nome_favorecido=@nome_favorecido,
    numero_documento=@numero_documento,
    gestao_pagamento=@gestao_pagamento,
    data_pagamento=@data_pagamento,
    valor=@valor,
    data_pagamento_original=@data_pagamento_original,
    ano=@ano,
    mes=@mes;
    
SHOW WARNINGS;
