score = input ('Enter Score:')
try:
    fscore = float(score)
except:
    print ('Input is wrong!')
    quit()
if  0.0 <= fscore < 0.6:
    print ('F')
elif 0.6 <= fscore < 0.7:
    print ('D')
elif 0.7 <= fscore < 0.8:
    print ('C')
elif 0.8 <= fscore < 0.9:
    print ('B')
elif 0.9 <= fscore <= 1.0:
    print ('A')
else :
    print('The input is not between 0 and 1.')
