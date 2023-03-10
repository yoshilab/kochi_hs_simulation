# coding: utf-8                                                                                                                                                                                                                               

import math
import random
import matplotlib.pyplot as plt

time_c = 5.0      # 次の客(customer)が来るまでの平均時間(分)
time_s = 1.0      # 平均的なレジのサービス時間(service)(分)

t = 0
tc = 0
n = 0

t_all=[ ]   # 行列の人数が変化する時刻
n_all=[ ]   # 行列の人数

while t < 240:   # 240分(4時間)のシミュレーション
    n_prev = n
    if n == 0:   # もしレジの客が0人なら
        x = -time_c * math.log(1-random.random())   # 次の客が来るまでの時間
        t = tc
        tc = tc + x  # 客が来る時刻tc は x分だけ進んだ時刻
        n = 1    # x分経過し，次の客が来て，レジに1人いる状態になる
        e = -time_s * math.log(1-random.random())  # サービスにかかる時間
        ts = t + e # レジが終わる時刻 ts
    else:        # レジに既に人がいるとき
        if tc < ts:   # 次に客が来る時間が，レジより短ければ
            n = n + 1 # 待ち客が1人増える
            x = -time_c * math.log(1-random.random())
            t = tc
            tc = tc + x
        elif tc == ts: # 前の客が終わったと同時に次の客が来る場合
                       # 行列の人数は変わらず，次の客が来る時間を計算
            x = -time_c * math.log(1-random.random())
            t = tc
            tc = tc + x
        elif tc > ts:  # 次の客が来る前にレジが終われば，1人減る
            n = n - 1
            e = -time_s * math.log(1-random.random())
            t = ts
            ts = ts + e
    t_all.append(t)
    n_all.append(n_prev)
    t_all.append(t)
    n_all.append(n)

plt.plot(t_all,n_all, color="red", linewidth=1.0)
plt.xlabel('Time (min)')
plt.ylabel('Waiting People')
plt.grid(True)
plt.show()
