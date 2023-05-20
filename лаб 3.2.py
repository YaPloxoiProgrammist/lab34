def bracket_check():
    a = input()
    a = 0
    for i in a:
        if i == "(":
            a += 1
        elif i == ")":
            a -= 1
    if a != 0 or a[0] == ")":
        print("Нет")
    else:
        print("Является")
bracket_check()