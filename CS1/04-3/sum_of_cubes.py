# １からＮまでの数をそれぞれ３乗して足し合わせた数を計算するプログラム
# 関数名はsum_of_cubes(n)

def sum_of_cubes(n):
    result=0
    i=1
    for i in range(n+1):
        result+=i**3
        i+=1
    return result

print(sum_of_cubes(10))
