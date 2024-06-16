# ●20人の身長がリストになっているデータ(data)に対して、標本平均と標 本分散を表示するプログラム height_statistics.py を作成して提出
# してください。
# ■ 20人の身長のデータは次のスライドに掲載しています。
# ● 以下のステップでプログラムを組み立ててください
# 1. このデータをすべて表示するプログラムを書いてください。
# 2. 引数に data を受け取り、そのデータの標本平均を戻り値として返す関数 mean (data)を作 成してください。
# ・ 標本平均の定義は後のスライド
# 3. 引数に data を受け取り、そのデータの標本分散を戻り値として返す関数 variance(data) を作成してください。
# ・ 標本分散の定義は後のスライド
# • 2. で作った mean (data) 関数も variance(data) 関数内で活用しましょう

data = [172.8, 156.9, 175.9, 156.1, 166.8, 161.9, 166.9, 176, 159.8, 164, 160.3, 153.5, 174.1, 172.2, 172.7, 166.7, 173.7, 158, 172.7, 155.9]

#STEP1
for i in data:
    print(i)

#STEP2
def mean(data):
    count=len(data)
    result=0
    for i in data:
        result+=i
    BAR = result/count

    return BAR

print(mean(data))

#STEP3
def variance(data):
    count=len(data)
    result=0
    total=0
    for i in data:
        result+=i
    BAR = result/count

    for i in data:
        total+= (i- BAR)**2
    BUNSAN=total/count
    return BUNSAN

print(variance(data))