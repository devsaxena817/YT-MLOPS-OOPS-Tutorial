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
            if self.loggedin:
                self.write_post()
            else:
                print("You need to sign in first.")
                self.menu()
        elif user_input == '4':
            if self.loggedin:
                self.message_friend()
            else:
                print("You need to sign in first.")
                self.menu()
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
    
    def write_post(self):
        post = input("Write your post here: ")
        print(f"Your post has been published: {post}\n")
        self.menu()
    
    def message_friend(self):
        friend = input("Enter your friend's name: ")
        msg = input(f"Write your message to {friend}: ")
        print(f"Message sent to {friend}: {msg}\n")
        self.menu()


obj = Chatbook()
