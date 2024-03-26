$name = "NeoSpleen"
$dir = "Fonts"
$input = "$name.sfd"
$output = "$dir/$name.ttf"
$outputNfIn = "${name}NerdFont-Regular.ttf"
$outputNfOut = "$dir/$Name-NerdFont.ttf"

Remove-Item $output -ErrorAction SilentlyContinue
Remove-Item $outputnfOut -ErrorAction SilentlyContinue

fontforge -lang=ff -c "Open(`"$input`"); Generate(`"$output`")"
fontforge -script NerdFontPatcher/font-patcher $output -c --boxdrawing --removeligs --progressbars

Move-Item -Path $outputNfIn -Destination $outputNfOut
