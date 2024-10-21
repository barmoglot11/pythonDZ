# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TakeProfessionNonePage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Logo
import Icons

class Ui_TakeProfessionNonePage(object):
    def setupUi(self, TakeProfessionNonePage):
        if not TakeProfessionNonePage.objectName():
            TakeProfessionNonePage.setObjectName(u"TakeProfessionNonePage")
        TakeProfessionNonePage.resize(1920, 1144)
        TakeProfessionNonePage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.takeProfessionNonePage = QWidget(TakeProfessionNonePage)
        self.takeProfessionNonePage.setObjectName(u"takeProfessionNonePage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeProfessionNonePage.sizePolicy().hasHeightForWidth())
        self.takeProfessionNonePage.setSizePolicy(sizePolicy)
        self.takeProfessionNonePage.setMaximumSize(QSize(16777215, 16777215))
        self.takeProfessionNonePage.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.takeProfessionNonePage)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 30)
        self.headerFrame = QFrame(self.takeProfessionNonePage)
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
"   color: #101010;\n"
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
"   color: #101010;\n"
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
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.title = QFrame(self.takeProfessionNonePage)
        self.title.setObjectName(u"title")
        self.horizontalLayout_4 = QHBoxLayout(self.title)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, 0, 30, 0)
        self.titleButton = QHBoxLayout()
        self.titleButton.setSpacing(20)
        self.titleButton.setObjectName(u"titleButton")
        self.title_2 = QLabel(self.title)
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

        self.titleButton.addWidget(self.title_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.titleButton.addItem(self.horizontalSpacer)

        self.pushButtonAddTags = QPushButton(self.title)
        self.pushButtonAddTags.setObjectName(u"pushButtonAddTags")
        self.pushButtonAddTags.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonAddTags.sizePolicy().hasHeightForWidth())
        self.pushButtonAddTags.setSizePolicy(sizePolicy1)
        self.pushButtonAddTags.setMinimumSize(QSize(324, 48))
        self.pushButtonAddTags.setMaximumSize(QSize(324, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonAddTags.setPalette(palette3)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.pushButtonAddTags.setFont(font2)
        self.pushButtonAddTags.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        self.pushButtonAddTags.setIconSize(QSize(20, 20))

        self.titleButton.addWidget(self.pushButtonAddTags)


        self.horizontalLayout_4.addLayout(self.titleButton)


        self.verticalLayout_4.addWidget(self.title, 0, Qt.AlignTop)

        self.addLayoutFrame = QFrame(self.takeProfessionNonePage)
        self.addLayoutFrame.setObjectName(u"addLayoutFrame")
        self.addLayout = QHBoxLayout(self.addLayoutFrame)
        self.addLayout.setSpacing(0)
        self.addLayout.setObjectName(u"addLayout")
        self.label_2 = QLabel(self.addLayoutFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 0))
        self.label_2.setMaximumSize(QSize(30, 16777215))

        self.addLayout.addWidget(self.label_2)

        self.addFrame = QFrame(self.addLayoutFrame)
        self.addFrame.setObjectName(u"addFrame")
        self.addFrame.setMinimumSize(QSize(1861, 860))
        self.addFrame.setMaximumSize(QSize(1861, 860))
        self.addFrame.setLayoutDirection(Qt.LeftToRight)
        self.addFrame.setStyleSheet(u"QWidget {\n"
"	background-color: #FFFFFF;\n"
"	border: 2px dashed #501EBC;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.addFrame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.bigButton = QHBoxLayout()
        self.bigButton.setObjectName(u"bigButton")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bigButton.addItem(self.horizontalSpacer_3)

        self.pushBigButton = QPushButton(self.addFrame)
        self.pushBigButton.setObjectName(u"pushBigButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(96)
        sizePolicy2.setVerticalStretch(96)
        sizePolicy2.setHeightForWidth(self.pushBigButton.sizePolicy().hasHeightForWidth())
        self.pushBigButton.setSizePolicy(sizePolicy2)
        self.pushBigButton.setMinimumSize(QSize(96, 96))
        self.pushBigButton.setMaximumSize(QSize(96, 96))
        self.pushBigButton.setLayoutDirection(Qt.LeftToRight)
        self.pushBigButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons And Logo/File.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushBigButton.setIcon(icon)
        self.pushBigButton.setIconSize(QSize(56, 56))

        self.bigButton.addWidget(self.pushBigButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bigButton.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.bigButton)

        self.text = QFrame(self.addFrame)
        self.text.setObjectName(u"text")
        self.text.setStyleSheet(u"border:none;")
        self.verticalLayout_2 = QVBoxLayout(self.text)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_1 = QLabel(self.text)
        self.text_1.setObjectName(u"text_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(28)
        sizePolicy3.setHeightForWidth(self.text_1.sizePolicy().hasHeightForWidth())
        self.text_1.setSizePolicy(sizePolicy3)
        self.text_1.setMinimumSize(QSize(0, 28))
        self.text_1.setMaximumSize(QSize(16777215, 28))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.text_1.setPalette(palette4)
        self.text_1.setFont(font2)
        self.text_1.setStyleSheet(u"border: none;")
        self.text_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.text_1, 0, Qt.AlignHCenter)

        self.text_2 = QLabel(self.text)
        self.text_2.setObjectName(u"text_2")
        sizePolicy3.setHeightForWidth(self.text_2.sizePolicy().hasHeightForWidth())
        self.text_2.setSizePolicy(sizePolicy3)
        self.text_2.setMinimumSize(QSize(360, 28))
        self.text_2.setMaximumSize(QSize(360, 28))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.text_2.setPalette(palette5)
        self.text_2.setFont(font2)
        self.text_2.setLayoutDirection(Qt.LeftToRight)
        self.text_2.setStyleSheet(u"border: none;")
        self.text_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.text_2)


        self.verticalLayout_3.addWidget(self.text, 0, Qt.AlignHCenter)

        self.download = QFrame(self.addFrame)
        self.download.setObjectName(u"download")
        self.download.setStyleSheet(u"border: none;")
        self.verticalLayout = QVBoxLayout(self.download)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.downloadButton = QPushButton(self.download)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy1)
        self.downloadButton.setMinimumSize(QSize(155, 48))
        self.downloadButton.setMaximumSize(QSize(155, 16777215))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.downloadButton.setPalette(palette6)
        self.downloadButton.setFont(font2)
        self.downloadButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        self.downloadButton.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.downloadButton)

        self.textFiles = QLabel(self.download)
        self.textFiles.setObjectName(u"textFiles")
        sizePolicy3.setHeightForWidth(self.textFiles.sizePolicy().hasHeightForWidth())
        self.textFiles.setSizePolicy(sizePolicy3)
        self.textFiles.setMinimumSize(QSize(0, 28))
        self.textFiles.setMaximumSize(QSize(16777215, 28))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textFiles.setPalette(palette7)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.textFiles.setFont(font3)
        self.textFiles.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.textFiles, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.download, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.addLayout.addWidget(self.addFrame)

        self.label_3 = QLabel(self.addLayoutFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setMaximumSize(QSize(30, 16777215))

        self.addLayout.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.addLayoutFrame, 0, Qt.AlignTop)

        TakeProfessionNonePage.setCentralWidget(self.takeProfessionNonePage)

        self.retranslateUi(TakeProfessionNonePage)

        QMetaObject.connectSlotsByName(TakeProfessionNonePage)
    # setupUi

    def retranslateUi(self, TakeProfessionNonePage):
        TakeProfessionNonePage.setWindowTitle(QCoreApplication.translate("TakeProfessionNonePage", u"Your Vacancy", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("TakeProfessionNonePage", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e", None))
        self.pushButton_2.setText(QCoreApplication.translate("TakeProfessionNonePage", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u044b", None))
        self.pushButton_3.setText(QCoreApplication.translate("TakeProfessionNonePage", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.title_2.setText(QCoreApplication.translate("TakeProfessionNonePage", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e", None))
        self.pushButtonAddTags.setText(QCoreApplication.translate("TakeProfessionNonePage", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0440\u0435\u0437\u044e\u043c\u0435", None))
        self.label_2.setText("")
        self.pushBigButton.setText("")
        self.text_1.setText(QCoreApplication.translate("TakeProfessionNonePage", u"\u0417\u0434\u0435\u0441\u044c \u043f\u043e\u043a\u0430 \u043f\u0443\u0441\u0442\u043e :(", None))
        self.text_2.setText(QCoreApplication.translate("TakeProfessionNonePage", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b \u0440\u0435\u0437\u044e\u043c\u0435", None))
        self.downloadButton.setText(QCoreApplication.translate("TakeProfessionNonePage", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.textFiles.setText(QCoreApplication.translate("TakeProfessionNonePage", u"*PDF, DOC, DOCX", None))
        self.label_3.setText("")
    # retranslateUi

