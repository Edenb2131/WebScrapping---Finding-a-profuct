import requests
import bs4
from selenium import webdriver
import argparse

def telegram_bot_sendtext(bot_message):
    bot_token = ************************************ # Here you enter you token 
    bot_chatID = *********************************** # Here you enter you chatID number
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


parser = argparse.ArgumentParser(description="getting an html link from decatlon - check availability")
parser.add_argument('-p', '--path', required=True, help='getting the link to the product')
args = parser.parse_args()

print(args.path)


#result = requests.get("http://www.example.com")
#print(result.text)


driver = webdriver.Chrome()
url_search = args.path
# url = https://www.decathlon.co.il/iw/p/8491831_-20-.html - this is the suitcase
driver.get(url_search)
try:
    content = driver.find_element_by_xpath('//*[@id="availability_message"]')
except:
    content = driver.find_element_by_xpath('//*[@id="pr_add_to_cart"]')

if content.text == 'אין מספיק מוצרים במלאי':
    print("This product is out of stock")
    test = telegram_bot_sendtext("This product is out of stock")
else:
    print("Yay! go buy it!")
    test = telegram_bot_sendtext("You can now go buy your product")

print(test)

driver.close()

