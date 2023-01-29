student = []
python_student = []
marks = []

if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        student.append(name)
        student.append(score)
        python_student.append(student)
        student = []

    for i in python_student:
        marks.append(i[1])

marks.sort()

set_of_marks = list(set(marks))

second_largest = set_of_marks[1]

python_student.sort()

for i in python_student:
    
    if i[1] == second_largest:
        print(i[0])