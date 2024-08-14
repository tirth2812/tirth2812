import pandas as pd

header = ['serial no', 'name', 'birthdate','city']
data = [['1', 'tirth', '28-12-2002','surat'], ['2', 'nilay', '10-1-2004','surat'], ['3', 'milan', '2-7-2003','surat']]
data = pd.DataFrame(data, columns=header)
data.to_csv('Stu_data.csv', index=False)

