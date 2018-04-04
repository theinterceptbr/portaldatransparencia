# Abrindo as contas do Governo Federal

Script de raspagem e consulta de gastos diretos do Governo Federal.

Raspagem e estruturação feita em Python, exportando os dados para CSV e SQLite.

Consultas em formato SQL.

Caso você não queira rodar o script em sua máquina, [acesse diretamente os
dados já
convertidos](https://drive.google.com/open?id=1VAiocAsmI_tXw1wvyam5IekzqXj7anXZ)
(nota: os arquivos CSVs muito grandes, provavelmente não abrirão em softwares
de planilha eletrônica comuns e precisarão de softwares específicos, a
recomendação é de utilizar um banco de dados, como SQLite ou MySQL).


# Rodando o script

Todo processo leva várias horas, dependendo da sua velocidade de conexão e de
processamento.

## Pré-requisitos

- 50GB livres em disco
- Python3 (com suporte a lzma) e pip
- wget
- MySQL

Instale as dependências Python com o comando:

```bash
pip install -r requirements.txt
```


## Raspagem e organização do banco

Baixe os arquivos executando o comando:

```bash
./download.sh
```

> Nota: esse script baixará dados para anos/meses pré-estabelecidos. Caso
> queira alterá-los, modifique o script `create-download-script.sh` e rode-o
> para gerar um novo `download.sh`.

O diretório `download` será criado, com os arquivos ZIP baixados. Para
converter os arquivos e consolidá-los em uma base de dados, rode os seguintes
comandos:

```bash
python converte.py gastos-diretos
python converte.py transferencias
```

Esses comandos podem demorar alguns minutos (são muitos dados para
descompactar, converter e então compactar novamente). Os arquivos
`output/gastos-diretos.csv.xz` e `output/transferencias.csv.xz` serão gerados.

Caso queira apenas utilizar MySQL, você pode pular para a próxima etapa. Senão,
caso queira converter os arquivos CSV para SQLite, execute o comando:

```bash
python csv2sqlite.py
```

O arquivo `output/portaldatransparencia.sqlite` será gerado.


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

