import keyboard
import pyautogui
print(1 * '\n') #Two Blanks lines

print("             ON-SCREEN RGB COLOR DETECTOR          ")

print(2 * '\n') #Three Blanks lines)

print(" R,G,B = 255,255,255   #Absolute White ")

print(" R,G,B =   0,  0,  0   #Absolute Black",)

print(1 * '\n')

print("  Respectively For All Colors :" , '\n')

print(" R or G or B is (255, Represent Maximum Amount of that Color )", '\n')

print(" R or G or B is (  0, Represent Minimum Amount Of that Color )")

print(2 * '\n')

print("              'Press Space Key To Start'")

print(1 * '\n')#One blank line
while True:
     if keyboard.is_pressed('space'):
         print('[Cursor Coordinates]  [ RGB Values ]')
         print('                                         #', end='')
         print( pyautogui.displayMousePosition() )
