## Docker hub

You can check the image in docker hub [welcometors/mp3converter](https://hub.docker.com/repository/docker/welcometors/mp3converter)

## Building Image

```sh
docker build -t welcometors/mp3converter:latest .
```

To remove old images

```sh
docker image prune -f
```

Test

```sh
docker run --rm -v <src-path>:/convert/from -v <dst-path>:/convert/to welcometors/mp3converter
```
