#!/bin/bash

IMPORTKEY="${IMPORT:-false}"
UPDATESOURCE="${UPDATE:-false}"

if [ "$UPDATESOURCE" = true ]; then
    wget -O main.sh https://raw.githubusercontent.com/rahulsrma26/dockers/master/archiver/main.sh
fi

if [ "$IMPORTKEY" = true ]; then
    gpg --trust-model always --import "$IMPORT_FILE"
fi

rm -rf /tmp/*

for f in "$IN_DIR"/* ; do
    if [ -d "$f" ]; then
        name=$(basename "$f")
        rebuild=true
        if [[ -e "$OUT_DIR/$name.zip.gpg" ]]; then
            newest="$(find $f -type f -print0 | xargs -0 ls -drt | tail -n 1)"
            if [ "$newest" -nt "$OUT_DIR/$name.zip.gpg" ]; then
                echo "Newest modified $newest"
            else
                echo "Skipping $name"
                rebuild=false
            fi
        fi
        if [ "$rebuild" = true ]; then
            zip -r -q "/tmp/$name.zip" "$f"
            echo "Encrypting $name"
            gpg -e --recipient "$EMAIL" --yes --trust-model always -o "$OUT_DIR/$name.zip.gpg" "/tmp/$name.zip"
            rm "/tmp/$name.zip"
        fi
    fi
done

rm -rf /tmp/*