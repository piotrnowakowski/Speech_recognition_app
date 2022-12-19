from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# Set up the webdriver
driver = webdriver.Chrome()

# Wait for 3 seconds to give the browser time to open
time.sleep(3)

# Switch to the tab with the given title
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if driver.title == "LEK - Kurs - Więcej niż LEK":
        break

# Wait for 3 seconds to give the page time to load
time.sleep(3)

# Find the button by its name
button = driver.find_element(By.NAME, "Komentarze do slajdu 20")

# Click the button
button.click()

# Close the webdriver
driver.close()
