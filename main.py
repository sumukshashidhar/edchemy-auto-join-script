"""
A Script for automatically joining classes
on edchemy
"""

# IMPORTS
from selenium import webdriver
import pyautogui
import time


# CONSTANTS
studentid = ""
passer = ""
chromedriver = "/Applications/chromedriver"
driver = webdriver.Chrome(chromedriver)


# HELPER FUNCTIONS
def get_time():
    return time.localtime()


def get_day():
    return time.strftime("%A", get_time())


def get_hours():
    return int(time.strftime("%H", get_time()))


def get_minutes():
    return int(time.strftime("%M", get_time()))


def determine_timings():
    ps = (
            (7, 30), 
            (8, 45), 
            (10, 0), 
            (11, 15), 
            (12, 45), 
            (13, 0), 
            (14, 0)
            )
    # to determine the day's timings
    day = get_day()
    print("Today is: ", day)
    if day == "Monday":
        return []
    elif day == "Tuesday":
        return []
    elif day == "Wednesday":
        return [ps[1], ps[3], ps[4], ps[6]]
    elif day == "Thursday":
        return [ps[0], ps[1], ps[4]]
    elif day == "Friday":
        timings = []
    return


def login(studentid, password):
    driver.get("https://edchemy.kumarans.org")
    driver.maximize_window()
    time.sleep(1.2)
    driver.find_element_by_xpath('//*[@id="sn_login_id"]').send_keys(studentid)
    driver.find_element_by_xpath(
        '//*[@id="sn_login_password"]'
        ).send_keys(passer)
    driver.find_element_by_xpath('//*[@id="sn_login_form"]/button').click()


def joinclass(period):
    time.sleep(1.2)
    driver.find_element_by_xpath(
        '//*[@id="online-class"]/div['+str(period)+']/div[2]/a'
        ).click()

    time.sleep(3)
    pyautogui.click(879, 256)
    time.sleep(4)
    pyautogui.click(755, 421)



def join_period():
    # meaning that we store whether we joined the period or not in a list
    flagarr = [True]*len(timings)
    ptr = 0  # points to the start of the array
    while ptr < len(timings):
        hm = get_hours(), get_minutes()
        if hm[0] > timings[ptr][0]:
            print(f"Period #{ptr+1} is over")
            flagarr[ptr] = False
            ptr += 1
        elif (hm[0] == timings[ptr][0] and (hm[1] - timings[ptr][1]) <= 10
                and flagarr[ptr]):
            login(studentid, passer)
            joinclass(ptr+1)
            flagarr[ptr] = False
            print(f"Joined period #{ptr+1}")
            ptr += 1
        else:
            time.sleep(100)


if __name__ == "__main__":
    timings = determine_timings()
    print(f"You have {len(timings)} classes today at \n {timings}")
    join_period()
