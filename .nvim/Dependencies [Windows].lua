return {
	terminal_commands = {
		[1] = {
			"winget install FontForge.FontForge --accept-package-agreements --accept-source-agreements",
			"Remove-Item -Path 'NerdFontPatcher' -Force -Recurse",
			"Invoke-WebRequest -Uri 'https://github.com/ryanoasis/nerd-fonts/raw/master/FontPatcher.zip' -OutFile 'FontPatcher.zip'",
			"Expand-Archive -Path 'FontPatcher.zip' -DestinationPath 'NerdFontPatcher'",
			"Remove-Item -Path 'FontPatcher.zip'",
		}
	}
}
