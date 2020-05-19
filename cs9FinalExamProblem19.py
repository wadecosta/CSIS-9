# CS 9 final exam problem 19

def centered_average(t):
    t.sort()
    return int(sum(t[1:-1]) / (len(t) -2))


# main
t1 = [1, 2, 3, 4, 100]
r1 = centered_average(t1)
print(t1, 'expected result is 3. Your result is', r1)

t2 = [1, 1, 5, 5, 10, 8, 7]
r2 = centered_average(t2)
print(t2, 'expected result is 5. Your result is', r2)

t3 = [-10, -4, -2, -4, -2, 0]
r3 = centered_average(t3)
print(t3, 'expected result is -3. Your result is', r3)

t4 = [5, 3, 4, 6, 2]
r4 = centered_average(t4)
print(t4, 'expected result is 4. Your result is', r4)

t5 = [5, 3, 4, 0, 100]
r5 = centered_average(t5)
print(t5, 'expected result is 4. Your result is', r5)

t6 = [100, 0, 5, 3, 4]
r6 = centered_average(t6)
print(t6, 'expected result is 4. Your result is', r6)

t7 = [4, 0, 100]
r7 = centered_average(t7)
print(t7, 'expected result is 4. Your result is', r7)

t8 = [0, 2, 3, 4, 100]
r8 = centered_average(t8)
print(t8, 'expected result is 3. Your result is', r8)


t9 = [1, 1, 100]
r9 = centered_average(t9)
print(t9, 'expected result is 1. Your result is', r9)


t10 = [7, 7, 7]
r10 = centered_average(t10)
print(t10, 'expected result is 7. Your result is', r10)

t11 = [1, 7, 8]
r11 = centered_average(t11)
print(t11, 'expected result is 7. Your result is', r11)


t12 = [1, 1, 99, 99]
r12 = centered_average(t12)
print(t12, 'expected result is 50. Your result is', r12)

t13 = [1000, 0, 1, 99]
r13 = centered_average(t13)
print(t13, 'expected result is 50. Your result is', r13)

t14 = [4, 4, 4, 4, 5]
r14 = centered_average(t14)
print(t14, 'expected result is 4. Your result is', r14)


t15 = [4, 4, 4, 1, 5]
r15 = centered_average(t15)
print(t15, 'expected result is 4. Your result is', r15)


t16 = [6, 4, 8, 12, 3]
r16 = centered_average(t16)
print(t16, 'expected result is 6. Your result is', r16)
