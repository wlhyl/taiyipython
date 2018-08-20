import sys
import datetime
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
from shipan.shipan import NianJiShiPan, YueJiShiPan, RiJiShiPan, ShiJiShiPan

# Create application
app = QtWidgets.QApplication(sys.argv)

# Create main window
window = QtWidgets.QMainWindow()
window.setWindowTitle("时计太乙")

# Create main layout
layout = QtWidgets.QHBoxLayout()

# Create main widget and set the layout
mainWidget = QtWidgets.QWidget()
mainWidget.setLayout(layout)
# Create a line edit and add it to the layout
textBrowser = QWebEngineView()
# textBrowser = QtWidgets.QTextBrowser()
layout.addWidget(textBrowser)

# 设置右则面板
rightWidget = QtWidgets.QWidget()
rightWidget.setFixedWidth(100)
layout.addWidget(rightWidget)

# 为右则面板使用水平布局
rightVBoxLayout = QtWidgets.QVBoxLayout()
rightWidget.setLayout(rightVBoxLayout)
#
yearInput = QtWidgets.QLineEdit()
yearInput.setPlaceholderText("年 ")
regx = QtCore.QRegExp("^(0|[1-9][0-9]*|-[1-9][0-9]*)$")
validator = QtGui.QRegExpValidator()
validator.setRegExp(regx)
yearInput.setValidator(validator)
# yearInput.setPlaceholderText("年 1920-2050")
# yearInput.setValidator(QtGui.QIntValidator(1920, 2050, yearInput))
rightVBoxLayout.addWidget(QtWidgets.QLabel("年："))
rightVBoxLayout.addWidget(yearInput)

monthInput = QtWidgets.QLineEdit()
monthInput.setPlaceholderText("月")
monthInput.setValidator(QtGui.QIntValidator(1, 12, monthInput))
rightVBoxLayout.addWidget(QtWidgets.QLabel("月："))
rightVBoxLayout.addWidget(monthInput)

dayInput = QtWidgets.QLineEdit()
dayInput.setPlaceholderText("日")
dayInput.setValidator(QtGui.QIntValidator(1, 31, dayInput))
rightVBoxLayout.addWidget(QtWidgets.QLabel("日："))
rightVBoxLayout.addWidget(dayInput)

hourInput = QtWidgets.QLineEdit()
hourInput.setPlaceholderText("时")
hourInput.setValidator(QtGui.QIntValidator(0, 23, hourInput))
rightVBoxLayout.addWidget(QtWidgets.QLabel("时："))
rightVBoxLayout.addWidget(hourInput)

minutesInput = QtWidgets.QLineEdit()
minutesInput.setPlaceholderText("分")
minutesInput.setValidator(QtGui.QIntValidator(0, 59, minutesInput))
rightVBoxLayout.addWidget(QtWidgets.QLabel("分："))
rightVBoxLayout.addWidget(minutesInput)

secondInput = QtWidgets.QLineEdit()
secondInput.setPlaceholderText("秒")
secondInput.setValidator(QtGui.QIntValidator(0, 59, secondInput))
rightVBoxLayout.addWidget(QtWidgets.QLabel("秒："))
rightVBoxLayout.addWidget(secondInput)

juTypeInput = QtWidgets.QComboBox()
juTypeInput.addItems(["年计太乙", "月计太乙", "日计太乙", "时计太乙"])
rightVBoxLayout.addWidget(juTypeInput)

yueJiang = QtWidgets.QComboBox()
yueJiang.addItems(["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"])
rightVBoxLayout.addWidget(QtWidgets.QLabel("月将"))
rightVBoxLayout.addWidget(yueJiang)

button = QtWidgets.QPushButton("起太乙局")
rightVBoxLayout.addWidget(button)
# rightVBoxLayout.addStretch()

helpButton = QtWidgets.QPushButton("帮助")
rightVBoxLayout.addWidget(helpButton)
rightVBoxLayout.addStretch()

# 设置默认时间
nowDateTime = datetime.datetime.now()
yearInput.setText("{}".format(nowDateTime.year))
monthInput.setText("{}".format(nowDateTime.month))
dayInput.setText("{}".format(nowDateTime.day))
hourInput.setText("{}".format(nowDateTime.hour))
minutesInput.setText("{}".format(nowDateTime.minute))
secondInput.setText("{}".format(nowDateTime.second))


# Connect event for button
def 年计():
    yearText = yearInput.text()
    if yearText == "":
        yearText = "0"
    year = int(yearText)
    # year = int("0{}".format(yearInput.text()))
    # year = int("0{}".format(yearInput.text()))
#     month = monthInput.currentIndex()+1
#     juType=juTypeInput.currentIndex()
    # day = int("0{}".format(dayInput.text()))
    # hour = int("0{}".format(hourInput.text()))
    # minutes = int("0{}".format(minutesInput.text()))
    if year == 0:
        QtWidgets.QMessageBox.information(None, "OK", "输入时间不正确",
                                          QtWidgets.QMessageBox.Ok,
                                          QtWidgets.QMessageBox.Ok)
        return
    s = NianJiShiPan(year)
    # print(string(shiPan))
    textBrowser.setHtml("{}".format(s))
    # textBrowser.setText("{}".format(s))


