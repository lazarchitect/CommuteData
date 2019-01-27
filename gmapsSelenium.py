from selenium import webdriver
from time import sleep
from datetime import datetime

URL = """https://www.google.com/maps/dir/48+Sutton+Dr,+Manalapan+Township,+NJ+07726-8720,+USA/
3+Mountainview+Rd,+Warren,+NJ+07059,+USA/@40.4324339,-74.3722867,12.04z/
data=!4m14!4m13!1m5!1m1!1s0x89c3d3ffe71e64f3:
0x4ff899b88ef86b4c!2m2!1d-74.31134!2d40.286171!1m5!1m1!1s0x89c3bde69510cd01:0x1f8b6da905ddbcbc!2m2!1d-74.5742467!2d40.6456742!3e0"""

x = 0

def weekdayAsString(weekdayasInt):
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][weekdayasInt]


while x < 1000:
    driver = webdriver.Chrome()
    driver.get(URL)

    elem = driver.find_element_by_id("section-directions-trip-0")

    print(elem.text)

    textArray = elem.text.split("\n")

    print(textArray)
    
    duration = textArray[0]
    route = textArray[2]
    mileage = textArray[1]
    
    time = str(datetime.today())
    
    with open("commutes.csv", "a") as f:
        f.write(time+","+duration+","+route+","+mileage+"\n")

    driver.close()    
    
    sleep(30)
    x+=1