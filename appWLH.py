#!/usr/bin/python3
#-*- coding:utf-8 -*-

__author__ = "Wang Siyu"
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from bs4 import BeautifulSoup
import sys
import core
import requests
import os
import time

'''Courses = [
{'notice': [], 'homework': [], 'file': [], 'name': '二年级男生游泳'} ,

{'notice': [],
 'homework': [],
 'file': [
     {'state': '', 'memory': '255.2K', 'time': '2017-03-07', 'rank': '2','url': 'http://learn.tsinghua.edu.cn/uploadFile/downloadFile_student.jsp?module_id=322&filePath=BdUF76se7kaNSpbEFkVemYMy/qVzVqobi8ai3k6ztgTdqcLbq7JPHRArtpnUa0iqpinOZY6ZNRY%3D&course_id=143160&file_id=1757960', 'intro': '', 'title': '课件2'}, {'state': '', 'memory': '275.7K', 'time': '2017-03-21', 'rank': '4', 'url': 'http://learn.tsinghua.edu.cn/uploadFile/downloadFile_student.jsp?module_id=322&filePath=bifk1CccD9ksMhGE6OyEYAGLcLNLZLKlCCsGU9cWiwz%2BOjxn/k4hPP0B2m51IbYdxw6veCs9H3A%3D&course_id=143160&file_id=1770357', 'intro': '', 'title': '课件4'}, {'state': '新文件', 'memory': '332.0K', 'time': '2017-04-20', 'rank': '6', 'url': 'http://learn.tsinghua.edu.cn/uploadFile/downloadFile_student.jsp?module_id=322&filePath=WaDgGqOWd5HOUZXeqEXUdSBF47vkRPCH9Kw7FlfiMwtuNu0qrDDuvPURonbE/p4cO4U9a6tTDo8%3D&course_id=143160&file_id=1795166', 'intro': '', 'title': '课件6'}, {'state': '', 'memory': '222.5K', 'time': '2017-03-07', 'rank': '1', 'url': 'http://learn.tsinghua.edu.cn/uploadFile/downloadFile_student.jsp?module_id=322&filePath=wku4VEBrUky4w0CoOMtu637jAFj22r5FLCI3Y2RxySF0C1CQqfHhTbaVMkd1zNYyGyMc5AF4W%2BA%3D&course_id=143160&file_id=1757958', 'intro': '', 'title': '课件1'}, {'state': '', 'memory': '365.4K', 'time': '2017-03-07', 'rank': '3', 'url': 'http://learn.tsinghua.edu.cn/uploadFile/downloadFile_student.jsp?module_id=322&filePath=uDjPlV0wuLxpWTNo%2BLEM0yyxBpJ2qbC5tRZd2tw3otrl3SKj313eCDehSkP6w4dd9DlxboLc9zI%3D&course_id=143160&file_id=1757962', 'intro': '', 'title': '课件3'}, {'state': '新文件', 'memory': '379.9K', 'time': '2017-04-20', 'rank': '5', 'url': 'http://learn.tsinghua.edu.cn/uploadFile/downloadFile_student.jsp?module_id=322&filePath=6kdzf6q3W91x116cO392/nhJLcaejrIF/43nYXjRC21FIXYjp3PEqrmt6px3/UepzmslmMk2w8k%3D&course_id=143160&file_id=1795164', 'intro': '', 'title': '课件5'},
     {'state': '新文件', 'memory': '352.2K', 'time': '2017-04-29', 'rank': '7', 'url': 'http://learn.tsinghua.edu.cn/uploadFile/downloadFile_student.jsp?module_id=322&filePath=qgsIuPOIrQ2gucxB1zHY5sTwkHTuqXPA6x7%2BkNSNJsxjJYQIkCHVUR5ZE9CNe23zPClWeUJwdJA%3D&course_id=143160&file_id=1801528', 'intro': '', 'title': '课件7'}],
 'name': '概率论与随机过程 (1)'} ,

{'notice': [{'content': ' \n\n\n\n各位同学：\xa0\r\n            \n\xa0第5周开始正式上课，其中第5、6周安排在教室进行，其他时间安排在中央主楼9楼实验室。\n\n\xa0第5周各二级选课分班对应的上课时间地点如下：\xa0\n\xa0SS1：六教6A416，周二晚上第6大节（19：20~21：45）\n\xa0SS2：六教6A416，周三晚上第6大节（19：20~21：45）\n\xa0SS3：六教6A416，周五晚上第6大节（19：20~21：45）\n\n请大家按照自己的二级选课分班上课。第6周的上课地点可能发生变化，请提前注意网络学堂公告。\xa0\n\n孙忆南\r\n            \xa0\n\n\n\n\xa0\r\n\t\t\t', 'release': '孙忆南老师', 'title': '第五周上课安排', 'rank': '1', 'time': '2017-03-14', 'ifread': '已读'}],
 'name': '数字逻辑与处理器基础实验',
 'homework': [
     {'ddl': '2017-04-24',
      'name': '实验一\xa0计数器',
      'attachname': '2015011034_王思宇.pdf',
      'filename': '',
      'memory': '452.7KB',
      'release_time': '2017-04-07',
      'ifsubmit': '尚未提交',
      'title_url': 'http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/hom_wk_detail.jsp?id=750581&course_id=143174&rec_id=5051097'},
     {'ddl': '2017-04-17',
      'name': '使用Verilog的门级电路设计与仿真',
      'attachname': '2015011034_王思宇.pdf',
      'filename': 'Verilog作业.pdf',
       'memory': '557.2KB',
       'release_time': '2017-03-30',
       'ifsubmit': '尚未提交',
       'title_url': 'http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/hom_wk_detail.jsp?id=748859&course_id=143174&rec_id=null'},
     ],
    'file':[]
 }
]'''

