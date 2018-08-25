import datetime
# import sqlite3
import eacal
from ganzhiwuxin import *
from shipan.point import *

# DB = os.path.dirname(os.path.realpath(__file__)) + '/data/lifa.db'


class ShiPan():
    # 太乙积年 = 10153917
    太乙积年 = 1936557
    岁实整数 = 365
    岁实分子 = 7877
    岁实分母 = 32193
    三基积年 = 284287

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
        self.合神 = None
        self.始击 = None
        self.主大将 = None
        self.主参将 = None
        self.客大将 = None
        self.客参将 = None
        self.主算 = None
        self.客算 = None
        self.定目 = None
        self.定大将 = None
        self.定参将 = None
        self.定算 = None
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
        self.get合神()
        self.get天目()
        self.get主将()
        self.get始击()
        self.get客将()
        self.get定目()
        self.get定将()

        self.get格局()
        self.get君基()
        self.get臣基()
        self.get民基()
        self.get五福()
        self.get大游()

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
        __值事八门 = '<div><font color="red">{}门值事</font><div>'.format(self.值事八门)
        __格局 = '<div><font color="red">格局：</font></div> <div>{}</div>'.format(
            '、'.join(self.格局))
        __shiPanTable = "<table>{}</table>".format(__shiPanTable)

        return "<html><head>{}</head><body>{}{}{}{}</body></html>".format(
            __css, self.header, __值事八门, __格局, __shiPanTable)

    def set(self, s, p):
        self.shiPan[p.x][p.y].append(s)

    def init(self):
        pass

    def is阳遁(self):
        return True

    def shuType(self, n):
        t = []
        if n > 10 and n % 10 > 5:
            t.append("三才足数")
        if n < 10:
            t.append("无天")
        if n % 10 < 5:
            t.append("无地")
        if n % 10 == 0:
            t.append("无人")
        to_type = {1: "杂阴", 2: "纯阴", 3: "纯阳", 4: "杂阳", 6: "纯阴", 7: "杂阴", 8: "杂阳", 9: "纯阳",
                   11: "阴中重阳", 12: "下和", 13: "杂重阳", 14: "上和", 16: "下和", 17: "阴中重阳", 18: "上和", 19: "杂重阳",
                   22: "纯阴", 23: "次和", 24: "杂重阴", 26: "纯阴", 27: "下和", 28: "杂重阴", 29: "次和", 31: "杂重阳",
                   32: "次和", 33: "纯阳", 34: "下和", 37: "杂重阳", 38: "下和", 39: "纯阳"}
        t.append(to_type.get(n, None))
        return [i for i in t if i is not None]

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
        self.值事八门 = __八门[__值事八门 - 1]

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

    def get合神(self):
        __积算 = self.积算
        __支num = __积算 % 12
        if __支num == 0:
            __支num = 12
        __支 = 支(__支num)
        __丑 = 支("丑")
        __合神支 = __丑 + (-1 * (__支 - 支("子")))

        __合神 = '<font color="red">合神</font>'
        self.合神 = Get间辰Point("{}".format(__合神支))
        self.set(__合神, self.合神)

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

        __主算_type = self.shuType(__主算)
        self.header = '{}<div><font color="red">主算:{} {}</font></div>'.format(
            self.header, __主算, "、".join(__主算_type))
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
        __客算_type = self.shuType(__客算)
        self.header = '{}<div><font color="red">客算:{} {}</font></div>'.format(
            self.header, __客算, "、".join(__客算_type))
        self.客算 = __客算

    def get定目(self):
        __积算 = self.积算
        __支num = __积算 % 12
        if __支num == 0:
            __支num = 12
        __支 = 支(__支num)

        # 求定目位置
        __支Point = Get间辰Point("{}".format(__支))
        __合神Point = self.合神
        __文昌Point = self.文昌
        __定目 = '<div><font color="red">定目</font></div >'

        for i in range(0, 16):
            if __合神Point + i == __支Point:
                self.定目 = __文昌Point + i
                break
        self.set(__定目, self.定目)

    def get定将(self):
        __定大将 = '<font color="red">定大将</font>'
        __定参将 = '<font color="red">定参将</font>'

        # 求定算
        __太乙point = self.太乙
        __定目point = self.定目
        __定算 = 0
        if __定目point.宫数 == 0:
            __定算 = 1
        for i in range(0, 16):
            if (__定目point + i).宫数 == __太乙point.宫数:
                break
            __定算 = __定算 + (__定目point + i).宫数
        if __太乙point.宫数 == __定目point.宫数:
            __定算 = __太乙point.宫数

        # 求定大将
        __定大将宫数 = __定算 % 10
        if __定大将宫数 == 0:
            __定大将宫数 = __定算 % 9
        self.定大将 = Get九宫Point(__定大将宫数)
        self.set(__定大将, self.定大将)

        # 求客参将
        __定参将宫数 = (__定大将宫数 * 3) % 10
        self.定参将 = Get九宫Point(__定参将宫数)
        self.set(__定参将, self.定参将)
        __定算_type = self.shuType(__定算)
        self.header = '{}<div><font color="red">定算:{} {}</font></div>'.format(
            self.header, __定算, "、".join(__定算_type))
        self.定算 = __定算

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
            if "文昌囚太乙" in self.格局 and "主大将与客大将关" in self.格局:
                self.格局.append("四郭固")
            if "文昌囚太乙" in self.格局 and "主参将与客参将关" in self.格局:
                self.格局.append("四郭固")

        def 执提():
            if "开" in self.值事八门 or "生" in self.值事八门 or "杜" in self.值事八门 \
                    or "死" in self.值事八门:
                self.格局.append("执提")

        def 提挟():
            __太乙所在的九宫Point = self.太乙
            __文昌所在的九宫Point = self.文昌.九宫Point
            __始击所在的九宫Point = self.始击.九宫Point
            __主大将所在的九宫Point = self.主大将
            __主参将所在的九宫Point = self.主参将
            __客大将所在的九宫Point = self.客大将
            __客参将所在的九宫Point = self.客参将
            __九宫list = [__文昌所在的九宫Point, __始击所在的九宫Point,
                        __主大将所在的九宫Point, __主参将所在的九宫Point,
                        __客大将所在的九宫Point, __客参将所在的九宫Point]
            __将list = [__主大将所在的九宫Point, __主参将所在的九宫Point,
                       __客大将所在的九宫Point, __客参将所在的九宫Point]
            if ((__太乙所在的九宫Point + 1) in __九宫list and
                (__太乙所在的九宫Point + 2) in __将list) or \
                ((__太乙所在的九宫Point + (-1)) in __九宫list and
                 (__太乙所在的九宫Point + (-2)) in __将list):
                self.格局.append("执挟")

        def 四郭杜():
            __文昌所在的九宫Point = self.文昌.九宫Point
            __主大将所在的九宫Point = self.主大将
            __主参将所在的九宫Point = self.主参将
            __客大将所在的九宫Point = self.客大将
            __客参将所在的九宫Point = self.客参将
            if __文昌所在的九宫Point in [__客大将所在的九宫Point, __客参将所在的九宫Point] and \
                    (__主参将所在的九宫Point == __客大将所在的九宫Point or
                     __主大将所在的九宫Point == __客参将所在的九宫Point):
                self.格局.append("四郭杜")
        __格局Func = [掩, 击, 迫, 囚, 关, 格对, 四郭固, 执提, 提挟, 四郭杜]
        for i in __格局Func:
            i()

    def get君基(self):
        pass

    def get臣基(self):
        pass

    def get民基(self):
        pass

    def get五福(self):
        # http://www.fengshui-168.com/thread-45937-1-1.html?_dsign=6ee23359
        pass

    def get大游(self):
        pass


