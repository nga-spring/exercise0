# 課題0

# １ 変数の使い方

name1 = "ねずこ"

name2 = "ぜんいつ"

print(name1 + "と" + name2 + "は仲間です" )

# ２ if文の使い方

name2 = "むざん"

if name2 == "むざん":
  print("仲間ではありません")
  
# ３ 配列の使い方

name = ["たんじろう","ぎゆう","ねずこ","むざん"]

name.append("ぜんいつ")

print(name)

# ４ for文の使い方

for i in name:
  print(i)
  
# ５ 関数の使い方

def double(n):
  print(2 * n)
  
double(10)

# ６ 引数を使う関数の使い方

def test(hikisuu):
  if hikisuu in name:
    print(hikisuu + "は含まれます")
  
test("ぎゆう")
test("カナヲ")