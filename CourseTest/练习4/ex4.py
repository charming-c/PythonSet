import random

def getWords():
    words = []
    with open('source.txt','r') as f:
        lines = f.readlines()
        for i in range(0,len(lines)):
            for word in lines[i].split():
                words.append(word)
        f.close()
    return words


if __name__ == '__main__':
    print("欢迎参加猜单词游戏")
    print("请把乱序后的字母组成一个单词\n")

    words = getWords()
    flag = 'Y'
    while flag == 'Y':
        ans = random.choice(words)

        puzzle = ans[:]
        for i in range(0,len(ans)//2,1):
            position = random.randrange(i+1,len(ans))
            puzzle = puzzle[:i] + puzzle[position] + puzzle[i+1:position] + puzzle[i] + puzzle[position +1 :]
        print(f"乱序后的单词：{puzzle}")
        guess = input("请输入您预测的结果：")
        if guess == ans:
            print("恭喜你，答对了！！！")
        else:
            guess = input("答案错误！请重新猜测：")

        flag = input("是否继续？（Y/N）")
    print("谢谢参与，欢迎下次再玩！")
