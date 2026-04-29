from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login(driver, username, password):
    driver.get("https://www.facebook.com")
    # enter_username(driver, username)
    # enter_password(driver, password)
    # click_login(driver)
    input()
    driver.get("https://www.facebook.com/pokes/?notif_id=1709071124273281&notif_t=poke&ref=notif")


def enter_username(driver, username):
    username_field = driver.find_element(By.ID, "email")
    username_field.send_keys(username)


def enter_password(driver, password):
    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys(password)


def click_login(driver):
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()


def get_account_name(driver, i):
    name_element_xpath = f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[{i}]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/span/span/span/a"
    return driver.find_element(By.XPATH, name_element_xpath).get_attribute("innerHTML")


def get_date_time(driver, i):
    date_time_element_xpath = f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[{i}]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/span"
    return driver.find_element(By.XPATH, date_time_element_xpath).get_attribute("innerHTML")


def poke_back(driver, i):
    poke_back_element_xpath = f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[{i}]/div/div/div[1]/div[2]/div[2]/div/div/div/div"
    driver.find_element(By.XPATH, poke_back_element_xpath).click()


def check_facebook_pokes(driver, bad_list):
    while True:
        i = 1
        while True:
            try:
                i += 1
                time.sleep(1)
                name = get_account_name(driver, i)
                if name in bad_list:
                    poke_back(driver, i)
                    dt = get_date_time(driver, i)
                    current_time = time.ctime(time.time())
                    print(name + " Poked Me At (" + dt + ")")
                    print("I Poked " + name + " Back! At (" + current_time + ")\n")
            except:
                break
        time.sleep(300)
        driver.refresh()
        print("--------------------------------------------------------------------------")
        print("Refreshed At (" + time.ctime(time.time()) + ")")
        print("--------------------------------------------------------------------------\n")


if __name__ == "__main__":

    poke_bad_list = ["Abdelrahman Ayman", "Mohamed Gad", "Moataz Ashraf",
                     "Mahmoud Elshahed",  "Omar Awad",   "Ahmed Amin"]

    Driver = webdriver.Firefox()
    Username = ""
    Password = ""
    try:
        login(Driver, Username, Password)
        check_facebook_pokes(Driver, poke_bad_list)
    finally:
        Driver.quit()
