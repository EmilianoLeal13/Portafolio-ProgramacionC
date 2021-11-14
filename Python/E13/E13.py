"""
import subprocess

comando = "Get-Process"
lineaPS = "powershell -Executionpolicy ByPass -Command "+ comando
runningProcesses = subprocess.check_output(lineaPS)
print(runningProcesses.decode())
"""
#Se importa el modulo subprocess el cual ejectua sub procesos
import subprocess
# se declara el comando a ejecutar en powershell
comando = "Get-Command -Type Cmdlet | Sort-Object -Property Noun | Format-Table -GroupBy Noun"
#de define donde se ejecutara, un comando quue se salta medidas de seguridad y el comando anterios
lineaPS = "powershell -Executionpolicy ByPass -Command "+ comando
#Se ejecuta el proceso y se imprime en pantalla
runningProcesses = subprocess.check_output(lineaPS)
print(runningProcesses.decode())