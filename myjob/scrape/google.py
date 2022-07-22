from selenium import webdriver



class Google(webdriver.Chrome, website):
    def __init__(self, driver_path):
        self.driver_path = driver_path
        super(Google, self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, *args):
        self.quit()

    def career_page(self):
        self.get(website)

    def search_interest(self, interest):
        search_field = self.find_element_by_id()
        search_field.clear()
        search_field.send_keys(interest)    