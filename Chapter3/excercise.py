import pandas as pd
import numpy as np
# from scipy.stats import binom
# import matplotlib.pyplot as plt

# 確認問題

# 3-1 次の事象について考える
# (1) 「修学年数が12年以上」という事象と、「修学年数が16年未満」という事象は排反事象か？
print("3-1")
print("(1)")
print("排反事象でない")

# (2) 「修学年数が12年以上16年未満」という事象と、「修学年数が12年未満」という事象は排反事象か？
print("(2)")
print("排反事象である")

# (3) 「修学年数が12年以上16年未満」という事象と、「修学年数が12年未満」という事象の和事象はどうなるか？
print("(3)")
print("修学年数が16年未満")

# (4) 「修学年数が12年以上」という事象と、「修学年数が16年未満」という事象の積事象はどうなるか？
print("(4)")
print("修学年数が12年以上16年未満")


# 3-2
# 日本人の血液型はA型が39%と最も多く、次はO型で29%、さらにB型の22%、AB型の10%となっていることが知られている。
# 日本人全体から1人を無作為に選び出し、その人の血液型が何型なのかを考える。
print("3-2")

# (1) 選ばれた人の血液型について、起こりうる結果である事象を全て書き、標本空間も書く。これらの事象はお互いに排反か？
print("(1)")
print("標本空間をΩとすると、Ω = {A型, B型, O型, AB型}")
print("1人の人間が、複数の血液型をとることは生物学的にあり得ないので、これらの事象は互いに排反である")

# (2) それぞれの事象の起こりやすさとしての確率を求める。これらの確率は、確率の「公理」を満たしているか？
print("(2)")
print("満たしている。")
print("確率の公理 (1) どのような事象についても、その事象が起きる確率は0以上1以下となる")
print("確率の公理 (2) 標本空間のうち、いずれかが起きる確率は1となる")
print("上記の公理については、(1)で示されていると考えている")
print("なので、確率の公理 (3) 排反事象の和事象が起きる確率は、それぞれの事象が起きる確率の和となる ことについて見ていく")
print("0.39+0.29+0.22+0.10=", 0.39+0.29+0.22 +
      0.10, "。他の場合も全て満たされているので、(3)も満たしている")

# 3-3
print("3-3 飛ばした")

# 3-4
# 平成25年度 全国学力・学習状況調査 報告書 クロス集計
# 朝食を毎日食べているかどうか -> 「している」 「どちらかといえばしている」 「あまりしていない」 「まったくしていない」
# 88.6% 7.6% 3.0% 0.7%
# この質問の答えごとに集計した算数Aの平均正答率は、それぞれ 78.4%, 70.5%, 65.1%, 61.2% だった
# そこで、「朝食を毎日食べている」という事象と、「算数Aの正答率が75%以上」となる事象についての同時確率が次のようになっているとする。
print("3-4")

# 以下は、html形式で表を作成した手順。
# 表をきれいに整形する方法を探すこと

data = [
    [0.65, 0.25],
    [0.05, 0.05]
]

column_arrays = [
    ["算数Aの正答率が75%以上", "算数Aの正答率が75%以上"],
    ["はい", "いいえ"]
]

index_arrays = [
    ["毎日朝食を食べている", "毎日朝食を食べている"],
    ["はい", "いいえ"]
]

# 1. arraysを `*` で unpacking できる。 (typescriptのスプレッド構文みたいなもの？)
# 詳細は -> https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments

# 2. zip関数は、同じ位置の要素同士をグルーピングする
# 詳細は -> https://docs.python.org/3/library/functions.html?highlight=zip#zip
# 行列の転置に似ているとも書かれている

# 3. list()は、型コンストラクタであり、例えば list((1, 2, 3)) は [1, 2, 3] を返す。
# 詳細は -> https://docs.python.org/3/library/stdtypes.html?highlight=list#list
column_tuples = list(zip(*column_arrays))
index_tuples = list(zip(*index_arrays))

columns = pd.MultiIndex.from_tuples(column_tuples, names=[None, None])
indexes = pd.MultiIndex.from_tuples(index_tuples, names=[None, None])

pd.DataFrame(data, index=indexes,
             columns=columns).to_html("Chapter3/3_4.html")

# (1)
print("(1)")
print("0.9")

# (2)
print("(2)")
print("P(B | A)=P(A ∩ B)/P(A) なので、 0.65 / 0.9=", 0.65/0.9)

# (3)
print("(3)")
print("P(B | A) と P(B) が等しければ、独立と言えると考えた。で、P(B)=0.7なので、独立ではないと考えられるが、どうか。<- あっていた")

# 3-5 から 3-10 までは紙にやった

