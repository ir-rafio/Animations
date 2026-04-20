#!/usr/bin/env bash

set -e

if [ $# -lt 2 ]; then
    echo "Usage: $0 path/to/project SceneName [manim flags...]"
    exit 1
fi

WORKING_DIR="$1"
SCENE_NAME="$2"
shift 2
EXTRA_FLAGS=("$@")

if [ ! -d "$WORKING_DIR" ]; then
    echo "Directory not found: $WORKING_DIR"
    exit 1
fi

ORIGINAL_DIR="$(pwd)"
trap 'cd "$ORIGINAL_DIR"' EXIT

cd "$WORKING_DIR"

MAIN_FILE="main.py"
OUTPUT_DIR="output"

mkdir -p "$OUTPUT_DIR"

echo "Working dir: $(pwd)"
echo "Scene: $SCENE_NAME"
echo "Flags: ${EXTRA_FLAGS[*]}"

echo "Rendering slide..."
manim-slides render -ql "${EXTRA_FLAGS[@]}" "$MAIN_FILE" "$SCENE_NAME"

echo "Generating HTML..."
manim-slides convert --to html "$SCENE_NAME" "$OUTPUT_DIR/${SCENE_NAME}.html"

echo "Generating PDF..."
manim-slides convert --to pdf "$SCENE_NAME" "$OUTPUT_DIR/${SCENE_NAME}.pdf"

echo "Generating PPTX..."
manim-slides convert --to pptx "$SCENE_NAME" "$OUTPUT_DIR/${SCENE_NAME}.pptx"

echo "Done! Files saved in $OUTPUT_DIR/"