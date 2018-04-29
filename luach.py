def leap(y):
  if (y % 400 == 0):
    return True
  if (y % 100 != 0):
    if (y % 4 == 0):
      return True
  return False

def PrintLeapYears(fr,to):
    for i in range(fr,to):
        if (leap(i)):
            print(i)
