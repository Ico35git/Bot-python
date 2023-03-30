from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from os import getenv
from time import sleep
import main
import datetime

load_dotenv()

USERNAME = 'Ico35'
PASSWORD = getenv('PASSWORD')
CODICE_SCUOLA = getenv('CODICE_SCUOLA')

LINK_REGISTRO = "http://www.sg25557.scuolanext.info/"

def compiti():

    chrome_driver = ChromeDriverManager().install()
    driver = Chrome(service=Service(chrome_driver))
    driver.maximize_window()

    driver.get(LINK_REGISTRO)

    print("\nAccedo al registro...")
    main.say("Accedo al registro...")

    sleep(3)

    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    submit_button = driver.find_element(By.ID, 'accediBtn')

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    submit_button.click()

    sleep(5)

    servizi_classe_button = ""

    try:
        servizi_classe_button = driver.find_element(By.ID, '_idJsp16')
    except:
        sleep(3)
        servizi_classe_button = driver.find_element(By.ID, '_idJsp16')

    servizi_classe_button.click()

    sleep(5)

    buttons = ""

    try:
        buttons = driver.find_elements(By.CLASS_NAME, 'btl-button-overlay')
    except:
        sleep(3)
        buttons = driver.find_elements(By.CLASS_NAME, 'btl-button-overlay')

    compiti_button = buttons[11]
    compiti_button.click()

    sleep(5)

    date = datetime.date.today()
    driver.save_screenshot(f"./compiti-{date}.png")

    driver.quit()

    print("Ho creato un'immagine nella cartella dell'applicazione con i compiti!")
    main.say("Ho creato un'immagine nella cartella dell'applicazione con i compiti!")

    main.Main()

    input()