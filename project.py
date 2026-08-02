questions=[
    ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],

       ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],

     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],

     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],

     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],

     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],

     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],

     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],

    
     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],
    
     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],
    
     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],
    
     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],
    
     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],
    
     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],
    
     ["which language is for Arificial intelligence and Machine learning ?",
    "french","javascript","php","Python","NONe",4],
    


]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,
        2500000,5000000,10000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nQuestion{i+1} for RS. {levels[i]}")
    print(f"  {questions[i] }")
    print(f"  a.{question[1]}      b.{question[2]}")
    print(f"  c.{question[1]}      d.{question[2]}")
    reply=int(input("Enter your answer (1-4)  or 0 to quit  "))
    if(reply==0):
        money=levels[i-1]
        print("you quit the game ")
        break
    if(reply==question[-1]):
        print(f"correct answer you won RS. {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            print("         -----------           " \
            "Congratulations  You Nailed this Game " 
        )
            money=10000000
    else:
        print("wrong answer ")
        break


print(f"YOUR HOME TAKE MONEY IS ::   {money}")
