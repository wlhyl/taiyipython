import datetime
import sqlite3
import os
from ganzhiwuxin import *

if __name__ == "__main__":
    from point import *
else:
    from .point import *

DB = os.path.dirname(os.path.realpath(__file__)) + '/data/lifa.db'


class ShiPan():
    # 太乙积年 = 10153917
    太乙积年 = 1936557
    岁实整数 = 365
    岁实分子 = 7877
    岁实分母 = 32193

    def __init__(self, y=1, m=0, d=0, h=0, minute=0, sec=0):
        self.year = y
        self.month = m
        self.day = d
        self.hour = h
        self.minute = minute
        self.sec = sec
        self.积算 = 0
        self.太乙 = None
        self.文昌 = None
        self.计神 = None
        self.始击 = None
        self.主大将 = None
        self.主参将 = None
        self.客大将 = None
        self.客参将 = None
        self.主算 = None
        self.客算 = None
        self.格局 = []
        self.shiPan = [
            [["大炅", "巽"], ["大神", "巳"], ["大威", "午"], ["天道", "未"], ["大武", "坤"]],
            [["太阳", "辰"], ["9", "<font color='blue'>绝阴</font>"], ["2", "<font color='blue'>易气</font>"], ["7"],
             ["武德", "申"]],
            [["高丛", "卯"], ["4", "<font color='blue'>绝气</font>"], ["5"], ["6", "<font color='blue'>绝气</font>"],
             ["太簇", "酉"]],
            [["吕申", "寅"], ["3"], ["8", "<font color='blue'>易气</font>"], ["1", "<font color='blue'>绝阳</font>"],
             ["阴主", "戌"]],
            [["和德", "艮"], ["阳德", "丑"], ["地主", "子"], ["大义", "亥"], ["阴德", "乾"]],
        ]
        self.header = ""
        self.init()
        self.get太乙()
        self.get八门()
        self.get计神()
        self.get天目()
        self.get主将()
        self.get始击()
        self.get客将()

        self.get格局()

    def __str__(self):
        __css = '''
<style type="text/css">
table{
  border-collapse:collapse;
  }
table,th,td{
border:1px solid black;
}

tr{
  text-align: center;
}

td{
  height:100px;
  width:100px;
  vertical-align:middle;
}
</style>
'''
        __shiPanTable = ""
        for row in self.shiPan:
            __shiPanRow = []
            for col in row:
                tmp = ["<div>{}</div>".format(i) for i in col]
                tmp = "".join(tmp)
                tmp = "<td>{}</td>".format(tmp)
                __shiPanRow.append(tmp)
            tmp = "".join(__shiPanRow)
            tmp = "<tr>{}</tr>".format(tmp)
            __shiPanTable = __shiPanTable + tmp
        __格局 = '<div><font color="red">格局：</font></div> <div>{}</div>'.format(
            '、'.join(self.格局))
        __shiPanTable = "<table>{}</table>".format(__shiPanTable)

        return "<html><head>{}</head><body>{}{}{}</body></html>".format(
            __css, self.header, __格局, __shiPanTable)

    def set(self, s, p):
        self.shiPan[p.x][p.y].append(s)

    # def __get宫数For间辰(self, p):
    #     if not isinstance(p, JianChenPoint):
    #         raise ValueError("参数只能是JianChenPoint")
    #
    #     if p.x == 0 and p.y == 0:
    #         return 9
    #     if p.x == 4 and p.y == 0:
    #         return 3
    #     if p.x == 4 and p.y == 4:
    #         return 1
    #     if p.x == 0 and p.y == 4:
    #         return 7
    #     if p.x == 0 and p.y == 2:
    #         return 2
    #     if p.x == 2 and p.y == 0:
    #         return 4
    #     if p.x == 4 and p.y == 2:
    #         return 8
    #     if p.x == 2 and p.y == 4:
    #         return 6
    #     return 0

    def init(self):
        y = self.year

        __积年 = self.太乙积年 + y
        if y < 0:
            __积年 = self.太乙积年 + 1 + y

        __年干支 = 干支(干("甲"), 支("子")) + (__积年 % 60 - 1)

        self.积算 = __积年
        self.header = "{} <div>干支: {} </div> <div>年计太乙</div>".format(
            self.header, __年干支)

    def is阳遁(self):
        return True

    def get八门(self):
        __积算 = self.积算
        __值事八门入局年数 = __积算 % 240
        if __值事八门入局年数 == 0:
            __值事八门入局年数 = 240

        __值事八门 = __值事八门入局年数 // 30
        if __值事八门入局年数 % 30 != 0:
            __值事八门 = __值事八门 + 1

        __太乙宫数 = self.太乙.宫数
        __太乙宫数所对应的九宫 = Get九宫Point(__太乙宫数)

        __八门 = ["开", "休", "生", "伤", "杜", "景", "死", "惊"]
        for i in range(0, 8):
            self.set(__八门[(__值事八门 - 1 + i) % 8], __太乙宫数所对应的九宫 + i)

    def get太乙(self):
        __积算 = self.积算
        __入纪元数 = __积算 % 360
        if __入纪元数 == 0:
            __入纪元数 = 360
        __入元周数 = __入纪元数 // 72
        __入元数 = __入纪元数 % 72
        if __入元数 == 0:
            __入元周数 = __入元周数 - 1
            __入元数 = 72

        __入元周数 = __入元周数 + 1

        __太乙入宫数 = __入元数 % 24
        if __太乙入宫数 == 0:
            __太乙入宫数 = 24

        __太乙宫数 = __太乙入宫数 // 3
        if __太乙入宫数 % 3 != 0:
            __太乙宫数 = __太乙宫数 + 1
        # 太乙不入中宫
        if __太乙宫数 >= 5:
            __太乙宫数 = __太乙宫数 + 1

        __太乙值事Func = lambda x: "理人" if x == 0 else ("理天" if x == 1 else "理地")
        __太乙值事 = __太乙值事Func(__太乙入宫数 % 3)

        dunType = '阳遁'
        if not self.is阳遁():
            __太乙宫数 = 10 - __太乙宫数
            dunType = '阴遁'

        __printString = "<div>{0}子元 {1} {2}局 {3}</div>".format(
            干(2 * __入元周数 - 1), dunType, __入元数, __太乙值事)
        self.header = "{}{}".format(self.header, __printString)

        __太乙 = '<div style = "color:#F00" >太乙</div>'
        # if 太乙宫数 == 1:
        #     self.__太乙 = JianChenPoint(4, 4)
        # elif 太乙宫数 == 2:
        #     self.__太乙 = JianChenPoint(0, 2)
        # elif 太乙宫数 == 3:
        #     self.__太乙 = JianChenPoint(4, 0)
        # elif 太乙宫数 == 4:
        #     self.__太乙 = JianChenPoint(2, 0)
        # elif 太乙宫数 == 6:
        #     self.__太乙 = JianChenPoint(2, 4)
        # elif 太乙宫数 == 7:
        #     self.__太乙 = JianChenPoint(0, 4)
        # elif 太乙宫数 == 8:
        #     self.__太乙 = JianChenPoint(4, 2)
        # else:
        #     self.__太乙 = JianChenPoint(0, 0)
        # self.__set(太乙, self.__太乙)
        self.太乙 = Get九宫Point(__太乙宫数)
        self.set(__太乙, self.太乙)

    def get计神(self):
        __积算 = self.积算
        __时支num = __积算 % 12
        if __时支num == 0:
            __时支num = 12
        __时支 = 支(__时支num)
        if self.is阳遁():
            __寅 = 支("寅")
            __计神支 = __寅 + (-1 * (__时支 - 支("子")))
        else:
            __申 = 支("申")
            __计神支 = __申 + (-1 * (__时支 - 支("子")))

        __计神 = '<font color="red">计神</font>'
        self.计神 = Get间辰Point("{}".format(__计神支))
        self.set(__计神, self.计神)

    def get天目(self):
        __积算 = self.积算
        __天目入宫数 = __积算 % 18
        if __天目入宫数 == 0:
            __天目入宫数 = 18

        __天目 = '<font color="red">文昌</font>'
        if self.is阳遁():
            pToN = ("0", "申", "酉", "戌", "乾", "乾", "亥", "子", "丑", "艮", "寅", "卯",
                    "辰", "巽", "巳", "午", "未", "坤", "坤",)
            p = Get间辰Point(pToN[__天目入宫数])
            self.文昌 = p
        else:
            pToN = ("0", "寅", "卯", "辰", "巽", "巽", "巳", "午", "未", "坤", "申", "酉",
                    "戌", "乾", "亥", "子", "丑", "艮", "艮",)
            p = Get间辰Point(pToN[__天目入宫数])
            self.文昌 = p
        self.set(__天目, self.文昌)

    def get主将(self):
        __主大将 = '<font color="red">主大将</font>'
        __主参将 = '<font color="red">主参将</font>'

        # 求主算
        __文昌point = self.文昌
        __太乙point = self.太乙
        __主算 = 0
        if __文昌point.宫数 == 0:
            __主算 = 1
        for i in range(0, 16):
            if (__文昌point + i).宫数 == __太乙point.宫数:
                break
            __主算 = __主算 + (__文昌point + i).宫数
        if __太乙point.宫数 == __文昌point.宫数:
            __主算 = __太乙point.宫数
        # 求主大将
        __主大将宫数 = __主算 % 10
        if __主大将宫数 == 0:
            __主大将宫数 = __主算 % 9
        self.主大将 = Get九宫Point(__主大将宫数)
        self.set(__主大将, self.主大将)

        # 求主参将
        __主参将宫数 = (__主大将宫数 * 3) % 10
        self.主参将 = Get九宫Point(__主参将宫数)
        self.set(__主参将, self.主参将)

        self.header = '{}<div><font color="red">主算:{}</font></div>'.format(
            self.header, __主算)
        self.主算 = __主算

    def get始击(self):
        # 求始击位置
        __和德point = JianChenPoint(4, 0)
        __计神point = self.计神
        __文昌point = self.文昌
        __始击 = '<div><font color="red">始击</font></div >'

        for i in range(0, 16):
            if __计神point + i == __和德point:
                self.始击 = __文昌point + i
                break
        self.set(__始击, self.始击)

    def get客将(self):
        __客大将 = '<font color="red">客大将</font>'
        __客参将 = '<font color="red">客参将</font>'

        # 求客算
        __太乙point = self.太乙
        __始击point = self.始击
        __客算 = 0
        if __始击point.宫数 == 0:
            __客算 = 1
        for i in range(0, 16):
            if (__始击point + i).宫数 == __太乙point.宫数:
                break
            __客算 = __客算 + (__始击point + i).宫数
        if __太乙point.宫数 == __始击point.宫数:
            __客算 = __太乙point.宫数

        # 求客大将
        __客大将宫数 = __客算 % 10
        if __客大将宫数 == 0:
            __客大将宫数 = __客算 % 9
        self.客大将 = Get九宫Point(__客大将宫数)
        self.set(__客大将, self.客大将)

        # 求客参将
        __客参将宫数 = (__客大将宫数 * 3) % 10
        self.客参将 = Get九宫Point(__客参将宫数)
        self.set(__客参将, self.客参将)

        self.header = '{}<div><font color="red">客算:{}</font></div>'.format(
            self.header, __客算)
        self.客算 = __客算

    def get格局(self):
        def 掩():
            __始击Point = self.始击
            __太乙Point = self.太乙
            if __始击Point.宫数 == __太乙Point.宫数:
                self.格局.append("始击掩太乙")
