import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager#se comunica con el navegador y evita que cada vez que se actualiza el navegador haya que actualizar el driver
# el webdriver hace de nexo, comunicacion entre python y el navegador



@pytest.fixture (scope="module") #el scope evita repetir el login
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver

    driver.quit()