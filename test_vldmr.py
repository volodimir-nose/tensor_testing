import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://fix-inside.tensor.ru/")

    def test_search_in_python_org(self):
        login_page = page.LoginPage(self.driver)
        login_page.login("check_rigth_user", "qwerty123")

    def staff_menu_open(self):
	buttonStaff_click = page.OpenStaff(self.driver)
	buttonStaff_click.staff()



'''           
    def tearDown(self):
        self.driver.close()
'''
if __name__ == "__main__":
    unittest.main()