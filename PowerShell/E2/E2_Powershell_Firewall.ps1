<#
Emiliano Leal Campos
E-manuel Manzanarez Mora
Luis Julian Ramos Castañeda
#>

do
{
  Write-Host "Menu"
  Write-Host "1 = Ver-StatusPerfil"
  Write-Host "2 = Cambiar-StatusPerfil"
  Write-Host "3 = Ver-PerfilRedActual"
  Write-Host "4 = Cambiar-PerfilRedActual"
  Write-Host "5 = Ver-ReglasBloqueo"
  Write-Host "6 = Agregar-ReglasBloqueo"
  Write-Host "7 = Eliminar-ReglasBloqueo"
  Write-Host "0 = Salir"
  $op = Read-Host
  switch($op)

  {
    1 {Write-Host "Ver-StatusPerfil"
    Ver-StatusPerfil}
    
    2 {Write-Host "Cambiar-StatusPerfil"
    Cambiar-StatusPerfil}
    
    3 {Write-Host "Ver-PerfilRedActual"
    Ver-PerfilRedActual}

    4 {Write-Host "Cambiar-PerfilRedActual"
    Cambiar-PerfilRedActual}

    5 {Write-Host "Ver-ReglasBloqueo"
    Ver-ReglasBloqueo}
    
    6 {Write-Host "Agregar-ReglasBloqueo"
    Agregar-ReglasBloqueo}

    7 {Write-Host "Eliminar-ReglasBloqueo"
    Eliminar-ReglasBloqueo}

  }
  
}while($op -ne 0)
