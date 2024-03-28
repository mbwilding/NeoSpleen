return {
	terminal_commands = {
		"rm NeoSpleen*.ttf;" ..
		"fontforge -lang=ff -c 'Open(\"NeoSpleen.sfd\"); Generate(\"NeoSpleen.ttf\")';" ..
		"fontforge -script NerdFontPatcher/font-patcher NeoSpleen.ttf --complete --boxdrawing;" ..
		"mv NeoSpleenNerdFont-Regular.ttf NeoSpleen-NerdFont.ttf"
	}
}
