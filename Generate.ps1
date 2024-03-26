$name = "NeoSpleen"
$input = "$name.sfd"
$output = "$name.ttf"
$outputnf = "${name}NerdFont-Regular.ttf"

Remove-Item $output -ErrorAction SilentlyContinue
Remove-Item $outputnf -ErrorAction SilentlyContinue

fontforge -lang=ff -c "Open(`"$input`"); Generate(`"$output`")"
& fontforge -script Patcher/font-patcher $output -c --boxdrawing --removeligs --progressbars
