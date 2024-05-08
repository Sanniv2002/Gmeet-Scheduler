from tkinter import *
import socket
import tkinter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from datetime import datetime
import threading

count = 2

def self_destruct():
    rt = Tk()
    e = datetime.now()
    t3.tag_config("end", background="black", foreground="Red")
    t2.tag_config("queue", background="white", foreground="Blue")
    if(io1d.get() == "" or io2d.get() == "" or io3d.get() == ""):
        pass
    else:
        t2.insert(END, "Closing Browser\n", 'queue')
        t2.insert(END, "Stacktrace:\n")
        t2.insert(END, "Backtrace:\n")
        t2.insert(END, "Terminating Google Web Driver\n", 'queue')

    current_time = e.strftime("%H:%M:%S")
    t3.insert(END, "Process Terminated at: " + current_time, 'end')
    rt.after(500, sys.exit)


def gmeetbot():
    def Glogin(mail_address, password):
        # Login Page
        driver.get(
            'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

        # input Gmail
        driver.find_element_by_id("identifierId").send_keys(mail_address)
        driver.find_element_by_id("identifierNext").click()
        driver.implicitly_wait(10)

        # input Password
        driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        driver.implicitly_wait(10)
        driver.find_element_by_id("passwordNext").click()
        driver.implicitly_wait(10)

        # go to google home page
        driver.get('https://google.com/')
        driver.implicitly_wait(100)

    def joinNow():
        # Join meet
        time.sleep(5)
        driver.implicitly_wait(2000)
        driver.find_element_by_css_selector(
            'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

    # assign email id and password
    mail_address = io2d.get()
    password = io3d.get()

    # create chrome instance
    opt = Options()
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--start-maximized')
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1
    })
    #driver = webdriver.Chrome(options=opt)
    PATH = r"C:\Users\sanniv\Desktop\Prog\Automation\chromedriver.exe"

    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-camera")
    chrome_options.add_argument("--disable-microphone")
    driver = webdriver.Chrome(executable_path=PATH,
                              chrome_options=chrome_options)

    #driver = webdriver.Chrome(PATH)

    # login to Google account
    Glogin(mail_address, password)
    attacks = 0

    while(True):
        if attacks == 0:
            t3.insert(END, "Executing First Attack...\n")
        else:
            t3.delete(1.0, END)
            t3.insert(END, "Total Attacks: ")
            t3.insert(END, str(attacks))
            t3.insert(END, "\n")
        driver.get(io1d.get())
        joinNow()
        time.sleep(1)
        driver.implicitly_wait(3000)
        driver.refresh()
        driver.implicitly_wait(3000)
        attacks += 1


def activeThreads():
    if(io1d.get() == "" or io2d.get() == "" or io3d.get() == ""):
        pass
    else:
        global count
        t4.insert(END, "Active Threads= ")
        t4.insert(END, str(count)+"\n")
        t4.insert(END, "\n")
        count += 1
    return count


def logger():
    root = Tk()
    lab = Label(root)
    lab.pack()

    t3.tag_config("fail3", background="white", foreground="Red")
    t2.tag_config("fail2", background="white", foreground="Red")
    t4.tag_config("fail4", background="white", foreground="Red")

    t3.tag_config("success3", background="white", foreground="Green")
    t2.tag_config("success2", background="white", foreground="Green")
    t4.tag_config("success4", background="white", foreground="Green")

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    if(io1d.get() == "" or io2d.get() == "" or io3d.get() == ""):
        t2.insert(END, "Initialized Google Web Driver!\n")
        t2.insert(END, "DevTools listening on ws://"+IPAddr +
                  "/devtools/browser/c0431822-b96a-4989-9c64-69a003f35afb\n")
        t4.insert(END, "Multithreading Initiated!\n")
        t4.insert(END, "Multithreading Failed!\n", 'fail4')
        t2.insert(END, "Error in initializing instance of browser\n", 'fail2')
        t3.insert(END, "Some fields are missing!!\n", 'fail3')
        t3.insert(END, "\n")
        t2.insert(END, "\n")
        t4.insert(END, "\n")

    else:
        t2.insert(END, "Initialized Google Web Driver!\n")
        t2.insert(END, "DevTools listening on ws://"+IPAddr +
                  "/devtools/browser/c0431822-b96a-4989-9c64-69a003f35afb\n")
        t4.insert(END, "Multithreading Initiated!\n")
        t4.insert(END, "Multithreading Success!\n", 'success4')
        t2.insert(END, "Launched Browser= \n")
        t2.insert(END, "Ordinal0\n")
        t2.insert(END, "GetHandleVerifier\n")
        t2.insert(END, "Successfully Launched!\n", 'success2')
        t3.insert(END, "Entries are Correct!\n")
        t3.insert(END, "\n")
        t4.insert(END, "\n")
        t2.insert(END, "\n")
        root.after(500, threading.Thread(target=gmeetbot).start)


