# Git Committer

This tool allows you to create fake commit(s) (as a git archive i.e. a zip file) before hand and then commit them at later time whenever the docker runs. This can be helpful in creating multiple changes at once and then committing them later one by one on different days/times.

## Installation

Pre-requisite:

- bash/zsh (Not tested on other's but should work)
- git
- docker

To download and install the `fakecommit` command either copy it from the file [fakecommit.sh](fakecommit.sh) into your bin `PATH` or run this command to do the same:

```sh
mkdir -p ~/bin && curl -s "https://raw.githubusercontent.com/rahulsrma26/dockers/gitcommitter/fakecommit.sh" > ~/bin/fakecommit && chmod ugo+x ~/bin/fakecommit
```

Usually `~/.bin` path will be added by default in most of the distros. You just need to re-login. But if in case it's not present then you can append these line to your `~/.profile` file and then re-login.

```sh
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi
```

## Running

There are two parts:

1. To create fake commits

   ```sh
   fakecommit "commit message"
   ```

   This will create a zip file containing all the files with staged changes and a text file containing repository info with commit message. By default it will create those files in `./tmp/` directory but you can change it with second argument.

   ```sh
   fakecommit "commit message" <out-dir>/
   ```

2. Second part is the docker that runs and submits the commit.

   Building Image for current git user:

   ```sh
   docker build --build-arg EMAIL="$(git config --get user.email)" --build-arg NAME="$(git config --get user.name)" -t gitcommitter:latest .
   ```

   [Optional] Change it to other `email` and `name` if you want to create commits using some other profile.

   ```sh
   docker build --build-arg EMAIL="<user-email>" --build-arg NAME="<user-name>" -t gitcommitter:latest .
   ```

   [Optional] You can export the image to different machine/server if you want using:

   ```sh
   docker save -o <out-dir>/gitcommitter.tar gitcommitter:latest
   ```

   If it's running for the first time then the you need to get the public key of the docker image so that it can be added to github. This command will copy the public key to the output directory.

   ```sh
   docker run --rm -e COPYPUB=true -v <out-dir>:/data gitcommitter
   ```

   After that you need to upload it to the github using either [gh auth login](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) or manually uploading into [settings](https://github.com/settings/keys). Once that is done, user should remove it.

   ```sh
   rm <out-dir>/id_ed25519.pub
   ```

   Now, whenever the docker runs, it will fetch one fake-commit (txt and zip file pair), create actual commit, push it to repo, and remove it (txt and zip file pair) from the directory.

   ```sh
   docker run --rm -v <out-dir>:/data gitcommitter
   ```

   You can also create a cron job to run it automatically every day e.g. this will run docker everyday at 1:30am.

   1. Edit
      ```sh
      crontab -e
      ```
   2. Add command
      ```sh
      30 1 \* \* \* docker run --rm -v <out-dir>:/data gitcommitter
      ```
   3. Restart cron
      ```sh
      service crond restart
      ```

---

## Extras

To remove old images

```sh
docker image prune -f
```
