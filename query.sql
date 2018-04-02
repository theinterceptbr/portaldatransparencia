
CREATE TABLE as cml AS SELECT * FROM gastos_diretos WHERE nome_unidade_gestora LIKE '%MILITAR DO LESTE%' OR codigo_unidade_gestora = '160299';
CREATE TABLE apoio AS SELECT * FROM gastos_diretos  where codigo_acao = '14VW';

/*Consultas*/
select nome_favorecido, sum(valor) as total from cml group by nome_favorecido order by total desc;
select nome_favorecido, sum(valor) as v from cml where codigo_acao = '14VW' group by nome_favorecido order by v desc;
select sum(valor) from cml where codigo_acao = '14VW' ;
select ano, sum(valor) from cml where codigo_acao = '14VW' group by ano;
select nome_unidade_gestora as nome, sum(valor) as v from APOIO where codigo_acao = '14VW' group by nome order by v desc;
