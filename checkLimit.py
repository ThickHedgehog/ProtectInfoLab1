def checkLimit(Password):
    alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dig = ",.?!;:"
    letter = True
    digit = False
    flag = True

    for i in Password:
        if letter is True and digit is False:
            if i in alf:
                letter = False
                digit = True
                continue
            else:
                flag = False
                break

        if letter is False and digit is True:
            if i in dig:
                letter = True
                digit = False
                continue
            else:
                flag = False
                break

    return flag
