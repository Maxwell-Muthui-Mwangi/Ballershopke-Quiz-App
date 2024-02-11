def main():
    Quiz = {
        

            "question1":{
            # 1. Science:
            "Question": "What is the chemical symbol for water?",
            "Answer": "H2O"

            },

            "question2":{
            #    2.History:
            "Question": "Who was the first President of the United States?",
            "Answer": "George Washington",

            },

            "question3":{
            #3.Geography:
            "Question": "What is the capital of France?",
            "Answer": "Paris"

            },

            "question4":{
                
            #4. Literature:
            "Question": 'Who wrote "Romeo and Juliet"?',
            "Answer": "William Shakespeare"
            },

            "question5":{
            #   5. Mathematics:
            "Question": " What is the value of π (pi) to two decimal places?",
            "Answer": 3.14
            },


            "question6":{
            #  6. Technology:
            "Question": "Who is the CEO of Tesla?",
            "Answer": "Elon Musk"

            },

            "question7":{
                
            # 7. **Sports:**
                "Question": "In which sport does a player score a 'try'?",
                "Answer": "Rugby"

            },

            "question8":{
                # 8. **Music:**
            "Question": 'Who was known as the "King of Pop"?',
            "Answer": "Michael Jackson"
            },

            "question9":{
                #9. **Politics:**
            "Question": "Who is the current Prime Minister of the United Kingdom?",
            "Answer": "Boris Johnson"
            },

            "question10":{
                # 10. **Film:**
                "Question": "What is the highest-grossing film of all time (as of 2022)?",
                "Answer": "Avatar"
            }
        
            

    }

    score = 0

    for key,value in Quiz.items():
        print(value['Question'])
        answer = input("Answer? ")


        if answer.lower() == value['Answer'].lower():
            print('Correct')
            score +=1
            print("Your Score is: "+ str(score))

        else:
            print("wrong!")
            print("The Answer is : "+ value['Answer'])
            print("Your Score is: "+ str(score))



main()