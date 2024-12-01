# cassandra

## Setup

Run database cluster:

```sh
docker compose up -d
```

Create database structure:

```sh
docker compose exec node-1 cqlsh -f /structure.sql
```

