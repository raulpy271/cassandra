# Cassandra

![Diagrama do banco Cassandra](./diagram.jpg)

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
docker compose exec client python query.py <table?>
```

## Consultar status do cluster

```
docker compose exec node-1 nodetool status
```

## Consultar onde está localizado um registro

Essa é uma operação utilizada para fins didáticos, na prática não é necessário consultar qual nó um dado é localizado, já que isso é feito automaticamente pelo banco de dados distribuido.

```
docker compose exec node-1 nodetool getendpoints store <table> <row-id>
```

