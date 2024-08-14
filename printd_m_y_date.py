import datetime 
print('enter date in dd/mm/yyyy format')
date=input(('enteer date'))
k=date.split("/")
print('date in formet mm-dd-yyyy:%s-%s-%s'%(k[1],k[0],k[2]))
