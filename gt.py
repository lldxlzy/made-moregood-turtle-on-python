from turtle import *
class gotoerror(Exception):
    pass
def gt(x=0,y=0):
    try:
        penup()
        goto(x,y)
        pendown()
        return "onclick gotoed "+str(x) +","+ str(y)
    except:
        raise gotoerror("error:system wrong")
print('''
      python turtle goto helper
      use it on python
      ///
      python gt.py 
      to run it
      from gt import gt
      gt(x,y)
      to run it
      ///
      ''')
print("system start!")
tracer(False)