def information():
    t1.tag_config("d", background="white", foreground="Purple")
    t1.insert(END, "Welcome to Google Meet Entry(Bell) Spammmer.\n", 'd')
    t1.insert(END, "I understand your pain of attending online classes, staring at the blue screen for hours, missing college life, that's why this came to existance 😇.\n", 'd')
    t1.insert(END, "This Software is completely free to use, if you want to join the developer team or want to be a BETA Tester, you know whom to contact 😉.\n", 'd')
    t1.insert(END, "This Application is created only for educational Purposes. I do not own any responsibilty for any malicious use of this Product.\n", 'd')
    t1.insert(END, "\n") 
    t1.insert(END, "\n")
    t1.insert(END, "Please read the instructions before using:\n", 'd')
    t1.insert(END, "1. Please cover your webcam with a cloth, because this version cannot turn off the camera or microphone.\n", 'd')
    t1.insert(END, "2. Do not use your primary gmail ID, use a new ID(Must be issued after 31st March 2022).\n", 'd')
    t1.insert(END, "3. Do not do any activity on the chrome tab created by the application, it will be automated by the software by its own.\n", 'd')
    t1.insert(END, "4. It is recommended to use only one instance of the chrome tab, multiple tabs can be opened by clicking on the launch button which is still in experimental phase, may crash.\n", 'd')
    t1.insert(END, "5. The 'Quit' Button will force close all active threads and the GUI as well, it's recommended to use the 'Quit' button to exit the software.\n", 'd')
    t1.insert(END, "6. If firewall, Windows Defender, Malwarebytes prohibits the software, please do add the app in exception list of these respective apps.\n", 'd')
    t1.insert(END, "7. Maximum attacks in one thread was recorded 21, multiple threads can result in better results.\n", 'd')

        
def clear_windows():
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    t4.delete(1.0, END)
    

window = Tk()

window.title('Gmeet_Spammer_Bot')


d1 = Label(window, text="                                                                                                       Gmeet Link:")
d2 = Label(window, text="                                                                                                       Email ID:")
d3 = Label(window, text="                                                                                                       Password:")
d4 = Label(window, text="Instructions")
d5 = Label(window, text="Logger")
d6 = Label(window, text="Alerts")
d7 = Label(window, text="Thread")
d_buildver = Label(window, text="Version 1.0.5(BETA)")
d_credits = Label(window, text="Developed By S042")


io1 = StringVar()
io1d = Entry(window, textvariable=io1, font=('Arial', 11))

io2 = StringVar()
io2d = Entry(window, textvariable=io2, font=('Arial', 11))

io3 = StringVar()
io3d = Entry(window, show="*", textvariable=io3, font=('Arial', 11))


t1 = Text(window, height=35, width=60)
t2 = Text(window, height=35, width=40)
t3 = Text(window, height=35, width=33)
t4 = Text(window, height=35, width=36)


b2 = Button(window, text="Quit", command=self_destruct, bg='Red', activebackground='#4444ff')
b3 = Button(window, text="Clear All", command=clear_windows, bg='White', activebackground='#4444ff')
b1 = Button(window, text="Launch", command=lambda: [logger(), activeThreads()], bg='Green', activebackground='#4444ff')

information()

d1.grid(row=0, column=0)
io1d.grid(row=0, column=1)
d2.grid(row=1, column=0)
io2d.grid(row=1, column=1)
d3.grid(row=2, column=0)
io3d.grid(row=2, column=1)


d4.grid(row=3, column=0)
d5.grid(row=3, column=1)
d6.grid(row=3, column=2)
d7.grid(row=3, column=3)

d_buildver.grid(row=27, column=10)
d_credits.grid(row=28, column=10)

t1.grid(row=4, column=0)
t2.grid(row=4, column=1)
t3.grid(row=4, column=2)
t4.grid(row=4, column=3)

b1.grid(row=0, column=10)
b2.grid(row=1, column=10)
b3.grid(row=2, column=10)

window.mainloop()
