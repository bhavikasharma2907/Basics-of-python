#continue the statement loop

number=9
for i in range(1,11):
     if i==5:
         continue
     print(number,'x',i,'=',number*i)

#break the statement loop

number=9
for i in range(1,11):
    if i==5:
        break
    print(number,'x',i,'=',number*i)