he = float(input("Input your height in meters:"))
we = float(input("Input your weight in kg:"))
ibm = we/(pow(he,2))

if ibm < 18.5:
    print('{:.{}f} you\'re underweight'.format(ibm,2))
elif ibm >= 18.5 and ibm <25:
    print('{:.{}f} you\'re in the ideal weight'.format(ibm,2))
elif ibm >= 25 and ibm <30:
    print('{:.{}f} you\'re slightly overweight'.format(ibm,2))
elif ibm >=30 and ibm <35:
    print('{:.{}f} you\'re obese'.format(ibm,2))
else:
    print('{:.{}f} you\'re clinically obese'.format(ibm,2))
    