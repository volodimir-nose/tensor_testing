from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGIN_TEXT_FIELD = (By.ID, 'fld-loginName')
    PASSWORD_TEXT_FIELD = (By.ID, 'fld-loginPass')
    LOGIN_BUTTON = (By.ID, 'logButton')  

class First  # Page2 
    STAFF_LINK = (By.ID, 'ws-84sovlajb9nhr5291443554980615')
    OUR_COMPANY = (By.ID, 'ourOrg')
'''

  # Page2 
    STAFF_LINK = (By.ID, 'staff')
    OUR_COMPANY = (By.ID, 'ourOrg')

'''
  # Org window
    OUR_COMPANY_LINK =(By.ID, 'div_sjWbFxyYpyT')

  # Search in our company
    SEARCH_FIELD =(By.ID, 'fld-searchStaff')

  # Olesya card
    OPEN_CARD =(By.ID, 'userName409')
    CLOSE_CARD_BUTTON =(By.ID, 'ws-5ta8r5ifygxbhuxr1443549911386')

  # Back to page
    INITIALS_LINK =(By.ID, 'headerLeft')
#     EXIT = (By.ID, '//*[@id="headerLeft')