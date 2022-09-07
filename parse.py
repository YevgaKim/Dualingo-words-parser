#the translator will be banned if you use the script often
import csv
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from translate import Translator
import re

driver = webdriver.Chrome(
        executable_path="C:\\Users\\ЯкименкоЄвгенійСергі\\source\\repos\\work\\chromedriver"
    )
try:

    driver.get(url="https://www.duolingo.com/words")
    time.sleep(60)

    with open("index_selenium.html", "w",encoding="utf-8") as file:
        file.write(driver.page_source)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
with open("index_selenium.html","r",encoding="utf-8") as file:
        src = file.read()

soup = BeautifulSoup(src,"html.parser")

result = soup.findAll("tr",class_="g_Zzj")

translator = Translator(from_lang="en",to_lang="ru")

with open('words.csv', 'w',newline="") as file:
    fieldnames = ['English', 'Translate']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    count=0
    for i in result:
        if "_2BiYf _2_Hk0 _1G1lu" in str(i):
            word=i.find("span").text
            word_trans=translator.translate(word)
            if not re.match(r"[^a-zA-Z]",word_trans): #translator translates words badly(half words were translated badly)
                continue
            else:
                writer.writerow({'English':word,'Translate':word_trans.lower()})#this file contains the full correct words
            count+=1

            print(f"Complited: {count}")