class NianJiShiPan(ShiPan):
    def __init__(self, y):
        super().__init__(y)

    def init(self):
        y = self.year

        __积年 = self.太乙积年 + y
        if y < 0:
            __积年 = self.太乙积年 + 1 + y

        __年干支 = 干支(干("甲"), 支("子")) + (__积年 % 60 - 1)

        self.积算 = __积年
        self.header = "{} <div>干支: {} </div> <div>年计太乙</div>".format(
            self.header, __年干支)

    def get君基(self):
        __jn = self.三基积年 + self.year
        if self.year < 0:
            __jn = __jn + 1
        jn = __jn % 360
        if jn == 0:
            jn = 360
        rg = jn // 30
        rn = jn % 30
        if rn == 0:
            rg = rg - 1
            rn = 30
        rg = rg + 1
        xu = 支("戌")
        junJi = xu + (rg - 1)
        junJiPoint = Get间辰Point("{}".format(junJi))
        __junJi = '<font color="green"><b>君基</b></font>'
        self.set(__junJi, junJiPoint)

    def get臣基(self):
        __jn = self.三基积年 + self.year
        if self.year < 0:
            __jn = __jn + 1
        jn = __jn % 36
        if jn == 0:
            jn = 36
        rg = jn // 3
        rn = jn % 3
        if rn == 0:
            rg = rg - 1
            rn = 3
        rg = rg + 1
        xu = 支("戌")
        junJi = xu + (rg - 1)
        junJiPoint = Get间辰Point("{}".format(junJi))
        __junJi = '<font color="green"><b>臣基</b></font>'
        self.set(__junJi, junJiPoint)

    def get民基(self):
        __jn = self.三基积年 + self.year
        if self.year < 0:
            __jn = __jn + 1
        jn = __jn % 12
        if jn == 0:
            jn = 12
        xu = 支("戌")
        junJi = xu + (jn - 1)
        junJiPoint = Get间辰Point("{}".format(junJi))
        __junJi = '<font color="green"><b>民基</b></font>'
        self.set(__junJi, junJiPoint)

    def get五福(self):
        # http://www.fengshui-168.com/thread-45937-1-1.html?_dsign=6ee23359
        __五福太乙积年 = 12607
        y = self.year
        __积算 = __五福太乙积年 + y
        if y < 0:
            __积年 = __五福太乙积年 + 1 + y
        __入纪元数 = __积算 % 225
        if __入纪元数 == 0:
            __入纪元数 = 225
        __入元周数 = __入纪元数 // 45
        __入元数 = __入纪元数 % 45
        if __入元数 == 0:
            __入元周数 = __入元周数 - 1
            __入元数 = 45
        __五福太乙所在宫数 = __入元周数 + 1
        __五福太乙宫组 = [JianChenPoint(4, 4), JianChenPoint(4, 0),
                    JianChenPoint(0, 0), JianChenPoint(0, 4),
                    JiuGongPoint(2, 2)]
        __五福太乙Point = __五福太乙宫组[__五福太乙所在宫数 - 1]
        __五福所主 = ["利士卒", "利君王", "利公侯宰臣", "利后妃", "利太子", "利庶民", "利师帅",
                  "利上将军", "利中将军", "利下将军"]
        __header = '{}<div><font color="#A52A2A">五福入宫{}年 {}</font></div>'
        self.header = __header.format(self.header, __入元数, __五福所主[__入元数 % 10])
        __五福 = '<div><font color="#A52A2A"><b>五福</b></font></div >'
        self.set(__五福, __五福太乙Point)

    def get大游(self):
        __大游积年 = 12607
        y = self.year
        __积算 = __大游积年 + y
        if y < 0:
            __积年 = __大游积年 + 1 + y
        __入纪元数 = __积算 % 288
        if __入纪元数 == 0:
            __入纪元数 = 228
        __入元周数 = __入纪元数 // 36
        __入元数 = __入纪元数 % 36
        if __入元数 == 0:
            __入元周数 = __入元周数 - 1
            __入元数 = 36
        __大游太乙所在宫数 = __入元周数 + 1
        # 7, 8, 9, 1, 2, 3, 4, 6


