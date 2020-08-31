from selenium import webdriver
import praw


reddit = praw.Reddit(client_id = "k065ufeuiRB0lw", #
             client_secret = "Y-N0RhWOTGdMHlG9WlslWbHMXYc",
             user_agent = "RScraperAPI")

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\tiwar\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
#setup done above----------------------------------------------------------------------

name = input('Enter the name of user or group : ')


user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

def scrape(sr, pl):
    for submission in reddit.subreddit(sr).hot(limit=int(pl)):
        msg_box.send_keys(submission.title + (' UPVOTES: {}'.format(submission.ups)) + " " + submission.url)
        button = driver.find_element_by_class_name('_1U1xa')
        button.click()

cont = True

while (cont == True):
    if (driver.find_element_by_name("//span[@text = "'Rscrap'")]")):
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        msg_box.send_keys('subreddit?-> ')
        srCategory = driver.find_elements_by_xpath("//*[contains(text(), 'Hello Rscrap')]")
        postsLimit = int(input('How many posts? -> '))
        scrape(srCategory, postsLimit)
