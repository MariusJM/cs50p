import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox
import bcrypt

user_name = None
user_password = None
remember_me = None
w_login = None
def main():
    check_saved_user()

SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
CREDENTIALS_FILE = os.path.join(os.path.join(os.path.dirname(__file__), "mathapp_client_secret.json"))

def create_gspread_client():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
    return gspread.authorize(creds)

def check_saved_user():
    rememberMe = open(os.path.join(os.path.dirname(__file__), "rememberMe.txt"))
    if rememberMe.readline() != "":
        rememberMe.close()
        mainApp()
    else:
        rememberMe.close()
        login_window()


def check_credentials(user, password):
    global w_login

    client = create_gspread_client()
    sheet = client.open('math_users').sheet1
    users = sheet.col_values(1)[1:]
    hashed_password = hash_password(password).decode("utf-8")
    if user in users:
        fuser = sheet.find(user)
        stored_hashed_password = sheet.cell(fuser.row, 2).value
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            if remember_me.get() == True:
                with open(os.path.join(os.getcwd(), r"FinalProject/rememberMe.txt"), "w") as rememberMe_file:
                    rememberMe_file.write(user)
                w_login.destroy()
                mainApp()
                return True
            else:
                w_login.destroy()
                mainApp()
                return True
        else:
            messagebox.showerror("Error", "Incorrect password")
    else:
        messagebox.showerror("Error", f"User {user} does not exist")

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def add_new_user(user, password, password_repeat, signupWindow):
    if password == password_repeat and password != "":
        client = create_gspread_client()
        sheet = client.open('math_users').sheet1
        users = sheet.col_values(1)[1:]
        if user in users:
            messagebox.showerror("Error", "User already exists")         
        else:
            hashed_password = hash_password(password).decode('utf-8')
            sheet.insert_row([user, hashed_password], 2)
            signupWindow.destroy()
            login_window()
    else:
        messagebox.showerror("Error", "Password does not match")

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
    user_name_su = tk.StringVar()
    user_password_su = tk.StringVar()
    user_password_reentry = tk.StringVar()
    l_username = ttk.Label(master=f_signup,text="Email address", anchor="w", justify="left",width=22).pack()
    e_user_name = ttk.Entry(master=f_signup,justify="left",width=20,textvariable=user_name_su).pack(padx=10,pady=(2, 10))
    l_password = ttk.Label(master=f_signup,text="Password", anchor="w", justify="left",width=22).pack()
    e_password = ttk.Entry(master=f_signup,justify="left",width=20,textvariable=user_password_su).pack(padx=10,pady=(2, 10))
    l_password_reentry = ttk.Label(master=f_signup,text="Repeat Password", anchor="w", justify="left",width=22).pack()
    e_password_reentry = ttk.Entry(master=f_signup,justify="left",width=20,textvariable=user_password_reentry).pack(padx=10,pady=(2, 10))
    b_sign_up = ttk.Button(master=f_signup, text="Sign up", command= lambda: add_new_user(user_name_su.get(), user_password_su.get(), user_password_reentry.get(), w_signup)).pack(padx=5, pady=5)
    b_back = ttk.Button(master=f_signup, text="Back", command= lambda:[w_signup.destroy(), login_window()]).pack(padx=5, pady=5)
    f_signup.pack()
    w_signup.mainloop()

def mainApp():
    w_main = ttk.Window(themename="flatly")
    w_main.title("Math App")
    w_main.geometry("660x600+680+360")
    w_main.configure(bg="#333333")
    w_main.propagate(False)
    b_frame = tk.Frame(w_main, height=800, width=200, borderwidth= 1, relief="solid", bg="#333333")
    b_frame.pack(side="top", pady=10)

    m_frame = tk.Frame(w_main,height=400, width=200, borderwidth= 1, relief="solid", bg="#333333")
    m_frame.pack(side="top", pady=10)

    paddingX, paddingY = 1, 1
    buttonW, buttonH = 14, 2

    b_userInfo = tk.Button(b_frame, text="User Info", width=buttonW, height=buttonH).pack(padx=paddingX,pady=paddingY,side="left")
    b_chalanges = tk.Button(b_frame, text="Chalanges", width=buttonW, height=buttonH).pack(padx=paddingX,pady=paddingY,side="left")
    b_userBestScore = tk.Button(b_frame, text="My Scoreboard", width=buttonW, height=buttonH).pack(padx=paddingX,pady=paddingY,side="left")

    b_leaderboard = tk.Button(b_frame, text="Leaderboard", width=buttonW, height=buttonH, command= lambda: load_scoreboard(m_frame)).pack(padx=paddingX,pady=paddingY,side="left")

    b_quit = tk.Button(b_frame, text="Quit", width=buttonW, height=buttonH, command= lambda: quit_application(w_main)).pack(padx=paddingX,pady=paddingY,side="left")
    b_logout = tk.Button(b_frame, text="Logout", width=buttonW, height=buttonH, command=lambda:logout(w_main)).pack(padx=paddingX,pady=paddingY,side="left")
    w_main.mainloop()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_scoreboard(sb_frame):
    clear_frame(sb_frame)
    client = create_gspread_client()
    sheet = client.open('math_users')
    scoreboard = sheet.get_worksheet(1)
    all_scores = scoreboard.get_all_records()
    columns = ["Place", "User", "Score", "Time", "Date"]


    style = ttk.Style()
    style.configure("Custom.Treeview", background="#333333", foreground="white")
    style.configure("Custom.Treeview.Heading", background="#333333", foreground="white")

    tree = ttk.Treeview(sb_frame, columns=columns, show="headings", height=20, style="Custom.Treeview")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center",)
    for data in all_scores:
        tree.insert("", "end", values=(data["Place"], data["User"], data["Score"], data["Time"], data["Date"]))
    tree.pack()

def quit_application(appwindow):
    answer = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if answer:
        appwindow.destroy()


def logout(appwindow):
    answer = messagebox.askyesno("Logout", "Are you sure you want to Logout?")
    if answer:
        with open(os.path.join(os.getcwd(), r"FinalProject/rememberMe.txt"), "r") as rememberMe_file:
            lines = rememberMe_file.readlines()
        if lines:
            lines.pop(0)
            with open(os.path.join(os.getcwd(), r"FinalProject/rememberMe.txt"), 'w') as file:
                file.writelines(lines)
        appwindow.destroy()
        login_window()




if __name__ == "__main__":
    main()