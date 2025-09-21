class Chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""\nWelcome to Chatbook! How would you like to proceed?
1. Press 1 to signup
2. Press 2 to signin
3. Press 3 to write a post
4. Press 4 to message a friend
5. Press any other key to exit
                           
                            
-> """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        else:
            print("Goodbye!")
            exit()  
    
    def signup(self):
        email = input("Enter your email id: ")
        pwd = input("Set up your password: ")
        self.username = email
        self.password = pwd   # fixed typo here
        print("Signup successful!\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup first.\n")
        else:
            uname = input("Enter your email/username -> ")
            pwd = input("Enter your password -> ")
            if uname == self.username and pwd == self.password:
                print("Signin successful!\n")
                self.loggedin = True
            else:
                print("Invalid credentials, please try again.\n")
        self.menu()
    
    def my_post(self):
        if self.loggedin==True:
            txt=input('Enter your message here ->')
            print('Following content has been published->',txt)
        else:
            print('Please signin to write a post')
        self.menu()
    
    def sendmsg(self):
        if self.loggedin==True:
            txt=input('Enter your message here ->')
            frnd=input("Whom to send the message? ")
            print(f"Your message has benn sent to {frnd}")
        else:
            print('Please signin to send a message')
        self.menu()

            
       

obj = Chatbook()
