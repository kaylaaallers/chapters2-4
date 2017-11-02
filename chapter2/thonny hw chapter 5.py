3 == 3
True
3 != 3
False
3 >= 4
False
not (3 < 4)
False

def grade(mark):
    if mark >= 90:
        return "A"
    else:
        if mark >= 80:
            return "B"
        else:
            if mark >= 70:
                return "C"
            else:
                if mark >= 60:
                    return "D"
                else:
                    return "F"

mark = 83
print( "Mark:", str(mark), "Grade:", grade(mark))
