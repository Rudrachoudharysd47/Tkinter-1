from tkinter import *
window = Tk()

window.title('Simple Interest Calculator')
window.geometery("380x400")
window.configure(bg = 'yellow')

app_heading = Label(window , text = "Simple Interest Calculator" , fg = "black", bg = "yellow", font = ("Calibri", 20), bd = 5)

principal = Label(window , text = "Principle", fg = "black", bg="yellow" ,font = ("Calibri", 20), bd = 4)

rateofinterest = Label(window, text = "Rate Of Interest" , fg = "black", bg= "yellow", font = ("Calibri", 20),bd  = 4)
 
UserInfo = Entry(window , text = "" , bd=2, width  = 22)

time = Label(window, text = "Time" , fg = "black" , bg = "yellow" , font = ("Calibri", 20), fd = 4)

Button = ("Calculate")

Result = LabelFrame(window , )
def calculate_interest():
    p = float(principal.get())
    r = float(rateofinterest.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i , 2)

Showlabel.destroy()



result_frame = LabelFrame(window, text = "result", bg = "gret", font = ("Calibri", 12))
result_frame.pack(padx = 20, pady=20)
result_frame.place (x = 20, y = 300)

showlabel = Label(result_frame, text = "Your Result will be displayed here" , bg = "grey" , font = ("Calibri", 12) , width = 55)
showlabel.place  (x = 20, y = 20)
showlabel.pack()

message= Label(result_frame, text = "Interest on Is ."+str{p}+" at rate of interest "+str{r}+" for "+str{t}+"years is "+str{interest},  bg="gray", font =( "Calibri", 20), width = 55)
message.place(x = 20 , y = -40)
message.pack()
