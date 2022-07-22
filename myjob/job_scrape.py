# from bs4 import BeautifulSoup
# import requests  

# # interests = [company.interest_one, company.interest_two, company.interest_three]
# # for interest in interests:
# #     website = company.website + "/?q=" + interest
    
# website = "https://careers.google.com/jobs/results/?q=frontend"

# def Google (website):
#     html_text = requests.get(website).text

#     print(html_text)
#     # soup = BeautifulSoup(html_text. 'lxml')
#     # job = soup.find_all('div', itemscope="itemscope")
 


# Google(website)

from selenium import webdriver

driver = webdriver.Chrome(executable_path= r"C:\Users\pc\SeleniumDriver\chromedriver.exe")


driver.get("https://careers.google.com/")
driver.maximize_window
driver.implicitly_wait(30)
search_field = driver.find_element_by_id('inline-search-input-query')
search_field.clear()
search_field.send_keys("Frontend")