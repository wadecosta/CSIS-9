# CS9 Final Exam Problem 20
# has22
def has22(t):
    for x in range(len(t)-1):
        if (t[x] == 2) and (t[x+1] == 2):
            return True
    return False


#main
t = [ 1, 2, 2 ]
print(t, 'expected answer is True. your answer', has22(t))

t= [1, 2, 1, 2]
print(t, 'expected answer is False. your answer', has22(t))

t = [2, 1, 2]
print(t, 'expected answer is False. your answer', has22(t))

t = [2, 2, 1, 2]
print(t, 'expected answer is True. your answer', has22(t))

t = [1, 3, 2]
print(t, 'expected answer is False. your answer', has22(t))

t = [1, 3, 2, 2]
print(t, 'expected answer is True. your answer', has22(t))

t = [2, 3, 2, 2]
print(t, 'expected answer is True. your answer', has22(t))

t = [4, 2, 4, 2, 2, 5]
print(t, 'expected answer is True. your answer', has22(t))

t = [1, 2]
print(t, 'expected answer is False. your answer', has22(t))

t = [2, 2]
print(t, 'expected answer is True. your answer', has22(t))

t = [2]
print(t, 'expected answer is False. your answer', has22(t))

t = [ ]
print(t, 'expected answer is False. your answer', has22(t))

t = [3, 3, 2, 2]
print(t, 'expected answer is True. your answer', has22(t))

t = [5, 2, 5, 2]
print(t, 'expected answer is False. your answer', has22(t))
