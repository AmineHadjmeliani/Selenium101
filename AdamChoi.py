from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd 

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
url = 'https://www.adamchoi.co.uk/overs/detailed'
driver.get(url)

# select elements in the Country, League and Season
country = str(input('''select a country, ex: England
                    Country: '''))
league = str(input('''select a league, ex: Premier League
                   league: '''))
season = str(input('''select a season, ex: 21/22 
                   season: '''))

## Create a function to automate all the tasks
def load_data(country,league, season):
    
# locate and click on a button
    all_matches = driver.find_element(By.XPATH, '//label[@analytics-event= "All matches"]')
    all_matches.click()
    
# select dropdown and select element inside by visible text
    dropdown = Select(driver.find_element(By.ID, 'country'))
    dropdown.select_by_visible_text(country)
    
    dropdown = Select(driver.find_element(By.ID, 'league'))
    dropdown.select_by_visible_text(league)
    
    dropdown = Select(driver.find_element(By.ID, 'season'))
    dropdown.select_by_visible_text(season)
    
    ''' implicit wait (useful in JavaScript driven websites when elements need seconds 
        to load and avoid error "ElementNotVisibleException") ''' 
   
    time.sleep(6)
    
    # select elements in the table
    matches = driver.find_elements(By.TAG_NAME, 'tr')
    
    
# storage data in lists
    date = []
    home_team = []  
    score = []
    away_team = []
# looping through the matches list
    for match in matches:
        date.append(match.find_element(By.XPATH, "./td[1]").text)
        home_team.append(match.find_element(By.XPATH, "./td[2]").text)
        score.append(match.find_element(By.XPATH, "./td[3]").text)
        away_team.append(match.find_element(By.XPATH, "./td[4]").text)
    
    
## close the page    
    driver.quit()
    
## Storage the data in a dataframe
    df = pd.DataFrame({
        'date': date,
        'home_team': home_team,
        'score': score,
        'away_team': away_team})
    return df

def main():
    df=  load_data(country= country, league= league, season=season)
    print(df)
    
if __name__== "__main__":
    main()