import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip = "enter todo")

add_button = sg.Button("Add")




window = sg.Window('My To-Do App', layout=[[label],[input_box,add_button]])
window.read()
window.close()

 