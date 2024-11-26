# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    previous_price = int(input("전날 가격: "))
    sell_list = []
    buy_list = []
    sell_num, buy_num = 1, 1
    print("----------------------------------------------")
    while True:
        tp0 = int(input('매도 수량: '))
        if tp0 == 0:
            break
        tp1 = float(input('매도 가격: '))

        sell_list.append([tp0, tp1, sell_num, 0, 0])
        #[수량, 가격, 거래 순서, 거래될 수량, 거래될 가격]
        sell_num += 1
    print("----------------------------------------------")
    while True:
        tp0 = int(input('매수 수량: '))
        if tp0 == 0:
            break
        tp1 = float(input('매수 가격: '))

        buy_list.append([tp0, tp1, buy_num, 0, 0])
        #[수량, 가격, 거래 순서, 거래될 수량, 거래될 가격]
        buy_num += 1

    #데이터 입력 받은 후 데이터 처리
    #---------------------------------------------------------------------------------
    #알고리즘

    buy_max = buy_list[0][1]
    sell_min = sell_list[0][1]

    buy_list.sort(key=lambda x: x[1])
    sell_list.sort(key=lambda x: x[1])

    max_q = 0
    today_price = 0
    for b in buy_list:
        if buy_max < b[1]:
            buy_max = b[1]

    for s in sell_list:
        if sell_min > s[1]:
            sell_min = s[1]

    if buy_max < sell_min:
        print("가격 형성 불가로 거래 가격은 kets 시장가격을 가져온다!!")
        return True
    else:
        mst = 0
        for s in sell_list:
            mst += s[0]
            mbt = 0
            tp = 0
            for b in buy_list:
                if s[1] <= b[1]:
                    if mbt == 0:
                        if s[1] == b[1]:
                            tp = s[1]
                        elif s[1] <= previous_price <= b[1]:
                            tp = previous_price
                        elif abs(s[1] - previous_price) > abs(b[1] - previous_price):
                            tp = b[1]
                        else:
                            tp = s[1]

                    mbt += b[0]
            if min(mbt, mst) > max_q:
                max_q = min(mbt, mst)
                today_price = tp

        buy_list.sort(key=lambda x: x[2])
        sell_list.sort(key=lambda x: x[2])
        mqb = max_q
        mqs = max_q
        for bn in range(buy_num):

            if buy_list[bn][1] >= today_price:
                buy_list[bn][4] = today_price
                buy_list[bn][3] = min(buy_list[bn][0], mqb)
                mqb -= min(buy_list[bn][0], mqb)

            if mqb == 0: break

        for sn in range(sell_num):

            if sell_list[sn][1] <= today_price:
                sell_list[sn][4] = today_price
                sell_list[sn][3] = min(sell_list[sn][0], mqs)
                mqs -= min(sell_list[sn][0], mqs)

            if mqs == 0: break
        print(f"previous_price: {previous_price}")
        print(f"today_price: {today_price}")
        print("------매도:        ------")
        for s in sell_list:
            print(f"수량: {s[0]} | 가격: {s[1]} | 거래 순서: {s[2]} "
                  f"| 거래될 수량: {s[3]} | 거래될 가격: {s[4]}")
        print("------매수:        ------")
        for s in buy_list:
            print(f"수량: {s[0]} | 가격: {s[1]} | 거래 순서: {s[2]} "
                  f"| 거래될 수량: {s[3]} | 거래될 가격: {s[4]}")










    #---------------------------------------------------------------------------------

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Kets-algorithm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
