return {
	terminal_commands = {
		[1] = {
			"$fontPath = \"$($env:USERPROFILE)/AppData/Local/Microsoft/Windows/Fonts\"",
			"Write-Host $fontPath",
			"New-Item -ItemType Directory -Force -Path $fontPath | Out-Null",
			"Remove-Item -Path '${fontPath}/NeoSpleen*.ttf' -Force -ErrorAction SilentlyContinue",
			"Copy-Item -Path 'NeoSpleen*.ttf' -Destination $fontPath",
		},
	},
}