# 実証分析問題
# 3-A
# t分布表及びF分布表をインターネットで見つける
# t分布表 : https://bellcurve.jp/statistics/course/8970.html
# F分布表 : https://bellcurve.jp/statistics/course/9932.html

# 3-B
print("3-B")
# 修学年数が16年以上の人を大卒とし、確率変数 X を使ってX=1, それ以外は0とする
# 年収については、年収が0より大きい人々のみを対象 確率変数Yとすると、 Y = {150, 450, 700} として、それぞれ300未満, 300以上600未満, 600以上 とする

# 相対度数表は以下

data = np.array([
    [0.38, 0.28, 0.03],
    [0.08, 0.18, 0.05]
])

column_arrays = [
    ["年収", "年収", "年収"],
    ["150", "450", "700"]
]

index_arrays = [
    ["大卒", "大卒"],
    ["0", "1"]
]

column_tuples = list(zip(*column_arrays))
index_tuples = list(zip(*index_arrays))

columns = pd.MultiIndex.from_tuples(column_tuples, names=[None, None])
indexes = pd.MultiIndex.from_tuples(index_tuples, names=[None, None])

pd.DataFrame(data, index=indexes,
             columns=columns).to_html("Chapter3/3_B.html")

# これを同時確率分布として、以下について考える

# (1) 年収(Y)の期待値と分散を求める
# 年収(Y) の期待値 E[Y] は、以下のようにも求められる。
# print("期待値 E[Y]")
# print(150*(0.38+0.08)+450*(0.28+0.18)+700*(0.03+0.05))
# だが、numpyの練習のために今回は別の方法を使う

print("3-B (1)")

# これは、以下のようにも書ける
# また、axisの指定については以下を参照のこと
# https://numpy.org/doc/1.24/reference/arrays.ndarray.html#calculation
sum_of_columns_y = data.sum(axis=0)
values_y = np.array(column_arrays[1], dtype=int)
product_y = sum_of_columns_y * values_y
expected_y = product_y.sum()

print("E[Y]:", expected_y, "万円")

# 分散 V[Y] は、以下のようにも求められる
# print("分散 V[Y]")
# print(((150 - 332)**2)*(0.38+0.08)+((450-332)**2)
#       * (0.28+0.18)+((700 - 332)**2)*(0.03+0.05))

variance_y = sum(((values_y - expected_y)**2) * sum_of_columns_y)
print("V[Y]:", variance_y)


# (2)
# 大卒(X)と年収(Y)の相関係数を求める
print("3-B (2)")

# Xについても、Yと同様に求めてみる
sum_of_rows_x = data.sum(axis=1)
values_x = np.array(index_arrays[1], dtype=int)
product_x = sum_of_rows_x * values_x
expected_x = product_x.sum()

# とはいえ、0と1だけだったら、これはX=1についての周辺確率がそのまま期待値になるのではないか
# そうすると、計算自体はX=1の周辺確率を計算したものと同じになっていれば検算できるのか
# sum_of_rows_x[1]は
# print(sum_of_rows_x[1]) = 0.31
# だったから、これは正しいことがわかった
print("E[X]:", expected_x)

variance_x = sum(((values_x - expected_x)**2) * sum_of_rows_x)

print("V[X]:", variance_x)

# XとYのそれぞれの標準偏差
sd_x = np.sqrt(variance_x)
sd_y = np.sqrt(variance_y)

print(sd_x)
print(sd_y)

# XとYの共分散
# ここで pylintrc に C0103 を 追加
cov_xy = 0

for i, x in enumerate(values_x):
    for j, y in enumerate(values_y):
        cov_xy += (x - expected_x) * \
            (y - expected_y)*data[i][j]

print("Cov[X,Y]:", cov_xy)

# なので、相関係数は、
corrcoef_education_income = cov_xy / (sd_x * sd_y)
print("ρ x,y :", corrcoef_education_income)

# (3)
# 大卒である(X=1)という条件のもとでの年収の期待値を求める
marginal_probabiliy_x_1 = sum_of_rows_x[1]
conditional_probability_y_x1_array = data[1]/marginal_probabiliy_x_1
conditional_expectation_y_x1 = np.sum(
    values_y * conditional_probability_y_x1_array)
print("大卒の年収期待値:", conditional_expectation_y_x1)

# (4)
# 大卒ではないという条件のもとでの年収の期待値を求めて、(3)の答えと比較する
marginal_probabiliy_x_0 = sum_of_rows_x[0]
conditional_probability_y_x0_array = data[0]/marginal_probabiliy_x_0
conditional_expectation_y_x0 = np.sum(
    values_y * conditional_probability_y_x0_array)
print("大卒未満の年収の期待値:", conditional_expectation_y_x0)
print("大卒と大卒未満の期待値の差分:", conditional_expectation_y_x1 -
      conditional_expectation_y_x0)
