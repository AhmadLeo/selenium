import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

sId = input('Enter your Sap Id: ')
sPass = input('Enter your Sap Password: ')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://hub.uol.edu.pk/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html?sap-client=500&sap-language=EN#Shell-home')

userTxt = driver.find_element_by_xpath('/html/body/div/div[4]/form/div[1]/div[1]/div/input')
userTxt.send_keys(sId)

passTxt = driver.find_element_by_xpath('/html/body/div/div[4]/form/div[1]/div[2]/div/input')
passTxt.send_keys(sPass)

logBtn = driver.find_element_by_xpath('/html/body/div/div[4]/form/div[3]/div[1]/button/span[1]')
logBtn.click()

time.sleep(18)

surveyTab = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/div/section/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/section/div/div[1]/div/div/ul/li[5]/div/a/div/div')
surveyTab.click()
time.sleep(2)

# warning = driver.find_element_by_xpath('//*[@id="__mbox-btn-1-content"]')
# warning.click()



infBtn = driver.find_element_by_xpath('/html/body/div[1]/div[1]/footer/div/button/span')
infBtn.click()




def mainTask():
    #step 1
    time.sleep(2)
    checkNum = 1
    for i in range(7):
        if checkNum != 4:
            check = driver.find_element_by_xpath('//*[@id="idApp1--q'+str(checkNum)+'n-Button"]/div')
            check.click()
            check.click()
        checkNum += 1
    inner1 = driver.find_element_by_xpath('//*[@id="idApp1--q4-inner"]')
    inner1.send_keys('k')
    inner2 = driver.find_element_by_xpath('//*[@id="idApp1--q8-inner"]')
    inner2.send_keys('k')
    nextBtn = driver.find_element_by_xpath('//*[@id="idApp1--id_wizStp1-nextButton-BDI-content"]')
    nextBtn.click()

    #step 2
    time.sleep(1)
    checkNum = 9
    for i in range(9):
        if checkNum != 13:
            check = driver.find_element_by_xpath('//*[@id="idApp1--q'+str(checkNum)+'n-Button"]/div')
            check.click()
            check.click()
        checkNum += 1
    inner1 = driver.find_element_by_xpath('//*[@id="idApp1--q13-inner"]')
    inner1.send_keys('k')
    inner2 = driver.find_element_by_xpath('//*[@id="idApp1--q18-inner"]')
    inner2.send_keys('k')
    nextBtn = driver.find_element_by_xpath('//*[@id="idApp1--id_wizStp2-nextButton-BDI-content"]')
    nextBtn.click()

    #step 3
    time.sleep(1)
    checkNum = 19
    for i in range(7):
        if checkNum != 22:
            check = driver.find_element_by_xpath('//*[@id="idApp1--q'+str(checkNum)+'n-Button"]/div')
            check.click()
            check.click()
        checkNum += 1
    inner1 = driver.find_element_by_xpath('//*[@id="idApp1--q22-inner"]')
    inner1.send_keys('k')
    inner2 = driver.find_element_by_xpath('//*[@id="idApp1--q26-inner"]')
    inner2.send_keys('k')
    nextBtn = driver.find_element_by_xpath('//*[@id="idApp1--id_wizStp3-nextButton-BDI-content"]')
    nextBtn.click()

    #step 4
    time.sleep(1)
    # checkNum = 28
    # for i in range(7):
        # if checkNum == 22:
        # check = driver.find_element_by_xpath('//*[@id="idApp1--q'+str(checkNum)+'n-Button"]/div')
    check = driver.find_element_by_xpath('//*[@id="idApp1--q27n-Button"]/div')
    check.click()
    check.click()
    check2 = driver.find_element_by_xpath('//*[@id="idApp1--q28n-Button"]/div')
    check2.click()
    check2.click()
    check2 = driver.find_element_by_xpath('//*[@id="idApp1--q29n-Button"]/div')
    check2.click()
    check2.click()
    check2 = driver.find_element_by_xpath('//*[@id="idApp1--q30n-Button"]/div')
    check2.click()
    check2.click()
    check2 = driver.find_element_by_xpath('//*[@id="idApp1--q31n-Button"]/div')
    check2.click()
    check2.click()
    check2 = driver.find_element_by_xpath('//*[@id="idApp1--q32n-Button"]/div')
    check2.click()
    check2.click()
    check2 = driver.find_element_by_xpath('//*[@id="idApp1--q33n-Button"]/div')
    check2.click()
    check2.click()
    # checkNum += 1
    # inner1 = driver.find_element_by_xpath('//*[@id="idApp1--q22-inner"]')
    # inner1.send_keys('k')
    # inner2 = driver.find_element_by_xpath('//*[@id="idApp1--q26-inner"]')
    # inner2.send_keys('k')
    nextBtn = driver.find_element_by_xpath('//*[@id="idApp1--id_wizStp4-nextButton-BDI-content"]')
    nextBtn.click()

    #step 5
    time.sleep(1)
    # checkNum = 34
    # for i in range(2):
        # if checkNum != 22:
    check = driver.find_element_by_xpath('//*[@id="idApp1--q34n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q35n-Button"]/div')
    check.click()
    check.click()
    # checkNum += 1
    inner1 = driver.find_element_by_xpath('//*[@id="idApp1--q36-inner"]')
    inner1.send_keys('k')
    inner2 = driver.find_element_by_xpath('//*[@id="idApp1--q37-inner"]')
    inner2.send_keys('k')
    time.sleep(2)
    nextBtn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/div/section/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div/section/article/section/article[5]/button/span/span/bdi')
    nextBtn.click()

    #step 6
    time.sleep(1)
    # checkNum = 38
    # for i in range(13):
        # if checkNum != 22:
    check = driver.find_element_by_xpath('//*[@id="idApp1--q38n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q39n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q40n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q41n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q42n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q43n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q44n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q45n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q46n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q47n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q48n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q49n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q50n-Button"]/div')
    check.click()
    check.click()
    # checkNum += 1
    # inner1 = driver.find_element_by_xpath('//*[@id="idApp1--q36-inner"]')
    # inner1.send_keys('k')
    # inner2 = driver.find_element_by_xpath('//*[@id="idApp1--q37-inner"]')
    # inner2.send_keys('k')
    time.sleep(2)
    nextBtn = driver.find_element_by_xpath('//*[@id="idApp1--id_wizStp6-nextButton-BDI-content"]')
    nextBtn.click()

    #step 7
    time.sleep(1)
    # checkNum = 51
    # for j in range(5):
        # if checkNum != 22:
    check = driver.find_element_by_xpath('//*[@id="idApp1--q51n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q52n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q53n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q54n-Button"]/div')
    check.click()
    check.click()
    check = driver.find_element_by_xpath('//*[@id="idApp1--q55n-Button"]/div')
    check.click()
    check.click()
    # checkNum += 1
    # inner1 = driver.find_element_by_xpath('//*[@id="idApp1--q36-inner"]')
    # inner1.send_keys('k')
    # inner2 = driver.find_element_by_xpath('//*[@id="idApp1--q37-inner"]')
    # inner2.send_keys('k')
    time.sleep(2)
    nextBtn = driver.find_element_by_xpath('//*[@id="idApp1--id_wizStp7-nextButton-BDI-content"]')
    nextBtn.click()
    # return 0

for i in range(5):
    mainTask()
    time.sleep(7)