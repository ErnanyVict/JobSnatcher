from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import SetLink, DatasJobs
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
QLineEdit, QPushButton, QFileDialog)
import sys

path_driver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=path_driver)
chrome_browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
app = QApplication(sys.argv)
link = SetLink(chrome_browser) # instanciar link
data_jobs = DatasJobs(chrome_browser)


window = QMainWindow()
window.setWindowTitle("JobSnatcher")
window.setStyleSheet("background-color: #D4D4D4")
all_widgets_menu = []
all_widgets_result = []

def select_folder_and_save_file():
    file_path = QFileDialog.getSaveFileName(window, dir=f'C:\\Searchs-Results-{link.profession}.txt')
    try:
        with open(file_path[0], 'w', encoding='utf-8') as file:
            content = ""
            i = 0
            result_names = data_jobs.results[0]
            result_empresas = data_jobs.results[1]
            result_locals = data_jobs.results[2]
            while i < data_jobs.quantity_searchs:
                content += f"{result_names[i]}\n"
                content += f"{result_empresas[i]}\n"
                content += f"{result_locals[i]}\n\n"
                i += 1
            file.write(content)
        print(file_path)
    except:
        print("ERROR. Failed to save the file")

title = QLabel("Searchs Works", window)
title.setStyleSheet(f'font-size: {30}px')
title.move(300, 30)
title.resize(200, 50)
all_widgets_menu.append(title)

info_display_vacancy = QLabel("Job Title", window)
info_display_vacancy.setStyleSheet(f'font-size: {20}px')
info_display_vacancy.move(30, 150)
info_display_vacancy.resize(200, 50)
all_widgets_menu.append(info_display_vacancy)

display_vacancy = QLineEdit(window)
display_vacancy.setStyleSheet(f'font-size: {20}px; background-color: white')
display_vacancy.move(30, 190)
display_vacancy.resize(200, 40)
all_widgets_menu.append(display_vacancy)

info_display_quantity = QLabel("Number of Results", window)
info_display_quantity.setStyleSheet(f'font-size: {20}px')
info_display_quantity.move(550, 150)
info_display_quantity.resize(250, 50)
all_widgets_menu.append(info_display_quantity)

display_quantity = QLineEdit(window)
display_quantity.setStyleSheet(f'font-size: {20}px; background-color: white')
display_quantity.move(550, 190)
display_quantity.resize(200, 40)
all_widgets_menu.append(display_quantity)

def back_menu():
    for widget in all_widgets_result:
        widget.deleteLater()
    all_widgets_result.clear()
    for widget in all_widgets_menu:
        widget.show()

def back_menu_and_open_result():
    y = 100
    x = 30
    for widget in all_widgets_menu:
        widget.close()

    result_names = data_jobs.results[0]
    result_company = data_jobs.results[1]
    result_locations = data_jobs.results[2]
    i = 0
    while (i < data_jobs.quantity_searchs):
        if i == 6:
            x = 450
            y = 100

        name = QLabel(result_names[i], window)
        name.setStyleSheet(f'font-size: {15}px')
        name.move(x, y)
        name.resize(400, 30)
        name.show()
        all_widgets_result.append(name)

        company = QLabel(result_company[i], window)
        company.setStyleSheet(f'font-size: {14}px')
        company.move(x, y+25)
        company.resize(400, 30)
        company.show()
        all_widgets_result.append(company)

        location = QLabel(result_locations[i], window)
        location.setStyleSheet(f'font-size: {15}px')
        location.move(x, y+50)
        location.resize(400, 30)
        location.show()
        all_widgets_result.append(location)

        i += 1
        y += 100
    
    select_folder_button = QPushButton("Save", window)
    select_folder_button.setStyleSheet(f'font-size: {20}px; background-color: white')
    select_folder_button.move(500, 30)
    select_folder_button.setFixedSize(200, 40)
    select_folder_button.show()
    select_folder_button.clicked.connect(select_folder_and_save_file)
    all_widgets_result.append(select_folder_button)

    back_menu_button = QPushButton("<-", window)
    back_menu_button.setStyleSheet(f'font-size: {20}px; background-color: white')
    back_menu_button.move(30, 30)
    back_menu_button.setFixedSize(200, 40)
    back_menu_button.show()
    all_widgets_result.append(back_menu_button)
    back_menu_button.clicked.connect(back_menu)

def search_and_make_button():
    link.profession = display_vacancy.text() # input profissão
    data_jobs.quantity_searchs = int(display_quantity.text())
    chrome_browser.get(link.get_link())
    data_jobs.get_datas_jobs() 
    
    button_of_result = QPushButton("Results", window)
    button_of_result.setStyleSheet(f'font-size: {20}px; background-color: white')
    button_of_result.move(30, 400)
    button_of_result.setFixedSize(200, 40)
    button_of_result.show()
    button_of_result.clicked.connect(back_menu_and_open_result)
    all_widgets_menu.append(button_of_result)

button_search = QPushButton("Search", window)
button_search.setStyleSheet(f'font-size: {20}px; background-color: white')
button_search.move(310, 300)
button_search.resize(200, 40)
button_search.clicked.connect(search_and_make_button)
all_widgets_menu.append(button_search)

window.adjustSize()
window.setFixedSize(800, 600)
window.show()
app.exec()