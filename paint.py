import pyautogui

distancia = 200

while distancia > 0:
    pyautogui.drag(distancia, 0,duration=0.5)
    distancia-=5    
    pyautogui.drag(0, distancia,duration=0.5)
    pyautogui.drag(-distancia, 0,duration=0.5)
    distancia-= 5
    pyautogui.drag(0,-distancia,duration=0.5)