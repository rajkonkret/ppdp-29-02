import pandas

# pip install pandas

data = pandas.read_csv('records.csv', delimiter=";")

print(data)
#   name,branch,year,cgpa
# 0         radek,coe,3,9
# 1       tomek,cos,2,9.1
# 2       marek,cot,1,0.8
# 3          asia,coa,3,0
print(data.columns)  # Index(['name,branch,year,cgpa'], dtype='object')
print(data.values)
print(type(data.values))  # <class 'numpy.ndarray'>
# [['radek,coe,3,9']
#  ['tomek,cos,2,9.1']
#  ['marek,cot,1,0.8']
#  ['asia,coa,3,0']]
print(data.items)
# <bound method DataFrame.items of   name,branch,year,cgpa
# 0         radek,coe,3,9
# 1       tomek,cos,2,9.1
# 2       marek,cot,1,0.8
# 3          asia,coa,3,0>
