# Cassandra

## Setup

Executa o cluster:

```sh
docker compose up -d
```

Cria estrutura de tabelas no cluster

```sh
docker compose exec node-1 cqlsh -f /structure.sql
```

## Conexão com cluster utilizando cliente em python

Existe um container chamado `client` que possue scripts necessário para conectar com o cluster e realizar certas operações. 

O comando abaixo realiza uma consulta no cluster:

```sh
docker compose exec client python query.py
```

