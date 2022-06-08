#https://stackoverflow.com/questions/12946384/windows-install-fonts-from-cmd-bat-file/67903796#67903796

# Install-Font.ps1
param($file)

$signature = @'
[DllImport("gdi32.dll")]
 public static extern int AddFontResource(string lpszFilename);
'@

$type = Add-Type -MemberDefinition $signature `
    -Name FontUtils -Namespace AddFontResource `
    -Using System.Text -PassThru
   
$type::AddFontResource($file)