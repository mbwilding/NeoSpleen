return {
	terminal_commands = {
		"sudo install wget unzip fontforge;" ..
		"rm -rf NerdFontPatcher;" ..
		"wget https://github.com/ryanoasis/nerd-fonts/raw/master/FontPatcher.zip;" ..
		"unzip FontPatcher.zip -d NerdFontPatcher;" ..
		"rm ./FontPatcher.zip;"
	}
}
