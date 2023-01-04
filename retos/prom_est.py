#The provided code stub will read in a dictionary containing
# key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        #regresa input como primer ingresado name y el resto de input en lista ej nombre y en lista notas
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.keys():
        if i == query_name:
            x=student_marks[query_name]
            average=sum(x)/3
    #formato de objeto float en 2 decimales
    average = "{:.2f}".format(average)
    print(average)