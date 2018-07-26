output = '\t'.join(['name', 'title', 'age', 'gender'])
with open('C:\\Users\\Administrator\\Desktop\\test.txt', "a+") as f:
    f.write(output)
    f.close()