#             return True

        def 击():
            __始击所在的九宫Point = self.始击.九宫Point
            __太乙所在的九宫Point = self.太乙
            # 宫击
            if (__始击所在的九宫Point + 1) == __太乙所在的九宫Point:
                self.格局.append("始击内宫击太乙")

            if (__始击所在的九宫Point + (-1)) == __太乙所在的九宫Point:
                self.格局.append("始击外宫击太乙")
            # 辰击
            __太乙在16神上的Point = __太乙所在的九宫Point.间辰Point

            if (self.始击 + 1) == __太乙在16神上的Point:
                self.格局.append("始击内辰击太乙")
            if (self.始击 + (-1)) == __太乙在16神上的Point:
                self.格局.append("始击外辰击太乙")
#             return True

        def 迫():
            __太乙所在的九宫Point = self.太乙
            __文昌所在的九宫Point = self.文昌.九宫Point
            __主大将所在的九宫Point = self.主大将
            __主参将所在的九宫Point = self.主参将
            __客大将所在的九宫Point = self.客大将
            __客参将所在的九宫Point = self.客参将

            # 文昌宫迫
            if (__文昌所在的九宫Point + 1) == __太乙所在的九宫Point and self.文昌.宫数 != 0:
                self.格局.append("文昌内宫迫太乙")

            if (__文昌所在的九宫Point + (-1)) == __太乙所在的九宫Point and self.文昌.宫数 != 0:
                self.格局.append("文昌外宫迫太乙")

            # 主大将宫迫
            if (__主大将所在的九宫Point + 1) == __太乙所在的九宫Point:
                self.格局.append("主大将内宫迫太乙")

            if (__主大将所在的九宫Point + (-1)) == __太乙所在的九宫Point:
                self.格局.append("主大将外宫迫太乙")

            # 主参将宫迫
            if (__主参将所在的九宫Point + 1) == __太乙所在的九宫Point:
                self.格局.append("主参将内宫迫太乙")

            if (__主参将所在的九宫Point + (-1)) == __太乙所在的九宫Point:
                self.格局.append("主参将外宫迫太乙")

            # 客大将宫迫
            if (__客大将所在的九宫Point + 1) == __太乙所在的九宫Point:
                self.格局.append("客大将内宫迫太乙")

            if (__客大将所在的九宫Point + (-1)) == __太乙所在的九宫Point:
                self.格局.append("客大将外宫迫太乙")

            # 客参将宫迫
            if (__客参将所在的九宫Point + 1) == __太乙所在的九宫Point:
                self.格局.append("客参将内宫迫太乙")

            if (__客参将所在的九宫Point + (-1)) == __太乙所在的九宫Point:
                self.格局.append("客参将外宫迫太乙")

            # 文昌辰击
            __太乙在16神上的Point = __太乙所在的九宫Point.间辰Point
            if (self.文昌 + 1) == __太乙在16神上的Point:
                self.格局.append("文昌内辰迫太乙")
            if (self.文昌 + (-1)) == __太乙在16神上的Point:
                self.格局.append("文昌外辰迫太乙")
