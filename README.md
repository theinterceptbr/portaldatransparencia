# Abrindo as contas do Governo Federal
Script de raspagem e consulta de gastos diretos do Governo Federal.

Raspagem e estruturação em Python, exportando os dados para CSV e SQLite.

Consultas em formato SQL.

# Rodando o script

Todo processo leva várias horas, dependendo da sua velocidade de conexão e de processamento. 

## Pré-requisitos 
* 50 gb (?) livre em disco.
* Python
* MySQL

## Raspagem e organização do banco


## Importação do banco e consulta

1. Com o arquivo CSV na mesma pasta do script, importe os dados de gasto direto rodando no terminal:
```
mysql -u [nomedousuario] -p < import.sql
```

2. E depois execute as consultas
```
mysql -u [nomedousuario] -p < query.sql
``` 

# Fonte Dos Dados
[Dados Abertos do Portal da Tranparência](http://transparencia.gov.br/downloads/)

# Realização

* [The Intercept](http://theintercept.com/)

* [Adriano Belisário](http://github.com/belisards/)

* [Álvaro Justen](http://github.com/turicas/)

