import Test
from time import sleep

# XPATHS are path expression strings that make it easier to locate buttons and other elements on a webpage
# EXAMPLE: //*[@id='LogInButton'] corresponds to all elements of a webpage with an id of "LogInButton"
# XPATH FINDER CHROME EXTENSION:
# https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph?hl=en
# More on XPATHS: https://www.w3schools.com/xml/xpath_syntax.asp

def login(driver, email="test", password="test"):
    # Giving the driver website xpath arguments
    driver.click("//*[@id='LogInButton']") # click log in button on on home page

    driver.input("//*[@id='Email']", email) # type email into character with email xpath
    driver.input("//*[@id='Password']", password)

    driver.click("/html/body/div[1]/div/div[1]/div[1]/div[2]/form/input[3]") # click submit

def logout(driver):
    driver.click("//*[@id='LoggedInDropdownButton']")
    sleep(0.1)
    driver.click("/html/body/div[1]/div/nav/div/div[2]/div/div/div/div[3]/button") #logout button

def goToBrowser(driver):
    driver.click("//*[@id='LoggedInDropdownButton']")
    sleep(0.1)
    driver.click("/html/body/div[1]/div/nav/div/div[2]/div/div/div/div[3]/button") #logout button

def createTask(driver):
    driver.goTo("//*[@id='LoggedInDropdownButton']")
    sleep(0.1)
    driver.click("/html/body/div[1]/div/nav/div/div[2]/div/div/div/div[3]/button") #logout button


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    email = ""
    password = ""

    browser = Test.Browser()
    browser.goTo("http://ec2-3-101-67-121.us-west-1.compute.amazonaws.com/")

    # -----LOGIN----- #
    login(browser, email=email, password=password)
    sleep(2)
    print("login submitted")

    if browser.getAlertText() == "login success":
        print("login successful")
    else:
        print("login fail")
    # should probably create else if statements for other possible responses
    sleep(0.1)

    browser.acceptAlert()

    # -------------------------- #

    # -----LOGOUT------ #
    logout(browser)
    # -------------------------- #

    # -----CREATE TASK------ #
    # -------------------------- #

    # -----CREATE JOURNAL------ #
    # -------------------------- #



