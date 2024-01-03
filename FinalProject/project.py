import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox
import bcrypt
import random

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
    w_login = ttk.Window()
    w_login.title("Login")
    w_login.geometry('250x360+1030+360')
    style = ttk.Style()
    style.theme_use("cyborg")
    ttk.Label(w_login, text="Login", font="Calibri 24 bold").pack(pady=20)
    f_login = ttk.Frame(w_login, width = 250, height = 400)
    f_login.pack_propagate(False)

    #login variables
    user_name = tk.StringVar()
    user_password = tk.StringVar()
    remember_me = ttk.IntVar()

    ttk.Label(master=f_login,text="Email address", anchor="w", justify="left",width=22).pack()
    ttk.Entry(master=f_login,justify="left",width=20,textvariable=user_name).pack(padx=10,pady=(2, 10))

    ttk.Label(master=f_login, text="Password", anchor="w", justify="left", width=22).pack()
    ttk.Entry(master=f_login, textvariable=user_password, show="*").pack(padx=10, pady=(2, 4))

    f_remember_me = ttk.Frame(f_login)
    ttk.Checkbutton(f_remember_me, variable=remember_me).pack(side="left")
    ttk.Label(f_remember_me, text="Remember me").pack(side="left")
    f_remember_me.pack()

    b_login = ttk.Button(master=f_login, text="Login", command= lambda: check_credentials(user_name.get(), user_password.get())).pack(padx=5, pady=5)
    b_sign_up = ttk.Button(master=f_login, text="Sign Up", command= lambda:[w_login.destroy(),signup_window()]).pack(padx=5, pady=5)
    
    f_login.pack()
    w_login.mainloop()

def signup_window():
    #signup window    
    w_signup = ttk.Window()
    w_signup.title("Signup")
    w_signup.geometry("250x360+1030+360")
    style = ttk.Style()
    style.theme_use("cyborg")
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

    w_main = ttk.Window()
    w_main.title("Math App")
    w_main.geometry("660x600+680+360")
    style = ttk.Style()
    style.theme_use("cyborg")
    w_main.propagate(False)
    b_frame = ttk.Frame(w_main, height=800, width=200)
    b_frame.pack(side="top", pady=10)

    m_frame = ttk.Frame(w_main,height=400, width=200)
    m_frame.pack(side="top", pady=2)

    paddingX, paddingY = 1, 1
    buttonW = 14

    ttk.Button(b_frame, text="User Info", width=buttonW, command= lambda: user_info(m_frame)).pack(padx=paddingX,pady=paddingY,side="left")
    ttk.Button(b_frame, text="Chalanges", width=buttonW, command= lambda: chalanges(m_frame)).pack(padx=paddingX,pady=paddingY,side="left")
    ttk.Button(b_frame, text="My Scoreboard", width=buttonW, command= lambda: my_score(m_frame)).pack(padx=paddingX,pady=paddingY,side="left")
    ttk.Button(b_frame, text="Leaderboard", width=buttonW, command= lambda: load_scoreboard(m_frame)).pack(padx=paddingX,pady=paddingY,side="left")
    ttk.Button(b_frame, text="Quit", width=buttonW, command= lambda: quit_application(w_main)).pack(padx=paddingX,pady=paddingY,side="left")
    ttk.Button(b_frame, text="Logout", width=buttonW, command=lambda:logout(w_main)).pack(padx=paddingX,pady=paddingY,side="left")
    user_info(m_frame)
    w_main.mainloop()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def user_info(frame):
    clear_frame(frame)
    ttk.Label(frame, text="Hello").pack()

def validate_numeric_input(action, value_if_allowed):
    # Check if the input is empty or a valid integer
    if action == '1':  # insert
        return value_if_allowed.isdigit() or value_if_allowed == ""
    return True

chalange_list = []


def check_answers(local_chalange, entry_widgets):
    user_answers = [entry.get() for entry in entry_widgets]
    chalange_list.extend(f"{chalange},{answer}" for chalange, answer in zip(local_chalange, user_answers))
    print(chalange_list)
    

def create_challenge(frame, x, operator, y):
    clear_frame(frame)
    local_chalange = []
    entry_widgets = []
    number_of_chalanges = 10
    for i in range(number_of_chalanges):
        x_value = random.randint(0, x.get())
        operator_val = operator.get()
        y_val = random.randint(0, y.get())
        local_chalange.append(f"{x_value},{operator_val},{y_val}")
        chal_frame = tk.Frame(frame, height=40, width=250)
        chal_frame.propagate(False)
        tk.Label(chal_frame, text=f"{x_value} {operator_val} {y_val} =", font="Calibri 16 bold").pack(side="left")
        vcmd = (chal_frame.register(validate_numeric_input), '%d', '%P')
        e_answer = ttk.Entry(chal_frame, justify="left", width=20, validate="key", validatecommand=vcmd)
        e_answer.pack(side="right",fill="x", expand=True, padx=10, pady=(2, 10))
        entry_widgets.append(e_answer)
        chal_frame.pack()


    bb_frame = tk.Frame(frame)
    tk.Button(bb_frame, text="Cancel", command=lambda:chalanges(frame), width=16).pack(side="left", padx=1, pady=1)
    tk.Button(bb_frame, text="Finish", command=lambda:check_answers(local_chalange, entry_widgets), width=16).pack(side="right", padx=1, pady=1)
    bb_frame.pack(side="left")
    
    print(chalange_list)
    print(local_chalange)


