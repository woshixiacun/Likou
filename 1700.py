from collections import deque
# students =[1,1,0,0]
# sandwiches = [0,1,0,1]
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
def countStudents(students, sandwiches):
    students = deque(students)
    sandwiches = deque(sandwiches)
    while True:
        if students[0]==sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
        else:
            students.append(students.popleft())
        
        if students==deque([]) and sandwiches==deque([]):
            break
        elif sandwiches[0] not in students:
            break
    return(len(students))

print(countStudents(students,sandwiches))


    