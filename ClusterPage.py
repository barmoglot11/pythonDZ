# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClusterPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollBar, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import Logo
import Icons

class Ui_ClusterPage(object):
    def setupUi(self, ClusterPage):
        if not ClusterPage.objectName():
            ClusterPage.setObjectName(u"ClusterPage")
        ClusterPage.resize(1920, 1118)
        ClusterPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.clusterPage = QWidget(ClusterPage)
        self.clusterPage.setObjectName(u"clusterPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clusterPage.sizePolicy().hasHeightForWidth())
        self.clusterPage.setSizePolicy(sizePolicy)
        self.clusterPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.clusterPage)
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 30)
        self.headerFrame = QFrame(self.clusterPage)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setLayoutDirection(Qt.LeftToRight)
        self.headerFrame.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-bottom: 2px solid #E7E7E7;")
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(30, 30, 30, 30)
        self.label = QLabel(self.headerFrame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(180, 80))
        self.label.setMaximumSize(QSize(180, 80))
        self.label.setStyleSheet(u"background-image: url(:/Logo/Icons And Logo/Logo.png);\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.headerFrame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(24)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #010101;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.headerFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButton_2.setPalette(palette1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #010101;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.headerFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #010101;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.headerFrame)

        self.title = QHBoxLayout()
        self.title.setSpacing(0)
        self.title.setObjectName(u"title")
        self.title.setContentsMargins(30, 0, 30, -1)
        self.title_2 = QLabel(self.clusterPage)
        self.title_2.setObjectName(u"title_2")
        sizePolicy1.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy1)
        palette2 = QPalette()
        brush1 = QBrush(QColor(80, 30, 188, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.title_2.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.title_2.setFont(font1)
        self.title_2.setStyleSheet(u"color: rgb(80, 30, 188);")

        self.title.addWidget(self.title_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title.addItem(self.horizontalSpacer)

        self.findCluster = QFrame(self.clusterPage)
        self.findCluster.setObjectName(u"findCluster")
        self.horizontalLayout_2 = QHBoxLayout(self.findCluster)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.findInput = QLineEdit(self.findCluster)
        self.findInput.setObjectName(u"findInput")
        self.findInput.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.findInput.sizePolicy().hasHeightForWidth())
        self.findInput.setSizePolicy(sizePolicy2)
        self.findInput.setMinimumSize(QSize(685, 48))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.findInput.setPalette(palette3)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setKerning(True)
        self.findInput.setFont(font2)
        self.findInput.setAcceptDrops(True)
        self.findInput.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid #5B5B5B;\n"
"	border-radius: 10px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"   color: #010101;\n"
"}")

        self.horizontalLayout_2.addWidget(self.findInput)

        self.pushButtonFind = QPushButton(self.findCluster)
        self.pushButtonFind.setObjectName(u"pushButtonFind")
        self.pushButtonFind.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonFind.sizePolicy().hasHeightForWidth())
        self.pushButtonFind.setSizePolicy(sizePolicy1)
        self.pushButtonFind.setMinimumSize(QSize(48, 48))
        self.pushButtonFind.setFont(font)
        self.pushButtonFind.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons And Logo/Search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonFind.setIcon(icon)
        self.pushButtonFind.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButtonFind)


        self.title.addWidget(self.findCluster)


        self.verticalLayout_5.addLayout(self.title)

        self.clusters = QHBoxLayout()
        self.clusters.setSpacing(20)
        self.clusters.setObjectName(u"clusters")
        self.clusters.setContentsMargins(30, -1, 30, -1)
        self.gridClusters = QGridLayout()
        self.gridClusters.setObjectName(u"gridClusters")
        self.gridClusters.setHorizontalSpacing(22)
        self.gridClusters.setVerticalSpacing(20)
        self.cluster = QFrame(self.clusterPage)
        self.cluster.setObjectName(u"cluster")
        self.cluster.setMaximumSize(QSize(346, 16777215))
        self.cluster.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.cluster)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons = QHBoxLayout()
        self.clusterButtons.setObjectName(u"clusterButtons")
        self.clusterName = QLabel(self.cluster)
        self.clusterName.setObjectName(u"clusterName")
        self.clusterName.setMinimumSize(QSize(248, 0))
        palette4 = QPalette()
        brush2 = QBrush(QColor(1, 1, 1, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName.setPalette(palette4)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setKerning(True)
        self.clusterName.setFont(font3)
        self.clusterName.setStyleSheet(u"border: none;")

        self.clusterButtons.addWidget(self.clusterName)

        self.buttons = QHBoxLayout()
        self.buttons.setSpacing(10)
        self.buttons.setObjectName(u"buttons")
        self.pushButtonRedact = QPushButton(self.cluster)
        self.pushButtonRedact.setObjectName(u"pushButtonRedact")
        self.pushButtonRedact.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact.setIconSize(QSize(24, 24))

        self.buttons.addWidget(self.pushButtonRedact)

        self.pushButtonDelete = QPushButton(self.cluster)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete.setIconSize(QSize(24, 24))

        self.buttons.addWidget(self.pushButtonDelete)


        self.clusterButtons.addLayout(self.buttons)


        self.verticalLayout_2.addLayout(self.clusterButtons)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vacancy = QLabel(self.cluster)
        self.vacancy.setObjectName(u"vacancy")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy.setPalette(palette5)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.vacancy.setFont(font4)
        self.vacancy.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.vacancy)

        self.prof_1 = QLabel(self.cluster)
        self.prof_1.setObjectName(u"prof_1")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_1.setPalette(palette6)
        self.prof_1.setFont(font4)
        self.prof_1.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.prof_1)

        self.prof_2 = QLabel(self.cluster)
        self.prof_2.setObjectName(u"prof_2")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_2.setPalette(palette7)
        self.prof_2.setFont(font4)
        self.prof_2.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.prof_2)

        self.prof_3 = QLabel(self.cluster)
        self.prof_3.setObjectName(u"prof_3")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_3.setPalette(palette8)
        self.prof_3.setFont(font4)
        self.prof_3.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.prof_3)

        self.prof_4 = QLabel(self.cluster)
        self.prof_4.setObjectName(u"prof_4")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_4.setPalette(palette9)
        self.prof_4.setFont(font4)
        self.prof_4.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.prof_4)

        self.prof_5 = QLabel(self.cluster)
        self.prof_5.setObjectName(u"prof_5")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_5.setPalette(palette10)
        self.prof_5.setFont(font4)
        self.prof_5.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.prof_5)

        self.prof_6 = QLabel(self.cluster)
        self.prof_6.setObjectName(u"prof_6")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_6.setPalette(palette11)
        self.prof_6.setFont(font4)
        self.prof_6.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.prof_6)

        self.prof_7 = QLabel(self.cluster)
        self.prof_7.setObjectName(u"prof_7")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_7.setPalette(palette12)
        self.prof_7.setFont(font4)
        self.prof_7.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.prof_7)

        self.prof_8 = QLabel(self.cluster)
        self.prof_8.setObjectName(u"prof_8")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_8.setPalette(palette13)
        self.prof_8.setFont(font4)
        self.prof_8.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.prof_8)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButtonMore = QPushButton(self.cluster)
        self.pushButtonMore.setObjectName(u"pushButtonMore")
        sizePolicy1.setHeightForWidth(self.pushButtonMore.sizePolicy().hasHeightForWidth())
        self.pushButtonMore.setSizePolicy(sizePolicy1)
        self.pushButtonMore.setMinimumSize(QSize(0, 0))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore.setPalette(palette14)
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setUnderline(True)
        self.pushButtonMore.setFont(font5)
        self.pushButtonMore.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButtonMore, 0, Qt.AlignHCenter)


        self.gridClusters.addWidget(self.cluster, 0, 0, 1, 1)

        self.clusterAdd = QFrame(self.clusterPage)
        self.clusterAdd.setObjectName(u"clusterAdd")
        self.clusterAdd.setLayoutDirection(Qt.LeftToRight)
        self.clusterAdd.setStyleSheet(u"background-color: #FFFFFF;\n"
"border: 2px dashed #501EBC;\n"
"border-radius: 10px;")
        self.pushButtonAdd = QPushButton(self.clusterAdd)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setGeometry(QRect(125, 123, 96, 96))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(96)
        sizePolicy3.setVerticalStretch(96)
        sizePolicy3.setHeightForWidth(self.pushButtonAdd.sizePolicy().hasHeightForWidth())
        self.pushButtonAdd.setSizePolicy(sizePolicy3)
        self.pushButtonAdd.setMinimumSize(QSize(96, 96))
        self.pushButtonAdd.setMaximumSize(QSize(96, 96))
        self.pushButtonAdd.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons And Logo/Add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonAdd.setIcon(icon1)
        self.pushButtonAdd.setIconSize(QSize(56, 56))
        self.textAdd = QLabel(self.clusterAdd)
        self.textAdd.setObjectName(u"textAdd")
        self.textAdd.setGeometry(QRect(30, 240, 294, 28))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(28)
        sizePolicy4.setHeightForWidth(self.textAdd.sizePolicy().hasHeightForWidth())
        self.textAdd.setSizePolicy(sizePolicy4)
        self.textAdd.setMinimumSize(QSize(0, 28))
        self.textAdd.setMaximumSize(QSize(16777215, 28))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textAdd.setPalette(palette15)
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(18)
        font6.setBold(True)
        self.textAdd.setFont(font6)
        self.textAdd.setStyleSheet(u"border: none;")

        self.gridClusters.addWidget(self.clusterAdd, 1, 1, 1, 1)

        self.cluster_10 = QFrame(self.clusterPage)
        self.cluster_10.setObjectName(u"cluster_10")
        self.cluster_10.setMaximumSize(QSize(346, 16777215))
        self.cluster_10.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.cluster_10)
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_5 = QHBoxLayout()
        self.clusterButtons_5.setObjectName(u"clusterButtons_5")
        self.clusterName_5 = QLabel(self.cluster_10)
        self.clusterName_5.setObjectName(u"clusterName_5")
        self.clusterName_5.setMinimumSize(QSize(248, 0))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_5.setPalette(palette16)
        self.clusterName_5.setFont(font3)
        self.clusterName_5.setStyleSheet(u"border: none;")

        self.clusterButtons_5.addWidget(self.clusterName_5)

        self.buttons_5 = QHBoxLayout()
        self.buttons_5.setSpacing(10)
        self.buttons_5.setObjectName(u"buttons_5")
        self.pushButtonRedact_5 = QPushButton(self.cluster_10)
        self.pushButtonRedact_5.setObjectName(u"pushButtonRedact_5")
        self.pushButtonRedact_5.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_5.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_5.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_5.setIconSize(QSize(24, 24))

        self.buttons_5.addWidget(self.pushButtonRedact_5)

        self.pushButtonDelete_5 = QPushButton(self.cluster_10)
        self.pushButtonDelete_5.setObjectName(u"pushButtonDelete_5")
        self.pushButtonDelete_5.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_5.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_5.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_5.setIconSize(QSize(24, 24))

        self.buttons_5.addWidget(self.pushButtonDelete_5)


        self.clusterButtons_5.addLayout(self.buttons_5)


        self.verticalLayout_19.addLayout(self.clusterButtons_5)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.vacancy_5 = QLabel(self.cluster_10)
        self.vacancy_5.setObjectName(u"vacancy_5")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_5.setPalette(palette17)
        self.vacancy_5.setFont(font4)
        self.vacancy_5.setStyleSheet(u"border: none;")

        self.verticalLayout_20.addWidget(self.vacancy_5)

        self.prof_33 = QLabel(self.cluster_10)
        self.prof_33.setObjectName(u"prof_33")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_33.setPalette(palette18)
        self.prof_33.setFont(font4)
        self.prof_33.setStyleSheet(u"border: none;")

        self.verticalLayout_20.addWidget(self.prof_33)

        self.prof_34 = QLabel(self.cluster_10)
        self.prof_34.setObjectName(u"prof_34")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_34.setPalette(palette19)
        self.prof_34.setFont(font4)
        self.prof_34.setStyleSheet(u"border: none;")

        self.verticalLayout_20.addWidget(self.prof_34)

        self.prof_35 = QLabel(self.cluster_10)
        self.prof_35.setObjectName(u"prof_35")
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_35.setPalette(palette20)
        self.prof_35.setFont(font4)
        self.prof_35.setStyleSheet(u"border: none;")

        self.verticalLayout_20.addWidget(self.prof_35)

        self.prof_36 = QLabel(self.cluster_10)
        self.prof_36.setObjectName(u"prof_36")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_36.setPalette(palette21)
        self.prof_36.setFont(font4)
        self.prof_36.setStyleSheet(u"border: none;")

        self.verticalLayout_20.addWidget(self.prof_36)

        self.prof_37 = QLabel(self.cluster_10)
        self.prof_37.setObjectName(u"prof_37")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_37.setPalette(palette22)
        self.prof_37.setFont(font4)
        self.prof_37.setStyleSheet(u"border: none;")

        self.verticalLayout_20.addWidget(self.prof_37)

        self.prof_38 = QLabel(self.cluster_10)
        self.prof_38.setObjectName(u"prof_38")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_38.setPalette(palette23)
        self.prof_38.setFont(font4)
        self.prof_38.setStyleSheet(u"border: none;")

        self.verticalLayout_20.addWidget(self.prof_38)

        self.prof_39 = QLabel(self.cluster_10)
        self.prof_39.setObjectName(u"prof_39")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_39.setPalette(palette24)
        self.prof_39.setFont(font4)
        self.prof_39.setStyleSheet(u"border: none;")

        self.verticalLayout_20.addWidget(self.prof_39)

        self.prof_40 = QLabel(self.cluster_10)
        self.prof_40.setObjectName(u"prof_40")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_40.setPalette(palette25)
        self.prof_40.setFont(font4)
        self.prof_40.setStyleSheet(u"border: none;")

        self.verticalLayout_20.addWidget(self.prof_40)


        self.verticalLayout_19.addLayout(self.verticalLayout_20)

        self.pushButtonMore_10 = QPushButton(self.cluster_10)
        self.pushButtonMore_10.setObjectName(u"pushButtonMore_10")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_10.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_10.setSizePolicy(sizePolicy1)
        self.pushButtonMore_10.setMinimumSize(QSize(0, 0))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_10.setPalette(palette26)
        self.pushButtonMore_10.setFont(font5)
        self.pushButtonMore_10.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_19.addWidget(self.pushButtonMore_10, 0, Qt.AlignHCenter)


        self.gridClusters.addWidget(self.cluster_10, 0, 3, 1, 1)

        self.cluster_7 = QFrame(self.clusterPage)
        self.cluster_7.setObjectName(u"cluster_7")
        self.cluster_7.setMaximumSize(QSize(346, 16777215))
        self.cluster_7.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.cluster_7)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_2 = QHBoxLayout()
        self.clusterButtons_2.setObjectName(u"clusterButtons_2")
        self.clusterName_2 = QLabel(self.cluster_7)
        self.clusterName_2.setObjectName(u"clusterName_2")
        self.clusterName_2.setMinimumSize(QSize(248, 0))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_2.setPalette(palette27)
        self.clusterName_2.setFont(font3)
        self.clusterName_2.setStyleSheet(u"border: none;")

        self.clusterButtons_2.addWidget(self.clusterName_2)

        self.buttons_2 = QHBoxLayout()
        self.buttons_2.setSpacing(10)
        self.buttons_2.setObjectName(u"buttons_2")
        self.pushButtonRedact_2 = QPushButton(self.cluster_7)
        self.pushButtonRedact_2.setObjectName(u"pushButtonRedact_2")
        self.pushButtonRedact_2.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_2.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_2.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_2.setIconSize(QSize(24, 24))

        self.buttons_2.addWidget(self.pushButtonRedact_2)

        self.pushButtonDelete_2 = QPushButton(self.cluster_7)
        self.pushButtonDelete_2.setObjectName(u"pushButtonDelete_2")
        self.pushButtonDelete_2.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_2.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_2.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_2.setIconSize(QSize(24, 24))

        self.buttons_2.addWidget(self.pushButtonDelete_2)


        self.clusterButtons_2.addLayout(self.buttons_2)


        self.verticalLayout_13.addLayout(self.clusterButtons_2)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.vacancy_2 = QLabel(self.cluster_7)
        self.vacancy_2.setObjectName(u"vacancy_2")
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_2.setPalette(palette28)
        self.vacancy_2.setFont(font4)
        self.vacancy_2.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.vacancy_2)

        self.prof_9 = QLabel(self.cluster_7)
        self.prof_9.setObjectName(u"prof_9")
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_9.setPalette(palette29)
        self.prof_9.setFont(font4)
        self.prof_9.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.prof_9)

        self.prof_10 = QLabel(self.cluster_7)
        self.prof_10.setObjectName(u"prof_10")
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_10.setPalette(palette30)
        self.prof_10.setFont(font4)
        self.prof_10.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.prof_10)

        self.prof_11 = QLabel(self.cluster_7)
        self.prof_11.setObjectName(u"prof_11")
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_11.setPalette(palette31)
        self.prof_11.setFont(font4)
        self.prof_11.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.prof_11)

        self.prof_12 = QLabel(self.cluster_7)
        self.prof_12.setObjectName(u"prof_12")
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_12.setPalette(palette32)
        self.prof_12.setFont(font4)
        self.prof_12.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.prof_12)

        self.prof_13 = QLabel(self.cluster_7)
        self.prof_13.setObjectName(u"prof_13")
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_13.setPalette(palette33)
        self.prof_13.setFont(font4)
        self.prof_13.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.prof_13)

        self.prof_14 = QLabel(self.cluster_7)
        self.prof_14.setObjectName(u"prof_14")
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_14.setPalette(palette34)
        self.prof_14.setFont(font4)
        self.prof_14.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.prof_14)

        self.prof_15 = QLabel(self.cluster_7)
        self.prof_15.setObjectName(u"prof_15")
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_15.setPalette(palette35)
        self.prof_15.setFont(font4)
        self.prof_15.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.prof_15)

        self.prof_16 = QLabel(self.cluster_7)
        self.prof_16.setObjectName(u"prof_16")
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_16.setPalette(palette36)
        self.prof_16.setFont(font4)
        self.prof_16.setStyleSheet(u"border: none;")

        self.verticalLayout_14.addWidget(self.prof_16)


        self.verticalLayout_13.addLayout(self.verticalLayout_14)

        self.pushButtonMore_7 = QPushButton(self.cluster_7)
        self.pushButtonMore_7.setObjectName(u"pushButtonMore_7")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_7.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_7.setSizePolicy(sizePolicy1)
        self.pushButtonMore_7.setMinimumSize(QSize(0, 0))
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette37.setBrush(QPalette.Active, QPalette.Button, brush)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_7.setPalette(palette37)
        self.pushButtonMore_7.setFont(font5)
        self.pushButtonMore_7.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_13.addWidget(self.pushButtonMore_7, 0, Qt.AlignHCenter)


        self.gridClusters.addWidget(self.cluster_7, 0, 1, 1, 1)

        self.cluster_8 = QFrame(self.clusterPage)
        self.cluster_8.setObjectName(u"cluster_8")
        self.cluster_8.setMaximumSize(QSize(346, 16777215))
        self.cluster_8.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.cluster_8)
        self.verticalLayout_15.setSpacing(15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_3 = QHBoxLayout()
        self.clusterButtons_3.setObjectName(u"clusterButtons_3")
        self.clusterName_3 = QLabel(self.cluster_8)
        self.clusterName_3.setObjectName(u"clusterName_3")
        self.clusterName_3.setMinimumSize(QSize(248, 0))
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette38.setBrush(QPalette.Active, QPalette.Button, brush)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_3.setPalette(palette38)
        self.clusterName_3.setFont(font3)
        self.clusterName_3.setStyleSheet(u"border: none;")

        self.clusterButtons_3.addWidget(self.clusterName_3)

        self.buttons_3 = QHBoxLayout()
        self.buttons_3.setSpacing(10)
        self.buttons_3.setObjectName(u"buttons_3")
        self.pushButtonRedact_3 = QPushButton(self.cluster_8)
        self.pushButtonRedact_3.setObjectName(u"pushButtonRedact_3")
        self.pushButtonRedact_3.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_3.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_3.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_3.setIconSize(QSize(24, 24))

        self.buttons_3.addWidget(self.pushButtonRedact_3)

        self.pushButtonDelete_3 = QPushButton(self.cluster_8)
        self.pushButtonDelete_3.setObjectName(u"pushButtonDelete_3")
        self.pushButtonDelete_3.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_3.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_3.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_3.setIconSize(QSize(24, 24))

        self.buttons_3.addWidget(self.pushButtonDelete_3)


        self.clusterButtons_3.addLayout(self.buttons_3)


        self.verticalLayout_15.addLayout(self.clusterButtons_3)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.vacancy_3 = QLabel(self.cluster_8)
        self.vacancy_3.setObjectName(u"vacancy_3")
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette39.setBrush(QPalette.Active, QPalette.Button, brush)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_3.setPalette(palette39)
        self.vacancy_3.setFont(font4)
        self.vacancy_3.setStyleSheet(u"border: none;")

        self.verticalLayout_16.addWidget(self.vacancy_3)

        self.prof_17 = QLabel(self.cluster_8)
        self.prof_17.setObjectName(u"prof_17")
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_17.setPalette(palette40)
        self.prof_17.setFont(font4)
        self.prof_17.setStyleSheet(u"border: none;")

        self.verticalLayout_16.addWidget(self.prof_17)

        self.prof_18 = QLabel(self.cluster_8)
        self.prof_18.setObjectName(u"prof_18")
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette41.setBrush(QPalette.Active, QPalette.Button, brush)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_18.setPalette(palette41)
        self.prof_18.setFont(font4)
        self.prof_18.setStyleSheet(u"border: none;")

        self.verticalLayout_16.addWidget(self.prof_18)

        self.prof_19 = QLabel(self.cluster_8)
        self.prof_19.setObjectName(u"prof_19")
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette42.setBrush(QPalette.Active, QPalette.Button, brush)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_19.setPalette(palette42)
        self.prof_19.setFont(font4)
        self.prof_19.setStyleSheet(u"border: none;")

        self.verticalLayout_16.addWidget(self.prof_19)

        self.prof_20 = QLabel(self.cluster_8)
        self.prof_20.setObjectName(u"prof_20")
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette43.setBrush(QPalette.Active, QPalette.Button, brush)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_20.setPalette(palette43)
        self.prof_20.setFont(font4)
        self.prof_20.setStyleSheet(u"border: none;")

        self.verticalLayout_16.addWidget(self.prof_20)

        self.prof_21 = QLabel(self.cluster_8)
        self.prof_21.setObjectName(u"prof_21")
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette44.setBrush(QPalette.Active, QPalette.Button, brush)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_21.setPalette(palette44)
        self.prof_21.setFont(font4)
        self.prof_21.setStyleSheet(u"border: none;")

        self.verticalLayout_16.addWidget(self.prof_21)

        self.prof_22 = QLabel(self.cluster_8)
        self.prof_22.setObjectName(u"prof_22")
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette45.setBrush(QPalette.Active, QPalette.Button, brush)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_22.setPalette(palette45)
        self.prof_22.setFont(font4)
        self.prof_22.setStyleSheet(u"border: none;")

        self.verticalLayout_16.addWidget(self.prof_22)

        self.prof_23 = QLabel(self.cluster_8)
        self.prof_23.setObjectName(u"prof_23")
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette46.setBrush(QPalette.Active, QPalette.Button, brush)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_23.setPalette(palette46)
        self.prof_23.setFont(font4)
        self.prof_23.setStyleSheet(u"border: none;")

        self.verticalLayout_16.addWidget(self.prof_23)

        self.prof_24 = QLabel(self.cluster_8)
        self.prof_24.setObjectName(u"prof_24")
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette47.setBrush(QPalette.Active, QPalette.Button, brush)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_24.setPalette(palette47)
        self.prof_24.setFont(font4)
        self.prof_24.setStyleSheet(u"border: none;")

        self.verticalLayout_16.addWidget(self.prof_24)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)

        self.pushButtonMore_8 = QPushButton(self.cluster_8)
        self.pushButtonMore_8.setObjectName(u"pushButtonMore_8")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_8.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_8.setSizePolicy(sizePolicy1)
        self.pushButtonMore_8.setMinimumSize(QSize(0, 0))
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette48.setBrush(QPalette.Active, QPalette.Button, brush)
        palette48.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette48.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette48.setBrush(QPalette.Active, QPalette.Base, brush)
        palette48.setBrush(QPalette.Active, QPalette.Window, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_8.setPalette(palette48)
        self.pushButtonMore_8.setFont(font5)
        self.pushButtonMore_8.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_15.addWidget(self.pushButtonMore_8, 0, Qt.AlignHCenter)


        self.gridClusters.addWidget(self.cluster_8, 0, 4, 1, 1)

        self.cluster_9 = QFrame(self.clusterPage)
        self.cluster_9.setObjectName(u"cluster_9")
        self.cluster_9.setMaximumSize(QSize(346, 16777215))
        self.cluster_9.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.cluster_9)
        self.verticalLayout_17.setSpacing(15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_4 = QHBoxLayout()
        self.clusterButtons_4.setObjectName(u"clusterButtons_4")
        self.clusterName_4 = QLabel(self.cluster_9)
        self.clusterName_4.setObjectName(u"clusterName_4")
        self.clusterName_4.setMinimumSize(QSize(248, 0))
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette49.setBrush(QPalette.Active, QPalette.Button, brush)
        palette49.setBrush(QPalette.Active, QPalette.Base, brush)
        palette49.setBrush(QPalette.Active, QPalette.Window, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette49.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette49.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_4.setPalette(palette49)
        self.clusterName_4.setFont(font3)
        self.clusterName_4.setStyleSheet(u"border: none;")

        self.clusterButtons_4.addWidget(self.clusterName_4)

        self.buttons_4 = QHBoxLayout()
        self.buttons_4.setSpacing(10)
        self.buttons_4.setObjectName(u"buttons_4")
        self.pushButtonRedact_4 = QPushButton(self.cluster_9)
        self.pushButtonRedact_4.setObjectName(u"pushButtonRedact_4")
        self.pushButtonRedact_4.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_4.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_4.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_4.setIconSize(QSize(24, 24))

        self.buttons_4.addWidget(self.pushButtonRedact_4)

        self.pushButtonDelete_4 = QPushButton(self.cluster_9)
        self.pushButtonDelete_4.setObjectName(u"pushButtonDelete_4")
        self.pushButtonDelete_4.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_4.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_4.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_4.setIconSize(QSize(24, 24))

        self.buttons_4.addWidget(self.pushButtonDelete_4)


        self.clusterButtons_4.addLayout(self.buttons_4)


        self.verticalLayout_17.addLayout(self.clusterButtons_4)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.vacancy_4 = QLabel(self.cluster_9)
        self.vacancy_4.setObjectName(u"vacancy_4")
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette50.setBrush(QPalette.Active, QPalette.Button, brush)
        palette50.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette50.setBrush(QPalette.Active, QPalette.Base, brush)
        palette50.setBrush(QPalette.Active, QPalette.Window, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette50.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette50.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette50.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette50.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_4.setPalette(palette50)
        self.vacancy_4.setFont(font4)
        self.vacancy_4.setStyleSheet(u"border: none;")

        self.verticalLayout_18.addWidget(self.vacancy_4)

        self.prof_25 = QLabel(self.cluster_9)
        self.prof_25.setObjectName(u"prof_25")
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette51.setBrush(QPalette.Active, QPalette.Button, brush)
        palette51.setBrush(QPalette.Active, QPalette.Base, brush)
        palette51.setBrush(QPalette.Active, QPalette.Window, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette51.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette51.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_25.setPalette(palette51)
        self.prof_25.setFont(font4)
        self.prof_25.setStyleSheet(u"border: none;")

        self.verticalLayout_18.addWidget(self.prof_25)

        self.prof_26 = QLabel(self.cluster_9)
        self.prof_26.setObjectName(u"prof_26")
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette52.setBrush(QPalette.Active, QPalette.Button, brush)
        palette52.setBrush(QPalette.Active, QPalette.Base, brush)
        palette52.setBrush(QPalette.Active, QPalette.Window, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette52.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette52.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_26.setPalette(palette52)
        self.prof_26.setFont(font4)
        self.prof_26.setStyleSheet(u"border: none;")

        self.verticalLayout_18.addWidget(self.prof_26)

        self.prof_27 = QLabel(self.cluster_9)
        self.prof_27.setObjectName(u"prof_27")
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette53.setBrush(QPalette.Active, QPalette.Button, brush)
        palette53.setBrush(QPalette.Active, QPalette.Base, brush)
        palette53.setBrush(QPalette.Active, QPalette.Window, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette53.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette53.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_27.setPalette(palette53)
        self.prof_27.setFont(font4)
        self.prof_27.setStyleSheet(u"border: none;")

        self.verticalLayout_18.addWidget(self.prof_27)

        self.prof_28 = QLabel(self.cluster_9)
        self.prof_28.setObjectName(u"prof_28")
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette54.setBrush(QPalette.Active, QPalette.Button, brush)
        palette54.setBrush(QPalette.Active, QPalette.Base, brush)
        palette54.setBrush(QPalette.Active, QPalette.Window, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette54.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette54.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_28.setPalette(palette54)
        self.prof_28.setFont(font4)
        self.prof_28.setStyleSheet(u"border: none;")

        self.verticalLayout_18.addWidget(self.prof_28)

        self.prof_29 = QLabel(self.cluster_9)
        self.prof_29.setObjectName(u"prof_29")
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette55.setBrush(QPalette.Active, QPalette.Button, brush)
        palette55.setBrush(QPalette.Active, QPalette.Base, brush)
        palette55.setBrush(QPalette.Active, QPalette.Window, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette55.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette55.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_29.setPalette(palette55)
        self.prof_29.setFont(font4)
        self.prof_29.setStyleSheet(u"border: none;")

        self.verticalLayout_18.addWidget(self.prof_29)

        self.prof_30 = QLabel(self.cluster_9)
        self.prof_30.setObjectName(u"prof_30")
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette56.setBrush(QPalette.Active, QPalette.Button, brush)
        palette56.setBrush(QPalette.Active, QPalette.Base, brush)
        palette56.setBrush(QPalette.Active, QPalette.Window, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette56.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette56.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_30.setPalette(palette56)
        self.prof_30.setFont(font4)
        self.prof_30.setStyleSheet(u"border: none;")

        self.verticalLayout_18.addWidget(self.prof_30)

        self.prof_31 = QLabel(self.cluster_9)
        self.prof_31.setObjectName(u"prof_31")
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette57.setBrush(QPalette.Active, QPalette.Button, brush)
        palette57.setBrush(QPalette.Active, QPalette.Base, brush)
        palette57.setBrush(QPalette.Active, QPalette.Window, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette57.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette57.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_31.setPalette(palette57)
        self.prof_31.setFont(font4)
        self.prof_31.setStyleSheet(u"border: none;")

        self.verticalLayout_18.addWidget(self.prof_31)

        self.prof_32 = QLabel(self.cluster_9)
        self.prof_32.setObjectName(u"prof_32")
        palette58 = QPalette()
        palette58.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette58.setBrush(QPalette.Active, QPalette.Button, brush)
        palette58.setBrush(QPalette.Active, QPalette.Base, brush)
        palette58.setBrush(QPalette.Active, QPalette.Window, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette58.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette58.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_32.setPalette(palette58)
        self.prof_32.setFont(font4)
        self.prof_32.setStyleSheet(u"border: none;")

        self.verticalLayout_18.addWidget(self.prof_32)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)

        self.pushButtonMore_9 = QPushButton(self.cluster_9)
        self.pushButtonMore_9.setObjectName(u"pushButtonMore_9")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_9.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_9.setSizePolicy(sizePolicy1)
        self.pushButtonMore_9.setMinimumSize(QSize(0, 0))
        palette59 = QPalette()
        palette59.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette59.setBrush(QPalette.Active, QPalette.Button, brush)
        palette59.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette59.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette59.setBrush(QPalette.Active, QPalette.Base, brush)
        palette59.setBrush(QPalette.Active, QPalette.Window, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette59.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette59.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette59.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette59.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette59.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette59.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_9.setPalette(palette59)
        self.pushButtonMore_9.setFont(font5)
        self.pushButtonMore_9.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_17.addWidget(self.pushButtonMore_9, 0, Qt.AlignHCenter)


        self.gridClusters.addWidget(self.cluster_9, 0, 2, 1, 1)

        self.cluster_2 = QFrame(self.clusterPage)
        self.cluster_2.setObjectName(u"cluster_2")
        self.cluster_2.setMaximumSize(QSize(346, 16777215))
        self.cluster_2.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.cluster_2)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_6 = QHBoxLayout()
        self.clusterButtons_6.setObjectName(u"clusterButtons_6")
        self.clusterName_6 = QLabel(self.cluster_2)
        self.clusterName_6.setObjectName(u"clusterName_6")
        self.clusterName_6.setMinimumSize(QSize(248, 0))
        palette60 = QPalette()
        palette60.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette60.setBrush(QPalette.Active, QPalette.Button, brush)
        palette60.setBrush(QPalette.Active, QPalette.Base, brush)
        palette60.setBrush(QPalette.Active, QPalette.Window, brush)
        palette60.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette60.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette60.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette60.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette60.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette60.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette60.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette60.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_6.setPalette(palette60)
        self.clusterName_6.setFont(font3)
        self.clusterName_6.setStyleSheet(u"border: none;")

        self.clusterButtons_6.addWidget(self.clusterName_6)

        self.buttons_6 = QHBoxLayout()
        self.buttons_6.setSpacing(10)
        self.buttons_6.setObjectName(u"buttons_6")
        self.pushButtonRedact_6 = QPushButton(self.cluster_2)
        self.pushButtonRedact_6.setObjectName(u"pushButtonRedact_6")
        self.pushButtonRedact_6.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_6.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_6.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_6.setIconSize(QSize(24, 24))

        self.buttons_6.addWidget(self.pushButtonRedact_6)

        self.pushButtonDelete_6 = QPushButton(self.cluster_2)
        self.pushButtonDelete_6.setObjectName(u"pushButtonDelete_6")
        self.pushButtonDelete_6.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_6.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_6.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_6.setIconSize(QSize(24, 24))

        self.buttons_6.addWidget(self.pushButtonDelete_6)


        self.clusterButtons_6.addLayout(self.buttons_6)


        self.verticalLayout_3.addLayout(self.clusterButtons_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.vacancy_6 = QLabel(self.cluster_2)
        self.vacancy_6.setObjectName(u"vacancy_6")
        palette61 = QPalette()
        palette61.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette61.setBrush(QPalette.Active, QPalette.Button, brush)
        palette61.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette61.setBrush(QPalette.Active, QPalette.Base, brush)
        palette61.setBrush(QPalette.Active, QPalette.Window, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette61.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette61.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette61.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette61.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_6.setPalette(palette61)
        self.vacancy_6.setFont(font4)
        self.vacancy_6.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.vacancy_6)

        self.prof_41 = QLabel(self.cluster_2)
        self.prof_41.setObjectName(u"prof_41")
        palette62 = QPalette()
        palette62.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette62.setBrush(QPalette.Active, QPalette.Button, brush)
        palette62.setBrush(QPalette.Active, QPalette.Base, brush)
        palette62.setBrush(QPalette.Active, QPalette.Window, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette62.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette62.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_41.setPalette(palette62)
        self.prof_41.setFont(font4)
        self.prof_41.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.prof_41)

        self.prof_42 = QLabel(self.cluster_2)
        self.prof_42.setObjectName(u"prof_42")
        palette63 = QPalette()
        palette63.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette63.setBrush(QPalette.Active, QPalette.Button, brush)
        palette63.setBrush(QPalette.Active, QPalette.Base, brush)
        palette63.setBrush(QPalette.Active, QPalette.Window, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette63.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette63.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_42.setPalette(palette63)
        self.prof_42.setFont(font4)
        self.prof_42.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.prof_42)

        self.prof_43 = QLabel(self.cluster_2)
        self.prof_43.setObjectName(u"prof_43")
        palette64 = QPalette()
        palette64.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette64.setBrush(QPalette.Active, QPalette.Button, brush)
        palette64.setBrush(QPalette.Active, QPalette.Base, brush)
        palette64.setBrush(QPalette.Active, QPalette.Window, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette64.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette64.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_43.setPalette(palette64)
        self.prof_43.setFont(font4)
        self.prof_43.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.prof_43)

        self.prof_44 = QLabel(self.cluster_2)
        self.prof_44.setObjectName(u"prof_44")
        palette65 = QPalette()
        palette65.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette65.setBrush(QPalette.Active, QPalette.Button, brush)
        palette65.setBrush(QPalette.Active, QPalette.Base, brush)
        palette65.setBrush(QPalette.Active, QPalette.Window, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette65.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette65.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_44.setPalette(palette65)
        self.prof_44.setFont(font4)
        self.prof_44.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.prof_44)

        self.prof_45 = QLabel(self.cluster_2)
        self.prof_45.setObjectName(u"prof_45")
        palette66 = QPalette()
        palette66.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette66.setBrush(QPalette.Active, QPalette.Button, brush)
        palette66.setBrush(QPalette.Active, QPalette.Base, brush)
        palette66.setBrush(QPalette.Active, QPalette.Window, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette66.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette66.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_45.setPalette(palette66)
        self.prof_45.setFont(font4)
        self.prof_45.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.prof_45)

        self.prof_46 = QLabel(self.cluster_2)
        self.prof_46.setObjectName(u"prof_46")
        palette67 = QPalette()
        palette67.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette67.setBrush(QPalette.Active, QPalette.Button, brush)
        palette67.setBrush(QPalette.Active, QPalette.Base, brush)
        palette67.setBrush(QPalette.Active, QPalette.Window, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette67.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette67.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_46.setPalette(palette67)
        self.prof_46.setFont(font4)
        self.prof_46.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.prof_46)

        self.prof_47 = QLabel(self.cluster_2)
        self.prof_47.setObjectName(u"prof_47")
        palette68 = QPalette()
        palette68.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette68.setBrush(QPalette.Active, QPalette.Button, brush)
        palette68.setBrush(QPalette.Active, QPalette.Base, brush)
        palette68.setBrush(QPalette.Active, QPalette.Window, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette68.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette68.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_47.setPalette(palette68)
        self.prof_47.setFont(font4)
        self.prof_47.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.prof_47)

        self.prof_48 = QLabel(self.cluster_2)
        self.prof_48.setObjectName(u"prof_48")
        palette69 = QPalette()
        palette69.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette69.setBrush(QPalette.Active, QPalette.Button, brush)
        palette69.setBrush(QPalette.Active, QPalette.Base, brush)
        palette69.setBrush(QPalette.Active, QPalette.Window, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette69.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette69.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.prof_48.setPalette(palette69)
        self.prof_48.setFont(font4)
        self.prof_48.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.prof_48)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.pushButtonMore_2 = QPushButton(self.cluster_2)
        self.pushButtonMore_2.setObjectName(u"pushButtonMore_2")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_2.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_2.setSizePolicy(sizePolicy1)
        self.pushButtonMore_2.setMinimumSize(QSize(0, 0))
        palette70 = QPalette()
        palette70.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette70.setBrush(QPalette.Active, QPalette.Button, brush)
        palette70.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette70.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette70.setBrush(QPalette.Active, QPalette.Base, brush)
        palette70.setBrush(QPalette.Active, QPalette.Window, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette70.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette70.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette70.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette70.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette70.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette70.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_2.setPalette(palette70)
        self.pushButtonMore_2.setFont(font5)
        self.pushButtonMore_2.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButtonMore_2, 0, Qt.AlignHCenter)


        self.gridClusters.addWidget(self.cluster_2, 1, 0, 1, 1)


        self.clusters.addLayout(self.gridClusters)

        self.verticalScrollBar = QScrollBar(self.clusterPage)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        palette71 = QPalette()
        brush4 = QBrush(QColor(231, 231, 231, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette71.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette71.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette71.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette71.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette71.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette71.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette71.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette71.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette71.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.verticalScrollBar.setPalette(palette71)
        self.verticalScrollBar.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #E7E7E7;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: #5B5B5B;\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #501EBC;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: #5B5B5B;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #501EBC;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: #5B5B5B;\n"
"	height: 15px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7p"
                        "x;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #501EBC;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.clusters.addWidget(self.verticalScrollBar)


        self.verticalLayout_5.addLayout(self.clusters)

        ClusterPage.setCentralWidget(self.clusterPage)

        self.retranslateUi(ClusterPage)

        QMetaObject.connectSlotsByName(ClusterPage)
    # setupUi

    def retranslateUi(self, ClusterPage):
        ClusterPage.setWindowTitle(QCoreApplication.translate("ClusterPage", u"Your Vacancy", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e", None))
        self.pushButton_2.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u044b", None))
        self.pushButton_3.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.title_2.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u044b", None))
        self.findInput.setText("")
        self.findInput.setPlaceholderText(QCoreApplication.translate("ClusterPage", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0430", None))
        self.pushButtonFind.setText("")
        self.clusterName.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.vacancy.setText(QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.prof_1.setText(QCoreApplication.translate("ClusterPage", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c", None))
        self.prof_2.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.prof_3.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435", None))
        self.prof_4.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430", None))
        self.prof_5.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436", None))
        self.prof_6.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_7.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_8.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442", None))
        self.pushButtonMore.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.pushButtonAdd.setText("")
        self.textAdd.setText(QCoreApplication.translate("ClusterPage", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043a\u043b\u0430\u0441\u0442\u0435\u0440", None))
        self.clusterName_5.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_5.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_5.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_5.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_5.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.vacancy_5.setText(QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.prof_33.setText(QCoreApplication.translate("ClusterPage", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c", None))
        self.prof_34.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.prof_35.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435", None))
        self.prof_36.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430", None))
        self.prof_37.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436", None))
        self.prof_38.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_39.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_40.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442", None))
        self.pushButtonMore_10.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.clusterName_2.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_2.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_2.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_2.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_2.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.vacancy_2.setText(QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.prof_9.setText(QCoreApplication.translate("ClusterPage", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c", None))
        self.prof_10.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.prof_11.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435", None))
        self.prof_12.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430", None))
        self.prof_13.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436", None))
        self.prof_14.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_15.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_16.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442", None))
        self.pushButtonMore_7.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.clusterName_3.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_3.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_3.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_3.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_3.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.vacancy_3.setText(QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.prof_17.setText(QCoreApplication.translate("ClusterPage", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c", None))
        self.prof_18.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.prof_19.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435", None))
        self.prof_20.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430", None))
        self.prof_21.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436", None))
        self.prof_22.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_23.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_24.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442", None))
        self.pushButtonMore_8.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.clusterName_4.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_4.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_4.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_4.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_4.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.vacancy_4.setText(QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.prof_25.setText(QCoreApplication.translate("ClusterPage", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c", None))
        self.prof_26.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.prof_27.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435", None))
        self.prof_28.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430", None))
        self.prof_29.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436", None))
        self.prof_30.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_31.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_32.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442", None))
        self.pushButtonMore_9.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.clusterName_6.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_6.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_6.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_6.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_6.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.vacancy_6.setText(QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.prof_41.setText(QCoreApplication.translate("ClusterPage", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c", None))
        self.prof_42.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.prof_43.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435", None))
        self.prof_44.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430", None))
        self.prof_45.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436", None))
        self.prof_46.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_47.setText(QCoreApplication.translate("ClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440", None))
        self.prof_48.setText(QCoreApplication.translate("ClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442", None))
        self.pushButtonMore_2.setText(QCoreApplication.translate("ClusterPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
    # retranslateUi

