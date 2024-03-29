if vim.fn.has "win32" == 1 then
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
else
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
end
