import sys
import datetime
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
from shipan.shipan import ShiPan, ShiJiShiPan

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

# font=QtGui.QFont()
# font.setPixelSize(18)
# textBrowser.setFont(font)
# font := gui.NewQFont()
# font.SetPixelSize(18)
# textBrowser.SetFont(font)
# //textBrowser.SetLineWidth(1000)
# layout.AddWidget(textBrowser, 0, 0)

# 设置右则面板
rightWidget = QtWidgets.QWidget()
rightWidget.setFixedWidth(100)
layout.addWidget(rightWidget)

# 为右则面板使用水平布局
rightVBoxLayout = QtWidgets.QVBoxLayout()
rightWidget.setLayout(rightVBoxLayout)
#
# // 设置输入验证
# //	regx := core.NewQRegExp()
# //	regx.SetPattern("^(0|[1-9][0-9]*|-[1-9][0-9]*)$")
# //	validator := gui.NewQRegExpValidator(nil)
# //	validator.SetRegExp(regx)
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
    s = ShiPan(year)
    # print(string(shiPan))
    textBrowser.setHtml("{}".format(s))
    # textBrowser.setText("{}".format(s))


def 时计():
    year = int("0{}".format(yearInput.text()))
    month = int("0{}".format(monthInput.text()))
    day = int("0{}".format(dayInput.text()))
    hour = int("0{}".format(hourInput.text()))
    minutes = int("0{}".format(minutesInput.text()))
    second = int("0{}".format(secondInput.text()))
    if year < 1920 or year > 2100 or \
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
    s = ShiJiShiPan(year, month, day, hour, minutes, second)
    # print(string(shiPan))
    textBrowser.setHtml("{}".format(s))
    # textBrowser.setText("{}".format(s))


def onclick():
    juType = juTypeInput.currentIndex()
    if juType == 0:
        年计()
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
        helpStrings = ("<div><font style=font-weight:bold;>说明：</font></div>"
                       "<div>八三四九为阳宫，二七六一为阴宫</div>"
                       "<div>太乙在一、八、三、四宫为内，助主；太乙在九、二、七、六宫为在外，助客 </div>"
                       "<div>阴阳易绝之气举事皆凶</div>"
                       "<div> 数 &lt; 10: 无天之算 </div>"
                       "<div> 数 % 10 &lt; 5: 无地之算 </div>"
                       "<div> 数 % 10 == 0: 无人之算 </div>"
                       "<div>开休生大吉，景小吉，惊小凶，杜死伤大凶</div>"
                       "<div><font style=font-weight:bold;color:red>格局：</font>"
                       "</div>"
                       "<div><font style=font-weight:bold;>掩 ：</font><div>"
                       "《经》曰：始击将临太乙宫，谓之掩。岁计遇之，王纲失序，臣强群弱，宜修德以禳之。"
                       "盖掩袭劫杀之义。若掩太乙在阳绝之地，君凶；阴绝之地，臣诛。掩主大将，主人算和，"
                       "吉；不和凶。参将击之胜。</div></div>"
                       "<div><font style=font-weight:bold;>击：</font><div>《经》曰："
                       "太乙所在宫，客目在太乙前一辰，为前击；在太乙后一辰，为后击；在太乙前一宫，为外宫击；"
                       "在太乙后一宫，为内宫击。所为击者，臣凌君卑。凌尊，下凌上，僭也。岁计遇之，将相相伐之义也。"
                       "</div></div>"
                       "<div><font style=font-weight:bold;>迫：</font><div>《经》曰："
                       "前为外迫，后为内迫，为上、下二目，主、客大小四将，在太乙左右为迫。"
                       "王希明曰：下目无迫。若上目在太乙前一辰，为外辰迫；在后一辰，为内辰迫； 在太乙前一宫，"
                       "为外宫迫；后一宫，为内宫迫。宫迫，灾微缓；"
                       "辰迫，灾急疾。岁计遇迫，人君慎之。</div></div>"
                       "<div><font style=font-weight:bold;>囚：</font><div>《经》曰："
                       "囚者，篡戮之义也。若文昌将并主、客、大、小四将俱与太乙同宫，总名曰囚。"
                       "若在易气、绝气之地，大凶；若在绝阳、绝阴之地，自败，臣受诛。若诸将与太乙同宫，或近大将，"
                       "谋在同类；近参将，谋在内也。算和者，利；算不和者，谋不成也。"
                       "（中国古代星占学，靠近天目者谋在内及同姓，近地目者谋在外及异姓。若算和谋成，"
                       "算不和则谋不成。）</div></div>"
                       "<div><font style=font-weight:bold;>关：</font><div>《经》曰："
                       "客、主、大、小将目相宫齐为关。王希明曰：关之为义，但将相怕忌之事，不及于君也。"
                       "主、客、大、小将同宫数齐，皆为关日。 </div></div>"
                       "<div><font style=font-weight:bold;>格：</font><div>《经》曰："
                       "客目、大、小将与太乙对宫为格，言政事上下格也。若在阳绝之地，又与岁计遇格，不利。"
                       "有为所格者，格易之义也，若格太乙者，盗侮其君，主客算不知者必败。</div></div>"
                       "<div><font style=font-weight:bold;>对：</font><div>《经》曰："
                       "下目文昌将与太乙冲而相当都为对，若下目相对之时皆为大臣怀二心，君逐良将，凶奸生，下"
                       "臣欺上。</div></div>"
                       "<div><font style=font-weight:bold;>四郭固：</font><div>"
                       "《经》曰："
                       "四郭固者，文昌将囚太乙宫，至大将参将又相关，或客目临之或客大小将相关，皆四郭固也。"
                       "主人胜固者凭胜不利先起四郭之固岁计遇之主篡废之祸利以修德禳之也。"
                       "《太乙通解》四郭固是指天子之都邑，四面皆有城墙，宜坚壁固守，谨防灾变。</div></div>"
                       )
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


