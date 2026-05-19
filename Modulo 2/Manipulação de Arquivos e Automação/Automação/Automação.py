import pyautogui as ptg

# ptg.mouseInfo()

ptg.press("win")
ptg.write("chrome")
ptg.press("enter")

ptg.sleep(2)

ptg.write("www.youtube.com")

ptg.press("enter")

ptg.moveTo(849,217, duration=0.5)

ptg.sleep(3)
ptg.click()

ptg.write("Wasted times-The weeknd", interval=0.5)
ptg.press("enter")

ptg.moveTo(675,978, duration=0.7)
ptg.sleep(2)
ptg.click()