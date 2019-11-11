from tkinter import *
import xlsxwriter
import smtplib
import random
import time

def varify():
    opt_info = opt.get()
    if(opt_info == str(x)):
        Label(screen2,text = "").pack()
        Label(screen2,text = "Success",bg = "green").pack()
        time.sleep(1.5)
        workbook = xlsxwriter.Workbook(username_info+".xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.write(0,0,username_info)
        worksheet.write(0,1,password_info)
        worksheet.write(0,2,email_info)
        worksheet.write(0,3,str(gender))
        workbook.close()
        username_input.delete(0,END)
        password_input.delete(0,END)
        email_input.delete(0,END)
    else:
        Label(screen2,text = "").pack()
        Label(screen2,text = "Try again",bg = "red").pack()
        Button(screen2,text = "Resend Opt",width = "10",height = "1",command = send_mail).pack()
        Label(screen2,text = "").pack()

def send_mail():
    global screen2
    email_address = "shivamyadav6205@gmail.com"
    email_password = "kirigaya1"
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        smtp.login(email_address,email_password)
        
        subject = "SHCS - Thank you for registering"
        global x
        x = random.randint(0000,9999)
        body = "Thank you for registering with us.\nHere is your varification code for completing further process.\n OTP -"+str(x)
        
        msg = "Subject:{}\n\n{}".format(subject,body)
        smtp.sendmail(email_address,email_info,msg)
    screen2 = Toplevel(screen)
    screen2.title("Varification")
    screen2.geometry("450x350")
    screen1.withdraw()
    global opt
    opt = StringVar()
    global opt_input
    Label(screen2,text = "Enter the varification code send to your mail address").pack()
    opt_input = Entry(screen2,textvariable = opt)
    opt_input.pack()
    Button(screen2,text = "Varify",width = "10", height = "1", command = varify).pack()
    
def register_user():
    global username_info
    global password_info
    global email_info
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    send_mail()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x350")
    global username
    global password
    global email
    global username_input
    global password_input
    global email_input
    global gender
    username = StringVar()
    password = StringVar()
    email = StringVar()
    gender = StringVar()
    
    screen.withdraw()
    
    Label(screen1,text = "Please enter your details").pack()
    Label(screen1,text = "").pack()
    Label(screen1,text = "Username *").pack()
    username_input = Entry(screen1,width = "30", textvariable = username)
    username_input.pack()
    Label(screen1,text = "Password *").pack()
    password_input = Entry(screen1,width ="30", textvariable = password)
    password_input.pack()
    Label(screen1,text = "Email *").pack()
    email_input = Entry(screen1,width = "30", textvariable = email)
    email_input.pack()
    Label(screen1,text = "").pack()
    Radiobutton(screen1,justify = LEFT,text="Male   ",textvariable = gender,value = "male").pack()
    Radiobutton(screen1,text="Female",textvariable = gender,value = "female").pack()
    Button(screen1,text = "Register",width = "10", height = "1", command = register_user).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x350")
    screen.title("Health Care")
    #photo = PhotoImage(file = "Screenshot (44).png")
    #w = Label(screen, image=photo)
    #w.pack()
    '''image1 = PhotoImage(file= "Screenshot (44).png")
    w = image1.width()
    h = image1.height()
    screen.geometry("%dx%d+0+0" % (w, h))

    cv = Canvas(width=w, height=h)
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=image1, anchor='nw')'''
    
    screen.configure(background = 'AntiqueWhite1')
    Label(text = "Smart Health Care",bg = "cyan",width = "300",height = "2",font = ("calibri",13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2",width = "10",command = "").pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2",width = "10",command = register).pack()
    
    screen.mainloop()
    
main_screen()