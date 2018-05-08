def leap(y):
  return (y % 19) in (3,6,8,11,14,17,0)

def PrintLeapYears(fr,to):
    for i in range(fr,to):
        if (leap(i)):
            print(i)
