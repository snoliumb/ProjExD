from random import choice
def main():
    seikai = shutudai()
    kaitou(seikai)
def shutudai():
    qanda = {"サザエの旦那の名前は？":["ますお", "マスオ"], "カツオの妹の名前は？":["わかめ", "ワカメ"], "タラオはカツオから見てどんな関係？":["甥", "甥っ子", "おい", "おいっこ"] }
    r = choice(list(qanda))
    print(f"問題:{r[0]}")
    return r[1]
def kaitou(seikai):
    ans = input("回答:")
    if ans is seikai:
        print("正解！")
    else:
        print("外れ")