def 月计():
    yearText = yearInput.text()
    if yearText == "":
        yearText = "0"
    year = int(yearText)
    month = int("0{}".format(monthInput.text()))
    # year = int("0{}".format(yearInput.text()))
    # year = int("0{}".format(yearInput.text()))
#     month = monthInput.currentIndex()+1
#     juType=juTypeInput.currentIndex()
    # day = int("0{}".format(dayInput.text()))
    # hour = int("0{}".format(hourInput.text()))
    # minutes = int("0{}".format(minutesInput.text()))
    if year == 0 or month < 1 or month > 12:
        QtWidgets.QMessageBox.information(None, "OK", "输入时间不正确",
                                          QtWidgets.QMessageBox.Ok,
                                          QtWidgets.QMessageBox.Ok)
        return
    s = YueJiShiPan(year, month)
    textBrowser.setHtml("{}".format(s))


def 日计():
    yearText = yearInput.text()
    if yearText == "":
        yearText = "0"
    year = int(yearText)
    month = int("0{}".format(monthInput.text()))
    # year = int("0{}".format(yearInput.text()))
    # year = int("0{}".format(yearInput.text()))
#     month = monthInput.currentIndex()+1
#     juType=juTypeInput.currentIndex()
    day = int("0{}".format(dayInput.text()))
    # hour = int("0{}".format(hourInput.text()))
    # minutes = int("0{}".format(minutesInput.text()))
    if year == 0 or month < 1 or month > 12:
        QtWidgets.QMessageBox.information(None, "OK", "输入时间不正确",
                                          QtWidgets.QMessageBox.Ok,
                                          QtWidgets.QMessageBox.Ok)
        return
    timeString = "{0:04d}-{1:02d}-{2:02d} 00:00:00"
    timeString = timeString.format(year, month, day)
    try:
        datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        QtWidgets.QMessageBox.information(None, "OK",
                                          "输入时间{}不正确".format(timeString),
                                          QtWidgets.QMessageBox.Ok,
                                          QtWidgets.QMessageBox.Ok)
        return
    s = RiJiShiPan(year, month, day)
    textBrowser.setHtml("{}".format(s))


def 时计():
    year = int("0{}".format(yearInput.text()))
    month = int("0{}".format(monthInput.text()))
    day = int("0{}".format(dayInput.text()))
    hour = int("0{}".format(hourInput.text()))
    minutes = int("0{}".format(minutesInput.text()))
    second = int("0{}".format(secondInput.text()))
    if year < 1900 or year > 2100 or \
            month < 1 or month > 12 or \
            day < 1 or day > 31 or \
            hour < 0 or hour > 23 or \
            minutes < 0 or minutes > 59 or \
            second < 0 or second > 59:
        QtWidgets.QMessageBox.information(None, "OK", "输入时间不正确",
                                          QtWidgets.QMessageBox.Ok,
                                          QtWidgets.QMessageBox.Ok)
        return
    timeString = "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}"
    timeString = timeString.format(year, month, day, hour, minutes, second)
    try:
        datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        QtWidgets.QMessageBox.information(None, "OK",
                                          "输入时间{}不正确".format(timeString),
                                          QtWidgets.QMessageBox.Ok,
                                          QtWidgets.QMessageBox.Ok)
        return
    DiZHiList = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    月将=DiZHiList[yueJiang.currentIndex()]
    s = ShiJiShiPan(year, month, day, hour, minutes, second, 月将)
    # print(string(shiPan))
    textBrowser.setHtml("{}".format(s))
    # textBrowser.setText("{}".format(s))


def onclick():
    juType = juTypeInput.currentIndex()
    if juType == 0:
        年计()
        return
    if juType == 1:
        月计()
        return
    if juType == 2:
        日计()
        return
    if juType == 3:
        时计()
        return


class HelpDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # QtWidgets.QDialog(self,parent)
        self.setWindowTitle("帮助")
        self.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint)
        self.resize(700, 500)
        helpLayout = QtWidgets.QVBoxLayout()
        # self.layout=helpLayout
        self.setLayout(helpLayout)
        helpTextBrowser = QtWidgets.QTextBrowser()
        helpLayout.addWidget(helpTextBrowser)
        with open('help/help.html', 'r') as f:
            helpStrings = f.read()
        helpFont = QtGui.QFont()
        helpFont.setPixelSize(18)
        helpTextBrowser.setFont(helpFont)
        helpTextBrowser.setHtml(helpStrings)


def helpOnclick():
    # return
    helpDialog = HelpDialog(window)
    # helpDialog.setWindowTitle("帮助")
    # helpDialog.exec_()
    helpDialog.show()


button.clicked.connect(onclick)
helpButton.clicked.connect(helpOnclick)

# // Set main widget as the central widget of the window
window.setCentralWidget(mainWidget)
#
# // Show the window
window.show()
#
# // Execute app
app.exec()