class YueJiShiPan(ShiPan):
    def __init__(self, y, m):
        super().__init__(y, m)

    def init(self):
        y = self.year
        m = self.month
        __积年 = self.太乙积年 + y - 1
        if y < 0:
            __积年 = __积年 + 1
        __积算 = __积年 * 12 + 2 + m
        self.积算 = __积算
        print(__积算)

        __年干支 = 干支(干("甲"), 支("子")) + ((__积年 + 1) % 60 - 1)
        __月干支 = 干支(干("甲"), 支("子")) + (__积算 % 60 - 1)

        self.header = "{} <div>干支: {} {}</div> <div>月计太乙</div>".format(
            self.header, __年干支, __月干支)


class RiJiShiPan(ShiPan):
    def __init__(self, y, m, d):
        super().__init__(y, m, d)

    def init(self):
        # __基准积日 = 708011105
        # __基准时间 = datetime.datetime.strptime("1900-12-21 00:00:00",
        #                                     "%Y-%m-%d %H:%M:%S")
        __基准积日 = 0
        __基准时间 = datetime.datetime.strptime("1900-06-19 00:00:00",
                                            "%Y-%m-%d %H:%M:%S")
        y = self.year
        m = self.month
        d = self.day

        __t = datetime.datetime.strptime(
            "{0:04}-{1:02d}-{2:02d} 00:00:00".format(y, m, d),
            "%Y-%m-%d %H:%M:%S")
        __积日 = __基准积日 + (__t - __基准时间).days
        self.积算 = __积日

        c = eacal.EACal(zh_s=True)
