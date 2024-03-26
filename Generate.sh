#!/usr/bin/env bash

name="NeoSpleen"
input="$name.sfd"
output="$name.ttf"
outputnf="${name}NerdFont-Regular.ttf"

rm "$output" 2>/dev/null
rm "$outputnf" 2>/dev/null

fontforge -lang=ff -c "Open(\"$input\"); Generate(\"$output\")" "$input" "$output"
fontforge -script Patcher/font-patcher "$output" -c --boxdrawing --removeligs --progressbars
