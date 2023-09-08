

def isleapyear(year) :
  if(year%4==0and year%100!=0):
     return True
  else:
    return False
year=int(input("enter a year:"))
if isleapyear(year) :
  print('{} is leapyear. '.format(year) )
else:
  print ('{} is not a leapyear. '.format(year) )
  
