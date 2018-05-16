
import sys
#
months = ('', 'january', 'february', 'march', 'april', 'may', 'june', \
          'july', 'august', 'september', 'october', 'november', 'december')
#
def mkBirthdayLst(birthdaysFile):
   def mkBirthdaysFromFile(fileObj):
     birthdays = []
     for line in fileObj:
        # it is assumed that the line format is dd,mm,yyyy
        Dstr, Mstr, Ystr = line[:-1].split(',')
        D, M, Y = int(Dstr), int(Mstr), int(Ystr)
        birthdays.append((D,M,Y))
     return birthdays
   if not birthdaysFile:
     birthdays = [(19, 3, 1968), (6, 4, 2011), (13, 1, 1972), \
             (8, 7, 2005), (28, 4, 2003), (25, 7, 1985), \
             (8, 3, 1978), (22, 8, 1988), (18, 9, 1974), \
             (22, 10, 2004), (25, 5, 1969), (1, 4, 1943), \
             (17, 2, 1990), (23, 12, 1986), (10, 4, 2000)]
   else:
     fileObj = open(birthdaysFile,'r')
     birthdays = mkBirthdaysFromFile(fileObj)
     fileObj.close()
   return birthdays
#
def mmyyCount(birthdays):
   def dictCount(keyValue, Dict):
      if keyValue in Dict:
        Dict[keyValue] += 1
      else:
        Dict[keyValue] = 1
      return
   monthCounts = dict([])
   yearCounts = dict([])
   for BD in birthdays:
      month = BD[1]
      dictCount(month, monthCounts)
      year  = BD[2]
      dictCount(year, yearCounts)
   return monthCounts, yearCounts
#
def leastFreq(Dict):
   least = sys.maxsize
   chosenKeys = []
   for item in Dict.items():
      if item[1] < least:
        least = item[1]
        chosenKeys = [item[0]]
      elif item[1] == least:
        chosenKeys.append(item[0])
   return chosenKeys, least
#
def mostFreq(Dict):
   most = -1 * sys.maxsize
   chosenKeys = []
   for item in Dict.items():
      if item[1] > most:
        most = item[1]
        chosenKeys = [item[0]]
      elif item[1] == most:
        chosenKeys.append(item[0])
   return chosenKeys, most
#
def monthsTrans(listOfMonthNrs):
   if len(listOfMonthNrs) == 1:
     return months[listOfMonthNrs[0]]
   Lout = []
   for monthNr in listOfMonthNrs:
      Lout.append(months[monthNr])
   return Lout
#
birthdaysFile = input("Enter the name of the input file: ")
BDlst = mkBirthdayLst(birthdaysFile)
MMcounts, YYcounts = mmyyCount(BDlst)
listOfMonths1, freq1 = mostFreq(MMcounts)
listOfMonths2, freq2 = leastFreq(MMcounts)
print ("The most frequent (", freq1, ") birthday month(s): ", monthsTrans(listOfMonths1))
if freq1 != freq2:
  print ("The least frequent (", freq2, ") birthday month(s): ", monthsTrans(listOfMonths2))
listOfYears1, freq1 = mostFreq(YYcounts)
listOfYears2, freq2 = leastFreq(YYcounts)
print ("The most frequent (", freq1, ") birthday year(s): ", listOfYears1)
if freq1 != freq2:
  print ("The least frequent (", freq2, ") birthday year(s): ", listOfYears2)
#
