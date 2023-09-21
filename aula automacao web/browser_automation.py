import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://www.gabrielcasemiro.com.br/atividade_pyautogui \n")

# Esperar a pagina abrir
time.sleep(5)

with open("membros.csv") as f:
    next(f)
    
    for line in f:
        line=line.strip()
        line=line.split(";")
        print("Dados: ", line)

        name=line[0]
        sex=line[1]
        email=line[2]
        phone=line[3]

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\nome.png", confidence=0.8), duration=1)
        pyautogui.typewrite(name, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\email.png", confidence=0.8), duration=1)
        pyautogui.typewrite(email, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\telefone.png", confidence=0.8), duration=1)
        pyautogui.typewrite(phone, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img\\sexo.png", confidence=0.8), duration=1)
        
        if sex=="Masculino":
            pyautogui.click(pyautogui.locateCenterOnScreen("img\\masculino.png", confidence=0.8), duration=1)
        else:
            pyautogui.click(pyautogui.locateCenterOnScreen("img\\feminino.png", confidence=0.8), duration=1)
        
        pyautogui.screenshot(f"cadastro_{name}.png")
        
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\botao_enviar.png", confidence=0.8), duration=1)

        time.sleep(3)

pyautogui.alert(text="Programa finalizado com sucesso!", title="Aviso do sistema", button="OK")


