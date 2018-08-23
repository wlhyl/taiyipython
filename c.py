from shipan.shipan import NianJiShiPan, YueJiShiPan, RiJiShiPan, ShiJiShiPan
import datetime

t = datetime.datetime.strptime("2018-08-23 23:01:01", "%Y-%m-%d %H:%M:%S")
# for i in range(0, 73):
#     t0 = t + datetime.timedelta(hours=2*i)
#     s = ShiJiShiPan(t0.year, t0.month, t0.day, t0.hour, t0.minute, t0.second, "子")
# # for i in range(0, 73):
# #     a = ShiJiShiPan(2044 + i)
#     print("{},{}".format(s.主算, s.客算))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23,
     24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40]
s = []
for i in a:
    if i < 10:
        continue
    if i % 10 < 5:
        continue
    if i % 10 == 0 or i % 10 == 5:
        continue
    s.append(i)
print(s)
s0 = []
for i in a:
    if i > 10 and i % 10 > 5:
        s0.append(i)
print(s0)
