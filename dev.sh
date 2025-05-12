#!/usr/bin/env bash

set -e

# Generate Fonts
FONT_NAME="NeoSpleen"
sfd="${FONT_NAME}.sfd"
formats=("ttf")
for format in "${formats[@]}"; do
    output="${FONT_NAME}-Regular.${format}"
    fontforge -lang=ff -c "Open(\"${sfd}\"); Generate(\"${output}\")"
done

# Generate Weight Fonts
fontforge -lang=py -script generate_font_weights.py
