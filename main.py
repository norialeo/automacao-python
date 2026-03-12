import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "email@gmail.com"
senha = "senha123"

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4)

pyautogui.click(x=739, y=396)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)

# Passo 4: Abrir a base de dados (importar o arquivo)
tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=731, y=278)
    
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.scroll(5000)