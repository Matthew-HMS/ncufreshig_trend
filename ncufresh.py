import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import csv

account = os.getenv('IG_ACCOUNT')
password = os.getenv('IG_PASSWORD')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")

# Login
time.sleep(3)
name = driver.find_element(By.XPATH, "//*[@name = 'username']")
name.send_keys(account)
pword = driver.find_element(By.XPATH, "//*[@name = 'password']")
pword.send_keys(password)
time.sleep(3)
submit = driver.find_element(By.XPATH, "//Button[@type = 'submit']")
submit.click()

# finding post links
link = ["https://www.instagram.com/p/Ct8WDJPL5iM/?img_index=1", "https://www.instagram.com/p/CuBURQoSqAo/?img_index=1", "https://www.instagram.com/p/CuHEpMByMsJ/?img_index=1",
        "https://www.instagram.com/p/Cv6AzGkyc0g/?img_index=1", "https://www.instagram.com/p/CwAChXkLXcg/?img_index=1", "https://www.instagram.com/p/CwFZvNlSRMX/?img_index=1"]
link.extend(["https://www.instagram.com/p/CuQ6sIgvBgg/?img_index=1", "https://www.instagram.com/p/CuWCkumvZnm/?img_index=1", "https://www.instagram.com/p/Cud79xxLkVA/?img_index=1"])
link.extend(["https://www.instagram.com/p/CuixdR_r0Bx/?img_index=1", "https://www.instagram.com/p/CulGeuPygIJ/?img_index=1", "https://www.instagram.com/p/Cuqpu65rwMq/?img_index=1",
             "https://www.instagram.com/p/CwegYypPBRn/?img_index=1", "https://www.instagram.com/p/CwjuyORLM3p/?img_index=1"])
link.extend(["https://www.instagram.com/p/Cuy4nM8LmGA/?img_index=1", "https://www.instagram.com/p/Cu3gMRcrNrK/?img_index=1", "https://www.instagram.com/p/Cu84aSXrWl-/?img_index=1",
             "https://www.instagram.com/p/CwPDDI4LXoU/?img_index=1", "https://www.instagram.com/p/CwRlNt8rd9g/?img_index=1", "https://www.instagram.com/p/CwZiYCDLhl6/?img_index=1"])
link.extend(["https://www.instagram.com/p/CvEU5oKLW8y/?img_index=1", "https://www.instagram.com/p/CvJecefyV4U/?img_index=1", "https://www.instagram.com/p/CvOoBoYyDIT/?img_index=1"])


rows = []
name_list = ['Zoe', 'Wang', 'Justin', 'Julia', 'Chang']
post_num = [6, 3, 5, 6, 3]
index = 0

for j in range(name_list.__len__()):

    reach_list = []
    like_share_list = []
    
    for i in range(post_num[j]):
        time.sleep(5)
        driver.get(link[index])
        time.sleep(3)
        report = driver.find_element(By.XPATH, "//*[text()='查看洞察報告']")
        report.click()
        time.sleep(5)

        stats = driver.find_elements(By.XPATH, "//span[@data-bloks-name='bk.components.Text']")
        likes = int(stats[0].text.replace(',', ''))
        shares = int(stats[2].text.replace(',', ''))
        reach = int(stats[6].text.replace(',', ''))
        likes_shares = likes + shares

        print(likes, shares, reach, likes_shares)
        rows.append([name_list[j],likes, shares, reach, likes_shares])
        reach_list.append(reach)
        like_share_list.append(likes_shares)
        index += 1

    max_reach = max(reach_list)
    like_share_sum = sum(like_share_list)
    rows.append([name_list[j],None, None, max_reach, like_share_sum])
    rows.append([None, None, None, None, None])



# writing to csv file
field = ['name','likes', 'shares', 'reach', 'likes&shares']
with open('ncufresh.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    
    # writing the fields
    csvwriter.writerow(field)
    
    # writing the data rows
    csvwriter.writerows(rows)


# quit
time.sleep(10)
driver.quit()