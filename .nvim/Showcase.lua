if vim.fn.has 'win32' == 1 then
	return {
		terminal_commands = {
			[1] = {
				"winget install python3 --accept-package-agreements --accept-source-agreements",
				"pip3 install Pillow",
				"python3 generate_image.py",
			}
		}
	}
else
	return {
		terminal_commands = {
			[1] = {
				"sudo install python3",
				"pip3 install Pillow",
				"python3 generate_image.py",
			}
		}
	}
end
