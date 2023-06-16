from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import discord
#arg11 = 'Rondo_Środka'
#arg22 = 'Stadion_Miejski'
import time

#def return_generator(table):
#    for j in range(5):
#            if table[0][j] != "":
#                first_travel=first_travel+table[i][j]+" "
#
#    return(first_travel)




def travel_response(arg1, arg2):
    PATH = 'C:\chromedriver.exe'
    # //*[@id="rasp_cmp"]/div/div[6]/button[2]
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get("https://jakdojade.pl/POZNAN/trasa")
    time.sleep(1)
    cookies = driver.find_element(By.XPATH, '//*[@id="rasp_cmp"]/div/div[6]/button[2]')
    cookies.click()
    # replacing '_' -> ' '
    arg1 = arg1.replace("_", " ")
    arg2 = arg2.replace("_", " ")

    input1 = driver.find_element(By.XPATH,
                                 '/html/body/app-root/div/div/app-planner/app-search-form/div/app-planner-search-form/div/form/app-point-form-field[1]/div/app-editable-input/div/div[2]/input')
    input2 = driver.find_element(By.XPATH,
                                 '/html/body/app-root/div/div/app-planner/app-search-form/div/app-planner-search-form/div/form/app-point-form-field[2]/div/app-editable-input/div/div[2]/input')
    # input1 clear and send
    input1.send_keys('X')
    input1.clear()
    time.sleep(1)

    time.sleep(1)
    input1.send_keys(arg1)
    time.sleep(1)
    input1.send_keys(Keys.ENTER)

    # input2 send
    input2.send_keys(arg2)
    time.sleep(1)
    input2.send_keys(Keys.ENTER)
    time.sleep(1)
    findway = driver.find_element(By.XPATH,'/html/body/app-root/div/div/app-planner/app-planner-main/div/div[2]/div/app-search-button/button')
    findway.click()

    venichle_table = [[0] * 10 for i in range(5)]
    time_table = [[0] * 2 for i in range(5)]
    onfoot_table = [[0] * 1 for i in range(5)]
    changes = [[0] * 16 for i in range(5)]

    #class="vehicle-line-name vehicle-line-name-container__name ng-tns-c180-5 vehicle-line-name-basic"
#class="vehicle-line-name vehicle-line-name-container__name ng-tns-c180-6 vehicle-line-name-basic"

    time.sleep(1)
    trasa = driver.find_elements(By.CLASS_NAME, 'ng-star-inserted')


    #print(len(trasa)) 5
    j = 0
    k = 0
    l=0
    for i in range(5):
        trasa[i].click()
        time.sleep(5)
        venichles=driver.find_elements(By.CSS_SELECTOR,'[data-cy="vehicle-line-name"]')
        for ven_j in venichles:
            venichle_table[i][j]=ven_j.text
            if ven_j.text=='KW':
                venichle_table[i][j]=100
            j += 1
        #---------------------------------------------------------------------------------------------------------
        onfoot=driver.find_elements(By.CLASS_NAME,'route-partial-duration')
        print(onfoot[0].text)
        for onf_j in onfoot:
            print('nizej')
            print(onf_j.text)
            print('wyzej')
            onfoot_table[l]=onf_j.text
            l +=1


        times=driver.find_elements(By.CSS_SELECTOR,"div[class='route-part-hour']")
        time_len=len(times)
        time_table[i][0]=times[0].text
        time_table[i][1]=times[time_len-1].text
        #----------------------------------------------------------------------------------------------------------
        changes_name=driver.find_elements(By.CLASS_NAME,'truncate-middle')

        for cha_j in changes_name:
            changes[i][k] = cha_j.text
            k = k + 1
        changes_filtered = list(filter(lambda x: x != '', changes[0]))
        changes_filtered = changes_filtered[:16] + changes_filtered[16:]
        changes_filtered = [x for x in changes_filtered if x != 0]

        print(venichle_table)
        print(time_table)
        print(changes_filtered)

        venichle_message = ""
        for i in range(5):
            if int(venichle_table[0][i]) ==0:
                break
            if int(venichle_table[0][i]) >100:
                venichle_message=venichle_message+"Autobus "+venichle_table[0][i]+', '
            if int(venichle_table[0][i])  < 100:
                venichle_message = venichle_message + "Tramwaj " + venichle_table[0][i] + ', '
            if int(venichle_table[0][i])  == 100:
                venichle_message = venichle_message + "Podróż pociągiem "+ ', '

        time_message="**"+time_table[0][0]+' | '+time_table[0][1]+" | "+str(onfoot_table[0]) + " " +"**"

        change_message=""
        for i in changes_filtered:
            change_message=change_message+i+" "

        return(time_message+'\n'+venichle_message+'\n'+'**Przesiadki:**'+'\n'+change_message)
        break







        exit_menu=driver.find_element(By.XPATH,'/html/body/app-root/div/div/app-planner/div/app-header-route-details/app-header/div/div[1]/app-back-arrow-icon/button')
        exit.click()














#travel_response(arg11, arg22)
