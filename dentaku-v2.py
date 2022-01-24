import PySimpleGUI as sg
from plyer import notification
#sg.theme("SandyBeach")
window = sg.Window('電卓',[[sg.Input()],[sg.Submit(button_text='Go!')]])
while True:
    event, values = window.read()
    if event == "Go!":
        notification.notify(
            title = str(eval(values[0])),
            message = str(values[0]),
            app_name = '電卓',
            app_icon='./icon.ico'
        )
        break
    elif event == sg.WIN_CLOSED:
        break
window.close()