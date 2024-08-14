import matplotlib.pyplot as plt
spi_list=[]
for i in range (0,8):
    spi=int(input('enter your spi: ',))
    spi_list.append(spi)
sem=[1,2,3,4,5,6,7,8]
Spi_per_sem=spi_list

plt.pie(sem,labels=spi_list)
plt.title("transcript")

# Adding the legends
plt.legend(["bar"])
plt.show()