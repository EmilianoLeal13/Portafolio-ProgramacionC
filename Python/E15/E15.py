import pyautogui,time

#primer envio del formulario
#Marvel o DC == Marvel
pyautogui.click(x= 701, y = 384, clicks = 1)
#Escribimos el Refran
pyautogui.click(x= 810, y = 580, clicks = 1)
pyautogui.typewrite("Mueres siendo un heroe o vives lo suficiente para volverte en un villano.")
#Seleccionamos la mejor hora de comer pastel
pyautogui.click(x= 777, y = 692, clicks = 1)
pyautogui.click(x= 788, y = 933 , clicks = 1)
#ingresamos direccion de correo falsa
pyautogui.click(x= 704, y = 807 , clicks = 1)
pyautogui.typewrite("correofalsopc@gmail.com")
#Enviamos El Formulario
pyautogui.click(x=743, y =876 , clicks = 1)
time.sleep(5)
#Volver a contestar el Formulario
pyautogui.click(x=721 , y = 393, clicks = 1)
time.sleep(3)

#Segundo Envio del Formulario
#Marvel o DC == Ambos
pyautogui.click(x= 701, y = 441, clicks = 1)
#Escribimos el Refran
pyautogui.click(x= 810, y = 580, clicks = 1)
pyautogui.typewrite("Si Dios es todopoderoso no es bueno del todo, y si es bueno del todo no puede ser todopoderoso")
#Seleccionamos la mejor hora de comer pastel
pyautogui.click(x= 777, y = 692, clicks = 1)
pyautogui.click(x= 768, y = 735 , clicks = 1)
#ingresamos direccion de correo falsa
pyautogui.click(x= 704, y = 807 , clicks = 1)
pyautogui.typewrite("CiberSeguridadFake@gmail.com")
#Enviamos El Formulario
pyautogui.click(x=743, y =876 , clicks = 1)
