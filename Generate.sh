#!/usr/bin/env bash

name="NeoSpleen"
input="$name.sfd"
output="$name.ttf"

fontforge -lang=ff -c "Open(\"$input\"); Generate(\"$output\")" "$input" "$output"
fontforge -script Patcher/font-patcher NeoSpleen.ttf -c --boxdrawing --removeligs --progressbars
