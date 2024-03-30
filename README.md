# NeoSpleen

A modern monospaced font inspired by [Spleen](https://github.com/fcambus/spleen).

## Showcase

[Showcase](https://github.com/mbwilding/NeoSpleen/releases/latest/download/Showcase.png) 

## Install

### Linux

```bash
font_path="~/.local/share/fonts"
mkdir -p ${font_path}
pushd ~/.local/share/fonts
rm NeoSpleen*.ttf
download_base="https://github.com/mbwilding/NeoSpleen/releases/latest/download/NeoSpleen"
wget ${download_base}.ttf
wget ${download_base}-NerdFont.ttf
popd
fc-cache -f
```

### Windows

Download the font you want, double click it, and click install.

![NeoSpleen](https://github.com/mbwilding/NeoSpleen/releases/latest/download/NeoSpleen.ttf) 
![NeoSpleen-NerdFont](https://github.com/mbwilding/NeoSpleen/releases/latest/download/NeoSpleen-NerdFont.ttf) 

## Notes

Recommended font size is 15 as it is the equivalent to Jetbrains Mono at font size 12 in the terminal.