#         print(c)
        __年干支, __月干支, __日干支 = c.get_cycle_ymd(datetime.datetime(y, m, d))
        __日干支 = 干支(干("癸"), 支("亥")) + __积日 % 60
#         __月干支 = 干支(干("甲"), 支("子")) + (__积算 % 60 - 1)

        self.header = "{} <div>干支: {} {} {}</div> <div>月计太乙</div>".format(
            self.header, __年干支, __月干支, __日干支)


class ShiJiShiPan(ShiPan):
    def __init__(self, y, m, d, h, minute, sec, 月将):
        super().__init__(y, m, d, h, minute, sec)
        self.月将 = 支(月将)

    def init(self):
        __基准积日 = 708011105
        __基准时间 = datetime.datetime.strptime("1900-12-21 00:00:00",
                                            "%Y-%m-%d %H:%M:%S")
        y = self.year
        m = self.month
        d = self.day

        __t = datetime.datetime.strptime(
            "{0:04}-{1:02d}-{2:02d} 00:00:00".format(y, m, d),
            "%Y-%m-%d %H:%M:%S")
        __积日 = __基准积日 + (__t - __基准时间).days
        __积时 = (__积日 - 1) * 12 + (self.hour + 1) // 2 + 1
        self.积算 = __积时

        c = eacal.EACal(zh_s=True)
        __年干支, __月干支, __日干支 = c.get_cycle_ymd(datetime.datetime(y, m, d))
        __日干支 = 干支(干("癸"), 支("亥")) + __积日 % 60
        if self.hour == 23:
            __日干支 = __日干支 + 1
        __时干支 = 干支(干("癸"), 支("亥")) + __积时 % 60
        siZhu = "{} {} {} {}".format(__年干支, __月干支, __日干支, __时干支)
        # 求空亡
        __旬首 = __日干支.支 + (干("甲") - __日干支.干)
        siZhu = '{} (甲{}旬，<font color="red">{}、{}</font>空亡)'.format(
            siZhu, __旬首, __旬首 + (-2), __旬首 + (-1))
        self.header = "{} <div>干支: {} </div> <div>时计太乙</div>".format(
            self.header, siZhu)

    def is阳遁(self):
        c = eacal.EACal(zh_s=True)
        __冬至Time = c.get_specified_solar_term(self.year, 21)[2].replace(
            tzinfo=None)
        __夏至Time = c.get_specified_solar_term(self.year, 9)[2].replace(
            tzinfo=None)
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
        self.值事八门 = __八门[__值事八门 - 1]

    def __str__(self):
        __起局时间 = "{}年{}月{}日{}时{}分{}秒".format(self.year, self.month, self.day,
                                             self.hour, self.minute, self.sec)
        return "<div>{}</div>{}".format(__起局时间, super().__str__())


if __name__ == "__main__":
    for i in range(0, 73):
        a = NianJiShiPan(2044 + i)
        print("{},{}".format(a.主算, a.客算))
#     print(a)
#     print(a.主算)
    # print(支(1))
#     for i in range(0, 72):
#         a = ShiPan(1972 + i, 4, 28, 23, 9, 8)
#         if a.文昌!=a.始击:
#             print("{} 局主算： {} 客算: {}".format(i+1, a.主算, a.客算))
#         if a.文昌 == a.始击:
#             print("{} {}".format(i+1, a.主算))
