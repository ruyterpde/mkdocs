``` cmd

Windows Registry Editor Version 5.00

[-HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\{2cc5ca98-6485-489a-920e-b3e88a6ccce3}]

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel]
"{2cc5ca98-6485-489a-920e-b3e88a6ccce3}"=dword:00000001


```

``` powershell

$namespaceKey = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\{2cc5ca98-6485-489a-920e-b3e88a6ccce3}"
if (Test-Path $namespaceKey) {
    Remove-Item -Path $namespaceKey -Recurse -Force
    Write-Output "Verwijderd: $namespaceKey"
} else {
    Write-Output "Sleutel niet gevonden: $namespaceKey"
}

$hideIconsKey = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel"
if (-not (Test-Path $hideIconsKey)) {
    New-Item -Path $hideIconsKey -Force | Out-Null
    Write-Output "Aangemaakt: $hideIconsKey"
}

New-ItemProperty -Path $hideIconsKey -Name "{2cc5ca98-6485-489a-920e-b3e88a6ccce3}" -PropertyType DWORD -Value 1 -Force
Write-Output "DWORD toegevoegd: {2cc5ca98-6485-489a-920e-b3e88a6ccce3} = 1"


```

https://learn.microsoft.com/en-us/answers/questions/2157455/how-to-remove-a-persistent-shortcut-learn-about-th