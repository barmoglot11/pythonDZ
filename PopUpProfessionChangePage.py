# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUpProfessionChangePage.ui'
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
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import Logo
import Icons

class Ui_PopUpProfessionChangePage(object):
    def setupUi(self, PopUpProfessionChangePage):
        if not PopUpProfessionChangePage.objectName():
            PopUpProfessionChangePage.setObjectName(u"PopUpProfessionChangePage")
        PopUpProfessionChangePage.resize(560, 830)
        PopUpProfessionChangePage.setMinimumSize(QSize(560, 830))
        PopUpProfessionChangePage.setMaximumSize(QSize(560, 830))
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
        self.verticalLayout = QVBoxLayout(self.popUpProfessionChangePage)
        self.verticalLayout.setSpacing(29)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(29, 29, 29, 29)
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

        self.verticalLayout.addWidget(self.title)

        self.professionName = QVBoxLayout()
        self.professionName.setSpacing(5)
        self.professionName.setObjectName(u"professionName")
        self.name = QLabel(self.popUpProfessionChangePage)
        self.name.setObjectName(u"name")
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setMinimumSize(QSize(500, 16))
        self.name.setMaximumSize(QSize(500, 16))
        palette1 = QPalette()
        brush2 = QBrush(QColor(91, 91, 91, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.name.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.name.setFont(font1)
        self.name.setStyleSheet(u"color: #5B5B5B;")

        self.professionName.addWidget(self.name)

        self.input = QLineEdit(self.popUpProfessionChangePage)
        self.input.setObjectName(u"input")
        self.input.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy2)
        self.input.setMinimumSize(QSize(500, 48))
        self.input.setMaximumSize(QSize(500, 48))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.input.setPalette(palette2)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setKerning(True)
        self.input.setFont(font2)
        self.input.setAcceptDrops(True)
        self.input.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid #5B5B5B;\n"
"	border-radius: 10px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	color: #101010;\n"
"}")

        self.professionName.addWidget(self.input)


        self.verticalLayout.addLayout(self.professionName)

        self.description = QVBoxLayout()
        self.description.setSpacing(5)
        self.description.setObjectName(u"description")
        self.name_2 = QLabel(self.popUpProfessionChangePage)
        self.name_2.setObjectName(u"name_2")
        sizePolicy1.setHeightForWidth(self.name_2.sizePolicy().hasHeightForWidth())
        self.name_2.setSizePolicy(sizePolicy1)
        self.name_2.setMinimumSize(QSize(500, 16))
        self.name_2.setMaximumSize(QSize(500, 16))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.name_2.setPalette(palette3)
        self.name_2.setFont(font1)
        self.name_2.setStyleSheet(u"color: #5B5B5B;")

        self.description.addWidget(self.name_2)

        self.inputDescription = QPlainTextEdit(self.popUpProfessionChangePage)
        self.inputDescription.setObjectName(u"inputDescription")
        self.inputDescription.setMinimumSize(QSize(500, 300))
        self.inputDescription.setMaximumSize(QSize(500, 300))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.inputDescription.setFont(font3)
        self.inputDescription.setStyleSheet(u"QPlainTextEdit {\n"
"	border: 2px solid #5B5B5B;\n"
"	border-radius: 10px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	padding-left: 20px;\n"
"	padding-right: 3px;\n"
"	color: #101010;\n"
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
""
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
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")

        self.description.addWidget(self.inputDescription)


        self.verticalLayout.addLayout(self.description)

        self.region = QVBoxLayout()
        self.region.setSpacing(5)
        self.region.setObjectName(u"region")
        self.name_3 = QLabel(self.popUpProfessionChangePage)
        self.name_3.setObjectName(u"name_3")
        sizePolicy1.setHeightForWidth(self.name_3.sizePolicy().hasHeightForWidth())
        self.name_3.setSizePolicy(sizePolicy1)
        self.name_3.setMinimumSize(QSize(500, 16))
        self.name_3.setMaximumSize(QSize(500, 16))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.name_3.setPalette(palette4)
        self.name_3.setFont(font1)
        self.name_3.setStyleSheet(u"color: #5B5B5B;")

        self.region.addWidget(self.name_3)

        self.comboBoxRegion = QComboBox(self.popUpProfessionChangePage)
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.addItem("")
        self.comboBoxRegion.setObjectName(u"comboBoxRegion")
        self.comboBoxRegion.setMinimumSize(QSize(500, 48))
        self.comboBoxRegion.setMaximumSize(QSize(500, 48))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.comboBoxRegion.setPalette(palette5)
        self.comboBoxRegion.setFont(font3)
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


        self.verticalLayout.addLayout(self.region)

        self.cluster = QVBoxLayout()
        self.cluster.setSpacing(5)
        self.cluster.setObjectName(u"cluster")
        self.name_4 = QLabel(self.popUpProfessionChangePage)
        self.name_4.setObjectName(u"name_4")
        sizePolicy1.setHeightForWidth(self.name_4.sizePolicy().hasHeightForWidth())
        self.name_4.setSizePolicy(sizePolicy1)
        self.name_4.setMinimumSize(QSize(500, 16))
        self.name_4.setMaximumSize(QSize(500, 16))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.name_4.setPalette(palette6)
        self.name_4.setFont(font1)
        self.name_4.setStyleSheet(u"color: #5B5B5B;")

        self.cluster.addWidget(self.name_4)

        self.comboBoxCluster = QComboBox(self.popUpProfessionChangePage)
        self.comboBoxCluster.addItem("")
        self.comboBoxCluster.addItem("")
        self.comboBoxCluster.addItem("")
        self.comboBoxCluster.addItem("")
        self.comboBoxCluster.addItem("")
        self.comboBoxCluster.setObjectName(u"comboBoxCluster")
        self.comboBoxCluster.setMinimumSize(QSize(500, 48))
        self.comboBoxCluster.setMaximumSize(QSize(500, 48))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.comboBoxCluster.setPalette(palette7)
        self.comboBoxCluster.setFont(font3)
        self.comboBoxCluster.setStyleSheet(u"QComboBox {\n"
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

        self.cluster.addWidget(self.comboBoxCluster)


        self.verticalLayout.addLayout(self.cluster)

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
        palette8 = QPalette()
        brush3 = QBrush(QColor(80, 30, 188, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.pushButtonYes.setPalette(palette8)
        self.pushButtonYes.setFont(font3)
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
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonNo.setPalette(palette9)
        self.pushButtonNo.setFont(font3)
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


        self.verticalLayout.addWidget(self.buttonsFrame, 0, Qt.AlignLeft)

        PopUpProfessionChangePage.setCentralWidget(self.popUpProfessionChangePage)

        self.retranslateUi(PopUpProfessionChangePage)

        QMetaObject.connectSlotsByName(PopUpProfessionChangePage)
    # setupUi

    def retranslateUi(self, PopUpProfessionChangePage):
        PopUpProfessionChangePage.setWindowTitle(QCoreApplication.translate("PopUpProfessionChangePage", u"Your Vacancy", None))
        self.title.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.name.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.input.setText("")
        self.input.setPlaceholderText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.name_2.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.inputDescription.setPlaceholderText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u043f\u0438\u0448\u0438\u0442\u0435 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e", None))
        self.name_3.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u0420\u0435\u0433\u0438\u043e\u043d", None))
        self.comboBoxRegion.setItemText(0, QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u043c\u0441\u043a", None))
        self.comboBoxRegion.setItemText(1, QCoreApplication.translate("PopUpProfessionChangePage", u"\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433", None))
        self.comboBoxRegion.setItemText(2, QCoreApplication.translate("PopUpProfessionChangePage", u"\u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433", None))
        self.comboBoxRegion.setItemText(3, QCoreApplication.translate("PopUpProfessionChangePage", u"\u0412\u043e\u043b\u0433\u043e\u0433\u0440\u0430\u0434", None))
        self.comboBoxRegion.setItemText(4, QCoreApplication.translate("PopUpProfessionChangePage", u"\u041c\u043e\u0441\u043a\u0432\u0430", None))

        self.name_4.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440", None))
        self.comboBoxCluster.setItemText(0, QCoreApplication.translate("PopUpProfessionChangePage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
        self.comboBoxCluster.setItemText(1, QCoreApplication.translate("PopUpProfessionChangePage", u"\u0421\u0442\u0438\u043b\u0438\u0441\u0442", None))
        self.comboBoxCluster.setItemText(2, QCoreApplication.translate("PopUpProfessionChangePage", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c", None))
        self.comboBoxCluster.setItemText(3, QCoreApplication.translate("PopUpProfessionChangePage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043c\u0435\u0431\u0435\u043b\u0438", None))
        self.comboBoxCluster.setItemText(4, QCoreApplication.translate("PopUpProfessionChangePage", u"\u0414\u0438\u0437\u0430\u0439\u043d\u0435\u0440 \u0438\u043d\u0442\u0435\u0440\u044c\u0435\u0440\u0430", None))

        self.pushButtonYes.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButtonNo.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

