import PySimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select files to compress: ")
input2 = sg.Input()
choose_button2 = sg.FilesBrowse("Choose")

compress_button = sg.Button()
window = sg.Window("File")