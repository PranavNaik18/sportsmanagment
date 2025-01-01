import tkinter as tk
from tkinter import messagebox, font
from tkinter.ttk import Combobox, Style
import mysql.connector
import random
from PIL import Image, ImageTk  # Add this import for images

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="581359",  # Replace with the password you set during MySQL installation
        database="sports_management"
    )

# Generate unique IDs
def generate_unique_id(role):
    return f"{role}{random.randint(1000, 9999)}"

# Registration Page with improved UI
def registration_page():
    reg_window = tk.Tk()
    reg_window.title("Sports Management System")
    reg_window.geometry("1200x800")
    
    # Create a gradient effect with frames
    top_frame = tk.Frame(reg_window, bg="#1a237e", height=200)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(reg_window, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Title with shadow effect
    title_frame = tk.Frame(top_frame, bg="#1a237e")
    title_frame.pack(pady=50)
    
    main_title = tk.Label(title_frame, 
                         text="🏆 Sports Management System", 
                         font=("Helvetica", 36, "bold"),
                         fg="#ffffff",
                         bg="#1a237e")
    main_title.pack()
    
    subtitle = tk.Label(title_frame,
                       text="Choose your role to get started",
                       font=("Helvetica", 14),
                       fg="#90caf9",
                       bg="#1a237e")
    subtitle.pack(pady=10)

    # Buttons Frame
    button_frame = tk.Frame(main_frame, bg="#ffffff")
    button_frame.pack(pady=50)

    # Custom button style
    button_style = {
        'font': ('Helvetica', 12),
        'width': 25,
        'height': 2,
        'border': 0,
        'cursor': 'hand2'
    }

    # Player Registration Button with hover effect
    player_btn = tk.Button(button_frame,
                          text="Register as Player",
                          bg="#2196F3",
                          fg="white",
                          command=register_player,
                          **button_style)
    
    def on_enter(e):
        e.widget['background'] = '#1976D2'

    def on_leave(e):
        e.widget['background'] = '#2196F3'

    player_btn.bind("<Enter>", on_enter)
    player_btn.bind("<Leave>", on_leave)
    player_btn.pack(pady=10)

    # Coach Registration Button
    coach_btn = tk.Button(button_frame,
                         text="Register as Coach",
                         bg="#4CAF50",
                         fg="white",
                         command=register_coach,
                         **button_style)
    
    def on_enter_coach(e):
        e.widget['background'] = '#388E3C'

    def on_leave_coach(e):
        e.widget['background'] = '#4CAF50'

    coach_btn.bind("<Enter>", on_enter_coach)
    coach_btn.bind("<Leave>", on_leave_coach)
    coach_btn.pack(pady=10)

    # Add separator
    separator = tk.Frame(main_frame, height=2, bg="#e0e0e0")
    separator.pack(fill='x', padx=150, pady=20)

    # Login section
    login_label = tk.Label(main_frame,
                          text="Already have an account?",
                          font=("Helvetica", 12),
                          bg="#ffffff",
                          fg="#757575")
    login_label.pack()

    # Login button
    login_btn = tk.Button(main_frame,
                         text="Login Here",
                         bg="#FF5722",
                         fg="white",
                         font=("Helvetica", 12),
                         width=20,
                         height=2,
                         border=0,
                         cursor="hand2",
                         command=login_window)
    
    def on_enter_login(e):
        e.widget['background'] = '#F4511E'

    def on_leave_login(e):
        e.widget['background'] = '#FF5722'

    login_btn.bind("<Enter>", on_enter_login)
    login_btn.bind("<Leave>", on_leave_login)
    login_btn.pack(pady=10)

    # Footer
    footer_frame = tk.Frame(reg_window, bg="#f5f5f5", height=50)
    footer_frame.pack(fill='x', side='bottom')
    
    footer_text = tk.Label(footer_frame,
                          text="© 2024 Sports Management System",
                          font=("Helvetica", 10),
                          fg="#757575",
                          bg="#f5f5f5")
    footer_text.pack(pady=15)

    reg_window.mainloop()

# Register Player
def register_player():
    reg_window = tk.Tk()
    reg_window.title("Player Registration")
    reg_window.geometry("1200x800")

    # Create frames for layout
    top_frame = tk.Frame(reg_window, bg="#1a237e", height=150)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(reg_window, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Title
    tk.Label(top_frame,
             text="Player Registration",
             font=("Helvetica", 24, "bold"),
             fg="white",
             bg="#1a237e").pack(pady=50)

    # Form frame
    form_frame = tk.Frame(main_frame, bg="white")
    form_frame.pack(pady=40)

    # Input style
    entry_style = {
        'font': ('Helvetica', 12),
        'width': 30,
        'bg': '#f5f5f5',
        'relief': 'flat'
    }

    # Username
    tk.Label(form_frame,
             text="Username",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    username_entry = tk.Entry(form_frame, **entry_style)
    username_entry.pack(pady=(0, 15))

    # Phone
    tk.Label(form_frame,
             text="Phone Number",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    phone_entry = tk.Entry(form_frame, **entry_style)
    phone_entry.pack(pady=(0, 15))

    # Place
    tk.Label(form_frame,
             text="Place",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    place_entry = tk.Entry(form_frame, **entry_style)
    place_entry.pack(pady=(0, 15))

    # Password
    tk.Label(form_frame,
             text="Password",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    password_entry = tk.Entry(form_frame, show="•", **entry_style)
    password_entry.pack(pady=(0, 30))

    def submit_player():
        username = username_entry.get()
        phone = phone_entry.get()
        place = place_entry.get()
        password = password_entry.get()

        if username and phone and place and password:
            conn = connect_db()
            cursor = conn.cursor()

            # Remove player_id from the INSERT query, let MySQL auto-generate it
            cursor.execute("INSERT INTO Players (username, phone, place, password) VALUES (%s, %s, %s, %s)",
                        (username, phone, place, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Player registered successfully!")
            reg_window.destroy()
            login_window()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    # Submit button with hover effect
    submit_btn = tk.Button(form_frame,
                          text="Register",
                          font=("Helvetica", 12),
                          width=20,
                          height=2,
                          bg="#2196F3",
                          fg="white",
                          border=0,
                          cursor="hand2",
                          command=submit_player)
    
    def on_enter(e):
        e.widget['background'] = '#1976D2'

    def on_leave(e):
        e.widget['background'] = '#2196F3'

    submit_btn.bind("<Enter>", on_enter)
    submit_btn.bind("<Leave>", on_leave)
    submit_btn.pack()

    reg_window.mainloop()

# Register Coach
def register_coach():
    reg_window = tk.Tk()
    reg_window.title("Coach Registration")
    reg_window.geometry("1200x800")

    # Create frames for layout
    top_frame = tk.Frame(reg_window, bg="#1a237e", height=150)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(reg_window, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Title
    tk.Label(top_frame,
             text="Coach Registration",
             font=("Helvetica", 24, "bold"),
             fg="white",
             bg="#1a237e").pack(pady=50)

    # Form frame
    form_frame = tk.Frame(main_frame, bg="white")
    form_frame.pack(pady=40)

    # Input style
    entry_style = {
        'font': ('Helvetica', 12),
        'width': 30,
        'bg': '#f5f5f5',
        'relief': 'flat'
    }

    # Username
    tk.Label(form_frame,
             text="Username",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    username_entry = tk.Entry(form_frame, **entry_style)
    username_entry.pack(pady=(0, 15))

    # Phone
    tk.Label(form_frame,
             text="Phone Number",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    phone_entry = tk.Entry(form_frame, **entry_style)
    phone_entry.pack(pady=(0, 15))

    # Place
    tk.Label(form_frame,
             text="Place",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    place_entry = tk.Entry(form_frame, **entry_style)
    place_entry.pack(pady=(0, 15))

    # Password
    tk.Label(form_frame,
             text="Password",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    password_entry = tk.Entry(form_frame, show="•", **entry_style)
    password_entry.pack(pady=(0, 30))

    def submit_coach():
        username = username_entry.get()
        phone = phone_entry.get()
        place = place_entry.get()
        password = password_entry.get()

        if username and phone and place and password:
            coach_id = generate_unique_id("CO")
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Coaches (coach_id, username, phone, place, password) VALUES (%s, %s, %s, %s, %s)",
                           (coach_id, username, phone, place, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Coach registered successfully!")
            reg_window.destroy()
            login_window()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    # Submit button with hover effect
    submit_btn = tk.Button(form_frame,
                          text="Register",
                          font=("Helvetica", 12),
                          width=20,
                          height=2,
                          bg="#4CAF50",
                          fg="white",
                          border=0,
                          cursor="hand2",
                          command=submit_coach)
    
    def on_enter(e):
        e.widget['background'] = '#388E3C'

    def on_leave(e):
        e.widget['background'] = '#4CAF50'

    submit_btn.bind("<Enter>", on_enter)
    submit_btn.bind("<Leave>", on_leave)
    submit_btn.pack()

    # Footer
    footer_frame = tk.Frame(reg_window, bg="#f5f5f5", height=50)
    footer_frame.pack(fill='x', side='bottom')
    
    footer_text = tk.Label(footer_frame,
                          text="© 2024 Sports Management System",
                          font=("Helvetica", 10),
                          fg="#757575",
                          bg="#f5f5f5")
    footer_text.pack(pady=15)

    reg_window.mainloop()

# Login Window
def login_window():
    login = tk.Tk()
    login.title("Login - Sports Management System")
    login.geometry("1200x800")
    
    # Create frames for layout
    top_frame = tk.Frame(login, bg="#1a237e", height=150)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(login, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Title
    tk.Label(top_frame,
             text="Welcome Back! 👋",
             font=("Helvetica", 24, "bold"),
             fg="white",
             bg="#1a237e").pack(pady=50)

    # Form frame
    form_frame = tk.Frame(main_frame, bg="white")
    form_frame.pack(pady=40)

    # Input style
    entry_style = {
        'font': ('Helvetica', 12),
        'width': 30,
        'bg': '#f5f5f5',
        'relief': 'flat'
    }

    # Username
    tk.Label(form_frame,
             text="Username",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    username_entry = tk.Entry(form_frame, **entry_style)
    username_entry.pack(pady=(0, 15))

    # Password
    tk.Label(form_frame,
             text="Password",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    password_entry = tk.Entry(form_frame, show="•", **entry_style)
    password_entry.pack(pady=(0, 30))

    def login_user():
        username = username_entry.get()
        password = password_entry.get()
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Players WHERE username=%s AND password=%s", (username, password))
        player = cursor.fetchone()

        if player:
            player_id = player[0]
            messagebox.showinfo("Success", "Player login successful!")
            login.destroy()
            player_dashboard(player_id)
        else:
            cursor.execute("SELECT * FROM Coaches WHERE username=%s AND password=%s", (username, password))
            coach = cursor.fetchone()

            if coach:
                coach_id = coach[0]
                messagebox.showinfo("Success", "Coach login successful!")
                login.destroy()
                coach_dashboard(coach_id)
            else:
                messagebox.showerror("Error", "Invalid credentials!")
        conn.close()

    # Login button with hover effect
    login_btn = tk.Button(form_frame,
                         text="Login",
                         font=("Helvetica", 12),
                         width=20,
                         height=2,
                         bg="#2196F3",
                         fg="white",
                         border=0,
                         cursor="hand2",
                         command=login_user)
    
    def on_enter(e):
        e.widget['background'] = '#1976D2'

    def on_leave(e):
        e.widget['background'] = '#2196F3'

    login_btn.bind("<Enter>", on_enter)
    login_btn.bind("<Leave>", on_leave)
    login_btn.pack()

    # Back to registration option
    tk.Label(main_frame,
             text="Don't have an account?",
             font=("Helvetica", 12),
             bg="white",
             fg="#757575").pack(pady=(40, 5))

    def back_to_register():
        login.destroy()
        registration_page()

    register_btn = tk.Button(main_frame,
                           text="Register Here",
                           bg="white",
                           fg="#2196F3",
                           font=("Helvetica", 12, "bold"),
                           border=0,
                           cursor="hand2",
                           command=back_to_register)
    register_btn.pack()

    # Footer
    footer_frame = tk.Frame(login, bg="#f5f5f5", height=50)
    footer_frame.pack(fill='x', side='bottom')
    
    footer_text = tk.Label(footer_frame,
                          text="© 2024 Sports Management System",
                          font=("Helvetica", 10),
                          fg="#757575",
                          bg="#f5f5f5")
    footer_text.pack(pady=15)

    login.mainloop()

# Player Dashboard with modern UI
def player_dashboard(player_id):
    dashboard = tk.Tk()
    dashboard.title("Player Dashboard")
    dashboard.geometry("1200x800")
    
    # Create frames
    top_frame = tk.Frame(dashboard, bg="#1a237e", height=150)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(dashboard, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Get player details
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM Players WHERE player_id = %s", (player_id,))
    player_name = cursor.fetchone()[0]
    conn.close()

    # Welcome message
    tk.Label(top_frame,
             text=f"Welcome, {player_name}! 👋",
             font=("Helvetica", 24, "bold"),
             fg="white",
             bg="#1a237e").pack(pady=50)

    # Button style
    button_style = {
        'font': ('Helvetica', 12),
        'width': 25,
        'height': 2,
        'border': 0,
        'cursor': 'hand2'
    }

    # Buttons Frame
    button_frame = tk.Frame(main_frame, bg="white")
    button_frame.pack(pady=50)

    # Create Team Button
    team_btn = tk.Button(button_frame,
                        text="Create Team",
                        bg="#4CAF50",
                        fg="white",
                        command=lambda: create_team(player_id),
                        **button_style)
    
    def on_enter_team(e):
        e.widget['background'] = '#388E3C'

    def on_leave_team(e):
        e.widget['background'] = '#4CAF50'

    team_btn.bind("<Enter>", on_enter_team)
    team_btn.bind("<Leave>", on_leave_team)
    team_btn.pack(pady=10)

    # View Team Button
    view_btn = tk.Button(button_frame,
                        text="View Team",
                        bg="#2196F3",
                        fg="white",
                        command=lambda: view_team(player_id),
                        **button_style)
    
    def on_enter_view(e):
        e.widget['background'] = '#1976D2'

    def on_leave_view(e):
        e.widget['background'] = '#2196F3'

    view_btn.bind("<Enter>", on_enter_view)
    view_btn.bind("<Leave>", on_leave_view)
    view_btn.pack(pady=10)

    # Equipment Management Button
    equip_btn = tk.Button(button_frame,
                         text="Manage Equipment",
                         bg="#FF9800",
                         fg="white",
                         command=equipment_management,
                         **button_style)
    
    def on_enter_equip(e):
        e.widget['background'] = '#F57C00'

    def on_leave_equip(e):
        e.widget['background'] = '#FF9800'

    equip_btn.bind("<Enter>", on_enter_equip)
    equip_btn.bind("<Leave>", on_leave_equip)
    equip_btn.pack(pady=10)

    # Events Management Button
    event_btn = tk.Button(button_frame,
                         text="Manage Events",
                         bg="#9C27B0",
                         fg="white",
                         command=event_management,
                         **button_style)
    
    def on_enter_event(e):
        e.widget['background'] = '#7B1FA2'

    def on_leave_event(e):
        e.widget['background'] = '#9C27B0'

    event_btn.bind("<Enter>", on_enter_event)
    event_btn.bind("<Leave>", on_leave_event)
    event_btn.pack(pady=10)

    # Logout Button
    logout_btn = tk.Button(button_frame,
                          text="Logout",
                          bg="#f44336",
                          fg="white",
                          command=lambda: [dashboard.destroy(), registration_page()],
                          **button_style)
    
    def on_enter_logout(e):
        e.widget['background'] = '#D32F2F'

    def on_leave_logout(e):
        e.widget['background'] = '#f44336'

    logout_btn.bind("<Enter>", on_enter_logout)
    logout_btn.bind("<Leave>", on_leave_logout)
    logout_btn.pack(pady=20)

    # Footer
    footer_frame = tk.Frame(dashboard, bg="#f5f5f5", height=50)
    footer_frame.pack(fill='x', side='bottom')
    
    footer_text = tk.Label(footer_frame,
                          text="© 2024 Sports Management System",
                          font=("Helvetica", 10),
                          fg="#757575",
                          bg="#f5f5f5")
    footer_text.pack(pady=15)

    dashboard.mainloop()

# Coach Dashboard with modern UI
def coach_dashboard(coach_id):
    dashboard = tk.Tk()
    dashboard.title("Coach Dashboard")
    dashboard.geometry("1200x800")
    
    # Create frames
    top_frame = tk.Frame(dashboard, bg="#1a237e", height=150)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(dashboard, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Get coach details
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM Coaches WHERE coach_id = %s", (coach_id,))
    coach_name = cursor.fetchone()[0]
    conn.close()

    # Welcome message
    tk.Label(top_frame,
             text=f"Welcome, Coach {coach_name}! 👋",
             font=("Helvetica", 24, "bold"),
             fg="white",
             bg="#1a237e").pack(pady=50)

    # Button style
    button_style = {
        'font': ('Helvetica', 12),
        'width': 25,
        'height': 2,
        'border': 0,
        'cursor': 'hand2'
    }

    # Buttons Frame
    button_frame = tk.Frame(main_frame, bg="white")
    button_frame.pack(pady=50)

    # View Teams Button
    teams_btn = tk.Button(button_frame,
                         text="View All Teams",
                         bg="#2196F3",
                         fg="white",
                         command=lambda: view_all_teams(),
                         **button_style)
    
    def on_enter_teams(e):
        e.widget['background'] = '#1976D2'

    def on_leave_teams(e):
        e.widget['background'] = '#2196F3'

    teams_btn.bind("<Enter>", on_enter_teams)
    teams_btn.bind("<Leave>", on_leave_teams)
    teams_btn.pack(pady=10)

    # Manage Training Button
    training_btn = tk.Button(button_frame,
                           text="Manage Training Sessions",
                           bg="#4CAF50",
                           fg="white",
                           command=lambda: manage_training(),
                           **button_style)
    
    def on_enter_training(e):
        e.widget['background'] = '#388E3C'

    def on_leave_training(e):
        e.widget['background'] = '#4CAF50'

    training_btn.bind("<Enter>", on_enter_training)
    training_btn.bind("<Leave>", on_leave_training)
    training_btn.pack(pady=10)

    # Logout Button
    logout_btn = tk.Button(button_frame,
                          text="Logout",
                          bg="#f44336",
                          fg="white",
                          command=lambda: [dashboard.destroy(), registration_page()],
                          **button_style)
    
    def on_enter_logout(e):
        e.widget['background'] = '#D32F2F'

    def on_leave_logout(e):
        e.widget['background'] = '#f44336'

    logout_btn.bind("<Enter>", on_enter_logout)
    logout_btn.bind("<Leave>", on_leave_logout)
    logout_btn.pack(pady=20)

    # Footer
    footer_frame = tk.Frame(dashboard, bg="#f5f5f5", height=50)
    footer_frame.pack(fill='x', side='bottom')
    
    footer_text = tk.Label(footer_frame,
                          text="© 2024 Sports Management System",
                          font=("Helvetica", 10),
                          fg="#757575",
                          bg="#f5f5f5")
    footer_text.pack(pady=15)

    dashboard.mainloop()


# Equipment Management Page
def equipment_management():
    equip_window = tk.Tk()
    equip_window.title("Equipment Management")
    equip_window.geometry("1200x800")
    
    # Create frames
    top_frame = tk.Frame(equip_window, bg="#1a237e", height=150)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(equip_window, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Title
    tk.Label(top_frame,
             text="Equipment Management",
             font=("Helvetica", 24, "bold"),
             fg="white",
             bg="#1a237e").pack(pady=50)

    # Form frame
    form_frame = tk.Frame(main_frame, bg="white")
    form_frame.pack(pady=40)

    # Input style
    entry_style = {
        'font': ('Helvetica', 12),
        'width': 30,
        'bg': '#f5f5f5',
        'relief': 'flat'
    }

    # Equipment Name
    tk.Label(form_frame,
             text="Equipment Name",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    equipment_name_entry = tk.Entry(form_frame, **entry_style)
    equipment_name_entry.pack(pady=(0, 15))

    # Sport Selection
    tk.Label(form_frame,
             text="Choose Sport",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    sport_combobox = Combobox(form_frame, 
                             font=('Helvetica', 12),
                             width=29,
                             state='readonly')
    sport_combobox['values'] = ["Football", "Basketball", "Tennis", "Cricket", "Badminton"]
    sport_combobox.pack(pady=(0, 30))

    def submit_equipment():
        equipment_name = equipment_name_entry.get()
        sport = sport_combobox.get()

        if equipment_name and sport:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO Equipment (equipment_name, sport_name) VALUES (%s, %s)",
                           (equipment_name, sport))
            conn.commit()

            cursor.execute("SELECT * FROM Equipment WHERE equipment_name = %s AND sport_name = %s", 
                           (equipment_name, sport))
            equipment = cursor.fetchone()
            conn.close()

            messagebox.showinfo("Success", "Equipment added successfully!")
            display_equipment_details(equipment)
            equip_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    # Submit button with hover effect
    submit_btn = tk.Button(form_frame,
                          text="Add Equipment",
                          font=("Helvetica", 12),
                          width=20,
                          height=2,
                          bg="#4CAF50",
                          fg="white",
                          border=0,
                          cursor="hand2",
                          command=submit_equipment)
    
    def on_enter(e):
        e.widget['background'] = '#388E3C'

    def on_leave(e):
        e.widget['background'] = '#4CAF50'

    submit_btn.bind("<Enter>", on_enter)
    submit_btn.bind("<Leave>", on_leave)
    submit_btn.pack(pady=20)

    # Footer
    footer_frame = tk.Frame(equip_window, bg="#f5f5f5", height=50)
    footer_frame.pack(fill='x', side='bottom')
    
    footer_text = tk.Label(footer_frame,
                          text="© 2024 Sports Management System",
                          font=("Helvetica", 10),
                          fg="#757575",
                          bg="#f5f5f5")
    footer_text.pack(pady=15)

    equip_window.mainloop()

def display_equipment_details(equipment):
    details_window = tk.Tk()
    details_window.title("Equipment Details")
    details_window.geometry("1200x800")
    
    # Create frames
    top_frame = tk.Frame(details_window, bg="#1a237e", height=150)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(details_window, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Title
    tk.Label(top_frame,
             text="Equipment Details",
             font=("Helvetica", 24, "bold"),
             fg="white",
             bg="#1a237e").pack(pady=50)

    # Details frame
    details_frame = tk.Frame(main_frame, bg="white")
    details_frame.pack(pady=40)

    equipment_id, equipment_name, sport_name = equipment

    # Display details with consistent styling
    tk.Label(details_frame,
             text=f"Equipment ID: {equipment_id}",
             font=("Helvetica", 14),
             bg="white").pack(pady=10)
             
    tk.Label(details_frame,
             text=f"Equipment Name: {equipment_name}",
             font=("Helvetica", 14),
             bg="white").pack(pady=10)
             
    tk.Label(details_frame,
             text=f"Sport: {sport_name}",
             font=("Helvetica", 14),
             bg="white").pack(pady=10)

    # Close button with hover effect
    close_btn = tk.Button(details_frame,
                         text="Close",
                         font=("Helvetica", 12),
                         width=20,
                         height=2,
                         bg="#f44336",
                         fg="white",
                         border=0,
                         cursor="hand2",
                         command=details_window.destroy)
    
    def on_enter(e):
        e.widget['background'] = '#D32F2F'

    def on_leave(e):
        e.widget['background'] = '#f44336'

    close_btn.bind("<Enter>", on_enter)
    close_btn.bind("<Leave>", on_leave)
    close_btn.pack(pady=30)

    # Footer
    footer_frame = tk.Frame(details_window, bg="#f5f5f5", height=50)
    footer_frame.pack(fill='x', side='bottom')
    
    footer_text = tk.Label(footer_frame,
                          text="© 2024 Sports Management System",
                          font=("Helvetica", 10),
                          fg="#757575",
                          bg="#f5f5f5")
    footer_text.pack(pady=15)

    details_window.mainloop()

# Sports Event Management Page
# Sports Event Management Page
def event_management():
    event_window = tk.Tk()
    event_window.title("Sports Event Management")
    event_window.geometry("900x900")
    event_window.configure(bg="#f1f1f1")

    label_font = font.Font(family="Helvetica", size=12)
    entry_font = font.Font(family="Helvetica", size=12)
    button_font = font.Font(family="Helvetica", size=12)

    # Event Name input field
    tk.Label(event_window, text="Event Name:", font=label_font, bg="#f1f1f1").pack(pady=10)
    event_name_entry = tk.Entry(event_window, font=entry_font, width=30)
    event_name_entry.pack()

    # Sport selection for event
    tk.Label(event_window, text="Choose Sport:", font=label_font, bg="#f1f1f1").pack(pady=10)
    sport_combobox = Combobox(event_window, font=entry_font, width=30)
    sport_combobox['values'] = ["Football", "Basketball", "Tennis", "Cricket", "Badminton"]  # Example sports
    sport_combobox.pack()

    # Event Date input field
    tk.Label(event_window, text="Event Date (YYYY-MM-DD):", font=label_font, bg="#f1f1f1").pack(pady=10)
    event_date_entry = tk.Entry(event_window, font=entry_font, width=30)
    event_date_entry.pack()

    # Function to submit event to the database
    def submit_event():
        event_name = event_name_entry.get()
        sport = sport_combobox.get()
        event_date = event_date_entry.get()

        if event_name and sport and event_date:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO Events (event_name, sport_name, event_date) VALUES (%s, %s, %s)",
                           (event_name, sport, event_date))
            conn.commit()

            # Retrieve the added event details
            cursor.execute("SELECT * FROM Events WHERE event_name = %s AND sport_name = %s AND event_date = %s",
                           (event_name, sport, event_date))
            event = cursor.fetchone()
            conn.close()

            messagebox.showinfo("Success", "Event added successfully!")

            # Display the event details
            display_event_details(event)
            event_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    tk.Button(event_window, text="Submit Event", font=button_font, width=20, height=2, bg="#4CAF50", fg="white", command=submit_event).pack(pady=20)

    event_window.mainloop()

# Function to display event details after adding
def display_event_details(event):
    details_window = tk.Tk()
    details_window.title("Event Details")
    details_window.geometry("900x900")
    details_window.configure(bg="#e1f5fe")

    tk.Label(details_window, text="Event Details:", font=("Helvetica", 14, "bold"), bg="#e1f5fe").pack(pady=10)

    event_id, event_name, sport_name, event_date = event

    tk.Label(details_window, text=f"Event ID: {event_id}", font=("Helvetica", 12), bg="#e1f5fe").pack(pady=5)
    tk.Label(details_window, text=f"Event Name: {event_name}", font=("Helvetica", 12), bg="#e1f5fe").pack(pady=5)
    tk.Label(details_window, text=f"Sport: {sport_name}", font=("Helvetica", 12), bg="#e1f5fe").pack(pady=5)
    tk.Label(details_window, text=f"Event Date: {event_date}", font=("Helvetica", 12), bg="#e1f5fe").pack(pady=5)

    tk.Button(details_window, text="Close", font=("Helvetica", 12), bg="#f44336", fg="white", width=15, command=details_window.destroy).pack(pady=20)

    details_window.mainloop()

def create_team(player_id):
    team_window = tk.Tk()
    team_window.title("Create Team")
    team_window.geometry("900x900")
    team_window.configure(bg="#f1f1f1")

    label_font = font.Font(family="Helvetica", size=12)
    entry_font = font.Font(family="Helvetica", size=12)
    button_font = font.Font(family="Helvetica", size=12)

    tk.Label(team_window, text="Team Name:", font=label_font, bg="#f1f1f1").pack(pady=10)
    team_name_entry = tk.Entry(team_window, font=entry_font, width=30)
    team_name_entry.pack()

    tk.Label(team_window, text="Sport:", font=label_font, bg="#f1f1f1").pack(pady=10)
    sport_combobox = Combobox(team_window, font=entry_font, width=30)
    sport_combobox['values'] = ["Football", "Basketball", "Tennis", "Cricket", "Badminton"]
    sport_combobox.pack()

    def submit_team():
        team_name = team_name_entry.get()
        sport = sport_combobox.get()

        if team_name and sport:
            conn = connect_db()
            cursor = conn.cursor()
            
            # Insert team details
            cursor.execute("INSERT INTO Teams (team_name, sport, captain_id) VALUES (%s, %s, %s)",
                         (team_name, sport, player_id))
            conn.commit()
            
            team_id = cursor.lastrowid
            
            # Add the captain (current player) to the team
            cursor.execute("INSERT INTO TeamMembers (team_id, player_id, role) VALUES (%s, %s, %s)",
                         (team_id, player_id, 'Captain'))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", "Team created successfully!")
            team_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill all fields")

    tk.Button(team_window, text="Create Team", font=button_font, width=20, height=2, 
              bg="#4CAF50", fg="white", command=submit_team).pack(pady=20)

def view_team(player_id):
    team_window = tk.Tk()
    team_window.title("View Team")
    team_window.geometry("900x900")
    team_window.configure(bg="#f1f1f1")

    label_font = font.Font(family="Helvetica", size=14, weight="bold")

    conn = connect_db()
    cursor = conn.cursor()

    # Get teams where player is a member
    cursor.execute("""
        SELECT t.team_id, t.team_name, t.sport 
        FROM Teams t 
        JOIN TeamMembers tm ON t.team_id = tm.team_id 
        WHERE tm.player_id = %s
    """, (player_id,))
    
    teams = cursor.fetchall()

    if teams:
        for team in teams:
            team_id, team_name, sport = team
            
            # Create frame for each team
            team_frame = tk.Frame(team_window, bg="#f1f1f1")
            team_frame.pack(pady=10, padx=10, fill="x")
            
            tk.Label(team_frame, text=f"Team: {team_name}", font=label_font, bg="#f1f1f1").pack(pady=5)
            tk.Label(team_frame, text=f"Sport: {sport}", font=("Helvetica", 12), bg="#f1f1f1").pack(pady=5)
            
            # Get team members
            cursor.execute("""
                SELECT p.username, tm.role 
                FROM Players p 
                JOIN TeamMembers tm ON p.player_id = tm.player_id 
                WHERE tm.team_id = %s
            """, (team_id,))
            
            members = cursor.fetchall()
            
            members_frame = tk.Frame(team_frame, bg="#f1f1f1")
            members_frame.pack(pady=5)
            
            tk.Label(members_frame, text="Team Members:", font=("Helvetica", 12), bg="#f1f1f1").pack(pady=5)
            for member in members:
                username, role = member
                tk.Label(members_frame, text=f"{username} - {role}", font=("Helvetica", 10), bg="#f1f1f1").pack()
    else:
        tk.Label(team_window, text="You are not a member of any team", font=label_font, bg="#f1f1f1").pack(pady=20)

    conn.close()

    tk.Button(team_window, text="Close", font=("Helvetica", 12), bg="#f44336", fg="white", 
              width=15, command=team_window.destroy).pack(pady=20)

def view_all_teams():
    teams_window = tk.Tk()
    teams_window.title("All Teams")
    teams_window.geometry("1200x800")
    
    # Create frames
    top_frame = tk.Frame(teams_window, bg="#1a237e", height=150)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(teams_window, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Title
    tk.Label(top_frame,
             text="All Teams",
             font=("Helvetica", 24, "bold"),
             fg="white",
             bg="#1a237e").pack(pady=50)

    # Teams frame
    teams_frame = tk.Frame(main_frame, bg="white")
    teams_frame.pack(pady=40)

    conn = connect_db()
    cursor = conn.cursor()

    # Get all teams
    cursor.execute("""
        SELECT t.team_id, t.team_name, t.sport, p.username as captain
        FROM Teams t
        JOIN Players p ON t.captain_id = p.player_id
    """)
    
    teams = cursor.fetchall()

    if teams:
        for team in teams:
            team_id, team_name, sport, captain = team
            
            # Create frame for each team
            team_frame = tk.Frame(teams_frame, bg="white", relief="solid", borderwidth=1)
            team_frame.pack(pady=10, padx=20, fill="x")
            
            tk.Label(team_frame,
                    text=f"Team: {team_name}",
                    font=("Helvetica", 14, "bold"),
                    bg="white").pack(pady=5)
            tk.Label(team_frame,
                    text=f"Sport: {sport}",
                    font=("Helvetica", 12),
                    bg="white").pack(pady=2)
            tk.Label(team_frame,
                    text=f"Captain: {captain}",
                    font=("Helvetica", 12),
                    bg="white").pack(pady=2)
            
            # Get team members
            cursor.execute("""
                SELECT p.username, tm.role 
                FROM Players p 
                JOIN TeamMembers tm ON p.player_id = tm.player_id 
                WHERE tm.team_id = %s
            """, (team_id,))
            
            members = cursor.fetchall()
            
            members_frame = tk.Frame(team_frame, bg="white")
            members_frame.pack(pady=5)
            
            tk.Label(members_frame,
                    text="Team Members:",
                    font=("Helvetica", 12),
                    bg="white").pack(pady=5)
            
            for member in members:
                username, role = member
                tk.Label(members_frame,
                        text=f"{username} - {role}",
                        font=("Helvetica", 10),
                        bg="white").pack()
    else:
        tk.Label(teams_frame,
                text="No teams found",
                font=("Helvetica", 14),
                bg="white").pack(pady=20)

    conn.close()

    # Close button with hover effect
    close_btn = tk.Button(main_frame,
                         text="Close",
                         font=("Helvetica", 12),
                         width=20,
                         height=2,
                         bg="#f44336",
                         fg="white",
                         border=0,
                         cursor="hand2",
                         command=teams_window.destroy)
    
    def on_enter(e):
        e.widget['background'] = '#D32F2F'

    def on_leave(e):
        e.widget['background'] = '#f44336'

    close_btn.bind("<Enter>", on_enter)
    close_btn.bind("<Leave>", on_leave)
    close_btn.pack(pady=20)

    # Footer
    footer_frame = tk.Frame(teams_window, bg="#f5f5f5", height=50)
    footer_frame.pack(fill='x', side='bottom')
    
    footer_text = tk.Label(footer_frame,
                          text="© 2024 Sports Management System",
                          font=("Helvetica", 10),
                          fg="#757575",
                          bg="#f5f5f5")
    footer_text.pack(pady=15)

    teams_window.mainloop()

def manage_training():
    training_window = tk.Tk()
    training_window.title("Training Management")
    training_window.geometry("1200x800")
    
    # Create frames
    top_frame = tk.Frame(training_window, bg="#1a237e", height=150)
    top_frame.pack(fill='x')
    
    main_frame = tk.Frame(training_window, bg="#ffffff")
    main_frame.pack(fill='both', expand=True)

    # Title
    tk.Label(top_frame,
             text="Training Session Management",
             font=("Helvetica", 24, "bold"),
             fg="white",
             bg="#1a237e").pack(pady=50)

    # Form frame
    form_frame = tk.Frame(main_frame, bg="white")
    form_frame.pack(pady=40)

    # Input style
    entry_style = {
        'font': ('Helvetica', 12),
        'width': 30,
        'bg': '#f5f5f5',
        'relief': 'flat'
    }

    # Session Name
    tk.Label(form_frame,
             text="Session Name",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    session_name_entry = tk.Entry(form_frame, **entry_style)
    session_name_entry.pack(pady=(0, 15))

    # Date
    tk.Label(form_frame,
             text="Date (YYYY-MM-DD)",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    date_entry = tk.Entry(form_frame, **entry_style)
    date_entry.pack(pady=(0, 15))

    # Time
    tk.Label(form_frame,
             text="Time (HH:MM)",
             font=("Helvetica", 12, "bold"),
             bg="white").pack(pady=(0, 5))
    time_entry = tk.Entry(form_frame, **entry_style)
    time_entry.pack(pady=(0, 30))

    def submit_session():
        session_name = session_name_entry.get()
        date = date_entry.get()
        time = time_entry.get()

        if session_name and date and time:
            messagebox.showinfo("Success", "Training session scheduled!")
            training_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill all fields")

    # Submit button with hover effect
    submit_btn = tk.Button(form_frame,
                          text="Schedule Session",
                          font=("Helvetica", 12),
                          width=20,
                          height=2,
                          bg="#4CAF50",
                          fg="white",
                          border=0,
                          cursor="hand2",
                          command=submit_session)
    
    def on_enter(e):
        e.widget['background'] = '#388E3C'

    def on_leave(e):
        e.widget['background'] = '#4CAF50'

    submit_btn.bind("<Enter>", on_enter)
    submit_btn.bind("<Leave>", on_leave)
    submit_btn.pack()

    # Footer
    footer_frame = tk.Frame(training_window, bg="#f5f5f5", height=50)
    footer_frame.pack(fill='x', side='bottom')
    
    footer_text = tk.Label(footer_frame,
                          text="© 2024 Sports Management System",
                          font=("Helvetica", 10),
                          fg="#757575",
                          bg="#f5f5f5")
    footer_text.pack(pady=15)

    training_window.mainloop()

# Start the registration page
registration_page()