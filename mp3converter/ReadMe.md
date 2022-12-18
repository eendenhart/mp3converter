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
docker run --rm -v /mnt/e/source/repos/dockers/tmp/original:/convert/from -v /mnt/e/source/repos/dockers/tmp/converted:/convert/to welcometors/mp3converter
```
