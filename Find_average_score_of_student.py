if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sums = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in  student_marks[query_name]:
        sums += i
    avg = sums/len(scores)
    average = round(avg,2)
    print("%.2f"%average)                           