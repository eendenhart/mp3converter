#!/bin/bash

IN_DIR="${IN_DIR:-./tmp/original}"
OUT_DIR="${OUT_DIR:-./tmp/converted}"

for f in "$IN_DIR"/* ; do
    if [ -d "$f" ]; then
        name=$(basename "$f")
        zip -r "$OUT_DIR/$name".zip "$f"
    fi
done
