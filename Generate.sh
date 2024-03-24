#!/usr/bin/env bash

name="NeoSpleen"
input="$name.sfd"
output="$name.ttf"
outputnf="${name}NerdFont-Regular.ttf"

rm "$output"
rm "$outputnf"
fontforge -lang=ff -c "Open(\"$input\"); Generate(\"$output\")" "$input" "$output"
fontforge -script Patcher/font-patcher "$output" -c --boxdrawing --removeligs --progressbars
