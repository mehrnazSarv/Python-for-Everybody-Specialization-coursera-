hours = input ('Enter hours:')
rate = input ('Enter rate:')
fhours = float(hours)
frate = float(rate)
if fhours > 40.0 :
    pay = (40 * frate) + (1.5 * frate * (fhours - 40))
else :
    pay = frate * fhours
print (pay)
