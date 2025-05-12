#!/usr/bin/env bash

set -e

formats=("ttf") # TODO: Add "woff2"
fontforge -lang=py -script generate_fonts.py "${formats[@]}"
