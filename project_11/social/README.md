# Django-Web-Scrapper

Scrapping Data from social mediia accounts

Only GET METHOD TO BE IMPLEMENTED HERE
 in Django using Web scraping tools like Beautiful soup or chrome driver

# Pre-Requisites
- Python
- Chrome driver https://chromedriver.chromium.org/downloads
- Git
- 

# Steps to run:
- Make changes by installing chrome driver and installing Beautiful soup and other dependencies 
- Selenium , chrome driver , Beautiful soup , Pyutogui
- Run "python manage.py runserver" to start the server
- Hit the server http://127.0.0.1:8000/ then follow terminal

# TEMPLATE 1
    Scrap data from social media accounts like 
    * Facebook (Meta)
    * Instagram 
    * Twitter
    * Linkedin
    - Any 2 or more social media accounts



# TEMPLATE 2 
    * We would require The user's name , (username will make each of them unique) and their profile pic 
    * their number of followers , posts 
    - RESULT > IN REST FRAMEWORK


# TEMPLATE 3
    - Here based on User input in terminal (like python manage.py runserver) - You can also see the data in the terminal
    - Make sure you use Multiple exceptions (try/catch blocks) if profile is hidden or it is not int for the public view etc...
    - Optional -> Only logged in users can see the data or Use the Get method to get the data


# Additional changes to be done
- Go to https://chromedriver.chromium.org/downloads , according to ur system download it or use Beautiful soup to scrape data
- make sure you give the chrome driver path in ur file , so that it can detect the existence of it.
- Use selenium for web broswer automation
- Scroll till you find the right path of the data like if  you need to scrap element Use XPath or CSS selector or classname or id etc.
- Here you will find that the data is accurate
- Now you can run the project 


* FOR FB AND LINKEDIN You NEED TO LOGIN FIRST TO CHECK EACH SPECIFICATIONS
# Hint:
* driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys("your_email_id") 
send_keys('password')
send_keys(Keys.ENTER)
# Hint:
* What if there are multiple classes and you want to fetch the data then you can use CSS selector with classname with .dot.
* followers_class_name = '.'+ '.'.join('css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'.split(' '))  | driver.find_elements_by_css_selector(followers_class_name)

#### This Way u can access the data even if element has multiple fields
#### I hope You liked this Project, If not Do give me a feedback




