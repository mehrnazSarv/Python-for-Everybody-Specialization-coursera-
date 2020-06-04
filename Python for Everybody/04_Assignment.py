def computepay (fhours,fraate):
   if fhours > 40.0:
       pay = (40 * frate) + (1.5 * frate * (fhours - 40))
   else:
       pay = frate * fhours
   return pay
hours = input ('Enter hours:')
rate = input ('Enter rate:')
try:
    fhours = float(hours)
    frate = float(rate)
except:
    prtint ('The input is wrong.')
    quit()
payment = computepay(fhours,frate)
print (payment)
