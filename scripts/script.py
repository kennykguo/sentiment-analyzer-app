from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from bs4 import BeautifulSoup
import pandas as pd

# Initialize driver object to simulate Chrome browsing
driver = webdriver.Chrome()

# Opens the review link and sorts the reviews to the latest
url = 'https://www.google.com/maps/place/E-Gyu+Revolving+Sushi+%26+Korean+BBQ/@33.9137463,-84.2635713,17z/data=!4m8!3m7!1s0x88f5a78015986f1b:0xa31fb6f1de20ec6b!8m2!3d33.9137463!4d-84.2613826!9m1!1b1!16s%2Fg%2F11fphnvz8m'
driver.get(url)
wait = WebDriverWait(driver, 20)  # Increase wait time to 20 seconds

# Click on the menu button to filter reviews by most recent
menu_bt = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[7]/div[2]/button'))
)
menu_bt.click()

# Wait for the menu to appear and click on "Newest"
recent_rating_bt = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="action-menu"]/div[2]'))
)
recent_rating_bt.click()
time.sleep(3)

# Simulates scrolling down to load all the reviews and extracts the review body containers
for _ in range(900):
    ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

# Parse the page source with BeautifulSoup
response = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep(2)
review_elements = response.find_all('div', class_='jftiEf')

# Dictionary to hold all review elements
reviews_dict = {'name': [], 'rating': [], 'date': [], 'review': []}
review_counter = 0

# Extracts all elements needed for scraping and stores them into dictionary
for review in review_elements:
    name_element = review.find('div', 'd4r55')
    rating_element = review.find('span', "kvMYJc")
    date_element = review.find('span', "rsqaWe")
    review_element = review.find('span', "wiI7pd")

    name = name_element.text if name_element else None
    rating = rating_element.get("aria-label") if rating_element else None
    date = date_element.text if date_element else None
    review_text = review_element.text if review_element else None

    reviews_dict['name'].append(name)
    reviews_dict['rating'].append(rating)
    reviews_dict['date'].append(date)
    reviews_dict['review'].append(review_text)
    
    review_counter += 1
    if review_counter == 50:
        break

print(f"{len(reviews_dict['name'])} reviews extracted")

# Create a DataFrame from the reviews dictionary
reviews_df = pd.DataFrame(reviews_dict)

# Export the DataFrame to a CSV file
reviews_df.to_csv('reviews.csv', index=False)

# Close the driver
driver.quit()
