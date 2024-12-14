from common import XMID, YMID, place, robots

TIME = 100

total_qnw = 0
total_qne = 0
total_qsw = 0
total_qse = 0

for pos, vel in robots():
    x, y = place(pos, vel, TIME)
    if x < XMID and y < YMID:
        total_qnw += 1
    elif x > XMID and y < YMID:
        total_qne += 1
    elif x < XMID and y > YMID:
        total_qsw += 1
    elif x > XMID and y > YMID:
        total_qse += 1

total = total_qnw * total_qne * total_qsw * total_qse

assert total == 216027840
