English_paper = int(input())
English_Student = input().split()

French_paper = int(input())
French_Student = input().split()

English = set(English_Student)
French = set(French_Student)

Union = English.union(French)

print(len(Union))