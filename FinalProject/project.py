import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox


user_name = None
user_password = None
remember_me = None
w_login = None
def main():
    login_window()
    mainApp()
        

def check_credentials(user, password):
    global w_login
    scope =  ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(os.getcwd(),r"FinalProject/mathapp_client_secret.json"), scope)
    client = gspread.authorize(creds)
    sheet = client.open('math_users').sheet1
    users = sheet.col_values(1)[1:]
    if user in users:
        print("user found")
        fuser = sheet.find(user)
        print("User is in the database")

        if sheet.cell(fuser.row, 2).value == password:
            w_login.destroy()
            mainApp()
            return True
        else:
            messagebox.showerror("Error", "Incorrect password")
    else:
        messagebox.showerror("Error", f"User {user} does not exist")


def login_window():
    global user_name, user_password, remember_me, w_login


    #login window    
    w_login = ttk.Window(themename="flatly")
    w_login.title("Login")
    w_login.geometry('250x360+1030+360')
    ttk.Label(w_login, text="Login", font="Calibri 24 bold").pack(pady=20)
    f_login = ttk.Frame(w_login, width = 250, height = 400)
    f_login.pack_propagate(False)

    #login variables
    user_name = tk.StringVar()
    user_password = tk.StringVar()
    remember_me = ttk.IntVar()

    l_username = ttk.Label(master=f_login,text="Email address", anchor="w", justify="left",width=22).pack()
    e_user_name = ttk.Entry(master=f_login,justify="left",width=20,textvariable=user_name).pack(padx=10,pady=(2, 10))

    l_password = ttk.Label(master=f_login, text="Password", anchor="w", justify="left", width=22).pack()
    e_user_password = ttk.Entry(master=f_login, textvariable=user_password, show="*").pack(padx=10, pady=(2, 4))

    f_remember_me = ttk.Frame(f_login)
    t_remember_me = ttk.Checkbutton(f_remember_me, variable=remember_me).pack(side="left")
    l_remember_me = ttk.Label(f_remember_me, text="Remember me").pack(side="left")
    f_remember_me.pack()

    b_login = ttk.Button(master=f_login, text="Login", command= lambda: check_credentials(user_name.get(), user_password.get())).pack(padx=5, pady=5)
    b_sign_up = ttk.Button(master=f_login, text="Sign Up", command= lambda:[w_login.destroy(),signup_window()]).pack(padx=5, pady=5)
    
    f_login.pack()
    w_login.mainloop()

def signup_window():
    #signup window    
    w_signup = ttk.Window(themename="flatly")
    w_signup.title("Signup")
    w_signup.geometry("250x360+1030+360")
    ttk.Label(w_signup, text="Signup", font="Calibri 24 bold").pack(pady=20)
    f_signup = ttk.Frame(w_signup, width = 250, height = 400, borderwidth= 1, relief="solid")
    f_signup.pack_propagate(False)
    user_name = tk.StringVar()
    user_password = tk.StringVar()
    user_password_reentry = tk.StringVar()
    l_username = ttk.Label(master=f_signup,text="Email address", anchor="w", justify="left",width=22).pack()
    e_user_name = ttk.Entry(master=f_signup,justify="left",width=20,textvariable=user_name).pack(padx=10,pady=(2, 10))
    l_password = ttk.Label(master=f_signup,text="Password", anchor="w", justify="left",width=22).pack()
    e_password = ttk.Entry(master=f_signup,justify="left",width=20,textvariable=user_password).pack(padx=10,pady=(2, 10))
    l_password_reentry = ttk.Label(master=f_signup,text="Repeat Password", anchor="w", justify="left",width=22).pack()
    e_password_reentry = ttk.Entry(master=f_signup,justify="left",width=20,textvariable=user_password_reentry).pack(padx=10,pady=(2, 10))
    b_sign_up = ttk.Button(master=f_signup, text="Sign up", command= lambda: check_credentials(user_name.get(), user_password.get())).pack(padx=5, pady=5)
    b_back = ttk.Button(master=f_signup, text="Back", command= lambda:[w_signup.destroy(), login_window()]).pack(padx=5, pady=5)
    f_signup.pack()
    w_signup.mainloop()

def mainApp():
    w_main = ttk.Window(themename="flatly")
    w_main.title("Math App")
    w_main.geometry("600x800+680+360")
    w_main.propagate(False)    
    l_frame = ttk.Frame(w_main, height=800, width=200, borderwidth= 1, relief="solid")
    l_frame.pack(side="left")
    w_main.mainloop()


if __name__ == "__main__":
    main()