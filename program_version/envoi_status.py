from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def evoyer_status(chrome_path, user_data_path, profile):
    options = Options()
    options.binary_location = chrome_path # C:/Program Files/Google/Chrome/Application/chrome.exe
    options.add_argument(f"user-data-dir={user_data_path}") # C:/Users/username/AppData/Local/Google/Chrome/User Data/Profile [number]
    options.add_argument(f'--profile-directory={profile}')
    driver = webdriver.Chrome(options=options)
    driver.get("https://moodle-miage-toulouse.westeurope.cloudapp.azure.com/login/index.php")
    longin_button = driver.find_element(By.CLASS_NAME,"loginbtn ")
    longin_button.click()
    sleep(1)
    driver.get("https://moodle-miage-toulouse.westeurope.cloudapp.azure.com/course/view.php?id=20&section=3#tabs-tree-start")
    sleep(1)
    activity_classes = driver.find_elements(By.CLASS_NAME,"activityname")
    for activity in activity_classes:
        try:
            activity.click()
        except:
            pass
    sleep(1)
    envoyer_status = driver.find_elements(By.PARTIAL_LINK_TEXT,"Envoyer le statut de présence")
    status_envoyes = 0
    for status in envoyer_status:
        try:
            status.click()
            status_envoyes += 1
            sleep(0.5)
        except:
            pass

    print(f"{status_envoyes}/{len(envoyer_status)} status validés")