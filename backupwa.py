from selenium import webdriver
import praw


reddit = praw.Reddit(client_id = "k065ufeuiRB0lw", #
             client_secret = 'client_secret',
             user_agent = "RScraperAPI")

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\tiwar\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')


def scrape(sr, pl):
    for submission in reddit.subreddit(sr).hot(limit=int(pl)):
        msg_box.send_keys(submission.title + (' UPVOTES: {}'.format(submission.ups)) + " " + submission.url)
        button = driver.find_element_by_class_name('_1U1xa')
        button.click()

name = input('Enter the name of user or group : ')
sr = input('What subreddit you want them to see? : ')
limit = int(input('Limit of posts? : '))

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

scrape(sr, limit)
