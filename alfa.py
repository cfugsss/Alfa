from tkinter import ttk, Tk, RIDGE, messagebox
from tkcalendar import DateEntry

class Front:
    def __init__(self, win):
        self.win = win
        self.main()
    
    def main(self):
        #init main win
        self.win.geometry("650x450")
        self.win.title("Alfa by Cfugs")

        #heading frame and title
        self.heading = ttk.Frame(self.win)
        self.heading.pack()
        ttk.Label(self.heading, text="ALFA", font=("Cambria", 25)).grid(row=0,column=0,padx=5,pady=5)

        #mainbody frame with username and password entry
        self.mainBody = ttk.Frame(self.win)
        self.mainBody.pack()
        ttk.Label(self.mainBody, text="Username: ").grid(row=0,column=0,padx=5,pady=7)
        ttk.Label(self.mainBody, text="Password: ").grid(row=1,column=0,padx=5,pady=7)
        self.userIn = ttk.Entry(self.mainBody, text="Username").grid(row=0, column=1,columnspan=2,padx=5,pady=7)
        self.passIn = ttk.Entry(self.mainBody, text="Password", show="*").grid(row=1, column=1,columnspan=2,padx=5,pady=7)

        #mainbody frame including buttons
        ttk.Button(self.mainBody, text="Create Account", command=self.newUser).grid(row=3,column=0,columnspan=2,padx=5,pady=7)
        ttk.Button(self.mainBody, text="Log in", command=self.home).grid(row=3,column=2,padx=5,pady=7)

    def newUser(self):
        #clear main page
        self.heading.forget()
        self.mainBody.forget()

        #new heading frame
        self.heading = ttk.Frame(self.win)
        self.heading.pack()
        ttk.Label(self.heading, text="ALFA", font=("Cambria", 25)).grid(row=0,column=0,padx=5,pady=5)
        ttk.Label(self.heading, text="Create Your Account!", font=("Cambria", 17)).grid(row=1,column=0,padx=5,pady=5)

        #body frame - get information for account
        self.mainBody = ttk.Frame(self.win)
        self.mainBody.pack()
        ttk.Label(self.mainBody, text="Username: ").grid(row=0,column=0,pady=7,padx=5)
        self.nuser = ttk.Entry(self.mainBody, text="Username")
        self.nuser.grid(row=0,column=1,pady=7,padx=5)
        ttk.Label(self.mainBody, text="Password: ").grid(row=1,column=0,pady=7,padx=5)
        self.npass = ttk.Entry(self.mainBody, text="Password")
        self.npass.grid(row=1,column=1,pady=7,padx=5)
        ttk.Label(self.mainBody, text="Email: ").grid(row=2,column=0,padx=7,pady=5)
        self.nmail = ttk.Entry(self.mainBody, text="Your Email: ")
        self.nmail.grid(row=2,column=1,pady=7,padx=5)

        #body frame - create button
        ttk.Button(self.mainBody, text="Create Account", command=self.checkNew).grid(row=3,column=0,columnspan=2,pady=7,padx=5)

    def checkNew(self):
        pass
        # add entries from new user to db
        #messagebox "new acc created" - on ok - go back to main
        # if username or email not unique ( use try and except when adding info to db)
        # messagebox "email or username already in use"
        # on ok - go back to main
    
    def feed(self):
        self.ldrFrame.forget()
        self.feedFrame.pack()
        if self.feedcount == 0:
            self.feedcount = 1
            ttk.Label(self.feedFrame, text="example post 1").pack()
            ttk.Label(self.feedFrame, text="example post 2").pack()
            ttk.Label(self.feedFrame, text="example post 3").pack()
            ttk.Label(self.feedFrame, text="example post 4").pack()
        else:
            pass

        

    def leaderboard(self):
        self.feedFrame.forget()
        self.ldrFrame.pack()
        if self.ldrcount == 0:
            self.ldrcount = 1
            ttk.Label(self.ldrFrame, text="1. Cfugs").pack()
            ttk.Label(self.ldrFrame, text="2. Trump").pack()
            ttk.Label(self.ldrFrame, text="3. yamom").pack()
            ttk.Label(self.ldrFrame, text="4. joe biden").pack()
        else:
            pass


    

    def home(self):
        # FIRST
        # check self.userIn and passIn match with db
        # if no match pass this function (back to login screen)
        # if a match then continue
        # use try and except with if statement (for now well make the pages with no sign in)
        self.heading.forget()
        self.mainBody.forget()
        self.heading = ttk.Frame(self.win)
        self.heading.pack()
        ttk.Label(self.heading, text="ALFA", font=("Cambria", 25)).grid(row=0,column=0,padx=5,pady=5)

        self.feedcount = 0
        self.ldrcount = 0
        self.profile = 0


        self.mainMenu = ttk.Frame(self.win)
        self.mainMenu.pack()
        ttk.Button(self.mainMenu, text="Feed", command=self.feed).grid(row=0,column=0,padx=10,pady=5)
        ttk.Button(self.mainMenu, text="Leaderboard", command=self.leaderboard).grid(row=0,column=1,padx=10,pady=5)
        ttk.Button(self.mainMenu, text="Profile").grid(row=0,column=2,padx=10,pady=5)

        self.feedFrame = ttk.Frame(self.win)
        self.feedFrame.config(relief=RIDGE, padding=(30, 15))

        self.ldrFrame = ttk.Frame(self.win)
        self.ldrFrame.config(relief=RIDGE, padding=(30, 15))

        












root = Tk()
Front(root)

root.mainloop()     