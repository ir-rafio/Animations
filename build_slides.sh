#!/usr/bin/env bash

set -e

if [ $# -lt 1 ]; then
    echo "Usage: $0 "path/to/project" [manim flags...]"
    exit 1
fi

WORKING_DIR="$1"
shift
EXTRA_FLAGS=("$@")

if [ ! -d "$WORKING_DIR" ]; then
    echo "Directory not found: $WORKING_DIR"
    exit 1
fi

ORIGINAL_DIR="$(pwd)"
trap 'cd "$ORIGINAL_DIR"' EXIT

cd "$WORKING_DIR"

MAIN_FILE="main.py"
SCENES_FILE="scenes.txt"
OUTPUT_DIR="output"

mkdir -p "$OUTPUT_DIR"

ROOT_NAME=$(basename "$(pwd)")

if [ ! -f "$SCENES_FILE" ]; then
    echo "Missing scenes file: $SCENES_FILE"
    exit 1
fi

SCENES=$(tr '\n' ' ' < "$SCENES_FILE")

echo "Working dir: $(pwd)"
echo "Scenes: $SCENES"
echo "Project name: $ROOT_NAME"
echo "Flags: ${EXTRA_FLAGS[*]}"

echo "Rendering slides..."
manim-slides render "${EXTRA_FLAGS[@]}" "$MAIN_FILE" $SCENES

echo "Generating HTML..."
manim-slides convert --to html $SCENES "$OUTPUT_DIR/${ROOT_NAME}.html"

echo "Generating PDF..."
manim-slides convert --to pdf $SCENES "$OUTPUT_DIR/${ROOT_NAME}.pdf"

echo "Generating PPTX..."
manim-slides convert --to pptx $SCENES "$OUTPUT_DIR/${ROOT_NAME}.pptx"

echo "Done! Files saved in $(pwd)/$OUTPUT_DIR/"