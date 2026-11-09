while True:

    print("=======StudyFlow=======")

    name = input("Enter Your Name:")
    print("Hello", name)
    subject = input("What did you study today?: ")
    time = int(input("how many mins did you study?: "))
    difficult = input("How difficult is this for you?:").strip().title()
    difficulty = ['Easy', 'Medium', 'Hard']

    if difficult in difficulty:
        print("You selected",difficult)
    else:
        print("Invalid choice. Please choice 1, 2 or 3")
    if difficult == 'Hard' and time < 30:
        print("This topic is hard and your study session is short")
    else:
        print("Good Job!")
    if difficult == 'Easy': 
        print("Great! Move on to practice problems")
    elif difficult == 'Medium':
        print("Review the topic once, then practice")
    elif difficult == 'Hard':
        print("Go bhack to theory and practice slowy")
    else:
        print("Invalid difficulty")
    subjects = ['Math', 'DSA', 'Python']
    if subject == 'Math':
        print("Solve 3 practice problems")
    elif subject == 'DSA':
        print("Practice one algorithm today")
    elif subject == 'Python':
        print("Build one small coding feature")
    else:
        print("Subject not recognized")
    if time >= 45. and difficult != 'Easy':
        print ("Productive study session")
    else:
        print("Keep going, try little longer next time")

    goal= int(input("what is your goal for today?: "))
    if goal <=time:
        print("congratulation! you have reached your goal")
    else:
        print("you have not reached your goal!")

    again= input("Do you want to start another session? Yes/No:").strip().lower()
    if again == 'No':
        print("Thank you for using study flow!")
        Break
    print("======StudyFlow Summary=====")

    print("Student:", name)
    print("Subject:", subject)
    print("Goal:", goal)
    print("Study Time:", time)
    print("Difficulty Level:", difficult)
    print("========Thank You==========")