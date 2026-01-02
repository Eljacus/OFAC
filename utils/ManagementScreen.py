urlOfac = "https://sanctionssearch.ofac.treas.gov/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import re
import time

class ManagementScreen:
    def __init__(self):
        self.urlOfac = "https://sanctionssearch.ofac.treas.gov/"
        self.driver = None

    def openBrowser(self):
        optionsDriver = webdriver.ChromeOptions()
        optionsDriver.add_argument("--start-maximized")

        self.driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=optionsDriver)
        self.driver.get(self.urlOfac)

    def searchPerson(self, name: str, address: str, country: str)-> int:
        """
        Retorna la cantidad de resultados encontrados
        """

        waitTime = WebDriverWait(self.driver, 10)

        searchInput = waitTime.until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_txtLastName")))
        searchInput.clear()
        searchInput.send_keys(name)

        searchInputAddress = waitTime.until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_txtAddress")))
        searchInputAddress.clear()
        searchInputAddress.send_keys(address)

        selectCountryElement = Select(waitTime.until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_ddlCountry"))))

        if country is not None and country != "All":
            
            selectCountryElement.select_by_visible_text(country)
        
        else:
            selectCountryElement.select_by_visible_text("All")

        searchBtn = waitTime.until(EC.element_to_be_clickable((By.ID, "ctl00_MainContent_btnSearch")))
        searchBtn.click()

        time.sleep(3)

        resultsRecord = self.driver.find_element(By.ID, "ctl00_MainContent_lblResults")
        textResults = resultsRecord.text
        match = re.search(r"\d+", textResults)
        amount = int(match.group()) if match else 0

        return amount
        
    def MakeScreenshot(self, idPerson: int):
        folderScreenshots = "./screenshots"
        dateTimeNow = datetime.now().strftime("%Y%m%d")
        fileScreenshot = f"{dateTimeNow}_{idPerson}.png"
        pathFile = os.path.join(folderScreenshots, fileScreenshot)
        self.driver.save_screenshot(pathFile)
        print(f"Screenshot guardado: {pathFile}")

    def close(self):
        if self.driver:
            self.driver.quit()