# button.ConnectClicked(func(checked bool) {
# 	yearString := yearInput.Text()
# 	//			year, _ := strconv.Atoi(yearString)
# 	//			if year == 0 {
# 	//				widgets.QMessageBox_Information(nil, "OK", "无此公元纪年",
# 	//					widgets.QMessageBox__Ok, widgets.QMessageBox__Ok)
# 	//				return
# 	//			}
#
# 	//		monthString := monthInput.CurrentText()
# 	monthString := monthInput.Text()
# 	dayString := dayInput.Text()
# 	hourString := hourInput.Text()
# 	minutesString := minutesInput.Text()
#
# 	year, _ := strconv.Atoi(yearString)
# 	month, _ := strconv.Atoi(monthString)
# 	day, _ := strconv.Atoi(dayString)
# 	hour, _ := strconv.Atoi(hourString)
# 	minutes, _ := strconv.Atoi(minutesString)
#
# 	if year < 1920 || year > 2100 || month < 1 || month > 12 || day < 1 || day > 31 || hour < 0 || hour > 23 || minutes < 0 || minutes > 59 {
# 		widgets.QMessageBox_Information(nil, "OK", "输入时间不正确",
# 			widgets.QMessageBox__Ok, widgets.QMessageBox__Ok)
# 		return
#
# 	}
# 	monthString = fmt.Sprintf("%02d", month)
# 	dayString = fmt.Sprintf("%02d", day)
# 	hourString = fmt.Sprintf("%02d", hour)
# 	minutesString = fmt.Sprintf("%02d", minutes)
#
# 	timeString := fmt.Sprintf("%s-%s-%s %s:%s", yearString, monthString, dayString, hourString, minutesString)
#
# 	_, err := time.Parse("2006-01-02 15:04", timeString)
# 	if err != nil {
# 		widgets.QMessageBox_Information(nil, "OK", "没有这个时间"+timeString,
# 			widgets.QMessageBox__Ok, widgets.QMessageBox__Ok)
# 		return
# 	}
#
# 	s := shipan.New(year, month, day, hour, minutes)
# 	//		s.GetWidget(scene)
# 	//		view.Viewport().Update()
# 	//		scene.Update2(0, 0, 100, 100)
# 	//		textBrowser.scene
# 	//		view.Viewport().UpdateDefault()
# 	//		var layoutView = widgets.NewQVBoxLayout()
# 	//		layoutView.AddWidget(s.GetWidget(), 0, 0)
# 	//		textBrowser.SetLayout(layoutView)
# 	//s.Get太乙(year)
# 	//		textBrowser.SetText(s.String())
# 	//			textBrowser.SetHtml(s.String())
# 	textBrowser.SetHtml(s.String())
# })
#
# // Set main widget as the central widget of the window
window.setCentralWidget(mainWidget)
#
# // Show the window
window.show()
#
# // Execute app
app.exec()