def on_slider_change(label_value, text ,value_var):
    label_value.config(text=f"{text}{value_var.get()}")

def set_operator(label_value, x_value, operator, y_value, operator_value):
    operator_value.set(operator)
    label_value.config(text=f"{x_value.get()} {operator} {y_value.get()} =")



def chalanges(c_frame):
    clear_frame(c_frame)
    button_frame = ttk.Frame(c_frame)#, borderwidth= 1, relief="solid")
    ttk.Button(button_frame, text="Addition", width=14, command=lambda: set_operator(operator_label, x_value_var, "+", y_value_var, operator_value)).pack(padx=1,pady=1,side="left")
    ttk.Button(button_frame, text="Substraction", width=14, command=lambda: set_operator(operator_label, x_value_var, "-", y_value_var, operator_value)).pack(padx=1,pady=1,side="left")
    ttk.Button(button_frame, text="Multiplication", width=14, command=lambda: set_operator(operator_label, x_value_var, "*", y_value_var, operator_value)).pack(padx=1,pady=1,side="left")
    ttk.Button(button_frame, text="Division", width=14, command=lambda: set_operator(operator_label, x_value_var, "\\", y_value_var, operator_value)).pack(padx=1,pady=1,side="left")
    button_frame.pack(side="top", padx=5,pady=5)

    dificulty_frame = ttk.Frame(c_frame, width=600, height=50)
    dificulty_frame.pack_propagate(False)
    x_dificulty_frame = ttk.Frame(dificulty_frame, width=250, height=50)
    x_dificulty_frame.pack_propagate(False)
    default_value = 10
    x_value_var = tk.IntVar()
    x_value_var.set(default_value)
    ttk.Scale(x_dificulty_frame, from_=0, to=100, orient="horizontal", variable=x_value_var, command=lambda value: on_slider_change(x_label_value, "X Range: ",x_value_var), length=100).pack(padx=1, pady=1, side="left")
    x_label_value = tk.Label(x_dificulty_frame, text="X Range: 0", padx=10, pady=10)
    x_label_value.pack(side="right")

    operator_label = tk.Label(dificulty_frame, text="10 + 10 =", padx=10,pady=10)
    operator_value_default = "+"
    operator_value = tk.StringVar()
    operator_value.set(operator_value_default)

    y_dificulty_frame = ttk.Frame(dificulty_frame, width=250, height=50)
    # y_dificulty_frame.pack_propagate(False)
    y_value_var = tk.IntVar()
    y_value_var.set(default_value)
    ttk.Scale(y_dificulty_frame, from_=0, to=100, orient="horizontal", variable=y_value_var, command=lambda value: on_slider_change(y_label_value, "Y Range: ",y_value_var), length=100).pack(padx=1, pady=1, side="right")
    y_label_value = tk.Label(y_dificulty_frame, text="Y Range: 0", padx=10, pady=10)
    y_label_value.pack(side="left")

    # ttk.Button(dificulty_frame, text="Medium", width=14).pack(padx=1,pady=1,side="left")
    # ttk.Button(dificulty_frame, text="Hard", width=14).pack(padx=1,pady=1,side="left")

    x_dificulty_frame.pack(side="left", padx=5,pady=5)
    operator_label.pack(side="left", padx=5, pady=5)
    y_dificulty_frame.pack(side="right", padx=5,pady=5)
    dificulty_frame.pack(side="top", padx=5,pady=5)

    ttk.Button(c_frame, text="Begin Chalange", width=14, command=lambda:create_challenge(c_frame, x_value_var, operator_value, y_value_var)).pack(padx=1,pady=1)

def my_score(frame):
    clear_frame(frame)
    ttk.Label(frame, text="My highest score in Addition is ****", font="Calibri 24 bold").pack()
    ttk.Label(frame, text="My highest score in Subtraction is ****", font="Calibri 24 bold").pack()
    ttk.Label(frame, text="My highest score in Multiplication is ****", font="Calibri 24 bold").pack()
    ttk.Label(frame, text="My highest score in Division is ****", font="Calibri 24 bold").pack()


def load_scoreboard(sb_frame):
    clear_frame(sb_frame)
    client = create_gspread_client()
    sheet = client.open('math_users')
    scoreboard = sheet.get_worksheet(1)
    all_scores = scoreboard.get_all_records()
    columns = ["Place", "User", "Score", "Time", "Date"]


    # style = ttk.Style()
    # style.configure("Custom.Treeview", background="#333333", foreground="white")
    # style.configure("Custom.Treeview.Heading", background="#333333", foreground="white")

    tree = ttk.Treeview(sb_frame, columns=columns, show="headings", height=20)#, style="Custom.Treeview")

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