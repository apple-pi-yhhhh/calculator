import PySimpleGUI as sg
from plyer import notification
#sg.theme("SandyBeach")
window = sg.Window('電卓',[[sg.Input()],[sg.Submit(button_text='Go!')]])
while True:
    event, values = window.read()
    if event == "Go!":
        print(eval(values[0]))
        break
    elif event == sg.WIN_CLOSED:
        break
window.close()
