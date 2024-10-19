import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

import subprocess

def download_video(video_id, start_time, end_time):
    url = f"https://1733451806.rsc.cdn77.org/msccjb/{video_id}/{video_id}_original.mp4"

    command = ["ffmpeg", "-y", "-i", url, "-ss", start_time, "-to", end_time, "-c", "copy", "output1.mp4"]
    
    subprocess.run(command)

    p = subprocess.Popen(command)
    p.wait()

def get_video_id(url):
    options = Options()
    options.binary_location = "/Users/jgomes/Downloads/chrome-mac-x64/"

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    video_element = driver.find_element(By.CLASS_NAME, 'blocked-video')
    video_img = video_element.find_element(By.CSS_SELECTOR, "img.ng-star-inserted")

    src = video_img.get_attribute('src')
    driver.quit()
    return src.split("msccjb/")[1].split('/')[0]
    
def main(url, start_time, end_time):
    video_id = get_video_id(url)
    print(video_id)
    download_video(video_id, start_time, end_time)
    
if __name__ == "__main__":
    url = sys.argv[1]
    print(url)
    start_time = input("What is the approximate start time of the game in the format of HH:MM:SS? ")
    end_time = input("What is the approximate end time of the game in the format of HH:MM:SS? ")
    main(url, start_time, end_time)

#src="https://1733451806.rsc.cdn77.org/msccjb/5b315f77-69d6-43a3-b553-bc0b589104ca/5b315f77-69d6-43a3-b553-bc0b589104ca_original.mp4"></video>
