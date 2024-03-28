return {
	terminal_commands = {
		[1] = {
			"sudo apt-get install wget unzip fontforge",
			"rm -rf NerdFontPatcher",
			"wget https://github.com/ryanoasis/nerd-fonts/raw/master/FontPatcher.zip",
			"unzip FontPatcher.zip -d NerdFontPatcher",
			"rm FontPatcher.zip",
		}
	}
}
