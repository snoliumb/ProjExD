import random
import datetime
from unittest import skip
max_trials = 5 #最大試行回数
piece_word = 10 #対象文字数
lack_word = 2 #欠損文字数

def main():
    st = datetime.datetime.now()
    for i in range(max_trials):
        seikai = shutudai()
        ans = kaitou(seikai)
        if ans ==1:
            break
    ed = datetime.datetime.now()
    print(f"所要時間:{(ed-st).seconds}")

def shutudai():
    alphabets = [chr(c+65) for c in range(26)]
    all_alp_lis = random.sample(alphabets, piece_word)
    print(f"対象の文字:{all_alp_lis}")
    return lack_word

def kaitou(seikai):
    num = int(input("欠損文字はいくつありますか？"))
    if num != lack_word:
        print("不正解、ゲームを強制終了します")
        return 0
    else:
        print("正解です。では具体的な欠損文字を答えなさい。")
        for i in range(lack_word):
            a = input(f"{i+1}文字目を入力しなさい。") 
            if a not in seikai:
                print("不正解です。 TRY AGAIN!!") 
                return 0
            seikai.remove(a)
        print("正解です！お見事！")
        return 1

if __name__ == "__main__":
    main()

