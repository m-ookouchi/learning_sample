from random import randint

print("1～100までの数を当ててください。")

# 入力回数の初期化
count = 0

# 答えの生成
ans = randint(1, 100)
# print("[debug]ans = " + str(ans))

# 入力値の初期化
enter = 0

# ゲームループ
while enter != ans :
    if count == 0 and enter ==0 :
        # 初回メッセージ
        print("それでは始めましょう")
    else :
        # ヒントの表示
        print("残念。違います")
        if ans < enter :
            # 入力値が大きかった場合
            print("残念。大きいです。")
        else :
            # 入力値が小さかった場合
            print("残念。小さいです。")
    # 入力回数のカウントアップ
    count += 1

    # 答えの入力
    enter = int(input(str(count) + "回目の挑戦>>"))

# 正解メッセージの表示
print("正解です。")
print(str(count) + "回目であたりました。おめでとう！！")
