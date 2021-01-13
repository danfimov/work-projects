f = open('1.3.txt', 'r')
result = open('1.3-result.txt', 'w')

s = f.read()
print(s.replace(', короче,', ''), file=result)

f.close()
result.close()