preCourses = ()
Courses = []

logWidth = 591
logHeight = 377
width = 1000
height = 870
uniHeight = 250
miniHeight = 30
leftWhite = 20

default_download_dir=""

class appWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUp()

    def setUp(self):
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        QApplication.setFont(font)
        self.setWindowTitle("清华大学网络学堂")
        self.setWindowIcon(QtGui.QIcon(".\\pic\\2.png"))
        self.username = ''
        self.password = ''
        self.memPass = False
        self.auto = False
        self.logTimes = 0
        self.resize(591, 377)
        self.logWidget = QWidget(self)
        self.logWidget.setGeometry(0, 0, 591, 377)
        self.setMouseTracking(False)
        self.setAutoFillBackground(False)
        self.logWidget.setStyleSheet("background: rgb(224, 201, 255)")
        self.label = QLabel(self.logWidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 221, 71))
        font.setPointSize(12)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.logWidget)
        self.label_2.setGeometry(QtCore.QRect(180, 120, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.logWidget)
        self.label_3.setGeometry(QtCore.QRect(180, 170, 72, 15))
        self.label_3.setObjectName("label_3")
        self.pushButton = QPushButton(self.logWidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 280, 181, 41))
        self.pushButton.setStyleSheet("background:rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LogIn)
        #self.pushButton.setShortcut("enter")
        self.checkBox = QCheckBox(self.logWidget)
        self.checkBox.setGeometry(QtCore.QRect(150, 220, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.rememberPassword)

        self.checkBox_2 = QCheckBox(self.logWidget)
        self.checkBox_2.setGeometry(QtCore.QRect(310, 220, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.autoLogIn)

        self.usernameCombo = QComboBox(self.logWidget)
        self.usernameCombo.setGeometry(QtCore.QRect(250, 110, 121, 31))
        self.usernameCombo.setStyleSheet("background:rgb(255, 255, 255)")
        self.usernameCombo.setEditable(True)
        self.lineEdit_2 = QLineEdit(self.logWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 160, 121, 31))
        self.lineEdit_2.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        code = open(".\\log\\logInfo.txt", "r")
        lines = code.readlines()
        code.close()
        if(lines.__len__() > 1):
            self.preUsername = []
            self.prePassword = {}
            t = 0
            for line in lines:
                if t == 0:
                    self.auto = eval(line[0])
                    t += 1
                    continue
                tmpuser = line.split(" ")[0]
                tmppass = line.split(" ")[1]
                tmppass = tmppass[0: tmppass.__len__() - 1]
                self.preUsername.append(tmpuser)
                self.prePassword[tmpuser] = tmppass
                t += 1
            i = 0
            for username in self.preUsername:
                self.usernameCombo.insertItem(i, self.tr(username))
            self.usernameCombo.currentIndexChanged.connect(self.usernameChange)
            self.lineEdit_2.setText(self.prePassword[self.usernameCombo.currentText()])
            if self.prePassword[self.usernameCombo.currentText()] != "":
                self.checkBox.setChecked(True)
        else:
            code = open(".\\log\\logInfo.txt", "w+")
            code.write("0\n")
            code.close()
        self.label.setText("清华大学网络学堂")
        self.label.setVisible(False)
        self.label_2.setText("账号")
        self.label_3.setText("密码")
        self.pushButton.setText("登录")
        self.checkBox.setText("记住密码")
        self.checkBox_2.setText("自动登录")
        if self.auto:
            self.LogIn()
        self.show()

    def usernameChange(self):
        curPassword = self.prePassword[self.usernameCombo.currentText()]
        self.lineEdit_2.setText(curPassword)
        if self.prePassword[self.usernameCombo.currentText()] != "":
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

    def rememberPassword(self, state):
        self.memPass = True if state == QtCore.Qt.Checked else False

    def autoLogIn(self, state):
        self.auto = True if state == QtCore.Qt.Checked else False

    def LogIn(self):
        self.pushButton.setText("正在登录...")
        self.username = self.usernameCombo.currentText()
        self.password = self.lineEdit_2.text()
        global preCourses
        global Courses
        preCourses = core.logIn(self.username, self.password)
        if preCourses[0] == False:
            if preCourses[1] == 1:
                QMessageBox.warning(self, "警告", "网络未连接！")
            else:
                QMessageBox.warning(self, "警告", "用户名或密码错误！")
            self.pushButton.setText("正在登录...")
            return 0
        Courses = preCourses[1]
        self.logWidget.setVisible(False)
        self.setFixedSize(width, height)

        self.statusBar()
        self.mymenuBar()
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.FileConstruct(1)
        self.NoticeConstruct(0)
        self.HomeworkConstruct(2)

        self.setCentralWidget(self.centralWidget)
        self.center()
        self.show()

        if self.memPass is False:
            self.password = ""

        code = open(".\\log\\logInfo.txt", "r+")
        lines = code.readlines()
        code.close()
        flag = 0
        for i in range(lines.__len__()):
            if lines[i].split(" ")[0] == self.username:
                flag = 1
                lines[i] = self.username + " " + self.password + "\n"
                tmp = lines[1]
                lines[1] = lines[i]
                lines[i] = tmp
                break
        if self.auto:
            lines[0] = "1\n"
        else:
            lines[0] = "0\n"
        if not flag:
            lines.append(self.username + " " + self.password + "\n")
            tmp = lines[1]
            lines[1] = lines[lines.__len__() - 1]
            lines[lines.__len__() - 1] = tmp

        code = open(".\\log\\logInfo.txt", 'w+')
        for line in lines:
            code.write(line)
        code.close()

    def mymenuBar(self):
        logoutAction = QAction("登出账号", self)
        logoutAction.setShortcut("Ctrl+O")
        logoutAction.setStatusTip("将会登出此账号")
        logoutAction.triggered.connect(self.logout)
        QuitAction = QAction("退出", self)
        QuitAction.setShortcut("Ctrl+Q")
        QuitAction.setStatusTip("将退出程序")
        QuitAction.triggered.connect(qApp.quit)
        self.menubar = self.menuBar()
        self.menubar.setVisible(True)
        if self.logTimes != 0:
            return 1
        self.QuitMenu = self.menubar.addMenu("退出")
        self.QuitMenu.addAction(logoutAction)
        self.QuitMenu.addAction(QuitAction)

    def NoticeConstruct(self, num):
        self.notices = []
        for course in Courses:
            for note in course['notice']:
                if note['ifread'] == "未读":
                    note['course'] = course['name']
                    self.notices.append(note)
        noteNum = self.notices.__len__()
        X = 0
        Y = (uniHeight) * num + miniHeight + 5
        pixmap = QtGui.QPixmap(".\\pic\\1.png")
        label1 = QLabel(self.centralWidget)
        label1.setPixmap(pixmap)
        label1.setGeometry(leftWhite - 3, 5, miniHeight - 5, miniHeight - 5)
        label0 = QLabel(self.centralWidget)
        label0.setText("未读公告")
        label0.setGeometry(leftWhite + miniHeight + 5, 5, width / 2, miniHeight)
        label2 = QLabel(self.centralWidget)
        tmp = "%d 条" %noteNum
        label2.setText(tmp)
        label2.setGeometry(200, 5, 100, miniHeight)
        # 第一行用去miniHeight + 5
        self.noticeScroll = QScrollArea(self.centralWidget)
        self.noticeScroll.setGeometry(QtCore.QRect(X, Y, width, uniHeight))
        self.noticeScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.noticeScroll.setStyleSheet("background:rgb(114, 206, 255)")
        self.noticeWidget = QWidget(self.centralWidget)
        noticeHeight = miniHeight * noteNum + 100
        if noticeHeight < uniHeight + 100:
            noticeHeight = uniHeight + 100
        self.noticeWidget.setGeometry(QtCore.QRect(X, Y, width, noticeHeight))
        self.noticeScroll.setWidget(self.noticeWidget)
        self.noticeWidget.setStyleSheet("background:rgb(114, 206, 255)")
        y = 0
        count = 0
        for note in self.notices:
            subject = note['course']
            title = note['title']
            date = note['time']
            self.getOneNotice(self.noticeWidget, title, date, subject, count, 2 * leftWhite, y)
            count += 1
            y += miniHeight

    def getOneNotice(self, parent, title, date, subject, count, x, y):
        oneNotice = QWidget(parent)
        oneNotice.setGeometry(x, y, width, miniHeight - 1)
        oneNotice.setStyleSheet("background:rgb(225, 223, 224)")
        label1 = QLabel(oneNotice)
        label1.setGeometry(leftWhite, 0, 450, miniHeight)
        label1.setText(title)
        label2 = QLabel(oneNotice)
        label2.setGeometry(leftWhite + 450, 0, 200, miniHeight)
        label2.setText(date)
        label3 = QLabel(oneNotice)
        label3.setGeometry(leftWhite + 600, 0, 400, miniHeight)
        label3.setText(subject)
        button = QPushButton(oneNotice)
        button.setGeometry(width - 160, 1, 50, miniHeight - 3)
        button.setText("查看")
        name = "%d" %count
        button.setObjectName(name)
        button.clicked.connect(self.seeNotice)


    def HomeworkConstruct(self, num):
        X = 0
        Y = (uniHeight + miniHeight) * num + 5
        self.hws = []
        for course in Courses:
            if course['homework'].__len__() != 0:
                for h in course['homework']:
                    if h['ifsubmit'] == '尚未提交':
                        h['course'] = course['name']
                        self.hws.append(h)
        hw_num = self.hws.__len__()
        pixmap = QtGui.QPixmap(".\\pic\\3.png")
        label1 = QLabel(self.centralWidget)
        label1.setPixmap(pixmap)
        label1.setGeometry(leftWhite - 3, Y, miniHeight, miniHeight)
        label0 = QLabel(self.centralWidget)
        label0.setText("未交作业")
        label0.setGeometry(leftWhite + miniHeight, Y, width / 2, miniHeight)
        label2 = QLabel(self.centralWidget)
        label2.setText("DDL")
        label2.setGeometry(630, Y, 100, miniHeight)
        label3 = QLabel(self.centralWidget)
        label3.setText("发布日期")
        label3.setGeometry(720, Y, 100, miniHeight)
        remindButton = QPushButton(self.centralWidget)
        remindButton.setText("添加提醒")
        remindButton.setGeometry(850, Y + 2, 100, miniHeight - 4)
        remindButton.clicked.connect(self.remindHW)

        Y += miniHeight
        self.hwScroll = QScrollArea(self.centralWidget)
        self.hwScroll.setGeometry(QtCore.QRect(X, Y, width, uniHeight))
        self.hwScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hwScroll.setStyleSheet("background:rgb(114, 206, 255)")
        self.hwWidget = QWidget(self.centralWidget)
        self.hwWidget.setGeometry(QtCore.QRect(X, Y, width, miniHeight * hw_num + 100))
        self.hwScroll.setWidget(self.hwWidget)
        self.hwWidget.setStyleSheet("background:rgb(114, 206, 255)")
        Y = 5
        count = 0
        self.HWfiles = []
        for hw in self.hws:
            title = hw['name']
            filename = hw['filename']
            ddl = hw['ddl']
            subject = hw['course']
            release_time = hw['release_time']
            self.getOnework(self.hwWidget, title, ddl, filename, subject, release_time, count, 2 * leftWhite, Y)
            if(filename != ''):
                self.HWfiles.append(hw)
                count+=1
            Y += miniHeight
    def getOnework(self, parent, title, ddl, filename, subject, release_time, count, x, y):
        oneHw = QWidget(parent)
        oneHw.setGeometry(x, y, width, miniHeight - 1)
        oneHw.setStyleSheet("background:rgb(225, 223, 224)")
        label1 = QLabel(oneHw)
        label1.setText(title)
        label1.setGeometry(leftWhite, 0, 300, miniHeight)
        label2 = QLabel(oneHw)
        label2.setText(subject)
        label2.setGeometry(leftWhite + 300, 0, 250, miniHeight)
        label3 = QLabel(oneHw)
        label3.setText(ddl)
        label3.setGeometry(leftWhite + 550, 0, 100, miniHeight)
        label4 = QLabel(oneHw)
        label4.setText(release_time)
        label4.setGeometry(leftWhite + 650, 0, 100, miniHeight)
        if (filename != ''):
            button = QPushButton(oneHw)
            button.setText("下载文件")
            button.setGeometry(width - 170, 0, 80, miniHeight - 3)
            name = "%d" %count
            button.setObjectName(name)
            button.clicked.connect(self.downloadHWFile)

    def FileConstruct(self, num):
        X = 0
        Y = (uniHeight) * num + miniHeight + 5
        fileNum = 0
        for i in Courses:
            fileNum += i['file'].__len__()
        pixmap = QtGui.QPixmap(".\\pic\\9.png")
        label1 = QLabel(self.centralWidget)
        label1.setPixmap(pixmap)
        label1.setGeometry(leftWhite - 3, Y, miniHeight, miniHeight)
        label0 = QLabel(self.centralWidget)
        label0.setText("所有文件")
        label0.setGeometry(leftWhite + miniHeight, Y, width / 2, miniHeight)
        button = QPushButton(self.centralWidget)
        button.setText("一键下载新文件")
        button.setGeometry(750, Y + 2, 150, miniHeight - 4)
        button.clicked.connect(self.downloadAllFiles)
        Y += miniHeight
        self.fileScroll = QScrollArea(self.centralWidget)
        self.fileScroll.setGeometry(QtCore.QRect(X, Y, width, uniHeight))
        self.fileScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileScroll.setStyleSheet("background:rgb(114, 206, 255)")
        self.fileWidget = QWidget(self.centralWidget)
        hwHeight = miniHeight * fileNum + 100
        if hwHeight < uniHeight + 100:
            hwHeight = uniHeight + 100
        self.fileWidget.setGeometry(QtCore.QRect(X, Y, width, hwHeight))
        self.fileScroll.setWidget(self.fileWidget)
        self.fileWidget.setStyleSheet("background:rgb(114, 206, 255)")
        # 第一行用去miniHeight + 5
        Y = 5
        count = 0
        self.files = []
        for course in Courses:
            file_num = course['file'].__len__()
            if file_num == 0:
                continue
            course_height = miniHeight * (file_num + 1) + 5
            oneCourse = QWidget(self.fileWidget)
            oneCourse.setGeometry(0, Y, width, course_height)
            label_courseName = QLabel(oneCourse)
            label_courseName.setText(course['name'])
            label_courseName.setGeometry(leftWhite, 0, width, miniHeight)
            Y = Y + course_height
            y = miniHeight
            tmp = 0
            newfiles = sorted(course['file'], key=lambda file:file['state']!='新文件')

            # newfiles = []
            # for file in course['file']:
            #     if(file['state'] == '新文件'):
            #         newfiles.append(file)
            # for file in course['file']:
            #     if(file['state'] != '新文件'):
            #         newfiles.append(file)
            course['file'] = newfiles
            for file in course['file']:
                self.files.append(file)
                filename = (file['title']).replace(u'\xa0', u' ')
                filememo = file['memory'].replace(u'\xa0', u' ')
                filedate = file['time'].replace(u'\xa0', u' ')
                new = True if file['state'] == '新文件' else False
                print(filename, filememo, filedate)
                self.getOneFile(oneCourse, filename, filememo, filedate, count, 2 * leftWhite, y, new)
                y = y + miniHeight
                count += 1
    def getOneFile(self, parent, filename, filememo, filedate, count, x, y, new):
        oneFile = QWidget(parent)
        oneFile.setGeometry(x, y, width, miniHeight - 1)
        oneFile.setStyleSheet("background:rgb(225, 223, 224)")
        label1 = QLabel(oneFile)
        label1.setText(filename)
        label1.setGeometry(leftWhite, 0, 200, miniHeight)
        label2 = QLabel(oneFile)
        label2.setText("大小:" + filememo)
        label2.setGeometry(250, 0, 200, miniHeight)
        label3 = QLabel(oneFile)
        label3.setText(filedate)
        label3.setGeometry(450, 0, 200, miniHeight)
        if (new):
            label4 = QLabel(oneFile)
            label4.setText("新文件")
            label4.setGeometry(650, 0, 200, miniHeight)
        button = QPushButton(oneFile)
        button.setText("下载")
        button.setGeometry(width - 160, 1, 50, miniHeight - 3)
        name = "%d" % count
        button.setObjectName(name)
        button.clicked.connect(self.downloadFile)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def logout(self):
        self.centralWidget.setVisible(False)
        self.menubar.setVisible(False)
        self.setFixedSize(logWidth, logHeight)
        self.logWidget.setVisible(True)
        self.pushButton.setText("登录")
        if(self.auto):
            self.checkBox_2.setChecked(True)
        else:
            self.checkBox_2.setChecked(False)
        self.logTimes += 1
        self.center()
        core.initial()

    def downloadFile(self):
        sender = self.sender()
        i = eval(sender.objectName())
        self.getFile(i)

    def downloadAllFiles(self):
        listi = []
        i = 0
        for file in self.files:
            if file['state'] == "新文件":
                listi.append(i)
            i += 1
        if len(listi)>0:
            self.getFile(*listi)

    def getFile(self, *listi):
        global default_download_dir
        path = QFileDialog.getExistingDirectory(self, '请选择文件目录', default_download_dir)
        if path == '':
            return 
        for i in listi:
            file = self.files[i]
            url = file['url']
            name = file['title']
            thefile = core.s.get(url, stream=True)
            tem_filename = thefile.headers.get('Content-Disposition')
            filename = tem_filename.split('=')[1]
            filename = filename.strip('"')
            filetype = filename.split('.')[-1]
            #filetype = filetype[filetype.__len__() - 1]
            name = name + '.' + filetype
            dirname = os.path.normpath(os.path.join(path, name))
            with open(dirname, "wb") as code:
                code.write(thefile.content)
        default_download_dir = path
        QMessageBox.information(self, "文件下载", "保存成功!")

    def downloadHWFile(self):
        sender = self.sender()
        i = eval(sender.objectName())
        hw = self.HWfiles[i]
        url = hw['title_url']
        name = hw['filename']
        thefile = core.s.get(url)
        soup = BeautifulSoup(thefile.text, 'html.parser')
        file_url = soup.find(name = 'a').get('href')
        file = core.s.get('http://learn.tsinghua.edu.cn'+file_url, stream=True)
        filename = soup.find(name = 'a').text
        filetype = filename.split('.')[1]
        path = QFileDialog.getSaveFileName(self, 'Save File', filename, filetype)
        if (path[0] == ''):
            return
        with open(path[0], "wb") as code:
            code.write(file.content)
        QMessageBox.information(self, "文件下载", "保存成功!")

    def seeNotice(self):
        sender = self.sender()
        i = eval(sender.objectName())
        url = self.notices[i]['content_url']
        title = self.notices[i]['title']
        content = core.get_notice_content(url)
        QMessageBox.information(self, title, content)

    def remindHW(self):
        code = open(".\\未交作业统计.txt", "w+")
        tmp = ""
        #time.strptime(hw['ddl'], format)
        for hw in self.hws:
            today = time.strftime('%Y-%m-%d')
            if hw['ddl']<today:
                continue
            tmp = hw['ddl'] + ":" + hw['name'] + "\n"
            try:
                code.write(tmp)
            except:
                QMessageBox.warning(self, "警告", "保存失败！")
                code.close()
                return False
        code.close()
        QMessageBox.information(self, "通知", "保存成功！")
        os.system('notepad 未交作业统计.txt')

def hash(pre):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = appWin()
    sys.exit(app.exec_())