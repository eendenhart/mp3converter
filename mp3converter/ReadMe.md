## Mp3 Converter

This docker file uses [ffmpeg](https://ffmpeg.org/) to convert audio files from [supported formats](https://ffmpeg.org/ffmpeg-formats.html) to `mp3`. It runs a simple python [script](main.py) to skip previously converted files.

You can check the image in docker hub [welcometors/mp3converter](https://hub.docker.com/r/welcometors/mp3converter)

## Pull Image

```sh
docker pull welcometors/mp3converter
```

## Run

You need to mount `source` and `destination` paths for the conversion.

```sh
docker run --rm -v <src-path>:/convert/from -v <dst-path>:/convert/to welcometors/mp3converter
```

## Building Image

```sh
docker build -t welcometors/mp3converter:latest .
```

To remove old images

```sh
docker image prune -f
```
