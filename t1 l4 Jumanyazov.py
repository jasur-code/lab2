# TODO решите задачу
def task() -> float:

    sum_ = 0
    n1 = 0
    n2 = 0
    file_ = open("input.json", "r")
    str_ = file_.readlines()

    for i in range(len(str_)):
        if str_[i].find("score") != -1:
            n1 = float(str_[i][((str_[i].find("score"))+8):len(str_[i])-2])
        elif (str_[i].find("weight")) != -1:
            n2 = float(str_[i][((str_[i].find("weight"))+9):len(str_[i])-1])
        if(n1 != 0) and (n2 != 0):
            sum_ += n1*n2
            n1 = 0
            n2 = 0
    file_.close()
    return round(sum_, 3)

print(task())