#             return True

        def 囚():
            __文昌Point = self.文昌
            __主大将Point = self.主大将
            __主参将Point = self.主参将
            __客大将Point = self.客大将
            __客参将Point = self.客参将
            __太乙Point = self.太乙
            if __文昌Point.宫数 == __太乙Point.宫数:
                self.格局.append("文昌囚太乙")

            if __主大将Point.宫数 == __太乙Point.宫数:
                self.格局.append("主大将囚太乙")

            if __主参将Point.宫数 == __太乙Point.宫数:
                self.格局.append("主参将囚太乙")

            if __客大将Point.宫数 == __太乙Point.宫数:
                self.格局.append("客大将囚太乙")

            if __客参将Point.宫数 == __太乙Point.宫数:
                self.格局.append("客参将囚太乙")
#             return True

        def 关():
            __将 = {
                "文昌": self.文昌,
                "始击": self.始击,
                "主大将": self.主大将.间辰Point,
                "主参将": self.主参将.间辰Point,
                "客大将": self.客大将.间辰Point,
                "客参将": self.客参将.间辰Point
            }
            __将list = ["文昌", "始击", "主大将", "主参将", "客大将", "客参将"]
            for k in range(0, len(__将list)):
                for k1 in __将list[(k+1):]:
                    if __将[__将list[k]].宫数 == 0 and __将[k1].宫数 == 0:
                        if self.文昌 == self.始击:
                            self.格局.append("文昌与始击")
                    else:
                        if __将[__将list[k]].宫数 != 5 and \
                                __将[__将list[k]].宫数 == __将[k1].宫数:
                            self.格局.append("{}与{}关".format(__将list[k], k1))
