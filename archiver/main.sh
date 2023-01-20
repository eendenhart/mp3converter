#!/bin/bash

gpg --trust-model always --import "$IMPORT_FILE"

for f in "$IN_DIR"/* ; do
    if [ -d "$f" ]; then
        name=$(basename "$f")
        zip -r "$OUT_DIR/$name".zip "$f"
        gpg -e --recipient "$EMAIL" --yes --trust-model always "$OUT_DIR/$name".zip
        rm "$OUT_DIR/$name".zip
    fi
done
