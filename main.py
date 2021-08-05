import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

#automated the installation of pip packages
try:
    subprocess.call("pip3 install pandas")
    subprocess.call("pip3 install pyautogui")
except:
    pass

curtime = datetime.now().strftime("%H:%M")
print("Current time -> " + curtime)
def sign_in(meetingid, pswd):
    #Opens up the zoom app
    #change the path specific to your computer
    
    #If on windows use below line for opening zoom
    ZOOM_EXECUTABLE = "C:\\Users\\username\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
    subprocess.call(ZOOM_EXECUTABLE)
    
    #If on mac / Linux use below line for opening zoom
    #subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    
    print("Zoom launching")
    time.sleep(10) #wait for zoom launch
    print("Zoom launched")
    
    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    time.sleep(1)
    pyautogui.click()
    print("Join clicked")
    time.sleep(4)
    
    # Type the meeting ID
    #no need to click meeting id textbox because its allready focused
    pyautogui.write(meetingid)
    
    print("Entered meeting id")
    
    time.sleep(2)
    
    # Disables both the camera and the mic when joining please follow readme instructions
    #clicking check box are unreliable and unstable

    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    print("Join button clicked")
    time.sleep(5)
    
    #Types the password and hits enter
    #no need to click meeting password textbox because its allready focused
    
    pyautogui.write(pswd)
    time.sleep(1)
    pyautogui.press('enter')
    
    print("Password entered")
    print("End of a login cycle")
# Reading the file
df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):
        row = df.loc[df['timings'] == now]
        m_id = str(row.iloc[0,1])
        m_pswd = str(row.iloc[0,2])
        sign_in(m_id, m_pswd)
        time.sleep(40)
        print('signed in')
