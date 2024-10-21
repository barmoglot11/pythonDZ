# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUpProfessionPage.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)
import Logo
import Icons

class Ui_PopUpProfessionPage(object):
    def setupUi(self, PopUpProfessionPage):
        if not PopUpProfessionPage.objectName():
            PopUpProfessionPage.setObjectName(u"PopUpProfessionPage")
        PopUpProfessionPage.resize(1382, 680)
        PopUpProfessionPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.popUpProfessionPage = QWidget(PopUpProfessionPage)
        self.popUpProfessionPage.setObjectName(u"popUpProfessionPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popUpProfessionPage.sizePolicy().hasHeightForWidth())
        self.popUpProfessionPage.setSizePolicy(sizePolicy)
        self.popUpProfessionPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.popUpProfessionPage)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.name = QHBoxLayout()
        self.name.setSpacing(0)
        self.name.setObjectName(u"name")
        self.title = QHBoxLayout()
        self.title.setSpacing(15)
        self.title.setObjectName(u"title")
        self.titleName = QLabel(self.popUpProfessionPage)
        self.titleName.setObjectName(u"titleName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleName.sizePolicy().hasHeightForWidth())
        self.titleName.setSizePolicy(sizePolicy1)
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
        self.titleName.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(30)
        font.setBold(True)
        self.titleName.setFont(font)
        self.titleName.setStyleSheet(u"color: #101010;")

        self.title.addWidget(self.titleName)

        self.pushButtonRedact = QPushButton(self.popUpProfessionPage)
        self.pushButtonRedact.setObjectName(u"pushButtonRedact")
        self.pushButtonRedact.setMinimumSize(QSize(36, 36))
        self.pushButtonRedact.setMaximumSize(QSize(36, 36))
        self.pushButtonRedact.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact.setIconSize(QSize(24, 24))

        self.title.addWidget(self.pushButtonRedact)

        self.pushButtonDelete = QPushButton(self.popUpProfessionPage)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(36, 36))
        self.pushButtonDelete.setMaximumSize(QSize(36, 36))
        self.pushButtonDelete.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete.setIconSize(QSize(24, 24))

        self.title.addWidget(self.pushButtonDelete)


        self.name.addLayout(self.title)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.name.addItem(self.horizontalSpacer_3)

        self.pushButtonClose = QPushButton(self.popUpProfessionPage)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        self.pushButtonClose.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonClose.sizePolicy().hasHeightForWidth())
        self.pushButtonClose.setSizePolicy(sizePolicy1)
        self.pushButtonClose.setMinimumSize(QSize(48, 48))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.pushButtonClose.setFont(font1)
        self.pushButtonClose.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons And Logo/Close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonClose.setIcon(icon)
        self.pushButtonClose.setIconSize(QSize(24, 24))

        self.name.addWidget(self.pushButtonClose)


        self.verticalLayout.addLayout(self.name)

        self.description = QVBoxLayout()
        self.description.setSpacing(10)
        self.description.setObjectName(u"description")
        self.professionName = QLabel(self.popUpProfessionPage)
        self.professionName.setObjectName(u"professionName")
        sizePolicy1.setHeightForWidth(self.professionName.sizePolicy().hasHeightForWidth())
        self.professionName.setSizePolicy(sizePolicy1)
        self.professionName.setMinimumSize(QSize(0, 30))
        self.professionName.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.professionName.setFont(font2)
        self.professionName.setStyleSheet(u"color: #501EBC;")

        self.description.addWidget(self.professionName)

        self.textDescription = QTextBrowser(self.popUpProfessionPage)
        self.textDescription.setObjectName(u"textDescription")
        self.textDescription.setMinimumSize(QSize(1320, 510))
        self.textDescription.setMaximumSize(QSize(1320, 510))
        self.textDescription.setStyleSheet(u"QWidget {\n"
"   color: #101010;\n"
"	border: none;\n"
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
"	border: none;\n"
"	background-color: #5B5B5B;\n"
"	height: 15px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-left-radi"
                        "us: 7px;\n"
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

        self.description.addWidget(self.textDescription)


        self.verticalLayout.addLayout(self.description)

        PopUpProfessionPage.setCentralWidget(self.popUpProfessionPage)

        self.retranslateUi(PopUpProfessionPage)

        QMetaObject.connectSlotsByName(PopUpProfessionPage)
    # setupUi

    def retranslateUi(self, PopUpProfessionPage):
        PopUpProfessionPage.setWindowTitle(QCoreApplication.translate("PopUpProfessionPage", u"Your Vacancy", None))
        self.titleName.setText(QCoreApplication.translate("PopUpProfessionPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
        self.pushButtonRedact.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonClose.setText("")
        self.professionName.setText(QCoreApplication.translate("PopUpProfessionPage", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.textDescription.setHtml(QCoreApplication.translate("PopUpProfessionPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff;\">\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u0438\u0433\u0440\u0430\u0435\u0442 \u043a\u043b\u044e\u0447\u0435\u0432\u0443\u044e \u0440\u043e\u043b\u044c \u0432 \u044d\u043a\u043e\u043d\u043e\u043c\u0438\u043a\u0435 \u0438 \u0431\u0438\u0437\u043d\u0435\u0441\u0435, \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0438\u0432\u0430\u044f \u0441\u0432\u044f\u0437\u044c \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u043e\u0438\u0437\u0432"
                        "\u043e\u0434\u0438\u0442\u0435\u043b\u044f\u043c\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432 \u0438 \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u043c\u0438 \u043f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b\u044f\u043c\u0438. \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043e\u0431\u044f\u0437\u0430\u043d\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u0432\u043a\u043b\u044e\u0447\u0430\u044e\u0442 \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432, \u0433\u0434\u0435 \u043f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432\u044b\u044f\u0432\u043b\u044f\u0435\u0442 \u043f\u043e\u0442\u0440\u0435\u0431\u043d\u043e\u0441\u0442\u0438 \u0438 \u043f\u0440\u0435\u0434\u043b\u0430\u0433\u0430\u0435\u0442 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u044b \u0438\u043b\u0438 \u0443\u0441\u043b\u0443\u0433\u0438, \u0430 \u0442\u0430"
                        "\u043a\u0436\u0435 \u043f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0438\u044e \u0442\u043e\u0432\u0430\u0440\u043e\u0432, \u0447\u0442\u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0443\u043c\u0435\u0432\u0430\u0435\u0442 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u044e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432 \u0438 \u043e\u0431\u044a\u044f\u0441\u043d\u0435\u043d\u0438\u0435 \u0438\u0445 \u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432. \u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0442\u0430\u043a\u0436\u0435 \u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0435\u0442 \u0437\u0430\u043a\u0430\u0437\u044b, \u043e\u0444\u043e\u0440\u043c\u043b\u044f\u0435\u0442 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b \u0438 \u0441\u043b\u0435\u0434\u0438\u0442 \u0437\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435\u043c \u0443\u0441\u043b\u043e\u0432\u0438\u0439 \u0441\u0434\u0435\u043b\u043a\u0438, \u0432\u043a\u043b"
                        "\u044e\u0447\u0430\u044f \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0443 \u0438 \u043e\u043f\u043b\u0430\u0442\u0443. \u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u043f\u043e\u0440\u044f\u0434\u043a\u0430 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435, \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f \u0432\u0438\u0442\u0440\u0438\u043d \u0438 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u0437\u0430 \u043d\u0430\u043b\u0438\u0447\u0438\u0435\u043c \u0442\u043e\u0432\u0430\u0440\u0430 \u0442\u0430\u043a\u0436\u0435 \u0432\u0445\u043e\u0434\u044f\u0442 \u0432 \u0435\u0433\u043e \u0437\u0430\u0434\u0430\u0447\u0438. \u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u043c \u0430\u043f\u043f\u0430\u0440\u0430\u0442\u043e\u043c \u0438 \u0443\u0447\u0435\u0442 \u043f\u0440\u043e\u0434\u0430\u0436 \u2014 \u0432\u0430\u0436\u043d\u044b\u0435 \u0430\u0441\u043f\u0435\u043a\u0442\u044b \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438"
                        "\u0438, \u043a\u0430\u043a \u0438 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0430\u0441\u0430\u043c\u0438, \u0447\u0442\u043e \u0432\u043a\u043b\u044e\u0447\u0430\u0435\u0442 \u0443\u0447\u0430\u0441\u0442\u0438\u0435 \u0432 \u0438\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u0438\u0437\u0430\u0446\u0438\u0438 \u0438 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u0437\u0430 \u0442\u043e\u0432\u0430\u0440\u043d\u044b\u043c\u0438 \u0437\u0430\u043f\u0430\u0441\u0430\u043c\u0438.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff;\">\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u043d\u0430\u0432\u044b\u043a"
                        "\u0438 \u0438 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430 \u0434\u043b\u044f \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u043e\u043c \u0432\u043a\u043b\u044e\u0447\u0430\u044e\u0442 \u043a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u043d\u0430\u0432\u044b\u043a\u0438, \u0443\u043c\u0435\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0432 \u043a\u043e\u043c\u0430\u043d\u0434\u0435, \u0441\u0442\u0440\u0435\u0441\u0441\u043e\u0443\u0441\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0441\u0442\u044c, \u0437\u043d\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430 \u0438 \u043d\u0430\u0432\u044b\u043a\u0438 \u043f\u0440\u043e\u0434\u0430\u0436. \u0423\u043c\u0435\u043d\u0438\u0435 \u0447\u0435\u0442\u043a\u043e \u0438 \u0443\u0431\u0435\u0434\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0431\u0449\u0430\u0442\u044c\u0441\u044f \u0441"
                        " \u043a\u043b\u0438\u0435\u043d\u0442\u0430\u043c\u0438, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u044c \u0441\u043b\u0443\u0448\u0430\u0442\u044c \u0438 \u043f\u043e\u043d\u0438\u043c\u0430\u0442\u044c \u0438\u0445 \u043f\u043e\u0442\u0440\u0435\u0431\u043d\u043e\u0441\u0442\u0438 \u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u043e\u0441\u043d\u043e\u0432\u043e\u043f\u043e\u043b\u0430\u0433\u0430\u044e\u0449\u0438\u043c\u0438. \u0425\u043e\u0442\u044f \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u043e\u043c \u043d\u0435 \u0432\u0441\u0435\u0433\u0434\u0430 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0432\u044b\u0441\u0448\u0435\u0435 \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435, \u043d\u0430\u043b\u0438\u0447\u0438\u0435 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043e\u0431\u0440\u0430"
                        "\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u0438\u043b\u0438 \u043a\u0443\u0440\u0441\u043e\u0432 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432\u043e\u043c, \u0430 \u043e\u043f\u044b\u0442 \u0440\u0430\u0431\u043e\u0442\u044b \u0432 \u0441\u0444\u0435\u0440\u0435 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u0442\u0430\u043a\u0436\u0435 \u0446\u0435\u043d\u0438\u0442\u0441\u044f.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff;\">\u041f\u0435\u0440"
                        "\u0441\u043f\u0435\u043a\u0442\u0438\u0432\u044b \u043a\u0430\u0440\u044c\u0435\u0440\u043d\u043e\u0433\u043e \u0440\u043e\u0441\u0442\u0430 \u0434\u043b\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u043e\u0432 \u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u043d\u044b. \u041e\u043d\u0438 \u043c\u043e\u0433\u0443\u0442 \u043f\u0440\u043e\u0434\u0432\u0438\u0433\u0430\u0442\u044c\u0441\u044f \u043f\u043e \u043a\u0430\u0440\u044c\u0435\u0440\u043d\u043e\u0439 \u043b\u0435\u0441\u0442\u043d\u0438\u0446\u0435, \u0441\u0442\u0430\u043d\u043e\u0432\u044f\u0441\u044c \u0441\u0442\u0430\u0440\u0448\u0438\u043c\u0438 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430\u043c\u0438, \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u0430\u043c\u0438 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c \u0438\u043b\u0438 \u0434\u0430\u0436\u0435 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f\u043c\u0438 \u043c\u0430"
                        "\u0433\u0430\u0437\u0438\u043d\u043e\u0432. \u041e\u043f\u044b\u0442 \u0440\u0430\u0431\u043e\u0442\u044b \u0432 \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u0445 \u043c\u043e\u0436\u0435\u0442 \u043e\u0442\u043a\u0440\u044b\u0442\u044c \u0434\u0432\u0435\u0440\u0438 \u043a \u0431\u043e\u043b\u0435\u0435 \u0432\u044b\u0441\u043e\u043a\u0438\u043c \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044f\u043c \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u043b\u0438 \u043c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433\u0430. \u0422\u0430\u043a\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c, \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u043d\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u0430\u0436\u043d\u0430 \u0434\u043b\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0431\u0438\u0437\u043d\u0435\u0441\u0430, \u043d"
                        "\u043e \u0438 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u0434\u043b\u044f \u043b\u0438\u0447\u043d\u043e\u0433\u043e \u0438 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0440\u043e\u0441\u0442\u0430.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff;\">\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u043d\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u0430\u0436\u043d\u0430 \u0434\u043b\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0438"
                        "\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0431\u0438\u0437\u043d\u0435\u0441\u0430, \u043d\u043e \u0438 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u0434\u043b\u044f \u043b\u0438\u0447\u043d\u043e\u0433\u043e \u0438 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0440\u043e\u0441\u0442\u0430. \u0412\u0430\u0436\u043d\u044b\u043c \u0430\u0441\u043f\u0435\u043a\u0442\u043e\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0443\u043c\u0435\u043d\u0438\u0435 \u0430\u0434\u0430\u043f\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f \u043a \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f\u043c \u043d\u0430 \u0440\u044b\u043d\u043a\u0435 \u0438 \u0432 \u043f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0445 \u043f\u0440"
                        "\u0435\u0434\u043f\u043e\u0447\u0442\u0435\u043d\u0438\u044f\u0445. \u0421\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438, \u0442\u0430\u043a\u0438\u0435 \u043a\u0430\u043a \u043e\u043d\u043b\u0430\u0439\u043d-\u043f\u0440\u043e\u0434\u0430\u0436\u0438 \u0438 \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0435\u0442\u0438, \u0442\u0440\u0435\u0431\u0443\u044e\u0442 \u043e\u0442 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u043e\u0432 \u043e\u0441\u0432\u043e\u0435\u043d\u0438\u044f \u043d\u043e\u0432\u044b\u0445 \u043f\u043b\u0430\u0442\u0444\u043e\u0440\u043c \u0438 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u043e\u0432, \u0447\u0442\u043e \u0434\u0435\u043b\u0430\u0435\u0442 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e \u0434\u0438\u043d\u0430\u043c\u0438\u0447\u043d\u043e\u0439 \u0438 \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u043e\u0439.</span></p>\n"
"<p style=\"-qt-paragraph-ty"
                        "pe:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff;\">\u041a\u0440\u043e\u043c\u0435 \u0442\u043e\u0433\u043e, \u0443\u0441\u043f\u0435\u0448\u043d\u044b\u0435 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0447\u0430\u0441\u0442\u043e \u0441\u0442\u0430\u043d\u043e\u0432\u044f\u0442\u0441\u044f \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u0430\u043c\u0438 \u0432 \u0441\u0432\u043e\u0435\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438, \u0447\u0442\u043e \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u0438\u043c \u043d\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u0440\u043e\u0434\u0430\u0432\u0430\u0442\u044c, \u043d\u043e \u0438 \u043e\u0431\u0443\u0447\u0430\u0442\u044c \u0434\u0440\u0443"
                        "\u0433\u0438\u0445 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432, \u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u043e\u043f\u044b\u0442\u043e\u043c \u0438 \u0440\u0430\u0437\u0432\u0438\u0432\u0430\u0442\u044c \u043a\u043e\u043c\u0430\u043d\u0434\u043d\u044b\u0439 \u0434\u0443\u0445. \u042d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u043f\u0440\u0438\u0432\u0435\u0441\u0442\u0438 \u043a \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044e \u0431\u043e\u043b\u0435\u0435 \u0441\u043f\u043b\u043e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u043a\u043e\u043b\u043b\u0435\u043a\u0442\u0438\u0432\u0430, \u0433\u0434\u0435 \u043a\u0430\u0436\u0434\u044b\u0439 \u0447\u043b\u0435\u043d \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u0441\u0442\u0440\u0435\u043c\u0438\u0442\u0441\u044f \u043a \u043e\u0431\u0449\u0435\u0439 \u0446\u0435\u043b\u0438.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px"
                        "; font-size:13pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff;\">\u0420\u0430\u0431\u043e\u0442\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u043e\u043c \u0442\u0430\u043a\u0436\u0435 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u044d\u043c\u043e\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e rewarding. \u0423\u0441\u043f\u0435\u0448\u043d\u044b\u0435 \u043f\u0440\u043e\u0434\u0430\u0436\u0438 \u0438 \u0434\u043e\u0432\u043e\u043b\u044c\u043d\u044b\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u044b \u043f\u0440\u0438\u043d\u043e\u0441\u044f\u0442 \u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0435\u043d\u0438\u0435 \u0438 \u0447\u0443\u0432\u0441\u0442\u0432\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043e\u043b\u0433\u0430. \u041c\u043d\u043e\u0433\u0438"
                        "\u0435 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u043d\u0430\u0445\u043e\u0434\u044f\u0442 \u0440\u0430\u0434\u043e\u0441\u0442\u044c \u0432 \u0442\u043e\u043c, \u0447\u0442\u043e \u043c\u043e\u0433\u0443\u0442 \u043f\u043e\u043c\u043e\u0447\u044c \u043b\u044e\u0434\u044f\u043c \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u043c\u0435\u043d\u043d\u043e \u0442\u043e, \u0447\u0442\u043e \u0438\u043c \u043d\u0443\u0436\u043d\u043e, \u0438 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0438\u0445 \u0434\u0435\u043d\u044c \u043b\u0443\u0447\u0448\u0435.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff;\">\u0412\u0430\u0436\u043d\u043e\u0439 \u0447\u0430\u0441"
                        "\u0442\u044c\u044e \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u0441 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u044c\u044e \u043e\u0442 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432. \u0423\u043c\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u044c \u043a\u0440\u0438\u0442\u0438\u043a\u0443 \u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0435\u0435 \u0434\u043b\u044f \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044f \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0432\u0430\u0436\u043d\u044b\u043c \u043d\u0430\u0432\u044b\u043a\u043e\u043c. \u041f\u0440\u043e\u0434\u0430\u0432\u0446\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0430\u043a\u0442\u0438\u0432\u043d"
                        "\u043e \u0441\u043e\u0431\u0438\u0440\u0430\u044e\u0442 \u0438 \u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u044e\u0442 \u043e\u0442\u0437\u044b\u0432\u044b, \u043c\u043e\u0433\u0443\u0442 \u043d\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u043e\u0432\u044b\u0448\u0430\u0442\u044c \u0441\u0432\u043e\u0438 \u043b\u0438\u0447\u043d\u044b\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438, \u043d\u043e \u0438 \u0432\u043d\u043e\u0441\u0438\u0442\u044c \u0432\u043a\u043b\u0430\u0434 \u0432 \u043e\u0431\u0449\u0443\u044e \u0441\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u044e \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff;\">\u041d\u0430\u043a\u043e\u043d\u0435\u0446, \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u043c\u043e\u0436\u0435\u0442 \u0441\u0442\u0430\u0442\u044c \u043e\u0442\u043f\u0440\u0430\u0432\u043d\u043e\u0439 \u0442\u043e\u0447\u043a\u043e\u0439 \u0434\u043b\u044f \u043a\u0430\u0440\u044c\u0435\u0440\u044b \u0432 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u043e\u0431\u043b\u0430\u0441\u0442\u044f\u0445, \u0442\u0430\u043a\u0438\u0445 \u043a\u0430\u043a \u043c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433, \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u043d\u044b\u043c\u0438 \u0437\u0430\u043f\u0430\u0441\u0430\u043c\u0438 \u0438\u043b\u0438 \u0434\u0430\u0436\u0435 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e. \u041e\u043f\u044b\u0442 \u0440"
                        "\u0430\u0431\u043e\u0442\u044b \u0432 \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u0445 \u0434\u0430\u0435\u0442 \u043f\u043e\u043d\u0438\u043c\u0430\u043d\u0438\u0435 \u043f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0433\u043e \u043f\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f, \u0447\u0442\u043e \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0446\u0435\u043d\u043d\u044b\u043c \u0430\u043a\u0442\u0438\u0432\u043e\u043c \u0434\u043b\u044f \u0431\u0443\u0434\u0443\u0449\u0438\u0445 \u0431\u0438\u0437\u043d\u0435\u0441-\u0438\u043d\u0438\u0446\u0438\u0430\u0442\u0438\u0432.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff"
                        ";\">\u0422\u0430\u043a\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c, \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u0441\u043e\u0447\u0435\u0442\u0430\u0435\u0442 \u0432 \u0441\u0435\u0431\u0435 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0430\u0441\u043f\u0435\u043a\u0442\u043e\u0432: \u044d\u0442\u043e \u0438 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043a\u0430\u0440\u044c\u0435\u0440\u043d\u043e\u0433\u043e \u0440\u043e\u0441\u0442\u0430, \u0438 \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u0435 \u043b\u0438\u0447\u043d\u044b\u0445 \u043d\u0430\u0432\u044b\u043a\u043e\u0432, \u0438 \u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0435\u043d\u0438\u0435 \u043e\u0442 \u043f\u043e\u043c\u043e\u0449\u0438 \u043b\u044e\u0434\u044f\u043c. \u042d\u0442\u043e \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0451 \u043f\u0440\u0438\u0432\u043b\u0435\u043a\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0439"
                        " \u0434\u043b\u044f \u043c\u043d\u043e\u0433\u0438\u0445, \u043a\u0442\u043e \u0438\u0449\u0435\u0442 \u0434\u0438\u043d\u0430\u043c\u0438\u0447\u043d\u0443\u044e \u0438 \u0437\u043d\u0430\u0447\u0438\u043c\u0443\u044e \u0440\u0430\u0431\u043e\u0442\u0443.</span></p></body></html>", None))
    # retranslateUi

