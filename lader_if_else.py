temp=float(input('enter value of temprature '))
hum=float(input('enter value of humidity %'))
if((temp>30)and(hum<20)):
    print('hot and dey')
elif((temp>=20)and(temp<=30)and(hum>=20)and(hum<40)):
    print('Good whether condition')
elif((temp>=20)and(temp<=30)and(hum>80)):
    print('Moisture present')
else:
    print('please enter valid temprature and humidity')
    

    