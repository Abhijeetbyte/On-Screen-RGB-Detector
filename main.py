from tkinter import * # all
import pyautogui # For Cursor Coordinates
from PIL import ImageGrab # to capture rapid screenshot
import webbrowser
import clipboard as pc


root=Tk() #call tkinter function
root.geometry("380x480") #Width x Height 
root.resizable(False,False) # window always stay in same size 
root.title("On-Screen RGB Color Detector ") #Title bar
root.configure(background='white')

# Creating object of photoimage class
p1= PhotoImage(file = 'RGBwincon.png')
root.iconphoto(False, p1)# Setting icon of master window


# Controle Structure/Logic----------------------------------------------------------------------------


def Capture_RGB(event): # main function to capture RGB values from live screen

    if event.keysym=='c': # check c key is pressed ?

        print('Key press detected, RGB values :')

        pos = pyautogui.position() # Varible to store Cursore value
        pixelRGB = ImageGrab.grab().getpixel((pos)) # pass coordinate as x,y (pos)
        
        print(pos,pixelRGB)
        

        pc.copy(f" {pixelRGB}" ) # auto copy RGB values to clipboard/keyboard , tuple data type to string

        v = pc.paste() # for shell
        print('clipboard : ',v)

        #Push Cursor Coordinates & RGB value to GUI labels

        L1=Label(text="Cursor Coordinates , RGB Values ",font=('Helvetica',14,'bold'),width=30, height=4)
        L1.place(x=7,y=140)
        L2=Label(text=f" {pos},{pixelRGB} ",font=('Helvetica',14,'bold'),width=30, height=3)
        L2.place(x=7,y=200)

        L3=Label(root,text='Copied to clipboard \u2713',font=('Helvetica',10,'bold'), bg="white") #static label
        L3.place(x=120,y=280)

        
def open_link(*args): #function binded to clickable hyperlink label
    webbrowser.open_new("https://github.com/Abhijeetbyte/On-Screen-RGB-Detector")

   
  
# Graphical User Interface (GUI)--------------------------------------------------------------------------------


# Labels 
L0=Label(root,font=('Helvetica',15,'bold'),text="ON-SCREEN RGB COLOR DETECTOR ", borderwidth=3, relief="raised",justify=CENTER,bg="#FFDA2F",width=100) #Font Size/style, bg color (Head Label)
L0.pack(padx=2)

L4=Label(text="Point your mouse circure and \n\npress 'C' on keyboard to capture ",font=('Helvetica',12,'bold'),bg="white") #instruction label
L4.place(x=60,y=350) #Text, FontSize/style, bg color, Location

L5=Label(root,text=' \u24D8 About ', fg='lightblue', font=('Helvetica',12,'bold'), borderwidth=0.5, relief="sunken",bg="white") # open link (text label)
L5.place(x=10,y=60) # webbrowser link label position
L5.bind("<Button-1>", open_link)

#Buttons
root.bind('<KeyPress>', Capture_RGB) #Keyboard key as command to execute function

root.mainloop() #Execute tkinter
