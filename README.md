<img width="300" alt="image" src="https://user-images.githubusercontent.com/25587856/197742478-0be6735c-6be5-4363-b1e2-00c06718210f.png">

_"This data is great! Can we have a report every day?"_ 💀

Sometimes you need a quick and hacky way of querying and summarising data on a regular basis. `cronsql` is a simple 
Docker-enabled SQL query scheduler & reporting toolkit for analytics workloads.

## Usage

Query, `cron` strings, and auth details are defined in the `config.yaml` file. The default settings are:

```yaml
database:
  host: database
  user: postgres
  password: postgres
  database: postgres
  port: 5432
query: |
  SELECT *
  FROM example
  WHERE timestamp > NOW() - INTERVAL '30 seconds'
cron: "*/1 * * * *"
```

## Development

`./run-test-harness.sh` spins up the default `cronsql` image, a Postgres instance and a `harness` service (which populates
the database instance).