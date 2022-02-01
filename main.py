
from PIL import ImageGrab # to capture rapid screenshot
import pyautogui # For Cursor Coordinates
from tkinter import * # all


root=Tk() #call tkinter function
root.geometry("630x650") #Width x Height
root.resizable(False,False) # window always stay in same size 
root.title("On-Screen RGB Color Detector ") #Title bra
root.configure(background='white')



# Creating object of photoimage class
p1= PhotoImage(file = 'Images/RGBwincon.png')
root.iconphoto(False, p1)# Setting icon of master window



# Controle Structure/Logic----------------------------------------------------------------------------



Value=str('START') # Global varible to break while loop



def stop(*args): #function to get Selected value from list DropDown menu ( show_selected, button command)
    
        global Value # Passing global variables data between functions
        
        Value = 'STOP'
        
        print('stop Function value ', Value) # for shell
    
   
        
def show_RGB(*args):#function to get value of Cursor Coordinates & RGB in every 1000ms

        global Value # Passing global variables data between functions

        print('RGB Function value ',Value) # for shell
        

        if Value == 'START':

                pos = pyautogui.position() # Varible to store Cursore value
                pixelRGB = ImageGrab.grab().getpixel((pos)) # pass coordinate as x,y (pos)

                print(pos,pixelRGB)
 
                #Push Cursor Coordinates & RGB value to GUI labels
    
                L6=Label(text="[Cursor Coordinates]  [ RGB Values ]",font=('Helvetica',14,'bold'),bg="#f0f0f0",width=40, height=4).place(x=70,y=350)


                L7=Label(text=f"{pos,pixelRGB} ",font=('Helvetica',14,'bold'),bg="#f0f0f0",width=40, height=3).place(x=70,y=420)

                L1=Label(text=" Values update in every 3 seconds !",font=("Courier", 12),fg='red',bg="white").place(x=120,y=520) #Text, FontSize/style, bg color, Location ( instruction )


                
                root.after(3000, show_RGB)# Tkinter has it own while true loop (root.mainloop). to run another while loop function
                                  # use this (before mainloop) and that function have to run the same after(...) to work in loop.
                                  # root.after(time_ms, function_name_without_brackets )

        Value = 'START' # Preset the value for next loop

        

                
# Graphical User Interface (GUI)---------------------------------------------------------------------------------------------------------                                        



# Labels
L0=Label(root,font=('Helvetica',15,'bold'),text="ON-SCREEN RGB COLOR DETECTOR ", borderwidth=3, relief="raised",justify=CENTER,bg="#FFDA2F",width=100)#FontSize/style, bg color(Head Label)
L0.pack(padx=2)

L1=Label(text="R,G,B = 255,255,255 (Absolute White)",font=("Courier", 12, "italic"),bg="white").place(x=120,y=70) #Text, FontSize/style, bg color, Location ( instruction )
L2=Label(text="R,G,B = 0,  0,  0   (Absolute Black)",font=("Courier", 12, "italic"),bg="white").place(x=120,y=120)
L3=Label(text="Respectively For All Colors :",font=("Courier", 12, "italic"),bg="white").place(x=150,y=170)
L4=Label(text="R or G or B is (255, Represent Maximum Amount of that Color)",font=("Courier", 12, "italic"),bg="white").place(x=10,y=230)
L5=Label(text="R or G or B is (  0, Represent Minimum Amount Of that Color)",font=("Courier", 12, "italic"),bg="white").place(x=10,y=280) 

#Buttons
Show_Button=Button(text ="Stop",font=('Helvetica',12,'bold'), bg="#FFDA2F",fg="black",width=8,height=1, command = stop).place(x=80,y=570) #Clear All command button & location 
Stop_Button=Button(text ="Start",font=('Helvetica',12,'bold'), bg="#FFDA2F",fg="black",width=8,height=1, command = show_RGB).place(x=450,y=570) #Calculte Volume command button & location 


root.mainloop() #Execute tkinter
