#!/usr/bin/env bash

name="NeoSpleen"
dir="Fonts"
input="$name.sfd"
output="$dir/$name.ttf"
outputNfIn="${name}NerdFont-Regular.ttf"
outputNfOut="$dir/${name}-NerdFont.ttf"

rm -f "$output"
rm -f "$outputNfOut"

fontforge -lang=ff -c "Open(\"$input\"); Generate(\"$output\")"
fontforge -script Patcher/font-patcher "$output" -c --boxdrawing --removeligs --progressbars

mv "$outputNfIn" "$outputNfOut"
