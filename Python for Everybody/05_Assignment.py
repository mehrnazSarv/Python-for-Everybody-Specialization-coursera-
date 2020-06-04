max = None
min = None
while True:
    number = input('Enter a number:')
    if number == 'done' :
        break
    try:
        fnumber = float(number)
    except:
        print('Invalid input')
        continue
    if min is None:
        min = fnumber
    if max is None:
        max = fnumber
    if fnumber > max:
        max = fnumber
    elif fnumber < min:
        min = fnumber
    imax = int(max)
    imin = int(min)
print('Maximum is',imax)
print('Minimum is',imin)
