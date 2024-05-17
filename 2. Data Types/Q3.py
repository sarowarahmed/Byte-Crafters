#Input Format
#The first line contains an integer, N, the number of students.
#The 2N subsequent lines describe each student over N lines.
#- The first line contains a student's name.
#- The second line contains their grade.

#Constraints
#2<=N<=5
#There will always be one or more students having the second lowest grade.

#Output Format
#Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

if __name__ == '__main__':
    students = {}
    for j in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score

    min_score = min(students.values())
    second = max(students.values())
    for j in students.values():
        if second >= j > min_score:
            second = j

    result = []
    for c in students.keys():
        if students[c] == second:
            result.append(c)
    for _ in sorted(result):
        print(_)
