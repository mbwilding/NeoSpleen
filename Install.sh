#!/usr/bin/env bash

name="NeoSpleen"
input="$name.sfd"
output="$name.ttf"
outputnf="${name}NerdFont-Regular.ttf"
fonts="$HOME/.local/share/fonts"

mkdir -p "$fonts"
cp -f "$output" "$fonts/"
cp -f "$outputnf" "$fonts/"
