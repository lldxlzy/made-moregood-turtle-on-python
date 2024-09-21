from turtle import *

class clouduserreporterror(Exception):
    pass
tracer(False)

def cloud(cd=100,colors = "white"):
    fillcolor(colors)
    begin_fill()
    cd = cd // 2 * 2
    seth(0)
    fd(cd)
    seth(90)
    circle(cd//2,90)
    seth(90)
    circle(cd//2,180)
    seth(180)
    circle(cd//2,90)
    seth(0)
    fd(cd)
    end_fill()


cloud(colors="grey")
print("cloud start!")
if input("print over.\nis that a cloud?(yes or no)") == "yes":
    pass
else:
    raise clouduserreporterror("user report error")