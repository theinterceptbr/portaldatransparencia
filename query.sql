
/*Filtra CML e ações de apoio à seg. pública no RJ*/
CREATE TABLE cml AS SELECT * FROM gastos_diretos 
WHERE nome_unidade_gestora LIKE '%MILITAR DO LESTE%' OR codigo_unidade_gestora = '160299' OR codigo_unidade_gestora = '167299';

CREATE TABLE apoio AS SELECT * FROM gastos_diretos 
WHERE codigo_acao = '14VW';

/*Consulta empresas favorecidas*/
SELECT nome_favorecido, sum(valor) as total from cml 
GROUP BY nome_favorecido order by total desc limit 3;
-- "MASAN SERVICOS ESPECIALIZADOS LTDA [MASAN]"	"21 3718 15.51"
-- "HANNA E ROSE SERVICO E COMERCIO LTDA [LEJU INFORMATICA]"	"9 968 986.78"
-- "AAVA SOLUCOES E TRANSPORTE LTDA  - ME [AAVA]"	"8919539.12"

/* Total do órgão */
SELECT sum(valor) from cml;
-- 164 024 165.87

/* Total por ano */
select ano, sum( valor) from CML group by ano;
-- "2011"	"7 686 354.80999999"
-- "2012"	"7 123 878.89999999"
-- "2013"	"4 906 512.04000001"
-- "2014"	"25 005 912.65"
-- "2015"	"65 447 475.4200001"
-- "2016"	"37 337 746.79"
-- "2017"	"16 516 285.26"

/* Total por ano - Masan */
select ano, sum( valor) from CML where nome_favorecido like 'masan%' group by ano;
-- "2014"	"4 042 210.4"
-- "2015"	"17 329 605.11"

-- Total 14VW apor unidade
select nome_unidade_gestora as nome, sum(valor) as v from APOIO where codigo_acao = '14VW' group by nome order by v desc;
