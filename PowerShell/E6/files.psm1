function Get-CompressFiles
  {
     param(
    [Parameter()][String]$Ruta,
    [Parameter()][String]$DesPath)

    $Ruta = Read-Host "Ingrese la ruta del archivo a comprimir"
    $DesPath = Read-Host "Ingrese la ruta donde sera guardado"
    try
    {
        Compress-Archive -LiteralPath $Ruta -DestinationPath $DesPath -InvalidArgument Stop
    }
    catch { "Argumento invalido, Alguna ruta fue mal escrita, favor de escribirlo correctamente" }
}
 function Get-ModifyFiles
{
    param(
    [Parameter()][String]$op,
    [Parameter()][String]$Ruta,
    [Parameter()][String]$RutaDes)

    $op = Read-Host "
    Selecciona que quieres hacer:
    1: Crear Un Archivo
    2: Borrar Un Archivo
    3: Copiar Un Archivo
    :" 

    switch ( $op )
    {

        1{
            $Ruta = Read-Host "Ruta del archivo a crear"
            New-Item -Path $Ruta -ItemType File
        }

        2{
            $Ruta = Read-Host "Ruta del archivo a borrar"
            Remove-Item -Path $Ruta
        }

        3{
            $Ruta = Read-Host "Ruta del archivo a copiar"
            $RutaDes = Read-Host "Ruta del archivo donde se pegara"
            Copy-Item -Path $Ruta -Destination $RutaDes

        }
    }
} 
function Get-Unzip
{
     param(
    [Parameter()][String]$Ruta,
    [Parameter()][String]$DesPath)

    $Ruta = Read-Host "Ingrese la ruta del archivo a comprimir"
    $DesPath = Read-Host "Ingrese la ruta donde sera guardado"
    try
    {
        Expand-Archive -LiteralPath $Ruta -DestinationPath $DesPath -InvalidOperation Stop
    }
    catch { "Operacion invalida, el archivo a decompriir ya existe" }
}
function Get-ArchivosPorFecha
{
    param(
    [Parameter()][Array]$TipoArchivo,
    [Parameter()][String]$Mes,
    [Parameter()][Array]$Año,
    [Parameter()][Array]$Ruta)

    Read-Host "Tipo de Archivo" $TipoArchivo
    Read-Host "Mes" $Mes
    Read-host "Año" $Año
    Read-Host "Ruta" $Ruta

    Get-ChildItem -Path $Ruta -Include $TipoArchivo -Recurse 

    Where-Object {$.lastwritetime.month -eq $Mes -AND $.lastwritetime.year -eq $Año }
}