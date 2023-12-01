def check(i):
    pwd = str(i)
    if pwd[0] <= pwd[1] <= pwd[2] <= pwd[3] <= pwd[4] <= pwd[5]:
        pwds = {pwd[0], pwd[1], pwd[2], pwd[3], pwd[4], pwd[5]}
        if len(pwds) < 6:
            if (pwd[0] == pwd[1] and pwd[1] != pwd[2]) \
                    or pwd[0] != pwd[1] and pwd[1] == pwd[2] and pwd[2] != pwd[3] \
                    or pwd[1] != pwd[2] and pwd[2] == pwd[3] and pwd[3] != pwd[4] \
                    or pwd[2] != pwd[3] and pwd[3] == pwd[4] and pwd[4] != pwd[5] \
                    or pwd[3] != pwd[4] and pwd[4] == pwd[5]:
                print(i)
                return True

    return False


# 128392-643281
number_of_pwds = 0
for i in range(128888, 666666):
    if check(i):
        number_of_pwds += 1

print(number_of_pwds)
