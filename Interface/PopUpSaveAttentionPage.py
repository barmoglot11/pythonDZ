# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUpSaveAttentionPage.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import Logo
import Icons

class Ui_PopUpSaveAttentionPage(object):
    def setupUi(self, PopUpSaveAttentionPage):
        if not PopUpSaveAttentionPage.objectName():
            PopUpSaveAttentionPage.setObjectName(u"PopUpSaveAttentionPage")
        PopUpSaveAttentionPage.resize(776, 176)
        PopUpSaveAttentionPage.setMinimumSize(QSize(776, 176))
        PopUpSaveAttentionPage.setMaximumSize(QSize(776, 176))
        PopUpSaveAttentionPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.popUpSaveAttentionPage = QWidget(PopUpSaveAttentionPage)
        self.popUpSaveAttentionPage.setObjectName(u"popUpSaveAttentionPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popUpSaveAttentionPage.sizePolicy().hasHeightForWidth())
        self.popUpSaveAttentionPage.setSizePolicy(sizePolicy)
        self.popUpSaveAttentionPage.setMaximumSize(QSize(16777215, 16777215))
        self.popUpSaveAttentionPage.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.popUpSaveAttentionPage)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.title = QLabel(self.popUpSaveAttentionPage)
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

        self.buttonsFrame = QFrame(self.popUpSaveAttentionPage)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttons = QHBoxLayout(self.buttonsFrame)
        self.buttons.setSpacing(20)
        self.buttons.setObjectName(u"buttons")
        self.pushButtonYes = QPushButton(self.buttonsFrame)
        self.pushButtonYes.setObjectName(u"pushButtonYes")
        self.pushButtonYes.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonYes.sizePolicy().hasHeightForWidth())
        self.pushButtonYes.setSizePolicy(sizePolicy1)
        self.pushButtonYes.setMinimumSize(QSize(71, 48))
        self.pushButtonYes.setMaximumSize(QSize(71, 16777215))
        palette1 = QPalette()
        brush2 = QBrush(QColor(80, 30, 188, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButtonYes.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(18)
        font1.setBold(True)
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
        self.pushButtonNo.setMinimumSize(QSize(83, 48))
        self.pushButtonNo.setMaximumSize(QSize(83, 16777215))
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
        self.pushButtonNo.setPalette(palette2)
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


        self.verticalLayout.addWidget(self.buttonsFrame, 0, Qt.AlignHCenter)

        PopUpSaveAttentionPage.setCentralWidget(self.popUpSaveAttentionPage)

        self.retranslateUi(PopUpSaveAttentionPage)

        QMetaObject.connectSlotsByName(PopUpSaveAttentionPage)
    # setupUi

    def retranslateUi(self, PopUpSaveAttentionPage):
        PopUpSaveAttentionPage.setWindowTitle(QCoreApplication.translate("PopUpSaveAttentionPage", u"Your Vacancy", None))
        self.title.setText(QCoreApplication.translate("PopUpSaveAttentionPage", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b, \u0447\u0442\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f?", None))
        self.pushButtonYes.setText(QCoreApplication.translate("PopUpSaveAttentionPage", u"\u0414\u0430", None))
        self.pushButtonNo.setText(QCoreApplication.translate("PopUpSaveAttentionPage", u"\u041d\u0435\u0442", None))
    # retranslateUi

