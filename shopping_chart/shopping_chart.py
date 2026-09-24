import os

product_list = [
    ['Iphone7', 5800],
    ['Coffee', 30],
    ['疙瘩汤', 10],
    ['Python Book', 99],
    ['Bike', 199],
    ['ViVo X9', 2499],
]

shopping_cart = {}
current_userinfo = []

db_file = r'db.txt'

while True:
    print('''
登陆
注册
购物
    ''')

    choice = input('>>: ').strip()
    choice=int(choice)

    if choice == 1:
        #1、登陆
        tag = True
        count = 0
        while tag:
            if count == 3:
                print('尝试次数过多，退出。。。')
                break
            uname = input('用户名：').strip()
            pwd = input('密码：').strip()

            with open(db_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip('\n')
                    user_info = line.split(',')

                    uname_of_db = user_info[0]
                    pwd_of_db = user_info[1]
                    balance_of_db = int(user_info[2])

                    if uname == uname_of_db and pwd == pwd_of_db:
                        print('登陆成功')

                        # 登陆成功则将用户名和余额添加到列表
                        current_userinfo = [uname_of_db, balance_of_db]
                        print('用户信息为：', current_userinfo)
                        tag = False
                        break
                else:
                    print('用户名或密码错误')
                    count += 1

    elif choice==2:
        #注册
        print("欢迎来到注册系统！！")
        username=input("请输入用户名>>").strip()
        password=input("请输入密码>>").strip()
        balance = input('请输入充值金额：').strip()

        balance=int(balance)

        with open(db_file,'a',encoding='utf-8') as fa:
            fa.write("%s,%s,%d" %(username,password,balance))

    elif choice==3:
        #购物
        if current_userinfo==[]:
            print("请登录！！")
        else:
            username=current_userinfo[0]
            balance=current_userinfo[1]
            print(f"欢迎{username}登录,您的余额为:{balance}")

            tag = True
            while tag:
                for index,product in enumerate(product_list):
                    print(index,product)
                choice = input('输入商品编号购物，输入q退出>>: ').strip()
                if choice.isdigit():
                    choice = int(choice)
                    if choice < 0 or choice >= len(product_list): continue

                    pname=product_list[choice][0]
                    pprice=product_list[choice][1]
                    if balance>pprice:
                        if pname in shopping_cart:
                            shopping_cart[pname]['count']+=1
                        else:
                            shopping_cart[pname] = {
                                'pprice': pprice,
                                'count': 1
                            }

                        balance -= pprice  # 扣钱
                        current_userinfo[1] = balance  # 更新用户余额
                        print(
                            "Added product " + pname +
                            " into shopping cart,your current balance "
                            + str(balance))
                    else:
                        print("余额不足，无法添加！！")
                        print(shopping_cart)
                elif choice == 'q':
                    print("""
                    ---------------------------------已购买商品列表---------------------------------
                    id          商品                   数量             单价               总价
                    """)

                    total_cost = 0
                    for i, key in enumerate(shopping_cart):
                        print('%22s%18s%18s%18s%18s' %
                              (i, key, shopping_cart[key]['count'],
                               shopping_cart[key]['pprice'],
                               shopping_cart[key]['pprice'] *
                               shopping_cart[key]['count']))
                        total_cost += shopping_cart[key][
                            'pprice'] * shopping_cart[key]['count']

                    print("""
                    您的总花费为: %s
                    您的余额为: %s
                    ---------------------------------end---------------------------------
                    """ % (total_cost, balance))

                    tag=True
                    while tag:
                        inp = input('确认购买(yes/no?)>>: ').strip()
                        if inp not in ['Y', 'N', 'y', 'n', 'yes', 'no']:
                            continue
                        if inp in ['Y', 'y', 'yes']:
                            # 将余额写入文件
                            
                            src_file=db_file
                            drt_file=r"%s.swap" %db_file
                            with open(src_file,'r',encoding='utf-8') as read_file,\
                             open(drt_file,'w',encoding='utf-8') as write_file:
                                for line in read_file:
                                    if line.startswith(uname_of_db):
                                        l = line.strip('\n').split(',')
                                        l[-1] = str(balance)
                                        line = ','.join(l) + '\n'

                                    write_file.write(line)
                            os.remove(src_file)
                            os.rename(drt_file, src_file)

                            print('购买成功，请耐心等待发货')

                        shopping_cart = {}
                        current_userinfo = []
                        tag = False

                else:
                    print('输入非法')
    elif choice == 'q':
        break

    else:
        print('非法操作')