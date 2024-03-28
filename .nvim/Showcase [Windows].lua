return {
	terminal_commands = {
		[1] = {
			"winget install python3 --accept-package-agreements --accept-source-agreements",
			"pip3 install Pillow",
			"python3 generate_image.py",
		}
	}
}
