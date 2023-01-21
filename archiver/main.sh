#!/bin/bash

gpg --trust-model always --import "$IMPORT_FILE"

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
            zip -r -q "$OUT_DIR/$name".zip "$f"
            echo "Encrypting $name"
            gpg -e --recipient "$EMAIL" --yes --trust-model always "$OUT_DIR/$name".zip
            rm "$OUT_DIR/$name".zip
        fi
    fi
done
