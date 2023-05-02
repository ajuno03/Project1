students = int(input('Total number of students: '))

scores = input(f'Enter {students} score(s): ').split()

while (len(scores) < students):
    scores = input(f'Enter {students} score(s): ').split()
    if (len(scores) >= students):
        break

index = 0
while (index < len(scores)):
    scores[index] = int(scores[index])
    index = index + 1

best = max(scores[0:students])

for i in range(students):
    if (scores[i] >= (best - 10)):
        print(f'Student {i + 1} score is {scores[i]} and grade is A.')
    elif (scores[i] >= (best - 20)):
        print(f'Student {i + 1 } score is {scores[i]} and grade is B.')
    elif (scores[i] >= (best - 30)):
        print(f'Student {i + 1 } score is {scores[i]} and grade is C.')
    elif (scores[i] >= (best - 40)):
        print(f'Student {i + 1 } score is {scores[i]} and grade is D.')
    else:
        print(f'Student {i + 1} score is {scores[i]} and grade is F.')