#             return True

        def 格对():
            __文昌Point = self.文昌.九宫Point
#             __始击Point = self.始击.九宫Point
#             __主大将Point = self.主大将
#             __主参将Point = self.主参将
#             __客大将Point = self.客大将
#             __客参将Point = self.客参将
            __太乙Point = self.太乙
            if __文昌Point != __太乙Point and (__文昌Point - __太乙Point) % 4 == 0:
                self.格局.append("文昌与太乙对")

            __将 = {
                "始击": self.始击.九宫Point,
                "主大将": self.主大将,
                "主参将": self.主参将,
                "客大将": self.客大将,
                "客参将": self.客参将
            }
            for k, v in __将.items():
                if v.宫数 != 5 and v != __太乙Point and (v - __太乙Point) % 4 == 0:
                    self.格局.append("{}与太乙格".format(k))
#             return True

        def 四郭固():
            if "文昌囚太乙" in self.格局 and "主大将与主参将关" in self.格局:
                self.格局.append("四郭固")

            if "始击掩太乙" in self.格局 and "客大将与客参将关" in self.格局:
                self.格局.append("四郭固")

        __格局Func = [掩, 击, 迫, 囚, 关, 格对, 四郭固]
        for i in __格局Func:
            i()


class ShiJiShiPan(ShiPan):
    def __init__(self, y, m, d, h, minute, sec):
        super().__init__(y, m, d, h, minute, sec)

    def init(self):
        y = self.year
        __积年 = self.太乙积年 + y - 1
        # 前一年冬至前一日积日
        __积日 = __积年 * (self.岁实整数 * self.岁实分母 + self.岁实分子) // self.岁实分母
        __冬至前一日干支 = (干支(干("甲"), 支("子")) + (__积日 % 60 - 1))

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        cursor = c.execute('select solarmonth, solarday, solarhours, '
                           'ganzhiday from litable where solaryear={} and '
                           'jiqi="冬至"'.format(y - 1))
        row = cursor.fetchall()[0]
        solarmonth = int(row[0])
        solarday = int(row[1])
        solarhours = row[2]
        ganzhiday = row[3][0:2]
        conn.close()

        # 校正误差
        __冬到前一日实际干支 = 干支(干(ganzhiday[0]), 支(ganzhiday[1])) + (-1)
        __积日 = __积日 - (__冬至前一日干支 - __冬到前一日实际干支)

        __冬至前一日Time = datetime.datetime.strptime(
            "{0}-{1:02d}-{2:02d} {3}".format(
                y - 1, solarmonth, solarday, "00:00:00"),
            "%Y-%m-%d %H:%M:%S") - datetime.timedelta(days=1)

        __前一日Time = datetime.datetime.strptime(
            "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}".format(
                self.year, self.month, self.day, 0, 0),
            "%Y-%m-%d %H:%M") - datetime.timedelta(days=1)

        __积日 = __积日 + (__前一日Time - __冬至前一日Time).days
        __积时 = __积日 * 12 + (self.hour + 1) // 2 + 1
        self.积算 = __积时

        # 获取年月干支
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        cursor = c.execute(
            "select solaryear, solarmonth, solarday, solarhours, ganzhiyear,"
            "ganzhimonth  from litable where solaryear>={} "
            "and solaryear<={}".format(y - 1, y + 1))
        siZhu = ""
        for row in cursor:
            solaryear = int(row[0])
            solarmonth = int(row[1])
            solarday = int(row[2])
            solarhours = row[3]
            ganzhiyear = row[4][0:2]
            ganzhimonth = row[5][0:2]
            tmpTime = datetime.datetime.strptime(
                "{0}-{1:02d}-{2:02d} {3}".format(
                    solaryear, solarmonth, solarday, solarhours),
                "%Y-%m-%d %H:%M:%S")
            __当日Time = datetime.datetime.strptime(
                "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}".format(
                    self.year,
                    self.month,
                    self.day,
                    self.hour,
                    self.minute,
                    self.sec),
                "%Y-%m-%d %H:%M:%S")
            if __当日Time == tmpTime:
                siZhu = "{} {}".format(ganzhiyear, ganzhimonth)
                break
            if __当日Time < tmpTime:
                break
            siZhu = "{} {}".format(ganzhiyear, ganzhimonth)
        conn.close()
        __日干支 = 干支(干("甲"), 支("子")) + ((__积日 + 1) % 60 - 1)
        if self.hour == 23:
            __日干支 = __日干支 + 1
        __时干支 = 干支(干("甲"), 支("子")) + (__积时 % 60 - 1)
        siZhu = "{} {} {}".format(siZhu, __日干支, __时干支)
        # 求空亡
        __旬首 = __日干支.支 + (干("甲") - __日干支.干)
        siZhu = '{} (甲{}旬，<font color="red">{}、{}</font>空亡)'.format(
            siZhu, __旬首, __旬首 + (-2), __旬首 + (-1))
        self.header = "{} <div>干支: {} </div> <div>时计太乙</div>".format(
            self.header, siZhu)

    def is阳遁(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()

        # 冬至
        querySql = ("select solaryear, solarmonth, solarday, solarhours from "
                    "litable where solaryear={} and jiqi=\"冬至\"".format(
                        self.year))
        cursor = c.execute(querySql)
        row = cursor.fetchall()[0]
        __冬至Time = datetime.datetime.strptime("{0}-{1:02d}-{2:02d} {3}".format(
            row[0], int(row[1]), int(row[2]), row[3]), "%Y-%m-%d %H:%M:%S")
        # 夏至
        querySql = ("select solaryear, solarmonth, solarday, solarhours from "
                    "litable where solaryear={} and jiqi=\"夏至\"".format(
                        self.year))
        cursor = c.execute(querySql)
        row = cursor.fetchall()[0]
        __夏至Time = datetime.datetime.strptime("{0}-{1:02d}-{2:02d} {3}".format(
            row[0], int(row[1]), int(row[2]), row[3]), "%Y-%m-%d %H:%M:%S")
        conn.close()
        __当日Time = datetime.datetime.strptime(
            "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{4:02d}".format(
                self.year, self.month, self.day, self.hour,
                self.minute, self.sec), "%Y-%m-%d %H:%M:%S")
        if __当日Time >= __夏至Time and __当日Time < __冬至Time:
            return False
        return True

    def get八门(self):
        __积算 = self.积算
        __值事八门入局年数 = __积算 % 120
        if __值事八门入局年数 == 0:
            __值事八门入局年数 = 120

        __值事八门 = __值事八门入局年数 // 30
        if __值事八门入局年数 % 30 != 0:
            __值事八门 = __值事八门 + 1

        if self.is阳遁():
            __四门 = [0, 1, 3, 8, 2]
            __值事八门 = __四门[__值事八门]
        else:
            __四门 = [0, 5, 7, 4, 6]
            __值事八门 = __四门[__值事八门]

        __太乙宫数 = self.太乙.宫数
        __太乙宫数所对应的九宫 = Get九宫Point(__太乙宫数)

        __八门 = ["开", "休", "生", "伤", "杜", "景", "死", "惊"]
        for i in range(0, 8):
            self.set(__八门[(__值事八门 - 1 + i) % 8], __太乙宫数所对应的九宫 + i)

    def __str__(self):
        __起局时间 = "{}年{}月{}日{}时{}分{}秒".format(self.year, self.month, self.day,
                                             self.hour, self.minute, self.sec)
        return "<div>{}</div>{}".format(__起局时间, super().__str__())


if __name__ == "__main__":
#     a = ShiPan(940, 4, 28, 23, 9, 8)
#     print(a.主算)
    # print(支(1))
    for i in range(0, 72):
        a = ShiPan(1972 + i, 4, 28, 23, 9, 8)
        if a.文昌!=a.始击:
            print("{} 局主算： {} 客算: {}".format(i+1, a.主算, a.客算))
