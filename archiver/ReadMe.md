## Archiver

This docker archives and encrypts directories for uploading to untrusted hosts (like public cloud) as an added layer of security.

You can check the image in docker hub [welcometors/archiver](https://hub.docker.com/r/welcometors/archiver/tags)

## Pull Image

```sh
docker pull welcometors/archiver
```

## Run

You need to mount `source` and `destination` paths for the conversion. Running for the first time or to update `gpg` key we need to set `IMPORT` env variable and mount directory for public key.

```sh
docker run --name archiver1 -v <src-path>:/convert/from -v <dst-path>:/convert/to -e EMAIL=your@email.com -v <key-dir>:/import -e IMPORT=true welcometors/archiver
```

After that we can start it normally.

```sh
docker container start archiver1
```

## Building Image

```sh
docker build -t archiver:latest .
```

To remove old images

```sh
docker image prune -f
```

To export image

```sh
docker save -o <out-dir>/archiver.tar archiver:latest
```
