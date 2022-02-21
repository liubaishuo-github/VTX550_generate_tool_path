a= ['[23', '[-.32342']

for index, i  in enumerate(a):
    a[index] = i.replace('[',  '')

print(a)
