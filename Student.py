import streamlit as st
 
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthSystem:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)
        print("User registered successfully!")

    def login_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print("Login successful!")
                return
        print("Invalid username or password.")

# Web Application
class WebApp:
    def __init__(self):
        self.auth_system = AuthSystem()
        self.logged_in_user = None

    def display_menu(self):
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.auth_system.register_user(username, password)

            elif choice == "2":
                if self.logged_in_user:
                    print("Already logged in as", self.logged_in_user)
                else:
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    self.auth_system.login_user(username, password)
                    self.logged_in_user = username

            elif choice == "3":
                if self.logged_in_user:
                    print("Logout successful!")
                    self.logged_in_user = None
                else:
                    print("Not logged in.")

            elif choice == "4":
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    web_app = WebApp()
    web_app.run()
