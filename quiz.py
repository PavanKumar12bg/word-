#quiz game

questions=('what is the full form of ias',
           'how many planates in the our milky way gallexy',
           'what is the capatial city of india',
           'what is the capatial city andhra pradesh')



options=(("a.indian police service","b.indian administrative service","c.indian army service","d.indian air force service"),
         ("a.8","b.9","c.10","d.11"),
         ("a.hyderabad","b.bangalore","c.delhi","d.mumbai"),
         ("a.vijayawada","b.visakhapatnam","c.amaravathi","d.tirupati"))

answers=("B","A","C","C")

guesses=[]
correct=0
question_num=0


for question in questions:
    print("********************************")
    print(question)
    for option in options[question_num]:
        print(option)

    user=input("ENTER YOUR OPTION=").strip().upper()
    guesses.append(user)

    if user in answers[question_num]:
        print('option is correct')
        correct+=1

    else:
        print(f"incorrect option ,correct option is {answers[question_num]}")

    question_num+=1

print("NOW RESULTS")

print("*****************************************")

v=",".join(guesses)

score=correct/len(questions) * 100

print(f"correct answers ={",".join(answers)} \nyour options ={v}")

print(f"your score is {score}%")