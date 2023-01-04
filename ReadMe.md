## Git Committer

Pull the latest repository and auto commits on git.

This command can be used to create a patch of staged changes

```sh
git --no-pager diff --staged --name-only | zip patch.zip -@
```

## Pull Image

```sh
docker pull welcometors/gitcommitter
```

## Run

You need to mount `source` path for the conversion.

```sh
docker run --rm -v <src-path>:/source welcometors/gitcommitter
```

## Building Image

```sh
docker build -t welcometors/gitcommitter:latest .
```

To remove old images

```sh
docker image prune -f
```
