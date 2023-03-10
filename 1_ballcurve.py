import matplotlib.pyplot as plt
import math

# シミュレーション関数
#   speed:初速度km/h　degree:角度　color:色  g:重力加速度
def simulation(speed,degree,color,g):
    v0 = speed*1000/3600       # 初速度 m/s に変換
    rad = math.radians(degree) # 投げ上げ角度をラジアンに変換
    x = [0]                    # 開始時の x 座標
    y = [0]                    # 開始時の y 座標
    vx = [v0 * math.cos(rad)]  # 開始時の速度 x 方向成分 (v0 cos θ)
    vy = [v0 * math.sin(rad)]  # 開始時の速度 y 方向成分 (v0 sin θ)
    dt = 0.3                   # シミュレーションの時間間隔Δt
    i = 0                      # 位置・速度データを格納するリストの番号(添字)
    while y[i] >= 0:           # y座標が0以上の間（空中にいる間）繰り返す
      vx.append(vx[i])         # 次の時刻の速度(x成分)は vx はそのまま変わらず(等速)
      vy.append(vy[i] - g*dt)  # 次の時刻の速度(y成分)は vy 重力加速度分減少
      x.append(x[i] + vx[i]*dt) # 次の時刻の位置xは速度vxのdx分だけ移動
      y.append(y[i] + (vy[i] + vy[i+1])/2.0*dt)
                               # 次の時刻の位置yは速度vyのdx分だけ移動
                               # vyは重力で変化するので，現時刻と次時刻の速度の平均
      i = i + 1
    label_text = "v=" + str(speed) +"km/h, " + "angle=" + str(degree) + ", dist=" + str(round(x[-1],1)) + "m"
    plt.scatter(x, y, color=color, label=label_text)

    return

# main 処理
# ここからプログラム開始

# 投げ上げ角度を変えながらシミュレーションを行い，色を変えてプロット
simulation(speed=150, degree=70, color="red", g=9.8) # 初速v0=150キロ, 角度70度, 重力加速度g=9.8 の投げ上げを赤でプロット
simulation(speed=150, degree=60, color="purple", g=9.8) # 初速v0=150キロ, 角度60度, 重力加速度g=9.8 の投げ上げを赤でプロット
simulation(speed=150, degree=45, color="gray", g=9.8) # 初速v0=150キロ, 角度45度, 重力加速度g=9.8 の投げ上げを赤でプロット
simulation(speed=150, degree=30, color="orange", g=9.8) # 初速v0=150キロ, 角度30度, 重力加速度g=9.8 の投げ上げを赤でプロット

# グラフ描画
plt.gca().set_aspect("equal", adjustable="box") #アスペクト（縦横比）を1:1に
plt.xlim(0,200)  # x軸は0～200m
plt.ylim(0,100)  # y軸は0～100m
plt.title("Ball curve")
plt.xlabel("distance(m)")
plt.ylabel("height(m)")
plt.legend()
plt.show()
