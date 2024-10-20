# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUpAddResumePage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Logo
import Icons

class Ui_PopUpProfessionChangePage(object):
    def setupUi(self, PopUpProfessionChangePage):
        if not PopUpProfessionChangePage.objectName():
            PopUpProfessionChangePage.setObjectName(u"PopUpProfessionChangePage")
        PopUpProfessionChangePage.resize(560, 810)
        PopUpProfessionChangePage.setMinimumSize(QSize(560, 810))
        PopUpProfessionChangePage.setMaximumSize(QSize(560, 810))
        PopUpProfessionChangePage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.popUpProfessionChangePage = QWidget(PopUpProfessionChangePage)
        self.popUpProfessionChangePage.setObjectName(u"popUpProfessionChangePage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popUpProfessionChangePage.sizePolicy().hasHeightForWidth())
        self.popUpProfessionChangePage.setSizePolicy(sizePolicy)
        self.popUpProfessionChangePage.setMaximumSize(QSize(16777215, 16777215))
        self.popUpProfessionChangePage.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.popUpProfessionChangePage)
        self.verticalLayout_4.setSpacing(29)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(29, 29, 29, 29)
        self.title = QLabel(self.popUpProfessionChangePage)
        self.title.setObjectName(u"title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(16, 16, 16, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.title.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(24)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: #101010;")

        self.verticalLayout_4.addWidget(self.title)

        self.addFrame = QFrame(self.popUpProfessionChangePage)
        self.addFrame.setObjectName(u"addFrame")
        self.addFrame.setMinimumSize(QSize(500, 500))
        self.addFrame.setMaximumSize(QSize(500, 500))
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
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.text_1 = QLabel(self.text)
        self.text_1.setObjectName(u"text_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(28)
        sizePolicy3.setHeightForWidth(self.text_1.sizePolicy().hasHeightForWidth())
        self.text_1.setSizePolicy(sizePolicy3)
        self.text_1.setMinimumSize(QSize(0, 28))
        self.text_1.setMaximumSize(QSize(16777215, 28))
        palette1 = QPalette()
        brush2 = QBrush(QColor(80, 30, 188, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.text_1.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.text_1.setFont(font1)
        self.text_1.setStyleSheet(u"border: none;")
        self.text_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.text_1, 0, Qt.AlignHCenter)

        self.textFrame = QFrame(self.text)
        self.textFrame.setObjectName(u"textFrame")
        self.horizontalLayout = QHBoxLayout(self.textFrame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.file = QLabel(self.textFrame)
        self.file.setObjectName(u"file")
        sizePolicy3.setHeightForWidth(self.file.sizePolicy().hasHeightForWidth())
        self.file.setSizePolicy(sizePolicy3)
        self.file.setMinimumSize(QSize(0, 28))
        self.file.setMaximumSize(QSize(360, 28))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.file.setPalette(palette2)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setUnderline(True)
        font2.setStrikeOut(False)
        self.file.setFont(font2)
        self.file.setLayoutDirection(Qt.LeftToRight)
        self.file.setStyleSheet(u"border: none;")
        self.file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.file)

        self.pushButtonDelete = QPushButton(self.textFrame)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons And Logo/Trash_purple.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonDelete.setIcon(icon1)
        self.pushButtonDelete.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButtonDelete)


        self.verticalLayout_2.addWidget(self.textFrame, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.text, 0, Qt.AlignHCenter)

        self.download = QFrame(self.addFrame)
        self.download.setObjectName(u"download")
        self.download.setStyleSheet(u"border: none;")
        self.verticalLayout = QVBoxLayout(self.download)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.downloadButton = QPushButton(self.download)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy1)
        self.downloadButton.setMinimumSize(QSize(155, 48))
        self.downloadButton.setMaximumSize(QSize(155, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.downloadButton.setPalette(palette3)
        self.downloadButton.setFont(font1)
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
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textFiles.setPalette(palette4)
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


        self.verticalLayout_4.addWidget(self.addFrame)

        self.region = QVBoxLayout()
        self.region.setSpacing(5)
        self.region.setObjectName(u"region")
        self.name = QLabel(self.popUpProfessionChangePage)
        self.name.setObjectName(u"name")
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setMinimumSize(QSize(500, 16))
        self.name.setMaximumSize(QSize(500, 16))
        palette5 = QPalette()
        brush4 = QBrush(QColor(91, 91, 91, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.name.setPalette(palette5)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.name.setFont(font4)
        self.name.setStyleSheet(u"color: #5B5B5B;")

        self.region.addWidget(self.name)

        self.comboBoxRegion = QComboBox(self.popUpProfessionChangePage)
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.setObjectName(u"comboBoxRegion")
        self.comboBoxRegion.setMinimumSize(QSize(500, 48))
        self.comboBoxRegion.setMaximumSize(QSize(500, 48))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.comboBoxRegion.setPalette(palette6)
        self.comboBoxRegion.setFont(font1)
        self.comboBoxRegion.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid #5B5B5B;\n"
"	border-radius: 10px;\n"
"	padding-left: 20px;\n"
"	padding-right: 3px;\n"
"	color: #101010;\n"
"}\n"
"\n"
"QListView {\n"
"	border-radius: 10px;\n"
"	padding-left: 20px;\n"
"	padding-right: 5px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	color: #101010;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border-radius: 7px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	image: url(:/Icons/Icons And Logo/Expand_down.png);\n"
"}\n"
"\n"
"QComboBox::drop-down:on {\n"
"	image: url(:/Icons/Icons And Logo/Expand_up.png);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #E7E7E7;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::ha"
                        "ndle:vertical {	\n"
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
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #501EBC;\n"
"}\n"
"\n"
"QScroll"
                        "Bar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")

        self.region.addWidget(self.comboBoxRegion)


        self.verticalLayout_4.addLayout(self.region)

        self.buttonsFrame = QFrame(self.popUpProfessionChangePage)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttons = QHBoxLayout(self.buttonsFrame)
        self.buttons.setSpacing(20)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.pushButtonYes = QPushButton(self.buttonsFrame)
        self.pushButtonYes.setObjectName(u"pushButtonYes")
        self.pushButtonYes.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonYes.sizePolicy().hasHeightForWidth())
        self.pushButtonYes.setSizePolicy(sizePolicy1)
        self.pushButtonYes.setMinimumSize(QSize(162, 48))
        self.pushButtonYes.setMaximumSize(QSize(162, 16777215))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButtonYes.setPalette(palette7)
        self.pushButtonYes.setFont(font1)
        self.pushButtonYes.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        self.pushButtonYes.setIconSize(QSize(20, 20))

        self.buttons.addWidget(self.pushButtonYes)

        self.pushButtonNo = QPushButton(self.buttonsFrame)
        self.pushButtonNo.setObjectName(u"pushButtonNo")
        self.pushButtonNo.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonNo.sizePolicy().hasHeightForWidth())
        self.pushButtonNo.setSizePolicy(sizePolicy1)
        self.pushButtonNo.setMinimumSize(QSize(153, 48))
        self.pushButtonNo.setMaximumSize(QSize(153, 16777215))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonNo.setPalette(palette8)
        self.pushButtonNo.setFont(font1)
        self.pushButtonNo.setStyleSheet(u"QPushButton {\n"
"	background-color: #FFFFFF;\n"
"	border: 2px solid #501EBC;\n"
"	border-radius: 10px;\n"
"	color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid #321374;\n"
"}")
        self.pushButtonNo.setIconSize(QSize(20, 20))

        self.buttons.addWidget(self.pushButtonNo)


        self.verticalLayout_4.addWidget(self.buttonsFrame, 0, Qt.AlignLeft)

        PopUpProfessionChangePage.setCentralWidget(self.popUpProfessionChangePage)

        self.retranslateUi(PopUpProfessionChangePage)

        QMetaObject.connectSlotsByName(PopUpProfessionChangePage)
    # setupUi

    def retranslateUi(self, PopUpProfessionChangePage):
        PopUpProfessionChangePage.setWindowTitle(QCoreApplication.translate("PopUpProfessionChangePage", u"Your Vacancy", None))
        self.title.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0440\u0435\u0437\u044e\u043c\u0435", None))
        self.pushBigButton.setText("")
        self.text_1.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0440\u0435\u0437\u044e\u043c\u0435", None))
        self.file.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"none.pdf", None))
        self.pushButtonDelete.setText("")
        self.downloadButton.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.textFiles.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"*PDF, DOC, DOCX", None))
        self.name.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u0420\u0435\u0433\u0438\u043e\u043d", None))
        self.comboBoxRegion.setItemText(0, QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u043c\u0441\u043a", None))
        self.comboBoxRegion.setItemText(1, QCoreApplication.translate("PopUpProfessionChangePage", u"\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433", None))
        self.comboBoxRegion.setItemText(2, QCoreApplication.translate("PopUpProfessionChangePage", u"\u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433", None))
        self.comboBoxRegion.setItemText(3, QCoreApplication.translate("PopUpProfessionChangePage", u"\u0412\u043e\u043b\u0433\u043e\u0433\u0440\u0430\u0434", None))
        self.comboBoxRegion.setItemText(4, QCoreApplication.translate("PopUpProfessionChangePage", u"\u041c\u043e\u0441\u043a\u0432\u0430", None))

        self.pushButtonYes.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButtonNo.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

