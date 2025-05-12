#!/usr/bin/env bash

set -e

# Generate Fonts
FONT_NAME="NeoSpleen"
FONT_DIR="fonts"
sfd="${FONT_NAME}.sfd"
formats=("ttf") # TODO: Add "woff2"
for format in "${formats[@]}"; do
    output="${FONT_DIR}/${FONT_NAME}.${format}"
    fontforge -lang=ff -c "Open(\"${sfd}\"); Generate(\"${output}\")"
done

# Generate Weight Fonts
fontforge -lang=py -script generate_font_weights.py

# Clean up
for format in "${formats[@]}"; do
    rm "${FONT_DIR}/${FONT_NAME}.${format}"
done
