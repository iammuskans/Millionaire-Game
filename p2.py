questions = [
    ["Who is shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of France?", "Rome", "Paris", "London", "Berlin", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Shark", 2],
    ["Who wrote the 'Romio and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Homer", 2],
    ["What is the square root of 64?", "6", "8", "10", "12", 2],
    ["Which country is known as the Land of Rising Sun?", "China", "Japan", "South Korea", "India", 2],
    ["Who painted the'Mona Lisa'?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 2],
    ["What is the fastest land animal?", "Cheetah", "Lion", "Elephant", "Horse", 2],
    ["Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 2],
    ["What is the smallest country in the world?", "Vatican City", "Monaco", "San Marino", "Liechtenstein", 2]
]

prizes = [100000, 320000, 400000, 500000, 1000000, 2000000, 30000000, 400000000, 500000000, 6000000000, 7000000000]

i = 0
for question in questions:
    
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    #check whether the answer is correct or not 
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d"))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break
    print(f"You won {prizes[i]}")
    i +=1
    