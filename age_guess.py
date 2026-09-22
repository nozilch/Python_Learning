age=18
i=0
gift={'a':'洋娃娃','b':'变形金刚','c':'遥控飞机'}

while i<3:
    print("欢迎来到猜年龄游戏！")
    guess=input("请输入猜测的年龄：")

    if not guess.isdigit():
        print("请输入数字！！")
        continue

    guess=int(guess)

    if guess<age:
        print("猜小了！！")
    
    elif guess>age:
        print("猜大了！！")
        
    elif guess==age:
        print("猜中了！！")

        print(gift)

        tag1=True
        while tag1:
            choice=input("请选择奖品:")

            if choice not in gift:
                print("请重新选择！！") 
                continue

            print(f"你选择了{gift[choice]}")
            tag1=False

        break

    i+=1

    if i != 3:
        continue

    again_choice = input('是否继续游戏,继续请输入"Y",否则任意键直接退出.')  # 交互是否再一次

    # 判断是否继续
    if again_choice == 'Y':
            i = 0