
'https://superuser.com/questions/201896/how-do-i-install-a-font-from-the-windows-command-prompt'

Set ofso = CreateObject("Scripting.FileSystemObject")
SourceFolder = ofso.GetParentFolderName(Wscript.ScriptFullName)

Const FONTS = &H14&

Set objShell  = CreateObject("Shell.Application")
Set oSource   = objShell.Namespace(SourceFolder)
Set oWinFonts = objShell.Namespace(FONTS)

' Lame VBscript needs 4 f*ing lines instead of "if (/\.ttf$/i) " ...
Set rxTTF = New RegExp
rxTTF.IgnoreCase = True
rxTTF.Pattern = "\.ttf$"

FOR EACH FontFile IN oSource.Items()
    IF rxTTF.Test(FontFile.Path) THEN   
        oWinFonts.CopyHere FontFile.Path
    END IF
NEXT
