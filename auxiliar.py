import time
import pyautogui

# aqui voce deixa o programa executar, ele vai demorar 5 seg pra executar o print, nesse tempo voce colocar seu mouse em cima da barra de loggin ou de onde voce quer achar a posiçao do mouse, o print vai te mostrar a posicao do mouse

time.sleep(5)
print(pyautogui.position())
