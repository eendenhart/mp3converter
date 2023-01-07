#!/bin/bash

DATADIR=/data
COPYSSH="${COPYPUB:-false}"

if [ "$COPYSSH" = false ]; then
    TXTFILE="$(ls -1 $DATADIR/*.txt | head -1)"
    echo "Oldest file $TXTFILE"
    EXT="${TXTFILE##*.}"
    TIMESTAMP="${TXTFILE%.*}"
    ZIPFILE="$TIMESTAMP.zip"
    if test -f "$ZIPFILE"; then
        echo "Datafile $ZIPFILE"
        while IFS= read -r line; do
            set -- "$@" "$line"
        done < "$TXTFILE"
        git clone -b "$2" "$1"
        REPO=$(basename -s .git "$1")
        unzip -o -d "$REPO/" "$ZIPFILE"
        git config --global user.email "$USER_EMAIL"
        git config --global user.name "$USER_NAME"
        cd "$REPO/" && git add . && git commit -m "$3" && git push --set-upstream origin "$2" && rm "$TXTFILE" "$ZIPFILE"
        rm -rf "$REPO/"
    else
        echo "Error: Corresponding zipfile not found. $ZIPFILE" >&2
    fi
else
    echo "Copying public ssh-key"
    cp ~/.ssh/id_ed25519.pub $DATADIR/
fi
