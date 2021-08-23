import pyautogui
print('\n') #blank line

print("             ON-SCREEN RGB COLOR DETECTOR          ")

print('\n')

print(""" R,G,B = 255,255,255   #Absolute White

 R,G,B =   0,  0,  0   #Absolute Black """)

print('\n')

print(""" Respectively For All Colors :

 R or G or B is (255, Represent Maximum Amount of that Color )

 R or G or B is (  0, Represent Minimum Amount Of that Color )""")

print('\n')

close=str(input("      --------- PRESS ENTER TO START ---------"))

print('\n')

print('[Cursor Coordinates]  [ RGB Values ]')
print('                                         #', end='')
print( pyautogui.displayMousePosition() )
