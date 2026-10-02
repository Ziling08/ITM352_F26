#interactive quiz system second version
#name: Ziling He
#date: Oct 2, 2026

questions = [
    ("what is the capital of France?", "paris"),
    ("what is the capital of Germany?", "berlin"),
    ("The last SUppar was painted by which artist?", "Leonardo da Vinci")    
]

for question, correct_answer in questions:
    answer = input(f"{question} ")
    if answer  == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer}, not {answer!r}.")