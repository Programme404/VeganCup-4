import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QSpacerItem, QSizePolicy, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QImage, QTransform, QIntValidator
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 300, 1000, 600)
        self.setWindowTitle('ArkCalculator')
        self.fullLayout = QHBoxLayout()
        self.hugeLayout = QVBoxLayout()

        self.title1 = ['难度', '结算分', '藏品', '取钱', '鸭狗熊鼠']
        self.inputLayout = QHBoxLayout()
        self.lineEdt = []
        for i in self.title1:
            self.lineEdt.append(QLineEdit(self))
            self.lineEdt[-1].setValidator(QIntValidator(0, 9999))
            self.lineEdt[-1].setPlaceholderText(i)
            self.lineEdt[-1].setFixedWidth(100)
            self.inputLayout.addWidget(self.lineEdt[-1])
        self.inputLayout.addItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.hugeLayout.addLayout(self.inputLayout)
        
        self.title2 = [['加固安全的角落', '加固诡意行商', '加固去伪存真'],
                       ['或然面纱', '奉献', '斩首', '赴敌者', '王冠之下', '离歌的庭院'], 
                       ['完成结局朝谒', '完成结局圣城'], 
                       ['混乱状态下击杀特雷西斯，黑冠君主，以及召唤的裹骸死士'], 
                       ['混乱状态下击杀博卓卡斯替，圣卫铳骑'], 
                       ['未抓取维什戴尔', '未抓取逻各斯', '未抓取锡人']]
        self.checkLayout1 = []
        self.checkEdt1 = []
        for i in self.title2:
            self.checkEdt1.append([])
            self.checkLayout1.append(QHBoxLayout())
            for j in i:
                self.checkEdt1[-1].append(QCheckBox(j, self))
                self.checkLayout1[-1].addWidget(self.checkEdt1[-1][-1])
            self.checkLayout1[-1].addItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
            self.hugeLayout.addLayout(self.checkLayout1[-1])
        
        self.title3 = {'第二层': ['拆东补西 清理所有年代之刺', '有序清场 清理所有年代之刺'], 
                       '第三层': ['大棋一盘', '苦难年代药枚、筑墙、活木甲不生效', '溃乱魔典', '其他紧急作战'],
                       '第四层': ['年代断层', '清理所有年代之刺', '假想对冲', '猩红甬道', '“预示之谜”发挥作用', '其他紧急作战'],
                       '第五层': ['计划耕种', '通道封锁', '寄人城池下', '其他紧急作战'],
                       '第六层': ['谋求共识', '神圣的渴求'],
                       '特殊作战': ['信号灯 紧急作战', '劫虚济实 紧急作战', '战场侧面 紧急作战', '狭路相逢'],
                       '        ':['阴魂不散', '不请自来', '沉默拳王', '鸭速公路', '紧急']}
        
        self.checkLayout2 = []
        self.checkEdt2 = []
        for i in self.title3:
            self.checkEdt2.append([])
            self.checkLayout2.append(QHBoxLayout())
            self.checkLayout2[-1].addWidget(QLabel(i))
            for j in self.title3[i]:
                self.checkEdt2[-1].append(QCheckBox(j, self))
                self.checkLayout2[-1].addWidget(self.checkEdt2[-1][-1])
            if len(self.title3[i]) > 2:
                self.lineEdt.append(QLineEdit(self))
                self.lineEdt[-1].setFixedWidth(50)
                self.lineEdt[-1].setValidator(QIntValidator(0, 9999))
                self.lineEdt[-1].setDisabled(True)
                self.checkLayout2[-1].addWidget(self.lineEdt[-1])
                if self.title3[i][0] == '大棋一盘':
                    self.checkEdt2[-1][1].setDisabled(True)
                    self.checkEdt2[-1][0].stateChanged.connect(self.onCheckBoxToggled)
                elif self.title3[i][0] == '年代断层':
                    self.checkEdt2[-1][1].setDisabled(True)
                    self.checkEdt2[-1][0].stateChanged.connect(self.onCheckBoxToggled)
                    self.checkEdt2[-1][4].setDisabled(True)
                    self.checkEdt2[-1][3].stateChanged.connect(self.onCheckBoxToggled)
                elif self.title3[i][-1] == '紧急':
                    self.checkEdt2[-1][-1].setDisabled(True)
                    self.checkEdt2[-1][-2].stateChanged.connect(self.onCheckBoxToggled)
                self.checkEdt2[-1][-1].stateChanged.connect(self.onCheckBoxToggled)
            self.checkLayout2[-1].addItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
            self.hugeLayout.addLayout(self.checkLayout2[-1])

        self.buttonLayout = QHBoxLayout()
        self.count = 0
        self.button1 = QPushButton('计算')
        self.button2 = QPushButton('清空输出')
        self.button3 = QPushButton('清空输入')
        self.button1.clicked.connect(self.doCal)
        self.button2.clicked.connect(self.clearOutput)
        self.button3.clicked.connect(self.clearInput)
        self.buttonLayout.addWidget(self.button1)
        self.buttonLayout.addWidget(self.button2)
        self.buttonLayout.addWidget(self.button3)
        self.buttonLayout.addItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.hugeLayout.addLayout(self.buttonLayout)

        self.textEdit = QTextEdit(QWidget(self))
        self.textEdit.setMinimumWidth(400)
        self.textEdit.setReadOnly(True)

        self.fullLayout.addLayout(self.hugeLayout)
        self.fullLayout.addWidget(self.textEdit)
        self.setLayout(self.fullLayout)
        self.show()
    
    def doCal(self):
        self.count += 1
        lineStatus = []
        checkStatus1 = []
        checkStatus2 = []
        fightScore0 = [0, 0, 0, 0, 10, 
                       10, 20, 20, 10, 10]
        fightScore1 = [0, 0, 0, 
                       20, 20, 20, 30, 30, 50,
                       150, 150, 50, 50, 0, 0, 0]
        fightScore2 = [10, 15,
                       30, 20, 40, 0,
                       30, 10, 30, 50, 30, 0,
                       60, 50, 40, 0,
                       70, 60,
                       30, 30, 60, 0,
                       40, 40, 40, 50, 10]
        for i in self.lineEdt:
            lineStatus.append(i.text())
        for i in self.checkEdt1:
            for j in i:
                checkStatus1.append(j.isChecked())
        for i in self.checkEdt2:
            for j in i:
                checkStatus2.append(j.isChecked())
        try:
            nowtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            multi = {'11': 1, '12': 1.1, '13': 1.2, '14': 1.3, '15': 1.6}
            solid = sum(1 for i in checkStatus1[0: 3] if i)
            sco1 = multi[lineStatus[0]] * int(lineStatus[1]) if lineStatus[0] != '' and lineStatus[1] != '' else 0
            sco2 = (3 * int(lineStatus[2]) if lineStatus[2] != '' else 0) + (50 if solid == 3 else solid * 10)
            sco3 = sum(fightScore0[i] * int(lineStatus[i]) for i in range(len(lineStatus)) if lineStatus[i] != '') + sum(fightScore1[i] for i in range(len(checkStatus1)) if checkStatus1[i]) + sum(fightScore2[i] for i in range(len(checkStatus2)) if checkStatus2[i])
            sco4 = (300 if checkStatus1[-3] else 0) + (150 if checkStatus1[-2] else 0) + (50 if checkStatus1[-1] else 0) - (5 * (int(lineStatus[3]) - 60) if lineStatus[3] != '' and int(lineStatus[3]) > 60 else 0)
            self.textEdit.append('第%d次结算' % self.count)
            self.textEdit.append('结算于：%s' % nowtime)
            self.textEdit.append('结算分：%d' % sco1)
            self.textEdit.append('后勤分：%d' % sco2)
            self.textEdit.append('作战分：%d' % sco3)
            self.textEdit.append('限制分：%d' % sco4)
            self.textEdit.append('总分：%d！' % (sco1 + sco2 + sco3 + sco4))
            self.textEdit.append('')
        except:
            self.textEdit.append('非法的输入')
            self.textEdit.append('')

    def clearOutput(self):
        self.count = 0
        self.textEdit.clear()
    
    def clearInput(self):
        for i in self.lineEdt:
            i.setText('')
        for i in self.checkEdt1:
            for j in i:
                j.setChecked(False)
        for i in self.checkEdt2:
            for j in i:
                j.setChecked(False)

    def onCheckBoxToggled(self, state):
        checkBox = self.sender()
        target1 = {self.checkEdt2[1][0]: self.checkEdt2[1][1], self.checkEdt2[2][0]: self.checkEdt2[2][1],
                   self.checkEdt2[2][3]: self.checkEdt2[2][4], self.checkEdt2[6][-2]: self.checkEdt2[6][-1]}
        target2 = {self.checkEdt2[1][-1]: self.lineEdt[5], self.checkEdt2[2][-1]: self.lineEdt[6],
                   self.checkEdt2[3][-1]: self.lineEdt[7], self.checkEdt2[5][-1]: self.lineEdt[8],
                   self.checkEdt2[6][-1]: self.lineEdt[9]}
        if checkBox in target1:
            if not state:
                    target1[checkBox].setChecked(False)
            target1[checkBox].setEnabled(state == Qt.Checked)
        else:
            if not state:
                    target2[checkBox].setText('')
            target2[checkBox].setEnabled(state == Qt.Checked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())