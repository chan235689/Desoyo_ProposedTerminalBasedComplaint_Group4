

students = {
    "Jonmar Edoria": "02-1819-05305",
    "Christian James Desoyo": "02-2526-019190",
    "Jillian Faith Tacugue": "02-2526-031683",
    "Chrysler John Roble": "02-2526-019001",
    "Ezeikel Labuntog": "02-1819-05308",
    "Xyrile Ivan Viterbo": "02-2526-00260",
    "Kyle Atlao": "02-2526-018697",
    "Jon Denver Amba": "02-2526-018884",
    "Stephanie Faith T. Ladra": "02-2526-015986"
}

admins = {"admin": "admin123"}

complaints = []


# Student Portal
def student_portal(username):
    while True:
        print("\n==================================================")
        print(f"🎓 Welcome, {username}!")
        print("")
        print("1. File a new complaint")
        print("2. View my complaint status")
        print("3. Logout")
        choice = input("Choose an option (1/2/3): ")
        print("=" * 50)

        if choice == "1":
            print("\n📝 Please fill out the complaint form below.")
            print("")
            course = input("Course & Year: ")
            phone = input("Phone Number: ")
            email = input("Email Address: ")
            date = input("Date: ")
            hour = input("Time: ")
            print("\n⚠️ Make sure all information is correct before submitting ⚠️\n")
            complaint_text = input("Enter your complaint: ")

            complaints.append({
                "student": username,
                "Course & Year": course,
                "Phone Number": phone,
                "Email Address": email,
                "Date": date,
                "Time": hour,
                "Complaint": complaint_text,
                "status": "Complaint Pending ❌"
            })

            print("\n✅ Complaint submitted successfully!")
            print("=" * 50)
        
        elif choice == "2":
            print("\n📋 Your Complaints:\n")
            found = False
            for i, c in enumerate(complaints, 1):
                if c["student"] == username:
                    found = True
                    print(f"====== Complaint #{i} ======")
                    print(f"Date: {c['Date']}")
                    print(f"Time: {c['Time']}")
                    print(f"Complaint: {c['Complaint']}")
                    print(f"Status: {c['status']}")
                    print("==========================\n")
            if not found:
                print("You have no submitted complaints yet.")
        
        elif choice == "3":
            print("\n🚪 Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")


# Admin Portal
def admin_portal(username):
    print(f"\n👨‍💼 Welcome, {username}! Current complaints:\n")
    if not complaints:
        print("No complaints have been submitted yet.\n")
        return

    while True:
        for i, c in enumerate(complaints, 1):
            print(f"================= Complaint #{i} =================")
            print(f"Student Username: {c['student']}")
            print(f"Course & Year: {c['Course & Year']}")
            print(f"Phone: {c['Phone Number']}")
            print(f"Email: {c['Email Address']}")
            print(f"Date: {c['Date']}")
            print(f"Time: {c['Time']}")
            print(f"Complaint: {c['Complaint']}")
            print(f"Status: {c['status']}")
            print("================================================\n")

        choice = input("Enter complaint number to update status (or press Enter to go back): ")
        if choice == "":
            break

        if choice.isdigit() and 1 <= int(choice) <= len(complaints):
            index = int(choice) - 1
            print("\n1. Mark as Solved ✅")
            print("2. Mark as Pending ❌")
            status_choice = input("Choose status (1/2): ")
            print("=" * 50)
            print("")

            if status_choice == "1":
                complaints[index]["status"] = "Complaint Solved ✅"
                print(f"✅ Complaint #{choice} marked as Solved.\n")
            elif status_choice == "2":
                complaints[index]["status"] = "Complaint Pending ❌"
                print(f"⚠️ Complaint #{choice} marked as Pending.\n")
            else:
                print("❌ Invalid option.")
        else:
            print("❌ Invalid complaint number.")


# Login Function
def login(user_type):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if user_type == "student":
        if username in students and students[username] == password:
            student_portal(username)
        else:
            print("❌ Invalid student login.\n")
    elif user_type == "admin":
        if username in admins and admins[username] == password:
            admin_portal(username)
        else:
            print("❌ Invalid admin login.\n")


# Main Menu
while True:
    print("\n====== Complaint System for CITE Department ======")
    print("")
    print("1. Student Login")
    print("2. Admin Login")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")
    print("=" * 50)
    print("")

    if choice == "1":
        login("student")
    elif choice == "2":
        login("admin")
    elif choice == "3":
        print("\n👋 Goodbye!")
        break
    else:
        print("Invalid choice, please try again.\n")