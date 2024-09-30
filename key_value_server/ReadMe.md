# Key Value Server

A simple in-memory `key-value` server.

You can check the image in docker hub [welcometors/key_value_server](https://hub.docker.com/r/welcometors/key_value_server/tags)

## Pull Image

```sh
docker pull welcometors/key_value_server
```

## Run

You need to map the post from docker to host.

```sh
docker run --rm -p 9000:9000 welcometors/key_value_server
```

## Building Image

```sh
docker build -t welcometors/key_value_server:latest .
```

To remove old images

```sh
docker image prune -f
```
