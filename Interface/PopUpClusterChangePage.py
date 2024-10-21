# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUpClusterChangePage.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import Logo
import Icons

class Ui_PopUpClusterChangePage(object):
    def setupUi(self, PopUpClusterChangePage):
        if not PopUpClusterChangePage.objectName():
            PopUpClusterChangePage.setObjectName(u"PopUpClusterChangePage")
        PopUpClusterChangePage.resize(560, 275)
        PopUpClusterChangePage.setMinimumSize(QSize(560, 275))
        PopUpClusterChangePage.setMaximumSize(QSize(560, 275))
        PopUpClusterChangePage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.popUpClusterChangePage = QWidget(PopUpClusterChangePage)
        self.popUpClusterChangePage.setObjectName(u"popUpClusterChangePage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popUpClusterChangePage.sizePolicy().hasHeightForWidth())
        self.popUpClusterChangePage.setSizePolicy(sizePolicy)
        self.popUpClusterChangePage.setMaximumSize(QSize(16777215, 16777215))
        self.popUpClusterChangePage.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.popUpClusterChangePage)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(29, 29, 29, 29)
        self.title = QLabel(self.popUpClusterChangePage)
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

        self.clusterName = QVBoxLayout()
        self.clusterName.setSpacing(5)
        self.clusterName.setObjectName(u"clusterName")
        self.name = QLabel(self.popUpClusterChangePage)
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

        self.clusterName.addWidget(self.name)

        self.input = QLineEdit(self.popUpClusterChangePage)
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
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
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
"   color: #101010;\n"
"	border: 2px solid #5B5B5B;\n"
"	border-radius: 10px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"}")

        self.clusterName.addWidget(self.input)


        self.verticalLayout.addLayout(self.clusterName)

        self.buttonsFrame = QFrame(self.popUpClusterChangePage)
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
        palette3 = QPalette()
        brush3 = QBrush(QColor(80, 30, 188, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.pushButtonYes.setPalette(palette3)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(18)
        font3.setBold(True)
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
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonNo.setPalette(palette4)
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

        PopUpClusterChangePage.setCentralWidget(self.popUpClusterChangePage)

        self.retranslateUi(PopUpClusterChangePage)

        QMetaObject.connectSlotsByName(PopUpClusterChangePage)
    # setupUi

    def retranslateUi(self, PopUpClusterChangePage):
        PopUpClusterChangePage.setWindowTitle(QCoreApplication.translate("PopUpClusterChangePage", u"Your Vacancy", None))
        self.title.setText(QCoreApplication.translate("PopUpClusterChangePage", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0430", None))
        self.name.setText(QCoreApplication.translate("PopUpClusterChangePage", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.input.setText("")
        self.input.setPlaceholderText(QCoreApplication.translate("PopUpClusterChangePage", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0430", None))
        self.pushButtonYes.setText(QCoreApplication.translate("PopUpClusterChangePage", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButtonNo.setText(QCoreApplication.translate("PopUpClusterChangePage", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

