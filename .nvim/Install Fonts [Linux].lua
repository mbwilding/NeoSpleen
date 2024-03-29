return {
	terminal_commands = {
		[1] = {
			"font_path=$HOME/.local/share/fonts",
			"mkdir -p ${font_path}",
			"rm ${font_path}/NeoSpleen*.ttf",
			"cp NeoSpleen*.ttf ${font_path}",
		},
	},
}
