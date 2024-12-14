femaleusernames = []
maleusernames = []
femalepasswords = []
malepasswords = []
femaleweights = []
maleweight = []

def loginchoices():
    print("Login Successful!")
    while True:
        print(f"Welcome {username}!")
        print("1. BMI Calculator")
        print("2. Waist to Hip Ratio")
        print("3. Weight Tracker")
        print("4. Logout")
        choicelogin = input("Choose an option (1/2/3/4): ")
        if choicelogin == "1":
            BMI()
        elif choicelogin == "2":
            WaistHipRatio()
        elif choicelogin == "3":
            WeightTracker()
        elif choicelogin == "4":
            print(f"You have been logged out. Thank you {username}")
            break
        else:
            print("Invalid Input, Please Try Again!")

def BMI():
    weight = float(input("What is your weight in kg? "))
    cm = float(input("What is your height in cm? "))
    height = cm/100
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")
    print("You are classified as:")
    if 12 <= bmi < 18.5:
        print("Underweight.")
    elif 18.5 <= bmi < 25:
        print("Normal Weight.")
    elif 25 <= bmi < 30:
        print("Overweight.")
    elif 30 <= bmi < 40:
        print("Obese.")
    elif 40 < bmi < 64:
        print("Morbidly Obese.")
    else:
        print("BMI is not within chart classifications.")

def WaistHipRatio():
    if sex == "1":
        waist = float(input("What is your waist measurement in cm? "))
        hip = float(input("What is your hip measurement in cm? "))
        waisthipratio = waist / hip
        print(f"Your Waist-to-Hip Ratio is {waisthipratio:.2f}")
        print("You are classified as:")
        if waisthipratio <= 0.80:
            print("Pear. You have low health risks.")
        elif 0.80 < waisthipratio < 0.85:
            print("Avocado. You have moderate health risks.")
        elif waisthipratio >= 0.85 :
            print("Apple. You have high health risks.")
        return True
    elif sex == "2":
        waist = float(input("What is your waist measurement in cm? "))
        hip = float(input("What is your hip measurement in cm? "))
        waisthipratio = waist / hip
        print(f"Your Waist-to-Hip Ratio is {waisthipratio:.2f}")
        if waisthipratio <= 0.95:
            print("Pear. You have low health risks.")
        elif 0.95 < waisthipratio < 1:
            print("Avocado. You have moderate health risks.")
        elif waisthipratio >= 1:
            print("Apple. You have high health risks.")
        return True
    else:
        print("Invalid Input, Please Try Again.")

def WeightTracker():
    asdasd
    
while True:
    print("Welcome to your Health Checker!")
    print("1. BMI Calculator")
    print("2. Waist to Hip Ratio")
    print("3. Register")
    print("4. Login")
    print("5. Exit")
    choice = input("Choose an option (1/2/3/4/5): ")

    if choice == '1':
        BMI()
    elif choice == '2':
        while True:
            sex = input("What is your sex? (1 for Male, 2 for Female): ")
            WaistHipRatio()
    elif choice == '3':
        username = input("Enter a username: ")
        if username in femaleusernames or username in maleusernames:
            print("Username already exists. Please choose a different username.")
        else:
            while True:
                sex = input("Are you male or female? (1 for Male, 2 for Female): ")
                if sex == "1":
                    password = input("Enter a password: ")
                    maleusernames.append(username)
                    malepasswords.append(password)
                    print("Registration successful!")
                    break
                elif sex == "2":
                    password = input("Enter a password: ")
                    femaleusernames.append(username)
                    femalepasswords.append(password)
                    print("Registration successful!")
                    break
                else: 
                    print("Invalid Input, Please Try Again.")
    elif choice == '4':
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in maleusernames:
                index = maleusernames.index(username)
                if malepasswords[index] == password:
                    sex = "1"
                    loginchoices()
                    break
            elif username in femaleusernames:
                index = femaleusernames.index(username)
                if femalepasswords[index] == password:
                    sex = "2"
                    loginchoices()
                    break
                else:
                    print("Incorrect password.")
            else:
                print("Username not found. Please Try Again.")


    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")