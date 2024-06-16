# 関数名:hit(a,b)
# リストa,bの対するヒットの個数を返す関数

def hit(a,b):
   count=0
   for i in range(0,4):
    if a[i]==b[i]:
      count+=1
    return count
   
print("(1234, 4321) =>", hit([1,2,3,4],[4,3,2,1]),"hit")
print("(1234, 1432) =>", hit([1,2,3,4],[1,4,3,2]),"hit")