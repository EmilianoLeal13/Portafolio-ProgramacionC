"""
Emiliano Leal Campos
E-manuel Manzanarez Mora
Fuentes:
https://uanledu.sharepoint.com/sites/Section_02305010133602031420000101204062/_layouts/15/Doc.aspx?sourcedoc={c1753fb2-fa72-4b85-ac8d-3f9167b11a0b}&action=view&wd=target%28_Content%20Library%2F1.%20Shell%20y%20scripting.one%7C8a98ad7c-d9a9-4e34-a924-eeb22076d04c%2FAn%C3%A1lisis%20de%20m%C3%B3dulos%7C0cf9a18e-767d-4f2c-808a-a825d9d182f5%2F%29
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/compress-archive?view=powershell-7.1
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/expand-archive?view=powershell-7.1&viewFallbackFrom=powershell-7.1https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fpowershell%2Fmodule%2Fmicrosoft.powershell.archive%2Fexpand-archive%3Fview%3Dpowershell-7.1
"""

do
{

  Write-Host "Menu"
  Write-Host "1 = Comprimir Archivos"
  Write-Host "2 = Descomprimir Archivos"
  Write-Host "3 = Crear, Borrar o Copiar"
  Write-Host "4 = Obtener Archivos Por Fecha"
  Write-Host "0 = Salir"
  $op = Read-Host
  switch($op)

  {
    1 {Write-Host "Get-CompressFiles"
    Get-CompressFiles}

    2 {Write-Host "Get-Unzip"
    Get-Unzip}
    
    3 {Write-Host "Get-ModifyFiles"
    Get-ModifyFiles}

    4 {Write-Host "Get-ArchivosPorFecha"
    Get-ArchivosPorFecha}

  }
  }while($op -ne 0)