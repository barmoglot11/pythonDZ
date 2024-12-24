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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame,
                               QGridLayout, QHBoxLayout, QListView,
                               QListWidget, QListWidgetItem, QLabel,
                               QLayout, QLineEdit, QMainWindow,
                               QPushButton, QScrollBar, QSizePolicy, QSpacerItem,
                               QTextBrowser, QVBoxLayout, QWidget, QFileDialog, QComboBox, QPlainTextEdit)

from Interface.Logo import *
from Interface.Icons import *


class Ui_TakeProfessionPage(object):
    def setupUi(self, TakeProfessionPage):
        if not TakeProfessionPage.objectName():
            TakeProfessionPage.setObjectName(u"TakeProfessionPage")
        TakeProfessionPage.resize(1920, 1110)
        TakeProfessionPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "font-family: Roboto;")
        self.takeProfessionPage = QWidget(TakeProfessionPage)
        self.takeProfessionPage.setObjectName(u"takeProfessionPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeProfessionPage.sizePolicy().hasHeightForWidth())
        self.takeProfessionPage.setSizePolicy(sizePolicy)
        self.takeProfessionPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.takeProfessionPage)
        self.verticalLayout_15.setSpacing(30)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 30)
        self.headerFrame = QFrame(self.takeProfessionPage)
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

        self.pushButton = QPushButton(self.headerFrame, clicked=lambda: TakeProfessionPage.ChangeUI(Ui_TakeProfessionNonePage()))
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

        self.pushButton_2 = QPushButton(self.headerFrame, clicked=lambda: TakeProfessionPage.ChangeUI(Ui_ClusterPage()))
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

        self.pushButton_3 = QPushButton(self.headerFrame,
                                        clicked=lambda: TakeProfessionPage.ChangeUI(Ui_ProfessionPage()))
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

        self.verticalLayout_15.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.title = QFrame(self.takeProfessionPage)
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

        self.pushButtonAddTags = QPushButton(self.title, clicked = lambda : TakeProfessionPage.CreatePopup("AddResume", PopUpAddResumePage()))
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
        self.pushButtonAddTags.setIconSize(QSize(24, 24))

        self.titleButton.addWidget(self.pushButtonAddTags)

        self.horizontalLayout_4.addLayout(self.titleButton)

        self.verticalLayout_15.addWidget(self.title, 0, Qt.AlignTop)

        self.vacancyFrame = QFrame(self.takeProfessionPage)
        self.vacancyFrame.setObjectName(u"vacancyFrame")
        self.vacancy = QVBoxLayout(self.vacancyFrame)
        self.vacancy.setSpacing(20)
        self.vacancy.setObjectName(u"vacancy")
        self.titleVacancy = QHBoxLayout()
        self.titleVacancy.setSpacing(20)
        self.titleVacancy.setObjectName(u"titleVacancy")
        self.titleVacancy.setContentsMargins(30, -1, 30, -1)
        self.title_3 = QLabel(self.vacancyFrame)
        self.title_3.setObjectName(u"title_3")
        sizePolicy1.setHeightForWidth(self.title_3.sizePolicy().hasHeightForWidth())
        self.title_3.setSizePolicy(sizePolicy1)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.title_3.setPalette(palette4)
        self.title_3.setFont(font1)
        self.title_3.setStyleSheet(u"color: rgb(80, 30, 188);")

        self.titleVacancy.addWidget(self.title_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.titleVacancy.addItem(self.horizontalSpacer_3)

        self.vacancy.addLayout(self.titleVacancy)

        self.professionFrame = QHBoxLayout()
        self.professionFrame.setSpacing(0)
        self.professionFrame.setObjectName(u"professionFrame")
        self.label_2 = QLabel(self.vacancyFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 0))
        self.label_2.setBaseSize(QSize(30, 0))

        self.professionFrame.addWidget(self.label_2)

        self.profession = QFrame(self.vacancyFrame)
        self.profession.setObjectName(u"profession")
        self.profession.setMinimumSize(QSize(1860, 306))
        self.profession.setMaximumSize(QSize(16667, 407))
        self.profession.setStyleSheet(u"QFrame {\n"
                                      "	border-right: 2px solid #E7E7E7;\n"
                                      "	border-bottom: 2px solid #E7E7E7;\n"
                                      "	border-radius: 10px;\n"
                                      "	background-color: rgb(255, 255, 255);\n"
                                      "}")
        self.verticalLayout = QVBoxLayout(self.profession)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.nameProfession = QHBoxLayout()
        self.nameProfession.setSpacing(20)
        self.nameProfession.setObjectName(u"nameProfession")
        self.nameButton = QPushButton(self.profession)
        self.nameButton.setObjectName(u"nameButton")
        self.nameButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.nameButton.sizePolicy().hasHeightForWidth())
        self.nameButton.setSizePolicy(sizePolicy1)
        self.nameButton.setMinimumSize(QSize(0, 40))
        self.nameButton.setMaximumSize(QSize(1000, 40))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton.setPalette(palette5)
        self.nameButton.setFont(font)
        self.nameButton.setLayoutDirection(Qt.RightToLeft)
        self.nameButton.setStyleSheet(u"QPushButton {\n"
                                      "	border: none;\n"
                                      "   color: #101010;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "	border-bottom: 4px solid #501EBC;\n"
                                      "	border-radius: 2px;\n"
                                      "}")
        self.nameButton.setAutoDefault(False)

        self.nameProfession.addWidget(self.nameButton)

        self.city = QHBoxLayout()
        self.city.setSpacing(10)
        self.city.setObjectName(u"city")
        self.iconCity = QPushButton(self.profession)
        self.iconCity.setObjectName(u"iconCity")
        self.iconCity.setMinimumSize(QSize(28, 28))
        self.iconCity.setMaximumSize(QSize(28, 28))
        self.iconCity.setStyleSheet(u"QAbstractButton {\n"
                                    "	border: none;\n"
                                    "	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
                                    "}")
        self.iconCity.setIconSize(QSize(24, 24))

        self.city.addWidget(self.iconCity)

        self.textCity = QLabel(self.profession)
        self.textCity.setObjectName(u"textCity")
        self.textCity.setMaximumSize(QSize(16777215, 20))
        palette6 = QPalette()
        brush3 = QBrush(QColor(91, 91, 91, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textCity.setPalette(palette6)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.textCity.setFont(font3)
        self.textCity.setStyleSheet(u"border: none;\n"
                                    "color: #5B5B5B;")

        self.city.addWidget(self.textCity)

        self.nameProfession.addLayout(self.city)

        self.money = QHBoxLayout()
        self.money.setSpacing(10)
        self.money.setObjectName(u"money")
        self.iconMoney = QPushButton(self.profession)
        self.iconMoney.setObjectName(u"iconMoney")
        self.iconMoney.setMinimumSize(QSize(28, 28))
        self.iconMoney.setMaximumSize(QSize(28, 30))
        self.iconMoney.setStyleSheet(u"QAbstractButton {\n"
                                     "	border: none;\n"
                                     "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                     "}")
        self.iconMoney.setIconSize(QSize(24, 24))

        self.money.addWidget(self.iconMoney)

        self.textMoney = QLabel(self.profession)
        self.textMoney.setObjectName(u"textMoney")
        self.textMoney.setMaximumSize(QSize(16777215, 20))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney.setPalette(palette7)
        self.textMoney.setFont(font3)
        self.textMoney.setStyleSheet(u"border: none;\n"
                                     "color: #5B5B5B;")

        self.money.addWidget(self.textMoney)

        self.nameProfession.addLayout(self.money)

        self.horizontalSpacer_5 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.nameProfession.addItem(self.horizontalSpacer_5)

        self.verticalLayout.addLayout(self.nameProfession)

        self.description = QVBoxLayout()
        self.description.setSpacing(5)
        self.description.setObjectName(u"description")
        self.titleDescription = QLabel(self.profession)
        self.titleDescription.setObjectName(u"titleDescription")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.titleDescription.setPalette(palette8)
        self.titleDescription.setFont(font2)
        self.titleDescription.setStyleSheet(u"border: none;")

        self.description.addWidget(self.titleDescription)

        self.textDescription = QTextBrowser(self.profession)
        self.textDescription.setObjectName(u"textDescription")
        self.textDescription.setStyleSheet(u"QFrame {\n"
                                           "	border: none;\n"
                                           "   color: #101010;\n"
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
                                           "	border-bottom-left-radiu"
                                           "s: 7px;\n"
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
        self.textDescription.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.description.addWidget(self.textDescription)

        self.verticalLayout.addLayout(self.description)

        self.professionFrame.addWidget(self.profession)

        self.label_3 = QLabel(self.vacancyFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setBaseSize(QSize(30, 0))

        self.professionFrame.addWidget(self.label_3)

        self.vacancy.addLayout(self.professionFrame)

        self.verticalLayout_15.addWidget(self.vacancyFrame, 0, Qt.AlignTop)

        self.otherVacancyFrame = QFrame(self.takeProfessionPage)
        self.otherVacancyFrame.setObjectName(u"otherVacancyFrame")
        self.otherVacancy = QVBoxLayout(self.otherVacancyFrame)
        self.otherVacancy.setSpacing(20)
        self.otherVacancy.setObjectName(u"otherVacancy")
        self.titleMoreVacancy = QHBoxLayout()
        self.titleMoreVacancy.setSpacing(20)
        self.titleMoreVacancy.setObjectName(u"titleMoreVacancy")
        self.titleMoreVacancy.setContentsMargins(30, -1, 30, -1)
        self.title_4 = QLabel(self.otherVacancyFrame)
        self.title_4.setObjectName(u"title_4")
        sizePolicy1.setHeightForWidth(self.title_4.sizePolicy().hasHeightForWidth())
        self.title_4.setSizePolicy(sizePolicy1)
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.title_4.setPalette(palette9)
        self.title_4.setFont(font1)
        self.title_4.setStyleSheet(u"color: rgb(80, 30, 188);")

        self.titleMoreVacancy.addWidget(self.title_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.titleMoreVacancy.addItem(self.horizontalSpacer_4)

        self.otherVacancy.addLayout(self.titleMoreVacancy)

        self.miniClustersFrame = QHBoxLayout()
        self.miniClustersFrame.setSpacing(20)
        self.miniClustersFrame.setObjectName(u"miniClustersFrame")
        self.miniClustersFrame.setContentsMargins(30, -1, 30, -1)
        self.miniClusters = QGridLayout()
        self.miniClusters.setSpacing(20)
        self.miniClusters.setObjectName(u"miniClusters")
        self.miniCluster_6 = QFrame(self.otherVacancyFrame)
        self.miniCluster_6.setObjectName(u"miniCluster_6")
        self.miniCluster_6.setMinimumSize(QSize(347, 104))
        self.miniCluster_6.setMaximumSize(QSize(347, 104))
        self.miniCluster_6.setStyleSheet(u"QFrame {\n"
                                         "	border-right: 2px solid #E7E7E7;\n"
                                         "	border-bottom: 2px solid #E7E7E7;\n"
                                         "	border-radius: 10px;\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.verticalLayout_6 = QVBoxLayout(self.miniCluster_6)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.nameButton_7 = QPushButton(self.miniCluster_6)
        self.nameButton_7.setObjectName(u"nameButton_7")
        sizePolicy1.setHeightForWidth(self.nameButton_7.sizePolicy().hasHeightForWidth())
        self.nameButton_7.setSizePolicy(sizePolicy1)
        self.nameButton_7.setMinimumSize(QSize(0, 30))
        self.nameButton_7.setMaximumSize(QSize(320, 30))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_7.setPalette(palette10)
        self.nameButton_7.setFont(font2)
        self.nameButton_7.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_7.setStyleSheet(u"QPushButton {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	border-bottom: 4px solid #501EBC;\n"
                                        "	border-radius: 2px;\n"
                                        "}")

        self.verticalLayout_6.addWidget(self.nameButton_7, 0, Qt.AlignLeft)

        self.money_6 = QHBoxLayout()
        self.money_6.setSpacing(10)
        self.money_6.setObjectName(u"money_6")
        self.iconMoney_6 = QPushButton(self.miniCluster_6)
        self.iconMoney_6.setObjectName(u"iconMoney_6")
        self.iconMoney_6.setMinimumSize(QSize(20, 20))
        self.iconMoney_6.setMaximumSize(QSize(20, 20))
        self.iconMoney_6.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_6.setIconSize(QSize(24, 24))

        self.money_6.addWidget(self.iconMoney_6)

        self.textMoney_6 = QLabel(self.miniCluster_6)
        self.textMoney_6.setObjectName(u"textMoney_6")
        self.textMoney_6.setMaximumSize(QSize(16777215, 20))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_6.setPalette(palette11)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.textMoney_6.setFont(font4)
        self.textMoney_6.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_6.addWidget(self.textMoney_6)

        self.verticalLayout_6.addLayout(self.money_6)

        self.miniClusters.addWidget(self.miniCluster_6, 0, 4, 1, 1)

        self.miniCluster_7 = QFrame(self.otherVacancyFrame)
        self.miniCluster_7.setObjectName(u"miniCluster_7")
        self.miniCluster_7.setMinimumSize(QSize(347, 104))
        self.miniCluster_7.setMaximumSize(QSize(347, 104))
        self.miniCluster_7.setStyleSheet(u"QFrame {\n"
                                         "	border-right: 2px solid #E7E7E7;\n"
                                         "	border-bottom: 2px solid #E7E7E7;\n"
                                         "	border-radius: 10px;\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.verticalLayout_7 = QVBoxLayout(self.miniCluster_7)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.nameButton_8 = QPushButton(self.miniCluster_7)
        self.nameButton_8.setObjectName(u"nameButton_8")
        sizePolicy1.setHeightForWidth(self.nameButton_8.sizePolicy().hasHeightForWidth())
        self.nameButton_8.setSizePolicy(sizePolicy1)
        self.nameButton_8.setMinimumSize(QSize(0, 30))
        self.nameButton_8.setMaximumSize(QSize(320, 30))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_8.setPalette(palette12)
        self.nameButton_8.setFont(font2)
        self.nameButton_8.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_8.setStyleSheet(u"QPushButton {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	border-bottom: 4px solid #501EBC;\n"
                                        "	border-radius: 2px;\n"
                                        "}")

        self.verticalLayout_7.addWidget(self.nameButton_8, 0, Qt.AlignLeft)

        self.money_7 = QHBoxLayout()
        self.money_7.setSpacing(10)
        self.money_7.setObjectName(u"money_7")
        self.iconMoney_7 = QPushButton(self.miniCluster_7)
        self.iconMoney_7.setObjectName(u"iconMoney_7")
        self.iconMoney_7.setMinimumSize(QSize(20, 20))
        self.iconMoney_7.setMaximumSize(QSize(20, 20))
        self.iconMoney_7.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_7.setIconSize(QSize(24, 24))

        self.money_7.addWidget(self.iconMoney_7)

        self.textMoney_7 = QLabel(self.miniCluster_7)
        self.textMoney_7.setObjectName(u"textMoney_7")
        self.textMoney_7.setMaximumSize(QSize(16777215, 20))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_7.setPalette(palette13)
        self.textMoney_7.setFont(font4)
        self.textMoney_7.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_7.addWidget(self.textMoney_7)

        self.verticalLayout_7.addLayout(self.money_7)

        self.miniClusters.addWidget(self.miniCluster_7, 1, 0, 1, 1)

        self.miniCluster_8 = QFrame(self.otherVacancyFrame)
        self.miniCluster_8.setObjectName(u"miniCluster_8")
        self.miniCluster_8.setMinimumSize(QSize(347, 104))
        self.miniCluster_8.setMaximumSize(QSize(347, 104))
        self.miniCluster_8.setStyleSheet(u"QFrame {\n"
                                         "	border-right: 2px solid #E7E7E7;\n"
                                         "	border-bottom: 2px solid #E7E7E7;\n"
                                         "	border-radius: 10px;\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.verticalLayout_9 = QVBoxLayout(self.miniCluster_8)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.nameButton_10 = QPushButton(self.miniCluster_8)
        self.nameButton_10.setObjectName(u"nameButton_10")
        sizePolicy1.setHeightForWidth(self.nameButton_10.sizePolicy().hasHeightForWidth())
        self.nameButton_10.setSizePolicy(sizePolicy1)
        self.nameButton_10.setMinimumSize(QSize(0, 30))
        self.nameButton_10.setMaximumSize(QSize(320, 30))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.Button, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_10.setPalette(palette14)
        self.nameButton_10.setFont(font2)
        self.nameButton_10.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_10.setStyleSheet(u"QPushButton {\n"
                                         "	border: none;\n"
                                         "   color: #101010;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "	border-bottom: 4px solid #501EBC;\n"
                                         "	border-radius: 2px;\n"
                                         "}")

        self.verticalLayout_9.addWidget(self.nameButton_10, 0, Qt.AlignLeft)

        self.money_9 = QHBoxLayout()
        self.money_9.setSpacing(10)
        self.money_9.setObjectName(u"money_9")
        self.iconMoney_9 = QPushButton(self.miniCluster_8)
        self.iconMoney_9.setObjectName(u"iconMoney_9")
        self.iconMoney_9.setMinimumSize(QSize(20, 20))
        self.iconMoney_9.setMaximumSize(QSize(20, 20))
        self.iconMoney_9.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_9.setIconSize(QSize(24, 24))

        self.money_9.addWidget(self.iconMoney_9)

        self.textMoney_9 = QLabel(self.miniCluster_8)
        self.textMoney_9.setObjectName(u"textMoney_9")
        self.textMoney_9.setMaximumSize(QSize(16777215, 20))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_9.setPalette(palette15)
        self.textMoney_9.setFont(font4)
        self.textMoney_9.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_9.addWidget(self.textMoney_9)

        self.verticalLayout_9.addLayout(self.money_9)

        self.miniClusters.addWidget(self.miniCluster_8, 1, 1, 1, 1)

        self.miniCluster_3 = QFrame(self.otherVacancyFrame)
        self.miniCluster_3.setObjectName(u"miniCluster_3")
        self.miniCluster_3.setMinimumSize(QSize(347, 104))
        self.miniCluster_3.setMaximumSize(QSize(347, 104))
        self.miniCluster_3.setStyleSheet(u"QFrame {\n"
                                         "	border-right: 2px solid #E7E7E7;\n"
                                         "	border-bottom: 2px solid #E7E7E7;\n"
                                         "	border-radius: 10px;\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.verticalLayout_3 = QVBoxLayout(self.miniCluster_3)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.nameButton_4 = QPushButton(self.miniCluster_3)
        self.nameButton_4.setObjectName(u"nameButton_4")
        sizePolicy1.setHeightForWidth(self.nameButton_4.sizePolicy().hasHeightForWidth())
        self.nameButton_4.setSizePolicy(sizePolicy1)
        self.nameButton_4.setMinimumSize(QSize(0, 30))
        self.nameButton_4.setMaximumSize(QSize(320, 30))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.Button, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_4.setPalette(palette16)
        self.nameButton_4.setFont(font2)
        self.nameButton_4.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_4.setStyleSheet(u"QPushButton {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	border-bottom: 4px solid #501EBC;\n"
                                        "	border-radius: 2px;\n"
                                        "}")

        self.verticalLayout_3.addWidget(self.nameButton_4, 0, Qt.AlignLeft)

        self.money_3 = QHBoxLayout()
        self.money_3.setSpacing(10)
        self.money_3.setObjectName(u"money_3")
        self.iconMoney_3 = QPushButton(self.miniCluster_3)
        self.iconMoney_3.setObjectName(u"iconMoney_3")
        self.iconMoney_3.setMinimumSize(QSize(20, 20))
        self.iconMoney_3.setMaximumSize(QSize(20, 20))
        self.iconMoney_3.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_3.setIconSize(QSize(24, 24))

        self.money_3.addWidget(self.iconMoney_3)

        self.textMoney_3 = QLabel(self.miniCluster_3)
        self.textMoney_3.setObjectName(u"textMoney_3")
        self.textMoney_3.setMaximumSize(QSize(16777215, 20))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_3.setPalette(palette17)
        self.textMoney_3.setFont(font4)
        self.textMoney_3.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_3.addWidget(self.textMoney_3)

        self.verticalLayout_3.addLayout(self.money_3)

        self.miniClusters.addWidget(self.miniCluster_3, 0, 1, 1, 1)

        self.miniCluster_2 = QFrame(self.otherVacancyFrame)
        self.miniCluster_2.setObjectName(u"miniCluster_2")
        self.miniCluster_2.setMinimumSize(QSize(347, 104))
        self.miniCluster_2.setMaximumSize(QSize(347, 104))
        self.miniCluster_2.setStyleSheet(u"QFrame {\n"
                                         "	border-right: 2px solid #E7E7E7;\n"
                                         "	border-bottom: 2px solid #E7E7E7;\n"
                                         "	border-radius: 10px;\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.verticalLayout_2 = QVBoxLayout(self.miniCluster_2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.nameButton_2 = QPushButton(self.miniCluster_2)
        self.nameButton_2.setObjectName(u"nameButton_2")
        sizePolicy1.setHeightForWidth(self.nameButton_2.sizePolicy().hasHeightForWidth())
        self.nameButton_2.setSizePolicy(sizePolicy1)
        self.nameButton_2.setMinimumSize(QSize(0, 30))
        self.nameButton_2.setMaximumSize(QSize(320, 30))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.Button, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_2.setPalette(palette18)
        self.nameButton_2.setFont(font2)
        self.nameButton_2.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_2.setStyleSheet(u"QPushButton {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	border-bottom: 4px solid #501EBC;\n"
                                        "	border-radius: 2px;\n"
                                        "}")

        self.verticalLayout_2.addWidget(self.nameButton_2, 0, Qt.AlignLeft)

        self.money_2 = QHBoxLayout()
        self.money_2.setSpacing(10)
        self.money_2.setObjectName(u"money_2")
        self.iconMoney_2 = QPushButton(self.miniCluster_2)
        self.iconMoney_2.setObjectName(u"iconMoney_2")
        self.iconMoney_2.setMinimumSize(QSize(20, 20))
        self.iconMoney_2.setMaximumSize(QSize(20, 20))
        self.iconMoney_2.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_2.setIconSize(QSize(24, 24))

        self.money_2.addWidget(self.iconMoney_2)

        self.textMoney_2 = QLabel(self.miniCluster_2)
        self.textMoney_2.setObjectName(u"textMoney_2")
        self.textMoney_2.setMaximumSize(QSize(16777215, 20))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_2.setPalette(palette19)
        self.textMoney_2.setFont(font4)
        self.textMoney_2.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_2.addWidget(self.textMoney_2)

        self.verticalLayout_2.addLayout(self.money_2)

        self.miniClusters.addWidget(self.miniCluster_2, 0, 0, 1, 1)

        self.miniCluster_9 = QFrame(self.otherVacancyFrame)
        self.miniCluster_9.setObjectName(u"miniCluster_9")
        self.miniCluster_9.setMinimumSize(QSize(347, 104))
        self.miniCluster_9.setMaximumSize(QSize(347, 104))
        self.miniCluster_9.setStyleSheet(u"QFrame {\n"
                                         "	border-right: 2px solid #E7E7E7;\n"
                                         "	border-bottom: 2px solid #E7E7E7;\n"
                                         "	border-radius: 10px;\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.verticalLayout_10 = QVBoxLayout(self.miniCluster_9)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 20, 20, 20)
        self.nameButton_11 = QPushButton(self.miniCluster_9)
        self.nameButton_11.setObjectName(u"nameButton_11")
        sizePolicy1.setHeightForWidth(self.nameButton_11.sizePolicy().hasHeightForWidth())
        self.nameButton_11.setSizePolicy(sizePolicy1)
        self.nameButton_11.setMinimumSize(QSize(0, 30))
        self.nameButton_11.setMaximumSize(QSize(320, 30))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.Button, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_11.setPalette(palette20)
        self.nameButton_11.setFont(font2)
        self.nameButton_11.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_11.setStyleSheet(u"QPushButton {\n"
                                         "	border: none;\n"
                                         "   color: #101010;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "	border-bottom: 4px solid #501EBC;\n"
                                         "	border-radius: 2px;\n"
                                         "}")

        self.verticalLayout_10.addWidget(self.nameButton_11, 0, Qt.AlignLeft)

        self.money_10 = QHBoxLayout()
        self.money_10.setSpacing(10)
        self.money_10.setObjectName(u"money_10")
        self.iconMoney_10 = QPushButton(self.miniCluster_9)
        self.iconMoney_10.setObjectName(u"iconMoney_10")
        self.iconMoney_10.setMinimumSize(QSize(20, 20))
        self.iconMoney_10.setMaximumSize(QSize(20, 20))
        self.iconMoney_10.setStyleSheet(u"QAbstractButton {\n"
                                        "	border: none;\n"
                                        "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                        "}")
        self.iconMoney_10.setIconSize(QSize(24, 24))

        self.money_10.addWidget(self.iconMoney_10)

        self.textMoney_10 = QLabel(self.miniCluster_9)
        self.textMoney_10.setObjectName(u"textMoney_10")
        self.textMoney_10.setMaximumSize(QSize(16777215, 20))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_10.setPalette(palette21)
        self.textMoney_10.setFont(font4)
        self.textMoney_10.setStyleSheet(u"border: none;\n"
                                        "color: #5B5B5B;")

        self.money_10.addWidget(self.textMoney_10)

        self.verticalLayout_10.addLayout(self.money_10)

        self.miniClusters.addWidget(self.miniCluster_9, 1, 2, 1, 1)

        self.miniCluster_10 = QFrame(self.otherVacancyFrame)
        self.miniCluster_10.setObjectName(u"miniCluster_10")
        self.miniCluster_10.setMinimumSize(QSize(347, 104))
        self.miniCluster_10.setMaximumSize(QSize(347, 104))
        self.miniCluster_10.setStyleSheet(u"QFrame {\n"
                                          "	border-right: 2px solid #E7E7E7;\n"
                                          "	border-bottom: 2px solid #E7E7E7;\n"
                                          "	border-radius: 10px;\n"
                                          "	background-color: rgb(255, 255, 255);\n"
                                          "}")
        self.verticalLayout_11 = QVBoxLayout(self.miniCluster_10)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 20, 20, 20)
        self.nameButton_12 = QPushButton(self.miniCluster_10)
        self.nameButton_12.setObjectName(u"nameButton_12")
        sizePolicy1.setHeightForWidth(self.nameButton_12.sizePolicy().hasHeightForWidth())
        self.nameButton_12.setSizePolicy(sizePolicy1)
        self.nameButton_12.setMinimumSize(QSize(0, 30))
        self.nameButton_12.setMaximumSize(QSize(320, 30))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.Button, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_12.setPalette(palette22)
        self.nameButton_12.setFont(font2)
        self.nameButton_12.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_12.setStyleSheet(u"QPushButton {\n"
                                         "	border: none;\n"
                                         "   color: #101010;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "	border-bottom: 4px solid #501EBC;\n"
                                         "	border-radius: 2px;\n"
                                         "}")

        self.verticalLayout_11.addWidget(self.nameButton_12, 0, Qt.AlignLeft)

        self.money_11 = QHBoxLayout()
        self.money_11.setSpacing(10)
        self.money_11.setObjectName(u"money_11")
        self.iconMoney_11 = QPushButton(self.miniCluster_10)
        self.iconMoney_11.setObjectName(u"iconMoney_11")
        self.iconMoney_11.setMinimumSize(QSize(20, 20))
        self.iconMoney_11.setMaximumSize(QSize(20, 20))
        self.iconMoney_11.setStyleSheet(u"QAbstractButton {\n"
                                        "	border: none;\n"
                                        "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                        "}")
        self.iconMoney_11.setIconSize(QSize(24, 24))

        self.money_11.addWidget(self.iconMoney_11)

        self.textMoney_11 = QLabel(self.miniCluster_10)
        self.textMoney_11.setObjectName(u"textMoney_11")
        self.textMoney_11.setMaximumSize(QSize(16777215, 20))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_11.setPalette(palette23)
        self.textMoney_11.setFont(font4)
        self.textMoney_11.setStyleSheet(u"border: none;\n"
                                        "color: #5B5B5B;")

        self.money_11.addWidget(self.textMoney_11)

        self.verticalLayout_11.addLayout(self.money_11)

        self.miniClusters.addWidget(self.miniCluster_10, 1, 3, 1, 1)

        self.miniCluster_11 = QFrame(self.otherVacancyFrame)
        self.miniCluster_11.setObjectName(u"miniCluster_11")
        self.miniCluster_11.setMinimumSize(QSize(347, 104))
        self.miniCluster_11.setMaximumSize(QSize(347, 104))
        self.miniCluster_11.setStyleSheet(u"QFrame {\n"
                                          "	border-right: 2px solid #E7E7E7;\n"
                                          "	border-bottom: 2px solid #E7E7E7;\n"
                                          "	border-radius: 10px;\n"
                                          "	background-color: rgb(255, 255, 255);\n"
                                          "}")
        self.verticalLayout_12 = QVBoxLayout(self.miniCluster_11)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.nameButton_13 = QPushButton(self.miniCluster_11)
        self.nameButton_13.setObjectName(u"nameButton_13")
        sizePolicy1.setHeightForWidth(self.nameButton_13.sizePolicy().hasHeightForWidth())
        self.nameButton_13.setSizePolicy(sizePolicy1)
        self.nameButton_13.setMinimumSize(QSize(0, 30))
        self.nameButton_13.setMaximumSize(QSize(320, 30))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.Button, brush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_13.setPalette(palette24)
        self.nameButton_13.setFont(font2)
        self.nameButton_13.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_13.setStyleSheet(u"QPushButton {\n"
                                         "	border: none;\n"
                                         "   color: #101010;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "	border-bottom: 4px solid #501EBC;\n"
                                         "	border-radius: 2px;\n"
                                         "}")

        self.verticalLayout_12.addWidget(self.nameButton_13, 0, Qt.AlignLeft)

        self.money_12 = QHBoxLayout()
        self.money_12.setSpacing(10)
        self.money_12.setObjectName(u"money_12")
        self.iconMoney_12 = QPushButton(self.miniCluster_11)
        self.iconMoney_12.setObjectName(u"iconMoney_12")
        self.iconMoney_12.setMinimumSize(QSize(20, 20))
        self.iconMoney_12.setMaximumSize(QSize(20, 20))
        self.iconMoney_12.setStyleSheet(u"QAbstractButton {\n"
                                        "	border: none;\n"
                                        "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                        "}")
        self.iconMoney_12.setIconSize(QSize(24, 24))

        self.money_12.addWidget(self.iconMoney_12)

        self.textMoney_12 = QLabel(self.miniCluster_11)
        self.textMoney_12.setObjectName(u"textMoney_12")
        self.textMoney_12.setMaximumSize(QSize(16777215, 20))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_12.setPalette(palette25)
        self.textMoney_12.setFont(font4)
        self.textMoney_12.setStyleSheet(u"border: none;\n"
                                        "color: #5B5B5B;")

        self.money_12.addWidget(self.textMoney_12)

        self.verticalLayout_12.addLayout(self.money_12)

        self.miniClusters.addWidget(self.miniCluster_11, 1, 4, 1, 1)

        self.miniCluster_5 = QFrame(self.otherVacancyFrame)
        self.miniCluster_5.setObjectName(u"miniCluster_5")
        self.miniCluster_5.setMinimumSize(QSize(347, 104))
        self.miniCluster_5.setMaximumSize(QSize(347, 104))
        self.miniCluster_5.setStyleSheet(u"QFrame {\n"
                                         "	border-right: 2px solid #E7E7E7;\n"
                                         "	border-bottom: 2px solid #E7E7E7;\n"
                                         "	border-radius: 10px;\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.verticalLayout_5 = QVBoxLayout(self.miniCluster_5)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.nameButton_6 = QPushButton(self.miniCluster_5)
        self.nameButton_6.setObjectName(u"nameButton_6")
        sizePolicy1.setHeightForWidth(self.nameButton_6.sizePolicy().hasHeightForWidth())
        self.nameButton_6.setSizePolicy(sizePolicy1)
        self.nameButton_6.setMinimumSize(QSize(0, 30))
        self.nameButton_6.setMaximumSize(QSize(320, 30))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.Button, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_6.setPalette(palette26)
        self.nameButton_6.setFont(font2)
        self.nameButton_6.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_6.setStyleSheet(u"QPushButton {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	border-bottom: 4px solid #501EBC;\n"
                                        "	border-radius: 2px;\n"
                                        "}")

        self.verticalLayout_5.addWidget(self.nameButton_6, 0, Qt.AlignLeft)

        self.money_5 = QHBoxLayout()
        self.money_5.setSpacing(10)
        self.money_5.setObjectName(u"money_5")
        self.iconMoney_5 = QPushButton(self.miniCluster_5)
        self.iconMoney_5.setObjectName(u"iconMoney_5")
        self.iconMoney_5.setMinimumSize(QSize(20, 20))
        self.iconMoney_5.setMaximumSize(QSize(20, 20))
        self.iconMoney_5.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_5.setIconSize(QSize(24, 24))

        self.money_5.addWidget(self.iconMoney_5)

        self.textMoney_5 = QLabel(self.miniCluster_5)
        self.textMoney_5.setObjectName(u"textMoney_5")
        self.textMoney_5.setMaximumSize(QSize(16777215, 20))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_5.setPalette(palette27)
        self.textMoney_5.setFont(font4)
        self.textMoney_5.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_5.addWidget(self.textMoney_5)

        self.verticalLayout_5.addLayout(self.money_5)

        self.miniClusters.addWidget(self.miniCluster_5, 0, 3, 1, 1)

        self.miniCluster_4 = QFrame(self.otherVacancyFrame)
        self.miniCluster_4.setObjectName(u"miniCluster_4")
        self.miniCluster_4.setMinimumSize(QSize(347, 104))
        self.miniCluster_4.setMaximumSize(QSize(347, 104))
        self.miniCluster_4.setStyleSheet(u"QFrame {\n"
                                         "	border-right: 2px solid #E7E7E7;\n"
                                         "	border-bottom: 2px solid #E7E7E7;\n"
                                         "	border-radius: 10px;\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.verticalLayout_4 = QVBoxLayout(self.miniCluster_4)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.nameButton_5 = QPushButton(self.miniCluster_4)
        self.nameButton_5.setObjectName(u"nameButton_5")
        sizePolicy1.setHeightForWidth(self.nameButton_5.sizePolicy().hasHeightForWidth())
        self.nameButton_5.setSizePolicy(sizePolicy1)
        self.nameButton_5.setMinimumSize(QSize(0, 30))
        self.nameButton_5.setMaximumSize(QSize(320, 30))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.Button, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_5.setPalette(palette28)
        self.nameButton_5.setFont(font2)
        self.nameButton_5.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_5.setStyleSheet(u"QPushButton {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	border-bottom: 4px solid #501EBC;\n"
                                        "	border-radius: 2px;\n"
                                        "}")

        self.verticalLayout_4.addWidget(self.nameButton_5, 0, Qt.AlignLeft)

        self.money_4 = QHBoxLayout()
        self.money_4.setSpacing(10)
        self.money_4.setObjectName(u"money_4")
        self.iconMoney_4 = QPushButton(self.miniCluster_4)
        self.iconMoney_4.setObjectName(u"iconMoney_4")
        self.iconMoney_4.setMinimumSize(QSize(20, 20))
        self.iconMoney_4.setMaximumSize(QSize(20, 20))
        self.iconMoney_4.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_4.setIconSize(QSize(24, 24))

        self.money_4.addWidget(self.iconMoney_4)

        self.textMoney_4 = QLabel(self.miniCluster_4)
        self.textMoney_4.setObjectName(u"textMoney_4")
        self.textMoney_4.setMaximumSize(QSize(16777215, 20))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_4.setPalette(palette29)
        self.textMoney_4.setFont(font4)
        self.textMoney_4.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_4.addWidget(self.textMoney_4)

        self.verticalLayout_4.addLayout(self.money_4)

        self.miniClusters.addWidget(self.miniCluster_4, 0, 2, 1, 1)

        self.miniCluster_12 = QFrame(self.otherVacancyFrame)
        self.miniCluster_12.setObjectName(u"miniCluster_12")
        self.miniCluster_12.setMinimumSize(QSize(347, 104))
        self.miniCluster_12.setMaximumSize(QSize(347, 104))
        self.miniCluster_12.setStyleSheet(u"QFrame {\n"
                                          "	border-right: 2px solid #E7E7E7;\n"
                                          "	border-bottom: 2px solid #E7E7E7;\n"
                                          "	border-radius: 10px;\n"
                                          "	background-color: rgb(255, 255, 255);\n"
                                          "}")
        self.verticalLayout_13 = QVBoxLayout(self.miniCluster_12)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.nameButton_14 = QPushButton(self.miniCluster_12)
        self.nameButton_14.setObjectName(u"nameButton_14")
        sizePolicy1.setHeightForWidth(self.nameButton_14.sizePolicy().hasHeightForWidth())
        self.nameButton_14.setSizePolicy(sizePolicy1)
        self.nameButton_14.setMinimumSize(QSize(0, 30))
        self.nameButton_14.setMaximumSize(QSize(320, 30))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.Button, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_14.setPalette(palette30)
        self.nameButton_14.setFont(font2)
        self.nameButton_14.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_14.setStyleSheet(u"QPushButton {\n"
                                         "	border: none;\n"
                                         "   color: #101010;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "	border-bottom: 4px solid #501EBC;\n"
                                         "	border-radius: 2px;\n"
                                         "}")

        self.verticalLayout_13.addWidget(self.nameButton_14, 0, Qt.AlignLeft)

        self.money_13 = QHBoxLayout()
        self.money_13.setSpacing(10)
        self.money_13.setObjectName(u"money_13")
        self.iconMoney_13 = QPushButton(self.miniCluster_12)
        self.iconMoney_13.setObjectName(u"iconMoney_13")
        self.iconMoney_13.setMinimumSize(QSize(20, 20))
        self.iconMoney_13.setMaximumSize(QSize(20, 20))
        self.iconMoney_13.setStyleSheet(u"QAbstractButton {\n"
                                        "	border: none;\n"
                                        "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                        "}")
        self.iconMoney_13.setIconSize(QSize(24, 24))

        self.money_13.addWidget(self.iconMoney_13)

        self.textMoney_13 = QLabel(self.miniCluster_12)
        self.textMoney_13.setObjectName(u"textMoney_13")
        self.textMoney_13.setMaximumSize(QSize(16777215, 20))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_13.setPalette(palette31)
        self.textMoney_13.setFont(font4)
        self.textMoney_13.setStyleSheet(u"border: none;\n"
                                        "color: #5B5B5B;")

        self.money_13.addWidget(self.textMoney_13)

        self.verticalLayout_13.addLayout(self.money_13)

        self.miniClusters.addWidget(self.miniCluster_12, 2, 0, 1, 1)

        self.miniCluster_13 = QFrame(self.otherVacancyFrame)
        self.miniCluster_13.setObjectName(u"miniCluster_13")
        self.miniCluster_13.setMinimumSize(QSize(347, 104))
        self.miniCluster_13.setMaximumSize(QSize(347, 104))
        self.miniCluster_13.setStyleSheet(u"QFrame {\n"
                                          "	border-right: 2px solid #E7E7E7;\n"
                                          "	border-bottom: 2px solid #E7E7E7;\n"
                                          "	border-radius: 10px;\n"
                                          "	background-color: rgb(255, 255, 255);\n"
                                          "}")
        self.verticalLayout_14 = QVBoxLayout(self.miniCluster_13)
        self.verticalLayout_14.setSpacing(15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(20, 20, 20, 20)
        self.nameButton_15 = QPushButton(self.miniCluster_13)
        self.nameButton_15.setObjectName(u"nameButton_15")
        sizePolicy1.setHeightForWidth(self.nameButton_15.sizePolicy().hasHeightForWidth())
        self.nameButton_15.setSizePolicy(sizePolicy1)
        self.nameButton_15.setMinimumSize(QSize(0, 30))
        self.nameButton_15.setMaximumSize(QSize(320, 30))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.Button, brush)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_15.setPalette(palette32)
        self.nameButton_15.setFont(font2)
        self.nameButton_15.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_15.setStyleSheet(u"QPushButton {\n"
                                         "	border: none;\n"
                                         "   color: #101010;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "	border-bottom: 4px solid #501EBC;\n"
                                         "	border-radius: 2px;\n"
                                         "}")

        self.verticalLayout_14.addWidget(self.nameButton_15, 0, Qt.AlignLeft)

        self.money_14 = QHBoxLayout()
        self.money_14.setSpacing(10)
        self.money_14.setObjectName(u"money_14")
        self.iconMoney_14 = QPushButton(self.miniCluster_13)
        self.iconMoney_14.setObjectName(u"iconMoney_14")
        self.iconMoney_14.setMinimumSize(QSize(20, 20))
        self.iconMoney_14.setMaximumSize(QSize(20, 20))
        self.iconMoney_14.setStyleSheet(u"QAbstractButton {\n"
                                        "	border: none;\n"
                                        "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                        "}")
        self.iconMoney_14.setIconSize(QSize(24, 24))

        self.money_14.addWidget(self.iconMoney_14)

        self.textMoney_14 = QLabel(self.miniCluster_13)
        self.textMoney_14.setObjectName(u"textMoney_14")
        self.textMoney_14.setMaximumSize(QSize(16777215, 20))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_14.setPalette(palette33)
        self.textMoney_14.setFont(font4)
        self.textMoney_14.setStyleSheet(u"border: none;\n"
                                        "color: #5B5B5B;")

        self.money_14.addWidget(self.textMoney_14)

        self.verticalLayout_14.addLayout(self.money_14)

        self.miniClusters.addWidget(self.miniCluster_13, 2, 1, 1, 1)

        self.miniClustersFrame.addLayout(self.miniClusters)

        self.verticalScrollBar = QScrollBar(self.otherVacancyFrame)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        palette34 = QPalette()
        brush4 = QBrush(QColor(231, 231, 231, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.verticalScrollBar.setPalette(palette34)
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

        self.miniClustersFrame.addWidget(self.verticalScrollBar)

        self.otherVacancy.addLayout(self.miniClustersFrame)

        self.verticalLayout_15.addWidget(self.otherVacancyFrame, 0, Qt.AlignTop)

        TakeProfessionPage.setCentralWidget(self.takeProfessionPage)

        self.retranslateUi(TakeProfessionPage)

        QMetaObject.connectSlotsByName(TakeProfessionPage)

    # setupUi

    def retranslateUi(self, TakeProfessionPage):
        TakeProfessionPage.setWindowTitle(QCoreApplication.translate("TakeProfessionPage", u"Ваша Вакансия", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("TakeProfessionPage",
                                                           u"Подобрать профессию",
                                                           None))
        self.pushButton_2.setText(
            QCoreApplication.translate("TakeProfessionPage", u"Кластеры", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("TakeProfessionPage", u"Профессии",
                                       None))
        self.title_2.setText(QCoreApplication.translate("TakeProfessionPage",
                                                        u"Подобрать профессию",
                                                        None))
        self.pushButtonAddTags.setText(QCoreApplication.translate("TakeProfessionPage",
                                                                  u"Загрузить новое резюме",
                                                                  None))
        self.title_3.setText(QCoreApplication.translate("TakeProfessionPage",
                                                        u"Ваша вакансия",
                                                        None))
        self.label_2.setText("")
        self.nameButton.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[0][3], None))
        self.iconCity.setText("")
        self.textCity.setText(QCoreApplication.translate("TakeProfessionPage", u"Омск", None))
        self.iconMoney.setText("")
        self.textMoney.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[0][-2] + " руб/мес",
                                       None))
        self.titleDescription.setText(
            QCoreApplication.translate("TakeProfessionPage", u"Описание", None))
        self.textDescription.setHtml(QCoreApplication.translate("TakeProfessionPage",
                                                                u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                "p, li { white-space: pre-wrap; }\n"
                                                                "</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">"+TakeProfessionPage.vacancy_info[0][4]+"</span></p></body></html>",
                                                                None))
        self.label_3.setText("")
        self.title_4.setText(QCoreApplication.translate("TakeProfessionPage",
                                                        u"Похожие вакансии",
                                                        None))
        self.nameButton_7.setText(QCoreApplication.translate("TakeProfessionPage",
                                                             TakeProfessionPage.vacancy_info[1][3],
                                                             None))
        self.iconMoney_6.setText("")
        self.textMoney_6.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[1][-2] + " руб/мес",
                                       None))
        self.nameButton_8.setText(QCoreApplication.translate("TakeProfessionPage",
                                                             TakeProfessionPage.vacancy_info[2][3],
                                                             None))
        self.iconMoney_7.setText("")
        self.textMoney_7.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[2][-2] + " руб/мес",
                                       None))
        self.nameButton_10.setText(QCoreApplication.translate("TakeProfessionPage",
                                                              TakeProfessionPage.vacancy_info[3][3],
                                                              None))
        self.iconMoney_9.setText("")
        self.textMoney_9.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[3][-2] + " руб/мес",
                                       None))
        self.nameButton_4.setText(QCoreApplication.translate("TakeProfessionPage",
                                                             TakeProfessionPage.vacancy_info[4][3],
                                                             None))
        self.iconMoney_3.setText("")
        self.textMoney_3.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[4][-2] + " руб/мес",
                                       None))
        self.nameButton_2.setText(QCoreApplication.translate("TakeProfessionPage",
                                                             TakeProfessionPage.vacancy_info[5][3],
                                                             None))
        self.iconMoney_2.setText("")
        self.textMoney_2.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[5][-2] + " руб/мес",
                                       None))
        self.nameButton_11.setText(QCoreApplication.translate("TakeProfessionPage",
                                                              TakeProfessionPage.vacancy_info[6][3],
                                                              None))
        self.iconMoney_10.setText("")
        self.textMoney_10.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[6][-2] + " руб/мес",
                                       None))
        self.nameButton_12.setText(QCoreApplication.translate("TakeProfessionPage",
                                                              TakeProfessionPage.vacancy_info[7][3],
                                                              None))
        self.iconMoney_11.setText("")
        self.textMoney_11.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[7][-2] + " руб/мес",
                                       None))
        self.nameButton_13.setText(QCoreApplication.translate("TakeProfessionPage",
                                                              TakeProfessionPage.vacancy_info[8][3],
                                                              None))
        self.iconMoney_12.setText("")
        self.textMoney_12.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[8][-2] + " руб/мес",
                                       None))
        self.nameButton_6.setText(QCoreApplication.translate("TakeProfessionPage",
                                                             TakeProfessionPage.vacancy_info[9][3],
                                                             None))
        self.iconMoney_5.setText("")
        self.textMoney_5.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[9][-2] + " руб/мес",
                                       None))
        self.nameButton_5.setText(QCoreApplication.translate("TakeProfessionPage",
                                                             TakeProfessionPage.vacancy_info[10][3],
                                                             None))
        self.iconMoney_4.setText("")
        self.textMoney_4.setText(
            QCoreApplication.translate("TakeProfessionPage", TakeProfessionPage.vacancy_info[10][-2] + " руб/мес",
                                       None))

    # retranslateUi
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

        self.pushButton = QPushButton(self.headerFrame,
                                      clicked=lambda: TakeProfessionNonePage.ChangeUI(Ui_TakeProfessionNonePage()))
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

        self.pushButton_2 = QPushButton(self.headerFrame,
                                        clicked=lambda: TakeProfessionNonePage.ChangeUI(Ui_ClusterPage()))
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

        self.pushButton_3 = QPushButton(self.headerFrame,
                                        clicked=lambda: TakeProfessionNonePage.ChangeUI(Ui_ProfessionPage()))
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

        self.pushButtonAddTags = QPushButton(self.title, clicked = lambda : TakeProfessionNonePage.CreatePopup("AddResume", PopUpAddResumePage()))
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
        self.downloadButton = QPushButton(self.download, clicked = lambda : TakeProfessionNonePage.load_file())
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
        TakeProfessionNonePage.setWindowTitle(
            QCoreApplication.translate("TakeProfessionNonePage", u"Ваша Вакансия", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("TakeProfessionNonePage",
                                                           u"Подобрать профессию",
                                                           None))
        self.pushButton_2.setText(
            QCoreApplication.translate("TakeProfessionNonePage", u"Кластеры",
                                       None))
        self.pushButton_3.setText(QCoreApplication.translate("TakeProfessionNonePage",
                                                             u"Профессии",
                                                             None))
        self.title_2.setText(QCoreApplication.translate("TakeProfessionNonePage",
                                                        u"Подобрать профессию",
                                                        None))
        self.pushButtonAddTags.setText(QCoreApplication.translate("TakeProfessionNonePage",
                                                                  u"Загрузить новое резюме",
                                                                  None))
        self.label_2.setText("")
        self.pushBigButton.setText("")
        self.text_1.setText(QCoreApplication.translate("TakeProfessionNonePage",
                                                       u"Здесь пока пусто :(",
                                                       None))
        self.text_2.setText(QCoreApplication.translate("TakeProfessionNonePage",
                                                       u"Загрузите новый файл резюме",
                                                       None))
        self.downloadButton.setText(QCoreApplication.translate("TakeProfessionNonePage",
                                                               u"Загрузить",
                                                               None))
        self.textFiles.setText(QCoreApplication.translate("TakeProfessionNonePage", u"*PDF, DOC, DOCX", None))
        self.label_3.setText("")

    # retranslateUi
class PopUpAddResumePage(object):
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
        self.downloadButton = QPushButton(self.download, clicked= lambda: PopUpProfessionChangePage.load_file())
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
        self.pushButtonYes = QPushButton(self.buttonsFrame, clicked = lambda : PopUpProfessionChangePage.load_data())
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

        self.pushButtonNo = QPushButton(self.buttonsFrame, clicked = lambda : PopUpProfessionChangePage.CloseWindow())
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

    def changeFileName(self, text):
        self.file.setText(QCoreApplication.translate("PopUpProfessionChangePage", text, None))

class Ui_ClusterPage(object):
    def setupUi(self, ClusterPage):
        if not ClusterPage.objectName():
            ClusterPage.setObjectName(u"ClusterPage")

        self.data = ClusterPage.TakeDataFromDB("Cluster")
        ClusterPage.resize(1920, 1142)
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
        self.verticalLayout_13 = QVBoxLayout(self.clusterPage)
        self.verticalLayout_13.setSpacing(30)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 30)
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

        self.pushButton = QPushButton(self.headerFrame, clicked = lambda: ClusterPage.ChangeUI(Ui_TakeProfessionNonePage()))
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

        self.pushButton_2 = QPushButton(self.headerFrame, clicked=lambda: ClusterPage.ChangeUI(Ui_ClusterPage()))
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

        self.pushButton_3 = QPushButton(self.headerFrame, clicked=lambda: ClusterPage.ChangeUI(Ui_ProfessionPage()))
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

        self.verticalLayout_13.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.titleFrame = QFrame(self.clusterPage)
        self.titleFrame.setObjectName(u"titleFrame")
        self.title = QHBoxLayout(self.titleFrame)
        self.title.setSpacing(0)
        self.title.setObjectName(u"title")
        self.title.setContentsMargins(30, 1, 30, -1)
        self.title_2 = QLabel(self.titleFrame)
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

        self.findCluster = QFrame(self.titleFrame)
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
                                     "   color: #101010;\n"
                                     "	border: 2px solid #5B5B5B;\n"
                                     "	border-radius: 10px;\n"
                                     "	padding-left: 20px;\n"
                                     "	padding-right: 20px;\n"
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

        self.verticalLayout_13.addWidget(self.titleFrame, 0, Qt.AlignTop)

        self.clustersFrame = QFrame(self.clusterPage)
        self.clustersFrame.setObjectName(u"clustersFrame")
        self.clusters = QHBoxLayout(self.clustersFrame)
        self.clusters.setSpacing(20)
        self.clusters.setObjectName(u"clusters")
        self.clusters.setContentsMargins(30, -1, 30, -1)
        self.gridClusters = QGridLayout()
        self.gridClusters.setObjectName(u"gridClusters")
        self.gridClusters.setHorizontalSpacing(22)
        self.gridClusters.setVerticalSpacing(20)
        self.clusterAdd = QFrame(self.clustersFrame)
        self.clusterAdd.setObjectName(u"clusterAdd")
        self.clusterAdd.setMinimumSize(QSize(346, 407))
        self.clusterAdd.setMaximumSize(QSize(346, 407))
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
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textAdd.setPalette(palette4)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.textAdd.setFont(font3)
        self.textAdd.setStyleSheet(u"border: none;")

        self.gridClusters.addWidget(self.clusterAdd, 1, 1, 1, 1)

        self.cluster = QFrame(self.clustersFrame)
        self.cluster.setObjectName(u"cluster")
        self.cluster.setMinimumSize(QSize(346, 407))
        self.cluster.setMaximumSize(QSize(346, 407))
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
        palette5 = QPalette()
        brush3 = QBrush(QColor(1, 1, 1, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName.setPalette(palette5)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setKerning(True)
        self.clusterName.setFont(font4)
        self.clusterName.setStyleSheet(u"border: none;")

        self.clusterButtons.addWidget(self.clusterName)

        self.buttons = QHBoxLayout()
        self.buttons.setSpacing(10)
        self.buttons.setObjectName(u"buttons")
        self.pushButtonRedact = QPushButton(self.cluster, clicked = lambda : ClusterPage.CreatePopup("ClusterEdit", Ui_PopUpClusterChangePage(), ID = 1))
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

        self.pushButtonDelete = QPushButton(self.cluster, clicked = lambda: ClusterPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
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
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vacancy = QLabel(self.cluster)
        self.vacancy.setObjectName(u"vacancy")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy.setPalette(palette6)
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.vacancy.setFont(font5)
        self.vacancy.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.vacancy)

        self.listWidget = QListWidget(self.cluster)
        self.assotiations = self.data[0][2].split(',')
        self.listWidget.setWordWrap(True)
        for text in self.assotiations:
            self.listWidget.addItem(text)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(302, 260))
        self.listWidget.setMaximumSize(QSize(302, 260))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.listWidget.setPalette(palette7)
        self.listWidget.setFont(font5)
        self.listWidget.setStyleSheet(u"QWidget {\n"
                                      "	border: none;\n"
                                      "   color: #101010;\n"
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
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty(u"showDropIndicator", False)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(4)

        self.verticalLayout.addWidget(self.listWidget)
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButtonMore = QPushButton(self.cluster, clicked = lambda :  ClusterPage.CreatePopup("Cluster", Ui_PopUpClusterPage(), ID = 1))
        self.pushButtonMore.setObjectName(u"pushButtonMore")
        sizePolicy1.setHeightForWidth(self.pushButtonMore.sizePolicy().hasHeightForWidth())
        self.pushButtonMore.setSizePolicy(sizePolicy1)
        self.pushButtonMore.setMinimumSize(QSize(0, 0))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore.setPalette(palette8)
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setUnderline(True)
        self.pushButtonMore.setFont(font6)
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

        self.cluster_4 = QFrame(self.clustersFrame)
        self.cluster_4.setObjectName(u"cluster_4")
        self.cluster_4.setMinimumSize(QSize(346, 407))
        self.cluster_4.setMaximumSize(QSize(346, 407))
        self.cluster_4.setStyleSheet(u"QFrame {\n"
                                     "	border-right: 2px solid #E7E7E7;\n"
                                     "	border-bottom: 2px solid #E7E7E7;\n"
                                     "	border-radius: 10px;\n"
                                     "}")
        self.verticalLayout_7 = QVBoxLayout(self.cluster_4)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_4 = QHBoxLayout()
        self.clusterButtons_4.setObjectName(u"clusterButtons_4")
        self.clusterName_4 = QLabel(self.cluster_4)
        self.clusterName_4.setObjectName(u"clusterName_4")
        self.clusterName_4.setMinimumSize(QSize(248, 0))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_4.setPalette(palette9)
        self.clusterName_4.setFont(font4)
        self.clusterName_4.setStyleSheet(u"border: none;")

        self.clusterButtons_4.addWidget(self.clusterName_4)

        self.buttons_4 = QHBoxLayout()
        self.buttons_4.setSpacing(10)
        self.buttons_4.setObjectName(u"buttons_4")
        self.pushButtonRedact_4 = QPushButton(self.cluster_4, clicked = lambda : ClusterPage.CreatePopup("ClusterEdit", Ui_PopUpClusterChangePage(), ID = 4))
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

        self.pushButtonDelete_4 = QPushButton(self.cluster_4, clicked = lambda: ClusterPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
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

        self.verticalLayout_7.addLayout(self.clusterButtons_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.vacancy_4 = QLabel(self.cluster_4)
        self.vacancy_4.setObjectName(u"vacancy_4")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_4.setPalette(palette10)
        self.vacancy_4.setFont(font5)
        self.vacancy_4.setStyleSheet(u"border: none;")

        self.verticalLayout_8.addWidget(self.vacancy_4)

        self.listWidget_4 = QListWidget(self.cluster)
        self.assotiations = self.data[3][2].split(',')
        self.listWidget_4.setWordWrap(True)
        for text in self.assotiations:
            self.listWidget_4.addItem(text)
        self.listWidget_4.setObjectName(u"listWidget")
        self.listWidget_4.setMinimumSize(QSize(302, 260))
        self.listWidget_4.setMaximumSize(QSize(302, 260))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.listWidget_4.setPalette(palette7)
        self.listWidget_4.setFont(font5)
        self.listWidget_4.setStyleSheet(u"QWidget {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
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
        self.listWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_4.setProperty(u"showDropIndicator", False)
        self.listWidget_4.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget_4.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget_4.setLayoutMode(QListView.SinglePass)
        self.listWidget_4.setSpacing(4)

        self.verticalLayout_8.addWidget(self.listWidget_4)
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.Button, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.pushButtonMore_4 = QPushButton(self.cluster_4, clicked = lambda : ClusterPage.CreatePopup("Cluster", Ui_PopUpClusterPage(), ID = 4))
        self.pushButtonMore_4.setObjectName(u"pushButtonMore_4")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_4.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_4.setSizePolicy(sizePolicy1)
        self.pushButtonMore_4.setMinimumSize(QSize(0, 0))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_4.setPalette(palette12)
        self.pushButtonMore_4.setFont(font6)
        self.pushButtonMore_4.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_7.addWidget(self.pushButtonMore_4, 0, Qt.AlignHCenter)

        self.gridClusters.addWidget(self.cluster_4, 0, 3, 1, 1)

        self.cluster_2 = QFrame(self.clustersFrame)
        self.cluster_2.setObjectName(u"cluster_2")
        self.cluster_2.setMinimumSize(QSize(346, 407))
        self.cluster_2.setMaximumSize(QSize(346, 407))
        self.cluster_2.setStyleSheet(u"QFrame {\n"
                                     "	border-right: 2px solid #E7E7E7;\n"
                                     "	border-bottom: 2px solid #E7E7E7;\n"
                                     "	border-radius: 10px;\n"
                                     "}")
        self.verticalLayout_3 = QVBoxLayout(self.cluster_2)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_2 = QHBoxLayout()
        self.clusterButtons_2.setObjectName(u"clusterButtons_2")
        self.clusterName_2 = QLabel(self.cluster_2)
        self.clusterName_2.setObjectName(u"clusterName_2")
        self.clusterName_2.setMinimumSize(QSize(248, 0))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_2.setPalette(palette13)
        self.clusterName_2.setFont(font4)
        self.clusterName_2.setStyleSheet(u"border: none;")

        self.clusterButtons_2.addWidget(self.clusterName_2)

        self.buttons_2 = QHBoxLayout()
        self.buttons_2.setSpacing(10)
        self.buttons_2.setObjectName(u"buttons_2")
        self.pushButtonRedact_2 = QPushButton(self.cluster_2, clicked = lambda : ClusterPage.CreatePopup("ClusterEdit", Ui_PopUpClusterChangePage(), ID = 2))
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

        self.pushButtonDelete_2 = QPushButton(self.cluster_2, clicked = lambda: ClusterPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
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

        self.verticalLayout_3.addLayout(self.clusterButtons_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.vacancy_2 = QLabel(self.cluster_2)
        self.vacancy_2.setObjectName(u"vacancy_2")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_2.setPalette(palette14)
        self.vacancy_2.setFont(font5)
        self.vacancy_2.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.vacancy_2)

        self.listWidget_2 = QListWidget(self.cluster)
        self.assotiations = self.data[1][2].split(',')
        self.listWidget_2.setWordWrap(True)
        for text in self.assotiations:
            self.listWidget_2.addItem(text)
        self.listWidget_2.setObjectName(u"listWidget")
        self.listWidget_2.setMinimumSize(QSize(302, 260))
        self.listWidget_2.setMaximumSize(QSize(302, 260))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.listWidget_2.setPalette(palette7)
        self.listWidget_2.setFont(font5)
        self.listWidget_2.setStyleSheet(u"QWidget {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
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
        self.listWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_2.setProperty(u"showDropIndicator", False)
        self.listWidget_2.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget_2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget_2.setLayoutMode(QListView.SinglePass)
        self.listWidget_2.setSpacing(4)

        self.verticalLayout_4.addWidget(self.listWidget_2)
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.Button, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.pushButtonMore_2 = QPushButton(self.cluster_2,clicked = lambda :  ClusterPage.CreatePopup("Cluster", Ui_PopUpClusterPage(), ID = 2))
        self.pushButtonMore_2.setObjectName(u"pushButtonMore_2")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_2.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_2.setSizePolicy(sizePolicy1)
        self.pushButtonMore_2.setMinimumSize(QSize(0, 0))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_2.setPalette(palette16)
        self.pushButtonMore_2.setFont(font6)
        self.pushButtonMore_2.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_3.addWidget(self.pushButtonMore_2, 0, Qt.AlignHCenter)

        self.gridClusters.addWidget(self.cluster_2, 0, 1, 1, 1)

        self.cluster_3 = QFrame(self.clustersFrame)
        self.cluster_3.setObjectName(u"cluster_3")
        self.cluster_3.setMinimumSize(QSize(346, 407))
        self.cluster_3.setMaximumSize(QSize(346, 407))
        self.cluster_3.setStyleSheet(u"QFrame {\n"
                                     "	border-right: 2px solid #E7E7E7;\n"
                                     "	border-bottom: 2px solid #E7E7E7;\n"
                                     "	border-radius: 10px;\n"
                                     "}")
        self.verticalLayout_5 = QVBoxLayout(self.cluster_3)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_3 = QHBoxLayout()
        self.clusterButtons_3.setObjectName(u"clusterButtons_3")
        self.clusterName_3 = QLabel(self.cluster_3)
        self.clusterName_3.setObjectName(u"clusterName_3")
        self.clusterName_3.setMinimumSize(QSize(248, 0))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_3.setPalette(palette17)
        self.clusterName_3.setFont(font4)
        self.clusterName_3.setStyleSheet(u"border: none;")

        self.clusterButtons_3.addWidget(self.clusterName_3)

        self.buttons_3 = QHBoxLayout()
        self.buttons_3.setSpacing(10)
        self.buttons_3.setObjectName(u"buttons_3")
        self.pushButtonRedact_3 = QPushButton(self.cluster_3, clicked = lambda : ClusterPage.CreatePopup("ClusterEdit", Ui_PopUpClusterChangePage(), ID = 3))
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

        self.pushButtonDelete_3 = QPushButton(self.cluster_3, clicked = lambda: ClusterPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
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

        self.verticalLayout_5.addLayout(self.clusterButtons_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.vacancy_3 = QLabel(self.cluster_3)
        self.vacancy_3.setObjectName(u"vacancy_3")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_3.setPalette(palette18)
        self.vacancy_3.setFont(font5)
        self.vacancy_3.setStyleSheet(u"border: none;")

        self.verticalLayout_6.addWidget(self.vacancy_3)

        self.listWidget_3 = QListWidget(self.cluster)
        self.assotiations = self.data[2][2].split(',')
        self.listWidget_3.setWordWrap(True)
        for text in self.assotiations:
            self.listWidget_3.addItem(text)
        self.listWidget_3.setObjectName(u"listWidget")
        self.listWidget_3.setMinimumSize(QSize(302, 260))
        self.listWidget_3.setMaximumSize(QSize(302, 260))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.listWidget_3.setPalette(palette7)
        self.listWidget_3.setFont(font5)
        self.listWidget_3.setStyleSheet(u"QWidget {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
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
        self.listWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_3.setProperty(u"showDropIndicator", False)
        self.listWidget_3.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget_3.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget_3.setLayoutMode(QListView.SinglePass)
        self.listWidget_3.setSpacing(4)

        self.verticalLayout_6.addWidget(self.listWidget_3)
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.Button, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.pushButtonMore_3 = QPushButton(self.cluster_3,clicked = lambda :  ClusterPage.CreatePopup("Cluster", Ui_PopUpClusterPage(), ID = 3))
        self.pushButtonMore_3.setObjectName(u"pushButtonMore_3")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_3.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_3.setSizePolicy(sizePolicy1)
        self.pushButtonMore_3.setMinimumSize(QSize(0, 0))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_3.setPalette(palette20)
        self.pushButtonMore_3.setFont(font6)
        self.pushButtonMore_3.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_5.addWidget(self.pushButtonMore_3, 0, Qt.AlignHCenter)

        self.gridClusters.addWidget(self.cluster_3, 0, 2, 1, 1)

        self.cluster_5 = QFrame(self.clustersFrame)
        self.cluster_5.setObjectName(u"cluster_5")
        self.cluster_5.setMinimumSize(QSize(346, 407))
        self.cluster_5.setMaximumSize(QSize(346, 407))
        self.cluster_5.setStyleSheet(u"QFrame {\n"
                                     "	border-right: 2px solid #E7E7E7;\n"
                                     "	border-bottom: 2px solid #E7E7E7;\n"
                                     "	border-radius: 10px;\n"
                                     "}")
        self.verticalLayout_9 = QVBoxLayout(self.cluster_5)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_5 = QHBoxLayout()
        self.clusterButtons_5.setObjectName(u"clusterButtons_5")
        self.clusterName_5 = QLabel(self.cluster_5)
        self.clusterName_5.setObjectName(u"clusterName_5")
        self.clusterName_5.setMinimumSize(QSize(248, 0))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_5.setPalette(palette21)
        self.clusterName_5.setFont(font4)
        self.clusterName_5.setStyleSheet(u"border: none;")

        self.clusterButtons_5.addWidget(self.clusterName_5)

        self.buttons_5 = QHBoxLayout()
        self.buttons_5.setSpacing(10)
        self.buttons_5.setObjectName(u"buttons_5")
        self.pushButtonRedact_5 = QPushButton(self.cluster_5, clicked = lambda : ClusterPage.CreatePopup("ClusterEdit", Ui_PopUpClusterChangePage(), ID = 5))
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

        self.pushButtonDelete_5 = QPushButton(self.cluster_5, clicked = lambda: ClusterPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
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

        self.verticalLayout_9.addLayout(self.clusterButtons_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.vacancy_5 = QLabel(self.cluster_5)
        self.vacancy_5.setObjectName(u"vacancy_5")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_5.setPalette(palette22)
        self.vacancy_5.setFont(font5)
        self.vacancy_5.setStyleSheet(u"border: none;")

        self.verticalLayout_10.addWidget(self.vacancy_5)

        self.listWidget_5 = QListWidget(self.cluster)
        self.assotiations = self.data[4][2].split(',')
        self.listWidget_5.setWordWrap(True)
        for text in self.assotiations:
            self.listWidget_5.addItem(text)
        self.listWidget_5.setObjectName(u"listWidget")
        self.listWidget_5.setMinimumSize(QSize(302, 260))
        self.listWidget_5.setMaximumSize(QSize(302, 260))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.listWidget_5.setPalette(palette7)
        self.listWidget_5.setFont(font5)
        self.listWidget_5.setStyleSheet(u"QWidget {\n"
                                        "	border: none;\n"
                                        "   color: #101010;\n"
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
        self.listWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_5.setProperty(u"showDropIndicator", False)
        self.listWidget_5.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget_5.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget_5.setLayoutMode(QListView.SinglePass)
        self.listWidget_5.setSpacing(4)

        self.verticalLayout_10.addWidget(self.listWidget_5)
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.Button, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.pushButtonMore_5 = QPushButton(self.cluster_5,clicked = lambda :  ClusterPage.CreatePopup("Cluster", Ui_PopUpClusterPage(), ID = 5))
        self.pushButtonMore_5.setObjectName(u"pushButtonMore_5")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_5.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_5.setSizePolicy(sizePolicy1)
        self.pushButtonMore_5.setMinimumSize(QSize(0, 0))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_5.setPalette(palette24)
        self.pushButtonMore_5.setFont(font6)
        self.pushButtonMore_5.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_9.addWidget(self.pushButtonMore_5, 0, Qt.AlignHCenter)

        self.gridClusters.addWidget(self.cluster_5, 0, 4, 1, 1)

        self.cluster_6 = QFrame(self.clustersFrame)
        self.cluster_6.setObjectName(u"cluster_6")
        self.cluster_6.setMinimumSize(QSize(346, 407))
        self.cluster_6.setMaximumSize(QSize(346, 407))
        self.cluster_6.setStyleSheet(u"QFrame {\n"
                                     "	border-right: 2px solid #E7E7E7;\n"
                                     "	border-bottom: 2px solid #E7E7E7;\n"
                                     "	border-radius: 10px;\n"
                                     "}")
        self.verticalLayout_11 = QVBoxLayout(self.cluster_6)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 20, 20, 20)
        self.clusterButtons_6 = QHBoxLayout()
        self.clusterButtons_6.setObjectName(u"clusterButtons_6")
        self.clusterName_6 = QLabel(self.cluster_6)
        self.clusterName_6.setObjectName(u"clusterName_6")
        self.clusterName_6.setMinimumSize(QSize(248, 0))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.clusterName_6.setPalette(palette25)
        self.clusterName_6.setFont(font4)
        self.clusterName_6.setStyleSheet(u"border: none;")

        self.clusterButtons_6.addWidget(self.clusterName_6)

        self.buttons_6 = QHBoxLayout()
        self.buttons_6.setSpacing(10)
        self.buttons_6.setObjectName(u"buttons_6")
        self.pushButtonRedact_6 = QPushButton(self.cluster_6, clicked = lambda : ClusterPage.CreatePopup("ClusterEdit", Ui_PopUpClusterChangePage(), ID = 6))
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

        self.pushButtonDelete_6 = QPushButton(self.cluster_6, clicked = lambda: ClusterPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
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

        self.verticalLayout_11.addLayout(self.clusterButtons_6)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.vacancy_6 = QLabel(self.cluster_6)
        self.vacancy_6.setObjectName(u"vacancy_6")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vacancy_6.setPalette(palette26)
        self.vacancy_6.setFont(font5)
        self.vacancy_6.setStyleSheet(u"border: none;")

        self.verticalLayout_12.addWidget(self.vacancy_6)

        self.listWidget_6 = QListWidget(self.cluster)
        self.assotiations = self.data[5][2].split(',')
        self.listWidget_6.setWordWrap(True)
        for text in self.assotiations:
            self.listWidget_6.addItem(text)
        self.listWidget_6.setObjectName(u"listWidget")
        self.listWidget_6.setMinimumSize(QSize(302, 260))
        self.listWidget_6.setMaximumSize(QSize(302, 260))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.listWidget_6.setPalette(palette7)
        self.listWidget_6.setFont(font5)
        self.listWidget_6.setStyleSheet(u"QWidget {\n"
                                      "	border: none;\n"
                                      "   color: #101010;\n"
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
        self.listWidget_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_6.setProperty(u"showDropIndicator", False)
        self.listWidget_6.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget_6.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget_6.setLayoutMode(QListView.SinglePass)
        self.listWidget_6.setSpacing(4)

        self.verticalLayout_12.addWidget(self.listWidget_6)
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.Button, brush)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.pushButtonMore_6 = QPushButton(self.cluster_6,clicked = lambda :  ClusterPage.CreatePopup("Cluster", Ui_PopUpClusterPage(), ID = 6))
        self.pushButtonMore_6.setObjectName(u"pushButtonMore_6")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_6.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_6.setSizePolicy(sizePolicy1)
        self.pushButtonMore_6.setMinimumSize(QSize(0, 0))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_6.setPalette(palette28)
        self.pushButtonMore_6.setFont(font6)
        self.pushButtonMore_6.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_11.addWidget(self.pushButtonMore_6, 0, Qt.AlignHCenter)

        self.gridClusters.addWidget(self.cluster_6, 1, 0, 1, 1)

        self.clusters.addLayout(self.gridClusters)

        self.verticalScrollBar = QScrollBar(self.clustersFrame)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        palette29 = QPalette()
        brush4 = QBrush(QColor(231, 231, 231, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.verticalScrollBar.setPalette(palette29)
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

        self.verticalLayout_13.addWidget(self.clustersFrame, 0, Qt.AlignTop)

        ClusterPage.setCentralWidget(self.clusterPage)

        self.retranslateUi(ClusterPage)

        QMetaObject.connectSlotsByName(ClusterPage)

    # setupUi

    def retranslateUi(self, ClusterPage):
        DB_data = ClusterPage.TakeDataFromDB("Cluster")


        ClusterPage.setWindowTitle(QCoreApplication.translate("ClusterPage", u"Ваша Вакансия", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("ClusterPage",
                                                           u"Подобрать профессию",
                                                           None))
        self.pushButton_2.setText(
            QCoreApplication.translate("ClusterPage", u"Кластеры", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("ClusterPage", u"Профессии", None))
        self.title_2.setText(
            QCoreApplication.translate("ClusterPage", u"Кластеры", None))
        self.findInput.setText("")
        self.findInput.setPlaceholderText(QCoreApplication.translate("ClusterPage",
                                                                     u"Введите название кластера",
                                                                     None))
        self.pushButtonFind.setText("")
        self.pushButtonAdd.setText("")
        self.textAdd.setText(QCoreApplication.translate("ClusterPage",
                                                        u"Добавить новый кластер",
                                                        None))
        self.clusterName.setText(
            QCoreApplication.translate("ClusterPage", DB_data[0][1], None))
        self.pushButtonRedact.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.vacancy.setText(
            QCoreApplication.translate("ClusterPage", u"Вакансии", None))

        self.pushButtonMore.setText(QCoreApplication.translate("ClusterPage",
                                                               u"Показать ещё",
                                                               None))
        self.clusterName_4.setText(
            QCoreApplication.translate("ClusterPage", DB_data[3][1], None))
        self.pushButtonRedact_4.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_4.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_4.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_4.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.vacancy_4.setText(
            QCoreApplication.translate("ClusterPage", u"Вакансии", None))

        self.pushButtonMore_4.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"Показать ещё",
                                                                 None))
        self.clusterName_2.setText(
            QCoreApplication.translate("ClusterPage", DB_data[1][1], None))
        self.pushButtonRedact_2.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_2.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_2.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_2.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.vacancy_2.setText(
            QCoreApplication.translate("ClusterPage", u"Вакансии", None))


        self.pushButtonMore_2.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"Показать ещё",
                                                                 None))
        self.clusterName_3.setText(
            QCoreApplication.translate("ClusterPage", DB_data[2][1], None))
        self.pushButtonRedact_3.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_3.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_3.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_3.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.vacancy_3.setText(
            QCoreApplication.translate("ClusterPage", u"Вакансии", None))


        self.pushButtonMore_3.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"Показать ещё",
                                                                 None))
        self.clusterName_5.setText(
            QCoreApplication.translate("ClusterPage", DB_data[4][1], None))
        self.pushButtonRedact_5.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_5.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_5.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_5.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.vacancy_5.setText(
            QCoreApplication.translate("ClusterPage", u"Вакансии", None))


        self.pushButtonMore_5.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"Показать ещё",
                                                                 None))
        self.clusterName_6.setText(
            QCoreApplication.translate("ClusterPage", DB_data[5][1], None))
        self.pushButtonRedact_6.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_6.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_6.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_6.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.vacancy_6.setText(
            QCoreApplication.translate("ClusterPage", u"Вакансии", None))

        self.pushButtonMore_6.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"Показать ещё",
                                                                 None))

    # retranslateUi
class Ui_PopUpClusterPage(object):
    def setupUi(self, PopUpClusterPage):
        if not PopUpClusterPage.objectName():
            PopUpClusterPage.setObjectName(u"PopUpClusterPage")
        self.data = PopUpClusterPage.data[0]
        PopUpClusterPage.resize(1380, 680)
        PopUpClusterPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.popUpClusterPage = QWidget(PopUpClusterPage)
        self.popUpClusterPage.setObjectName(u"popUpClusterPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popUpClusterPage.sizePolicy().hasHeightForWidth())
        self.popUpClusterPage.setSizePolicy(sizePolicy)
        self.popUpClusterPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.popUpClusterPage)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.name = QHBoxLayout()
        self.name.setSpacing(0)
        self.name.setObjectName(u"name")
        self.title = QHBoxLayout()
        self.title.setSpacing(15)
        self.title.setObjectName(u"title")
        self.titleName = QLabel(self.popUpClusterPage)
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

        self.pushButtonRedact = QPushButton(self.popUpClusterPage, clicked = lambda : PopUpClusterPage.CreatePopup("ClusterEdit", Ui_PopUpClusterChangePage(), ID = PopUpClusterPage.ID))
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

        self.pushButtonDelete = QPushButton(self.popUpClusterPage, clicked = lambda : PopUpClusterPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
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

        self.pushButtonClose = QPushButton(self.popUpClusterPage, clicked = lambda : PopUpClusterPage.CloseWindow())
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


        self.verticalLayout_2.addLayout(self.name)

        self.description = QVBoxLayout()
        self.description.setSpacing(10)
        self.description.setObjectName(u"description")
        self.vacancy = QLabel(self.popUpClusterPage)
        self.vacancy.setObjectName(u"vacancy")
        sizePolicy1.setHeightForWidth(self.vacancy.sizePolicy().hasHeightForWidth())
        self.vacancy.setSizePolicy(sizePolicy1)
        self.vacancy.setMinimumSize(QSize(0, 30))
        self.vacancy.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.vacancy.setFont(font2)
        self.vacancy.setStyleSheet(u"color: #501EBC;")

        self.description.addWidget(self.vacancy)

        self.listWidget = QListWidget(self.popUpClusterPage)
        for item in self.data[2].split(','):
            self.listWidget.addItem(item)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(1320, 510))
        self.listWidget.setMaximumSize(QSize(1320, 510))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.listWidget.setPalette(palette1)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.listWidget.setFont(font3)
        self.listWidget.setStyleSheet(u"QWidget {\n"
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
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty(u"showDropIndicator", False)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(4)

        self.description.addWidget(self.listWidget)


        self.verticalLayout_2.addLayout(self.description)

        PopUpClusterPage.setCentralWidget(self.popUpClusterPage)

        self.retranslateUi(PopUpClusterPage)

        QMetaObject.connectSlotsByName(PopUpClusterPage)
    # setupUi

    def retranslateUi(self, PopUpClusterPage):
        PopUpClusterPage.setWindowTitle(QCoreApplication.translate("PopUpClusterPage", u"Your Vacancy", None))
        self.titleName.setText(QCoreApplication.translate("PopUpClusterPage", self.data[1], None))
        self.pushButtonRedact.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonClose.setText("")
        self.vacancy.setText(QCoreApplication.translate("PopUpClusterPage", u"Вакансии", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)


    # retranslateUi
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
        self.pushButtonYes = QPushButton(self.buttonsFrame, clicked = lambda : PopUpClusterChangePage.CreatePopup("Apply", Ui_PopUpSaveAttentionPage()))
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

        self.pushButtonNo = QPushButton(self.buttonsFrame, clicked = lambda : PopUpClusterChangePage.close())
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

    def Save(self):
        return self.input.text()
    # Save

class Ui_ProfessionPage(object):

    def setupUi(self, ProfessionPage):
        if not ProfessionPage.objectName():
            ProfessionPage.setObjectName(u"ProfessionPage")

        DB_data = ProfessionPage.TakeDataFromDB("Vacancy")
        self.vacancies = list()
        for data in DB_data:
            self.vacancies.append([data[3], data[4], data[1], data[-2], data[-3], data[0]])

        ProfessionPage.resize(1920, 1134)
        ProfessionPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                     "font-family: Roboto;")
        self.professionPage = QWidget(ProfessionPage)
        self.professionPage.setObjectName(u"professionPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.professionPage.sizePolicy().hasHeightForWidth())
        self.professionPage.setSizePolicy(sizePolicy)
        self.professionPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.professionPage)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 30)
        self.headerFrame = QFrame(self.professionPage)
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

        self.pushButton = QPushButton(self.headerFrame, clicked=lambda: ProfessionPage.ChangeUI(Ui_TakeProfessionNonePage()))
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

        self.pushButton_2 = QPushButton(self.headerFrame, clicked=lambda: ProfessionPage.ChangeUI(Ui_ClusterPage()))
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

        self.pushButton_3 = QPushButton(self.headerFrame, clicked=lambda: ProfessionPage.ChangeUI(Ui_ProfessionPage()))
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

        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.title = QFrame(self.professionPage)
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

        self.horizontalLayout_4.addLayout(self.titleButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.find = QFrame(self.title)
        self.find.setObjectName(u"find")
        self.horizontalLayout_2 = QHBoxLayout(self.find)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.findInput = QLineEdit(self.find)
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
                                     "   color: #101010;\n"
                                     "	border: 2px solid #5B5B5B;\n"
                                     "	border-radius: 10px;\n"
                                     "	padding-left: 20px;\n"
                                     "	padding-right: 20px;\n"
                                     "}")

        self.horizontalLayout_2.addWidget(self.findInput)

        self.pushButtonFind = QPushButton(self.find)
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

        self.horizontalLayout_4.addWidget(self.find)

        self.verticalLayout.addWidget(self.title, 0, Qt.AlignTop)

        self.professionsFrame = QFrame(self.professionPage)
        self.professionsFrame.setObjectName(u"professionsFrame")
        self.professionsFrame.setStyleSheet(u"background-color: none;")
        self.professions = QHBoxLayout(self.professionsFrame)
        self.professions.setSpacing(20)
        self.professions.setObjectName(u"professions")
        self.professions.setContentsMargins(30, -1, 30, -1)
        self.gridProfessions = QGridLayout()
        self.gridProfessions.setObjectName(u"gridProfessions")
        self.gridProfessions.setHorizontalSpacing(22)
        self.gridProfessions.setVerticalSpacing(20)
        self.profession = QFrame(self.professionsFrame)
        self.profession.setObjectName(u"profession")
        self.profession.setMinimumSize(QSize(346, 407))
        self.profession.setMaximumSize(QSize(346, 407))
        self.profession.setStyleSheet(u"QFrame {\n"
                                      "	border-right: 2px solid #E7E7E7;\n"
                                      "	border-bottom: 2px solid #E7E7E7;\n"
                                      "	border-radius: 10px;\n"
                                      "	background-color: rgb(255, 255, 255);\n"
                                      "}")
        self.verticalLayout_6 = QVBoxLayout(self.profession)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.professionButtons = QHBoxLayout()
        self.professionButtons.setObjectName(u"professionButtons")
        self.professionName = QLabel(self.profession)
        self.professionName.setObjectName(u"professionName")
        self.professionName.setMinimumSize(QSize(248, 0))
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
        self.professionName.setPalette(palette4)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setKerning(True)
        self.professionName.setFont(font3)
        self.professionName.setStyleSheet(u"border: none;")

        self.professionButtons.addWidget(self.professionName)

        self.buttons = QHBoxLayout()
        self.buttons.setSpacing(10)
        self.buttons.setObjectName(u"buttons")
        self.pushButtonRedact = QPushButton(self.profession, clicked = lambda : ProfessionPage.CreatePopup("ProfessionEdit", Ui_PopUpProfessionChangePage(), ID = 1))
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

        self.pushButtonDelete = QPushButton(self.profession, clicked = lambda : ProfessionPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
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

        self.professionButtons.addLayout(self.buttons)

        self.verticalLayout_6.addLayout(self.professionButtons)

        self.professionInfo = QVBoxLayout()
        self.professionInfo.setSpacing(10)
        self.professionInfo.setObjectName(u"professionInfo")
        self.city = QHBoxLayout()
        self.city.setSpacing(10)
        self.city.setObjectName(u"city")
        self.iconCity = QPushButton(self.profession)
        self.iconCity.setObjectName(u"iconCity")
        self.iconCity.setMinimumSize(QSize(20, 20))
        self.iconCity.setMaximumSize(QSize(20, 20))
        self.iconCity.setStyleSheet(u"QAbstractButton {\n"
                                    "	border: none;\n"
                                    "	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
                                    "}")
        self.iconCity.setIconSize(QSize(24, 24))

        self.city.addWidget(self.iconCity)

        self.textCity = QLabel(self.profession)
        self.textCity.setObjectName(u"textCity")
        self.textCity.setMaximumSize(QSize(16777215, 20))
        palette5 = QPalette()
        brush4 = QBrush(QColor(91, 91, 91, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textCity.setPalette(palette5)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.textCity.setFont(font4)
        self.textCity.setStyleSheet(u"border: none;\n"
                                    "color: #5B5B5B;")

        self.city.addWidget(self.textCity)

        self.professionInfo.addLayout(self.city)

        self.money = QHBoxLayout()
        self.money.setSpacing(10)
        self.money.setObjectName(u"money")
        self.iconMoney = QPushButton(self.profession)
        self.iconMoney.setObjectName(u"iconMoney")
        self.iconMoney.setMinimumSize(QSize(20, 20))
        self.iconMoney.setMaximumSize(QSize(20, 20))
        self.iconMoney.setStyleSheet(u"QAbstractButton {\n"
                                     "	border: none;\n"
                                     "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                     "}")
        self.iconMoney.setIconSize(QSize(24, 24))

        self.money.addWidget(self.iconMoney)

        self.textMoney = QLabel(self.profession)
        self.textMoney.setObjectName(u"textMoney")
        self.textMoney.setMaximumSize(QSize(16777215, 20))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney.setPalette(palette6)
        self.textMoney.setFont(font4)
        self.textMoney.setStyleSheet(u"border: none;\n"
                                     "color: #5B5B5B;")

        self.money.addWidget(self.textMoney)

        self.professionInfo.addLayout(self.money)

        self.description = QVBoxLayout()
        self.description.setSpacing(5)
        self.description.setObjectName(u"description")
        self.titleDescription = QLabel(self.profession)
        self.titleDescription.setObjectName(u"titleDescription")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.titleDescription.setPalette(palette7)
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.titleDescription.setFont(font5)
        self.titleDescription.setStyleSheet(u"border: none;")

        self.description.addWidget(self.titleDescription)

        self.textDescription = QTextBrowser(self.profession)
        self.textDescription.setObjectName(u"textDescription")
        self.textDescription.setStyleSheet(u"QWidget {\n"
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

        self.professionInfo.addLayout(self.description)

        self.verticalLayout_6.addLayout(self.professionInfo)

        self.pushButtonMore = QPushButton(self.profession, clicked = lambda : ProfessionPage.CreatePopup("Profession", Ui_PopUpProfessionPage(), ID = 1))
        self.pushButtonMore.setObjectName(u"pushButtonMore")
        sizePolicy1.setHeightForWidth(self.pushButtonMore.sizePolicy().hasHeightForWidth())
        self.pushButtonMore.setSizePolicy(sizePolicy1)
        self.pushButtonMore.setMinimumSize(QSize(0, 0))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore.setPalette(palette8)
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setUnderline(True)
        self.pushButtonMore.setFont(font6)
        self.pushButtonMore.setStyleSheet(u"QAbstractButton {\n"
                                          "	border: none;\n"
                                          "	color: #010101;\n"
                                          "}\n"
                                          "\n"
                                          "QAbstractButton:hover {\n"
                                          "	color: #501EBC;\n"
                                          "}")

        self.verticalLayout_6.addWidget(self.pushButtonMore, 0, Qt.AlignHCenter)

        self.gridProfessions.addWidget(self.profession, 0, 0, 1, 1)

        self.professionAdd = QFrame(self.professionsFrame)
        self.professionAdd.setObjectName(u"professionAdd")
        self.professionAdd.setMinimumSize(QSize(346, 407))
        self.professionAdd.setMaximumSize(QSize(346, 407))
        self.professionAdd.setLayoutDirection(Qt.LeftToRight)
        self.professionAdd.setStyleSheet(u"background-color: #FFFFFF;\n"
                                         "border: 2px dashed #501EBC;\n"
                                         "border-radius: 10px;")
        self.pushButtonAdd = QPushButton(self.professionAdd)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setGeometry(QRect(125, 113, 96, 96))
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
        self.textAdd = QLabel(self.professionAdd)
        self.textAdd.setObjectName(u"textAdd")
        self.textAdd.setGeometry(QRect(80, 230, 191, 28))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(28)
        sizePolicy4.setHeightForWidth(self.textAdd.sizePolicy().hasHeightForWidth())
        self.textAdd.setSizePolicy(sizePolicy4)
        self.textAdd.setMinimumSize(QSize(0, 28))
        self.textAdd.setMaximumSize(QSize(16777215, 28))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textAdd.setPalette(palette9)
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(18)
        font7.setBold(True)
        self.textAdd.setFont(font7)
        self.textAdd.setStyleSheet(u"border: none;")
        self.textAdd_2 = QLabel(self.professionAdd)
        self.textAdd_2.setObjectName(u"textAdd_2")
        self.textAdd_2.setGeometry(QRect(110, 260, 131, 28))
        sizePolicy4.setHeightForWidth(self.textAdd_2.sizePolicy().hasHeightForWidth())
        self.textAdd_2.setSizePolicy(sizePolicy4)
        self.textAdd_2.setMinimumSize(QSize(0, 28))
        self.textAdd_2.setMaximumSize(QSize(16777215, 28))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textAdd_2.setPalette(palette10)
        self.textAdd_2.setFont(font7)
        self.textAdd_2.setStyleSheet(u"border: none;")

        self.gridProfessions.addWidget(self.professionAdd, 1, 1, 1, 1)

        self.profession_3 = QFrame(self.professionsFrame)
        self.profession_3.setObjectName(u"profession_3")
        self.profession_3.setMinimumSize(QSize(346, 407))
        self.profession_3.setMaximumSize(QSize(346, 407))
        self.profession_3.setStyleSheet(u"QFrame {\n"
                                        "	border-right: 2px solid #E7E7E7;\n"
                                        "	border-bottom: 2px solid #E7E7E7;\n"
                                        "	border-radius: 10px;\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "}")
        self.verticalLayout_7 = QVBoxLayout(self.profession_3)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_7 = QHBoxLayout()
        self.professionButtons_7.setObjectName(u"professionButtons_7")
        self.professionName_7 = QLabel(self.profession_3)
        self.professionName_7.setObjectName(u"professionName_7")
        self.professionName_7.setMinimumSize(QSize(248, 0))
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
        self.professionName_7.setPalette(palette11)
        self.professionName_7.setFont(font3)
        self.professionName_7.setStyleSheet(u"border: none;")

        self.professionButtons_7.addWidget(self.professionName_7)

        self.buttons_7 = QHBoxLayout()
        self.buttons_7.setSpacing(10)
        self.buttons_7.setObjectName(u"buttons_7")
        self.pushButtonRedact_7 = QPushButton(self.profession_3, clicked = lambda : ProfessionPage.CreatePopup("ProfessionEdit", Ui_PopUpProfessionChangePage(), ID = 2))
        self.pushButtonRedact_7.setObjectName(u"pushButtonRedact_7")
        self.pushButtonRedact_7.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_7.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_7.setStyleSheet(u"QAbstractButton {\n"
                                              "	border: none;\n"
                                              "	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
                                              "}\n"
                                              "\n"
                                              "QAbstractButton:hover {\n"
                                              "	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
                                              "}")
        self.pushButtonRedact_7.setIconSize(QSize(24, 24))

        self.buttons_7.addWidget(self.pushButtonRedact_7)

        self.pushButtonDelete_7 = QPushButton(self.profession_3, clicked = lambda : ProfessionPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
        self.pushButtonDelete_7.setObjectName(u"pushButtonDelete_7")
        self.pushButtonDelete_7.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_7.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_7.setStyleSheet(u"QAbstractButton {\n"
                                              "	border: none;\n"
                                              "	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
                                              "}\n"
                                              "\n"
                                              "QAbstractButton:hover {\n"
                                              "	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
                                              "}")
        self.pushButtonDelete_7.setIconSize(QSize(24, 24))

        self.buttons_7.addWidget(self.pushButtonDelete_7)

        self.professionButtons_7.addLayout(self.buttons_7)

        self.verticalLayout_7.addLayout(self.professionButtons_7)

        self.professionInfo_2 = QVBoxLayout()
        self.professionInfo_2.setSpacing(10)
        self.professionInfo_2.setObjectName(u"professionInfo_2")
        self.city_2 = QHBoxLayout()
        self.city_2.setSpacing(10)
        self.city_2.setObjectName(u"city_2")
        self.iconCity_2 = QPushButton(self.profession_3)
        self.iconCity_2.setObjectName(u"iconCity_2")
        self.iconCity_2.setMinimumSize(QSize(20, 20))
        self.iconCity_2.setMaximumSize(QSize(20, 20))
        self.iconCity_2.setStyleSheet(u"QAbstractButton {\n"
                                      "	border: none;\n"
                                      "	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
                                      "}")
        self.iconCity_2.setIconSize(QSize(24, 24))

        self.city_2.addWidget(self.iconCity_2)

        self.textCity_2 = QLabel(self.profession_3)
        self.textCity_2.setObjectName(u"textCity_2")
        self.textCity_2.setMaximumSize(QSize(16777215, 20))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textCity_2.setPalette(palette12)
        self.textCity_2.setFont(font4)
        self.textCity_2.setStyleSheet(u"border: none;\n"
                                      "color: #5B5B5B;")

        self.city_2.addWidget(self.textCity_2)

        self.professionInfo_2.addLayout(self.city_2)

        self.money_2 = QHBoxLayout()
        self.money_2.setSpacing(10)
        self.money_2.setObjectName(u"money_2")
        self.iconMoney_2 = QPushButton(self.profession_3)
        self.iconMoney_2.setObjectName(u"iconMoney_2")
        self.iconMoney_2.setMinimumSize(QSize(20, 20))
        self.iconMoney_2.setMaximumSize(QSize(20, 20))
        self.iconMoney_2.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_2.setIconSize(QSize(24, 24))

        self.money_2.addWidget(self.iconMoney_2)

        self.textMoney_2 = QLabel(self.profession_3)
        self.textMoney_2.setObjectName(u"textMoney_2")
        self.textMoney_2.setMaximumSize(QSize(16777215, 20))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_2.setPalette(palette13)
        self.textMoney_2.setFont(font4)
        self.textMoney_2.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_2.addWidget(self.textMoney_2)

        self.professionInfo_2.addLayout(self.money_2)

        self.description_2 = QVBoxLayout()
        self.description_2.setSpacing(5)
        self.description_2.setObjectName(u"description_2")
        self.titleDescription_2 = QLabel(self.profession_3)
        self.titleDescription_2.setObjectName(u"titleDescription_2")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.titleDescription_2.setPalette(palette14)
        self.titleDescription_2.setFont(font5)
        self.titleDescription_2.setStyleSheet(u"border: none;")

        self.description_2.addWidget(self.titleDescription_2)

        self.textDescription_2 = QTextBrowser(self.profession_3)
        self.textDescription_2.setObjectName(u"textDescription_2")
        self.textDescription_2.setStyleSheet(u"QWidget {\n"
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

        self.description_2.addWidget(self.textDescription_2)

        self.professionInfo_2.addLayout(self.description_2)

        self.verticalLayout_7.addLayout(self.professionInfo_2)

        self.pushButtonMore_3 = QPushButton(self.profession_3, clicked = lambda : ProfessionPage.CreatePopup("Profession", Ui_PopUpProfessionPage(), ID = 2))
        self.pushButtonMore_3.setObjectName(u"pushButtonMore_3")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_3.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_3.setSizePolicy(sizePolicy1)
        self.pushButtonMore_3.setMinimumSize(QSize(0, 0))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_3.setPalette(palette15)
        self.pushButtonMore_3.setFont(font6)
        self.pushButtonMore_3.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_7.addWidget(self.pushButtonMore_3, 0, Qt.AlignHCenter)

        self.gridProfessions.addWidget(self.profession_3, 0, 1, 1, 1)

        self.profession_4 = QFrame(self.professionsFrame)
        self.profession_4.setObjectName(u"profession_4")
        self.profession_4.setMinimumSize(QSize(346, 407))
        self.profession_4.setMaximumSize(QSize(346, 407))
        self.profession_4.setStyleSheet(u"QFrame {\n"
                                        "	border-right: 2px solid #E7E7E7;\n"
                                        "	border-bottom: 2px solid #E7E7E7;\n"
                                        "	border-radius: 10px;\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "}")
        self.verticalLayout_8 = QVBoxLayout(self.profession_4)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_8 = QHBoxLayout()
        self.professionButtons_8.setObjectName(u"professionButtons_8")
        self.professionName_8 = QLabel(self.profession_4)
        self.professionName_8.setObjectName(u"professionName_8")
        self.professionName_8.setMinimumSize(QSize(248, 0))
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
        self.professionName_8.setPalette(palette16)
        self.professionName_8.setFont(font3)
        self.professionName_8.setStyleSheet(u"border: none;")

        self.professionButtons_8.addWidget(self.professionName_8)

        self.buttons_8 = QHBoxLayout()
        self.buttons_8.setSpacing(10)
        self.buttons_8.setObjectName(u"buttons_8")
        self.pushButtonRedact_8 = QPushButton(self.profession_4, clicked = lambda : ProfessionPage.CreatePopup("ProfessionEdit", Ui_PopUpProfessionChangePage(), ID = 3))
        self.pushButtonRedact_8.setObjectName(u"pushButtonRedact_8")
        self.pushButtonRedact_8.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_8.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_8.setStyleSheet(u"QAbstractButton {\n"
                                              "	border: none;\n"
                                              "	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
                                              "}\n"
                                              "\n"
                                              "QAbstractButton:hover {\n"
                                              "	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
                                              "}")
        self.pushButtonRedact_8.setIconSize(QSize(24, 24))

        self.buttons_8.addWidget(self.pushButtonRedact_8)

        self.pushButtonDelete_8 = QPushButton(self.profession_4, clicked = lambda : ProfessionPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
        self.pushButtonDelete_8.setObjectName(u"pushButtonDelete_8")
        self.pushButtonDelete_8.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_8.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_8.setStyleSheet(u"QAbstractButton {\n"
                                              "	border: none;\n"
                                              "	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
                                              "}\n"
                                              "\n"
                                              "QAbstractButton:hover {\n"
                                              "	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
                                              "}")
        self.pushButtonDelete_8.setIconSize(QSize(24, 24))

        self.buttons_8.addWidget(self.pushButtonDelete_8)

        self.professionButtons_8.addLayout(self.buttons_8)

        self.verticalLayout_8.addLayout(self.professionButtons_8)

        self.professionInfo_3 = QVBoxLayout()
        self.professionInfo_3.setSpacing(10)
        self.professionInfo_3.setObjectName(u"professionInfo_3")
        self.city_3 = QHBoxLayout()
        self.city_3.setSpacing(10)
        self.city_3.setObjectName(u"city_3")
        self.iconCity_3 = QPushButton(self.profession_4)
        self.iconCity_3.setObjectName(u"iconCity_3")
        self.iconCity_3.setMinimumSize(QSize(20, 20))
        self.iconCity_3.setMaximumSize(QSize(20, 20))
        self.iconCity_3.setStyleSheet(u"QAbstractButton {\n"
                                      "	border: none;\n"
                                      "	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
                                      "}")
        self.iconCity_3.setIconSize(QSize(24, 24))

        self.city_3.addWidget(self.iconCity_3)

        self.textCity_3 = QLabel(self.profession_4)
        self.textCity_3.setObjectName(u"textCity_3")
        self.textCity_3.setMaximumSize(QSize(16777215, 20))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textCity_3.setPalette(palette17)
        self.textCity_3.setFont(font4)
        self.textCity_3.setStyleSheet(u"border: none;\n"
                                      "color: #5B5B5B;")

        self.city_3.addWidget(self.textCity_3)

        self.professionInfo_3.addLayout(self.city_3)

        self.money_3 = QHBoxLayout()
        self.money_3.setSpacing(10)
        self.money_3.setObjectName(u"money_3")
        self.iconMoney_3 = QPushButton(self.profession_4)
        self.iconMoney_3.setObjectName(u"iconMoney_3")
        self.iconMoney_3.setMinimumSize(QSize(20, 20))
        self.iconMoney_3.setMaximumSize(QSize(20, 20))
        self.iconMoney_3.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_3.setIconSize(QSize(24, 24))

        self.money_3.addWidget(self.iconMoney_3)

        self.textMoney_3 = QLabel(self.profession_4)
        self.textMoney_3.setObjectName(u"textMoney_3")
        self.textMoney_3.setMaximumSize(QSize(16777215, 20))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_3.setPalette(palette18)
        self.textMoney_3.setFont(font4)
        self.textMoney_3.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_3.addWidget(self.textMoney_3)

        self.professionInfo_3.addLayout(self.money_3)

        self.description_3 = QVBoxLayout()
        self.description_3.setSpacing(5)
        self.description_3.setObjectName(u"description_3")
        self.titleDescription_3 = QLabel(self.profession_4)
        self.titleDescription_3.setObjectName(u"titleDescription_3")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.titleDescription_3.setPalette(palette19)
        self.titleDescription_3.setFont(font5)
        self.titleDescription_3.setStyleSheet(u"border: none;")

        self.description_3.addWidget(self.titleDescription_3)

        self.textDescription_3 = QTextBrowser(self.profession_4)
        self.textDescription_3.setObjectName(u"textDescription_3")
        self.textDescription_3.setStyleSheet(u"QWidget {\n"
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

        self.description_3.addWidget(self.textDescription_3)

        self.professionInfo_3.addLayout(self.description_3)

        self.verticalLayout_8.addLayout(self.professionInfo_3)

        self.pushButtonMore_4 = QPushButton(self.profession_4, clicked = lambda : ProfessionPage.CreatePopup("Profession", Ui_PopUpProfessionPage(), ID = 3))
        self.pushButtonMore_4.setObjectName(u"pushButtonMore_4")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_4.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_4.setSizePolicy(sizePolicy1)
        self.pushButtonMore_4.setMinimumSize(QSize(0, 0))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_4.setPalette(palette20)
        self.pushButtonMore_4.setFont(font6)
        self.pushButtonMore_4.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_8.addWidget(self.pushButtonMore_4, 0, Qt.AlignHCenter)

        self.gridProfessions.addWidget(self.profession_4, 0, 2, 1, 1)

        self.profession_5 = QFrame(self.professionsFrame)
        self.profession_5.setObjectName(u"profession_5")
        self.profession_5.setMinimumSize(QSize(346, 407))
        self.profession_5.setMaximumSize(QSize(346, 407))
        self.profession_5.setStyleSheet(u"QFrame {\n"
                                        "	border-right: 2px solid #E7E7E7;\n"
                                        "	border-bottom: 2px solid #E7E7E7;\n"
                                        "	border-radius: 10px;\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "}")
        self.verticalLayout_9 = QVBoxLayout(self.profession_5)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_9 = QHBoxLayout()
        self.professionButtons_9.setObjectName(u"professionButtons_9")
        self.professionName_9 = QLabel(self.profession_5)
        self.professionName_9.setObjectName(u"professionName_9")
        self.professionName_9.setMinimumSize(QSize(248, 0))
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
        self.professionName_9.setPalette(palette21)
        self.professionName_9.setFont(font3)
        self.professionName_9.setStyleSheet(u"border: none;")

        self.professionButtons_9.addWidget(self.professionName_9)

        self.buttons_9 = QHBoxLayout()
        self.buttons_9.setSpacing(10)
        self.buttons_9.setObjectName(u"buttons_9")
        self.pushButtonRedact_9 = QPushButton(self.profession_5, clicked = lambda : ProfessionPage.CreatePopup("ProfessionEdit", Ui_PopUpProfessionChangePage(), ID = 4))
        self.pushButtonRedact_9.setObjectName(u"pushButtonRedact_9")
        self.pushButtonRedact_9.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_9.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_9.setStyleSheet(u"QAbstractButton {\n"
                                              "	border: none;\n"
                                              "	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
                                              "}\n"
                                              "\n"
                                              "QAbstractButton:hover {\n"
                                              "	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
                                              "}")
        self.pushButtonRedact_9.setIconSize(QSize(24, 24))

        self.buttons_9.addWidget(self.pushButtonRedact_9)

        self.pushButtonDelete_9 = QPushButton(self.profession_5, clicked = lambda : ProfessionPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
        self.pushButtonDelete_9.setObjectName(u"pushButtonDelete_9")
        self.pushButtonDelete_9.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_9.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_9.setStyleSheet(u"QAbstractButton {\n"
                                              "	border: none;\n"
                                              "	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
                                              "}\n"
                                              "\n"
                                              "QAbstractButton:hover {\n"
                                              "	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
                                              "}")
        self.pushButtonDelete_9.setIconSize(QSize(24, 24))

        self.buttons_9.addWidget(self.pushButtonDelete_9)

        self.professionButtons_9.addLayout(self.buttons_9)

        self.verticalLayout_9.addLayout(self.professionButtons_9)

        self.professionInfo_4 = QVBoxLayout()
        self.professionInfo_4.setSpacing(10)
        self.professionInfo_4.setObjectName(u"professionInfo_4")
        self.city_4 = QHBoxLayout()
        self.city_4.setSpacing(10)
        self.city_4.setObjectName(u"city_4")
        self.iconCity_4 = QPushButton(self.profession_5)
        self.iconCity_4.setObjectName(u"iconCity_4")
        self.iconCity_4.setMinimumSize(QSize(20, 20))
        self.iconCity_4.setMaximumSize(QSize(20, 20))
        self.iconCity_4.setStyleSheet(u"QAbstractButton {\n"
                                      "	border: none;\n"
                                      "	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
                                      "}")
        self.iconCity_4.setIconSize(QSize(24, 24))

        self.city_4.addWidget(self.iconCity_4)

        self.textCity_4 = QLabel(self.profession_5)
        self.textCity_4.setObjectName(u"textCity_4")
        self.textCity_4.setMaximumSize(QSize(16777215, 20))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textCity_4.setPalette(palette22)
        self.textCity_4.setFont(font4)
        self.textCity_4.setStyleSheet(u"border: none;\n"
                                      "color: #5B5B5B;")

        self.city_4.addWidget(self.textCity_4)

        self.professionInfo_4.addLayout(self.city_4)

        self.money_4 = QHBoxLayout()
        self.money_4.setSpacing(10)
        self.money_4.setObjectName(u"money_4")
        self.iconMoney_4 = QPushButton(self.profession_5)
        self.iconMoney_4.setObjectName(u"iconMoney_4")
        self.iconMoney_4.setMinimumSize(QSize(20, 20))
        self.iconMoney_4.setMaximumSize(QSize(20, 20))
        self.iconMoney_4.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_4.setIconSize(QSize(24, 24))

        self.money_4.addWidget(self.iconMoney_4)

        self.textMoney_4 = QLabel(self.profession_5)
        self.textMoney_4.setObjectName(u"textMoney_4")
        self.textMoney_4.setMaximumSize(QSize(16777215, 20))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_4.setPalette(palette23)
        self.textMoney_4.setFont(font4)
        self.textMoney_4.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_4.addWidget(self.textMoney_4)

        self.professionInfo_4.addLayout(self.money_4)

        self.description_4 = QVBoxLayout()
        self.description_4.setSpacing(5)
        self.description_4.setObjectName(u"description_4")
        self.titleDescription_4 = QLabel(self.profession_5)
        self.titleDescription_4.setObjectName(u"titleDescription_4")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.titleDescription_4.setPalette(palette24)
        self.titleDescription_4.setFont(font5)
        self.titleDescription_4.setStyleSheet(u"border: none;")

        self.description_4.addWidget(self.titleDescription_4)

        self.textDescription_4 = QTextBrowser(self.profession_5)
        self.textDescription_4.setObjectName(u"textDescription_4")
        self.textDescription_4.setStyleSheet(u"QWidget {\n"
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

        self.description_4.addWidget(self.textDescription_4)

        self.professionInfo_4.addLayout(self.description_4)

        self.verticalLayout_9.addLayout(self.professionInfo_4)

        self.pushButtonMore_5 = QPushButton(self.profession_5, clicked = lambda : ProfessionPage.CreatePopup("Profession", Ui_PopUpProfessionPage(), ID = 4))
        self.pushButtonMore_5.setObjectName(u"pushButtonMore_5")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_5.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_5.setSizePolicy(sizePolicy1)
        self.pushButtonMore_5.setMinimumSize(QSize(0, 0))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_5.setPalette(palette25)
        self.pushButtonMore_5.setFont(font6)
        self.pushButtonMore_5.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_9.addWidget(self.pushButtonMore_5, 0, Qt.AlignHCenter)

        self.gridProfessions.addWidget(self.profession_5, 0, 3, 1, 1)

        self.profession_6 = QFrame(self.professionsFrame)
        self.profession_6.setObjectName(u"profession_6")
        self.profession_6.setMinimumSize(QSize(346, 407))
        self.profession_6.setMaximumSize(QSize(346, 407))
        self.profession_6.setStyleSheet(u"QFrame {\n"
                                        "	border-right: 2px solid #E7E7E7;\n"
                                        "	border-bottom: 2px solid #E7E7E7;\n"
                                        "	border-radius: 10px;\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "}")
        self.verticalLayout_10 = QVBoxLayout(self.profession_6)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_10 = QHBoxLayout()
        self.professionButtons_10.setObjectName(u"professionButtons_10")
        self.professionName_10 = QLabel(self.profession_6)
        self.professionName_10.setObjectName(u"professionName_10")
        self.professionName_10.setMinimumSize(QSize(248, 0))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.professionName_10.setPalette(palette26)
        self.professionName_10.setFont(font3)
        self.professionName_10.setStyleSheet(u"border: none;")

        self.professionButtons_10.addWidget(self.professionName_10)

        self.buttons_10 = QHBoxLayout()
        self.buttons_10.setSpacing(10)
        self.buttons_10.setObjectName(u"buttons_10")
        self.pushButtonRedact_10 = QPushButton(self.profession_6, clicked = lambda : ProfessionPage.CreatePopup("ProfessionEdit", Ui_PopUpProfessionChangePage(), ID = 5))
        self.pushButtonRedact_10.setObjectName(u"pushButtonRedact_10")
        self.pushButtonRedact_10.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_10.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_10.setStyleSheet(u"QAbstractButton {\n"
                                               "	border: none;\n"
                                               "	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
                                               "}\n"
                                               "\n"
                                               "QAbstractButton:hover {\n"
                                               "	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
                                               "}")
        self.pushButtonRedact_10.setIconSize(QSize(24, 24))

        self.buttons_10.addWidget(self.pushButtonRedact_10)

        self.pushButtonDelete_10 = QPushButton(self.profession_6, clicked = lambda : ProfessionPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
        self.pushButtonDelete_10.setObjectName(u"pushButtonDelete_10")
        self.pushButtonDelete_10.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_10.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_10.setStyleSheet(u"QAbstractButton {\n"
                                               "	border: none;\n"
                                               "	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
                                               "}\n"
                                               "\n"
                                               "QAbstractButton:hover {\n"
                                               "	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
                                               "}")
        self.pushButtonDelete_10.setIconSize(QSize(24, 24))

        self.buttons_10.addWidget(self.pushButtonDelete_10)

        self.professionButtons_10.addLayout(self.buttons_10)

        self.verticalLayout_10.addLayout(self.professionButtons_10)

        self.professionInfo_5 = QVBoxLayout()
        self.professionInfo_5.setSpacing(10)
        self.professionInfo_5.setObjectName(u"professionInfo_5")
        self.city_5 = QHBoxLayout()
        self.city_5.setSpacing(10)
        self.city_5.setObjectName(u"city_5")
        self.iconCity_5 = QPushButton(self.profession_6)
        self.iconCity_5.setObjectName(u"iconCity_5")
        self.iconCity_5.setMinimumSize(QSize(20, 20))
        self.iconCity_5.setMaximumSize(QSize(20, 20))
        self.iconCity_5.setStyleSheet(u"QAbstractButton {\n"
                                      "	border: none;\n"
                                      "	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
                                      "}")
        self.iconCity_5.setIconSize(QSize(24, 24))

        self.city_5.addWidget(self.iconCity_5)

        self.textCity_5 = QLabel(self.profession_6)
        self.textCity_5.setObjectName(u"textCity_5")
        self.textCity_5.setMaximumSize(QSize(16777215, 20))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textCity_5.setPalette(palette27)
        self.textCity_5.setFont(font4)
        self.textCity_5.setStyleSheet(u"border: none;\n"
                                      "color: #5B5B5B;")

        self.city_5.addWidget(self.textCity_5)

        self.professionInfo_5.addLayout(self.city_5)

        self.money_5 = QHBoxLayout()
        self.money_5.setSpacing(10)
        self.money_5.setObjectName(u"money_5")
        self.iconMoney_5 = QPushButton(self.profession_6)
        self.iconMoney_5.setObjectName(u"iconMoney_5")
        self.iconMoney_5.setMinimumSize(QSize(20, 20))
        self.iconMoney_5.setMaximumSize(QSize(20, 20))
        self.iconMoney_5.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_5.setIconSize(QSize(24, 24))

        self.money_5.addWidget(self.iconMoney_5)

        self.textMoney_5 = QLabel(self.profession_6)
        self.textMoney_5.setObjectName(u"textMoney_5")
        self.textMoney_5.setMaximumSize(QSize(16777215, 20))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_5.setPalette(palette28)
        self.textMoney_5.setFont(font4)
        self.textMoney_5.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_5.addWidget(self.textMoney_5)

        self.professionInfo_5.addLayout(self.money_5)

        self.description_5 = QVBoxLayout()
        self.description_5.setSpacing(5)
        self.description_5.setObjectName(u"description_5")
        self.titleDescription_5 = QLabel(self.profession_6)
        self.titleDescription_5.setObjectName(u"titleDescription_5")
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.titleDescription_5.setPalette(palette29)
        self.titleDescription_5.setFont(font5)
        self.titleDescription_5.setStyleSheet(u"border: none;")

        self.description_5.addWidget(self.titleDescription_5)

        self.textDescription_5 = QTextBrowser(self.profession_6)
        self.textDescription_5.setObjectName(u"textDescription_5")
        self.textDescription_5.setStyleSheet(u"QWidget {\n"
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

        self.description_5.addWidget(self.textDescription_5)

        self.professionInfo_5.addLayout(self.description_5)

        self.verticalLayout_10.addLayout(self.professionInfo_5)

        self.pushButtonMore_6 = QPushButton(self.profession_6, clicked = lambda : ProfessionPage.CreatePopup("Profession", Ui_PopUpProfessionPage(), ID = 5))
        self.pushButtonMore_6.setObjectName(u"pushButtonMore_6")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_6.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_6.setSizePolicy(sizePolicy1)
        self.pushButtonMore_6.setMinimumSize(QSize(0, 0))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_6.setPalette(palette30)
        self.pushButtonMore_6.setFont(font6)
        self.pushButtonMore_6.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_10.addWidget(self.pushButtonMore_6, 0, Qt.AlignHCenter)

        self.gridProfessions.addWidget(self.profession_6, 0, 4, 1, 1)

        self.profession_7 = QFrame(self.professionsFrame)
        self.profession_7.setObjectName(u"profession_7")
        self.profession_7.setMinimumSize(QSize(346, 407))
        self.profession_7.setMaximumSize(QSize(346, 407))
        self.profession_7.setStyleSheet(u"QFrame {\n"
                                        "	border-right: 2px solid #E7E7E7;\n"
                                        "	border-bottom: 2px solid #E7E7E7;\n"
                                        "	border-radius: 10px;\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "}")
        self.verticalLayout_12 = QVBoxLayout(self.profession_7)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_12 = QHBoxLayout()
        self.professionButtons_12.setObjectName(u"professionButtons_12")
        self.professionName_12 = QLabel(self.profession_7)
        self.professionName_12.setObjectName(u"professionName_12")
        self.professionName_12.setMinimumSize(QSize(248, 0))
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
        self.professionName_12.setPalette(palette31)
        self.professionName_12.setFont(font3)
        self.professionName_12.setStyleSheet(u"border: none;")

        self.professionButtons_12.addWidget(self.professionName_12)

        self.buttons_12 = QHBoxLayout()
        self.buttons_12.setSpacing(10)
        self.buttons_12.setObjectName(u"buttons_12")
        self.pushButtonRedact_12 = QPushButton(self.profession_7)
        self.pushButtonRedact_12.setObjectName(u"pushButtonRedact_12")
        self.pushButtonRedact_12.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_12.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_12.setStyleSheet(u"QAbstractButton {\n"
                                               "	border: none;\n"
                                               "	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
                                               "}\n"
                                               "\n"
                                               "QAbstractButton:hover {\n"
                                               "	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
                                               "}")
        self.pushButtonRedact_12.setIconSize(QSize(24, 24))

        self.buttons_12.addWidget(self.pushButtonRedact_12)

        self.pushButtonDelete_12 = QPushButton(self.profession_7, clicked = lambda : ProfessionPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
        self.pushButtonDelete_12.setObjectName(u"pushButtonDelete_12")
        self.pushButtonDelete_12.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_12.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_12.setStyleSheet(u"QAbstractButton {\n"
                                               "	border: none;\n"
                                               "	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
                                               "}\n"
                                               "\n"
                                               "QAbstractButton:hover {\n"
                                               "	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
                                               "}")
        self.pushButtonDelete_12.setIconSize(QSize(24, 24))

        self.buttons_12.addWidget(self.pushButtonDelete_12)

        self.professionButtons_12.addLayout(self.buttons_12)

        self.verticalLayout_12.addLayout(self.professionButtons_12)

        self.professionInfo_7 = QVBoxLayout()
        self.professionInfo_7.setSpacing(10)
        self.professionInfo_7.setObjectName(u"professionInfo_7")
        self.city_7 = QHBoxLayout()
        self.city_7.setSpacing(10)
        self.city_7.setObjectName(u"city_7")
        self.iconCity_7 = QPushButton(self.profession_7)
        self.iconCity_7.setObjectName(u"iconCity_7")
        self.iconCity_7.setMinimumSize(QSize(20, 20))
        self.iconCity_7.setMaximumSize(QSize(20, 20))
        self.iconCity_7.setStyleSheet(u"QAbstractButton {\n"
                                      "	border: none;\n"
                                      "	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
                                      "}")
        self.iconCity_7.setIconSize(QSize(24, 24))

        self.city_7.addWidget(self.iconCity_7)

        self.textCity_7 = QLabel(self.profession_7)
        self.textCity_7.setObjectName(u"textCity_7")
        self.textCity_7.setMaximumSize(QSize(16777215, 20))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textCity_7.setPalette(palette32)
        self.textCity_7.setFont(font4)
        self.textCity_7.setStyleSheet(u"border: none;\n"
                                      "color: #5B5B5B;")

        self.city_7.addWidget(self.textCity_7)

        self.professionInfo_7.addLayout(self.city_7)

        self.money_7 = QHBoxLayout()
        self.money_7.setSpacing(10)
        self.money_7.setObjectName(u"money_7")
        self.iconMoney_7 = QPushButton(self.profession_7)
        self.iconMoney_7.setObjectName(u"iconMoney_7")
        self.iconMoney_7.setMinimumSize(QSize(20, 20))
        self.iconMoney_7.setMaximumSize(QSize(20, 20))
        self.iconMoney_7.setStyleSheet(u"QAbstractButton {\n"
                                       "	border: none;\n"
                                       "	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
                                       "}")
        self.iconMoney_7.setIconSize(QSize(24, 24))

        self.money_7.addWidget(self.iconMoney_7)

        self.textMoney_7 = QLabel(self.profession_7)
        self.textMoney_7.setObjectName(u"textMoney_7")
        self.textMoney_7.setMaximumSize(QSize(16777215, 20))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_7.setPalette(palette33)
        self.textMoney_7.setFont(font4)
        self.textMoney_7.setStyleSheet(u"border: none;\n"
                                       "color: #5B5B5B;")

        self.money_7.addWidget(self.textMoney_7)

        self.professionInfo_7.addLayout(self.money_7)

        self.description_7 = QVBoxLayout()
        self.description_7.setSpacing(5)
        self.description_7.setObjectName(u"description_7")
        self.titleDescription_7 = QLabel(self.profession_7)
        self.titleDescription_7.setObjectName(u"titleDescription_7")
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.titleDescription_7.setPalette(palette34)
        self.titleDescription_7.setFont(font5)
        self.titleDescription_7.setStyleSheet(u"border: none;")

        self.description_7.addWidget(self.titleDescription_7)

        self.textDescription_7 = QTextBrowser(self.profession_7)
        self.textDescription_7.setObjectName(u"textDescription_7")
        self.textDescription_7.setStyleSheet(u"QWidget {\n"
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

        self.description_7.addWidget(self.textDescription_7)

        self.professionInfo_7.addLayout(self.description_7)

        self.verticalLayout_12.addLayout(self.professionInfo_7)

        self.pushButtonMore_8 = QPushButton(self.profession_7, clicked = lambda : ProfessionPage.CreatePopup("Profession", Ui_PopUpProfessionPage(), ID = 6))
        self.pushButtonMore_8.setObjectName(u"pushButtonMore_8")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_8.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_8.setSizePolicy(sizePolicy1)
        self.pushButtonMore_8.setMinimumSize(QSize(0, 0))
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButtonMore_8.setPalette(palette35)
        self.pushButtonMore_8.setFont(font6)
        self.pushButtonMore_8.setStyleSheet(u"QAbstractButton {\n"
                                            "	border: none;\n"
                                            "	color: #010101;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractButton:hover {\n"
                                            "	color: #501EBC;\n"
                                            "}")

        self.verticalLayout_12.addWidget(self.pushButtonMore_8, 0, Qt.AlignHCenter)

        self.gridProfessions.addWidget(self.profession_7, 1, 0, 1, 1)

        self.professions.addLayout(self.gridProfessions)

        self.verticalScrollBar = QScrollBar(self.professionsFrame)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        palette36 = QPalette()
        brush5 = QBrush(QColor(231, 231, 231, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.verticalScrollBar.setPalette(palette36)
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

        self.professions.addWidget(self.verticalScrollBar)

        self.verticalLayout.addWidget(self.professionsFrame, 0, Qt.AlignTop)

        ProfessionPage.setCentralWidget(self.professionPage)

        self.retranslateUi(ProfessionPage)

        QMetaObject.connectSlotsByName(ProfessionPage)

    # setupUi

    def retranslateUi(self, ProfessionPage):

        ProfessionPage.setWindowTitle(QCoreApplication.translate("ProfessionPage", u"Ваша Вакансия", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("ProfessionPage",
                                                           u"Подобрать профессию",
                                                           None))
        self.pushButton_2.setText(
            QCoreApplication.translate("ProfessionPage", u"Кластеры", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("ProfessionPage", u"Профессии",
                                       None))
        self.title_2.setText(
            QCoreApplication.translate("ProfessionPage", u"Профессии",
                                       None))
        self.findInput.setText("")
        self.findInput.setPlaceholderText(QCoreApplication.translate("ProfessionPage",
                                                                     u"Введите название профессии",
                                                                     None))
        self.pushButtonFind.setText("")
        self.professionName.setText(
            QCoreApplication.translate("ProfessionPage", self.vacancies[0][0], None))
        self.pushButtonRedact.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.iconCity.setText("")
        # if QT_CONFIG(shortcut)
        self.iconCity.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textCity.setText(QCoreApplication.translate("ProfessionPage", u"Омск", None))
        self.iconMoney.setText("")
        # if QT_CONFIG(shortcut)
        self.iconMoney.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textMoney.setText(QCoreApplication.translate("ProfessionPage", self.vacancies[0][3], None))
        self.titleDescription.setText(
            QCoreApplication.translate("ProfessionPage", u"Описание", None))
        self.textDescription.setHtml(QCoreApplication.translate("ProfessionPage",
                                                                u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                "p, li { white-space: pre-wrap; }\n"
                                                                "</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">"+self.vacancies[0][1]+"</span></"
                                                                "p></body></html>", None))
        self.pushButtonMore.setText(QCoreApplication.translate("ProfessionPage",
                                                               u"Показать ещё",
                                                               None))
        self.pushButtonAdd.setText("")
        self.textAdd.setText(QCoreApplication.translate("ProfessionPage",
                                                        u"Добавить новую",
                                                        None))
        self.textAdd_2.setText(
            QCoreApplication.translate("ProfessionPage", u"профессию",
                                       None))
        self.professionName_7.setText(
            QCoreApplication.translate("ProfessionPage", self.vacancies[1][0], None))
        self.pushButtonRedact_7.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_7.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_7.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_7.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.iconCity_2.setText("")
        # if QT_CONFIG(shortcut)
        self.iconCity_2.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textCity_2.setText(QCoreApplication.translate("ProfessionPage", u"Омск", None))
        self.iconMoney_2.setText("")
        # if QT_CONFIG(shortcut)
        self.iconMoney_2.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textMoney_2.setText(QCoreApplication.translate("ProfessionPage", self.vacancies[1][3], None))
        self.titleDescription_2.setText(
            QCoreApplication.translate("ProfessionPage", u"Описание", None))
        self.textDescription_2.setHtml(QCoreApplication.translate("ProfessionPage",
                                                                  u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">"+self.vacancies[1][1]+"</span></"
                                                                  "p></body></html>", None))
        self.pushButtonMore_3.setText(QCoreApplication.translate("ProfessionPage",
                                                                 u"Показать ещё",
                                                                 None))
        self.professionName_8.setText(
            QCoreApplication.translate("ProfessionPage", self.vacancies[2][0], None))
        self.pushButtonRedact_8.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_8.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_8.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_8.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.iconCity_3.setText("")
        # if QT_CONFIG(shortcut)
        self.iconCity_3.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textCity_3.setText(QCoreApplication.translate("ProfessionPage", u"Омск", None))
        self.iconMoney_3.setText("")
        # if QT_CONFIG(shortcut)
        self.iconMoney_3.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textMoney_3.setText(QCoreApplication.translate("ProfessionPage", self.vacancies[2][3], None))
        self.titleDescription_3.setText(
            QCoreApplication.translate("ProfessionPage", u"Описание", None))
        self.textDescription_3.setHtml(QCoreApplication.translate("ProfessionPage",
                                                                  u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">"+self.vacancies[2][1]+"</span></"
                                                                  "p></body></html>", None))
        self.pushButtonMore_4.setText(QCoreApplication.translate("ProfessionPage",
                                                                 u"Показать ещё",
                                                                 None))
        self.professionName_9.setText(
            QCoreApplication.translate("ProfessionPage", self.vacancies[3][0], None))
        self.pushButtonRedact_9.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_9.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_9.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_9.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.iconCity_4.setText("")
        # if QT_CONFIG(shortcut)
        self.iconCity_4.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textCity_4.setText(QCoreApplication.translate("ProfessionPage", u"Омск", None))
        self.iconMoney_4.setText("")
        # if QT_CONFIG(shortcut)
        self.iconMoney_4.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textMoney_4.setText(QCoreApplication.translate("ProfessionPage", self.vacancies[3][3], None))
        self.titleDescription_4.setText(
            QCoreApplication.translate("ProfessionPage", u"Описание", None))
        self.textDescription_4.setHtml(QCoreApplication.translate("ProfessionPage",
                                                                  u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">"+self.vacancies[3][1]+"</span></"
                                                                  "p></body></html>", None))
        self.pushButtonMore_5.setText(QCoreApplication.translate("ProfessionPage",
                                                                 u"Показать ещё",
                                                                 None))
        self.professionName_10.setText(
            QCoreApplication.translate("ProfessionPage", self.vacancies[4][0], None))
        self.pushButtonRedact_10.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_10.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_10.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_10.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.iconCity_5.setText("")
        # if QT_CONFIG(shortcut)
        self.iconCity_5.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textCity_5.setText(QCoreApplication.translate("ProfessionPage", u"Омск", None))
        self.iconMoney_5.setText("")
        # if QT_CONFIG(shortcut)
        self.iconMoney_5.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textMoney_5.setText(QCoreApplication.translate("ProfessionPage", self.vacancies[4][3], None))
        self.titleDescription_5.setText(
            QCoreApplication.translate("ProfessionPage", u"Описание", None))
        self.textDescription_5.setHtml(QCoreApplication.translate("ProfessionPage",
                                                                  u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">"+self.vacancies[4][1]+"</span></"
                                                                  "p></body></html>", None))
        self.pushButtonMore_6.setText(QCoreApplication.translate("ProfessionPage",
                                                                 u"Показать ещё",
                                                                 None))
        self.professionName_12.setText(
            QCoreApplication.translate("ProfessionPage", self.vacancies[5][0], None))
        self.pushButtonRedact_12.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact_12.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_12.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete_12.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.iconCity_7.setText("")
        # if QT_CONFIG(shortcut)
        self.iconCity_7.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textCity_7.setText(QCoreApplication.translate("ProfessionPage", u"Омск", None))
        self.iconMoney_7.setText("")
        # if QT_CONFIG(shortcut)
        self.iconMoney_7.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.textMoney_7.setText(QCoreApplication.translate("ProfessionPage", self.vacancies[5][3], None))
        self.titleDescription_7.setText(
            QCoreApplication.translate("ProfessionPage", u"Описание", None))
        self.textDescription_7.setHtml(QCoreApplication.translate("ProfessionPage",
                                                                  u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">"+self.vacancies[5][1]+"</span></"
                                                                  "p></body></html>", None))
        self.pushButtonMore_8.setText(QCoreApplication.translate("ProfessionPage",
                                                                 u"Показать ещё",
                                                                 None))

    # retranslateUi
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

        self.pushButtonRedact = QPushButton(self.popUpProfessionPage, clicked = lambda : PopUpProfessionPage.CreatePopup("ProfessionEdit", Ui_PopUpProfessionChangePage(), PopUpProfessionPage.ID))
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

        self.pushButtonDelete = QPushButton(self.popUpProfessionPage, clicked = lambda : PopUpProfessionPage.CreatePopup("Delete", Ui_PopUpDeleteAttentionPage()))
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

        self.pushButtonClose = QPushButton(self.popUpProfessionPage, clicked = lambda : PopUpProfessionPage.CloseWindow())
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
        PopUpProfessionPage.setWindowTitle(QCoreApplication.translate("PopUpProfessionPage", u"Ваша Вакансия", None))
        self.titleName.setText(QCoreApplication.translate("PopUpProfessionPage", PopUpProfessionPage.data[0], None))
        self.pushButtonRedact.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonRedact.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText("")
        # if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut("")
        # endif // QT_CONFIG(shortcut)
        self.pushButtonClose.setText("")
        self.professionName.setText(QCoreApplication.translate("PopUpProfessionPage", u"Описание", None))
        self.textDescription.setHtml(QCoreApplication.translate("PopUpProfessionPage",
                                                                u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                "p, li { white-space: pre-wrap; }\n"
                                                                "</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:600; background-color:#ffffff;\">"+ PopUpProfessionPage.data[1] +"</span></p>\n"
                                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt; font-weight:600;\"><br /></p>\n",
                                                                None))


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

        DB_data = PopUpProfessionChangePage.TakeDataFromDB('Cluster')
        for data in DB_data:
            self.comboBoxCluster.addItem(data[1])

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
        self.pushButtonYes = QPushButton(self.buttonsFrame, clicked = lambda : PopUpProfessionChangePage.CreatePopup("Apply", Ui_PopUpSaveAttentionPage()))
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

        self.pushButtonNo = QPushButton(self.buttonsFrame, clicked = lambda : PopUpProfessionChangePage.CloseWindow())
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
        self.pushButtonYes.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButtonNo.setText(QCoreApplication.translate("PopUpProfessionChangePage", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

    def Save(self):
        professionName = self.input.text()
        description = self.inputDescription.toPlainText()
        cluster = self.comboBoxCluster.currentText()
        region = self.comboBoxRegion.currentText()
        return [professionName, description, region, cluster]

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
        self.pushButtonYes = QPushButton(self.buttonsFrame, clicked = lambda : PopUpSaveAttentionPage.Save())
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

        self.pushButtonNo = QPushButton(self.buttonsFrame, clicked = lambda : PopUpSaveAttentionPage.CloseWindow())
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
class Ui_PopUpDeleteAttentionPage(object):
    def setupUi(self, PopUpDeleteAttentionPage):
        if not PopUpDeleteAttentionPage.objectName():
            PopUpDeleteAttentionPage.setObjectName(u"PopUpDeleteAttentionPage")
        PopUpDeleteAttentionPage.resize(570, 176)
        PopUpDeleteAttentionPage.setMinimumSize(QSize(570, 176))
        PopUpDeleteAttentionPage.setMaximumSize(QSize(570, 184))
        PopUpDeleteAttentionPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.popUpDeleteAttentionPage = QWidget(PopUpDeleteAttentionPage)
        self.popUpDeleteAttentionPage.setObjectName(u"popUpDeleteAttentionPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popUpDeleteAttentionPage.sizePolicy().hasHeightForWidth())
        self.popUpDeleteAttentionPage.setSizePolicy(sizePolicy)
        self.popUpDeleteAttentionPage.setMaximumSize(QSize(16777215, 16777215))
        self.popUpDeleteAttentionPage.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.popUpDeleteAttentionPage)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.title = QLabel(self.popUpDeleteAttentionPage)
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

        self.buttonsFrame = QFrame(self.popUpDeleteAttentionPage)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttons = QHBoxLayout(self.buttonsFrame)
        self.buttons.setSpacing(20)
        self.buttons.setObjectName(u"buttons")
        self.pushButtonYes = QPushButton(self.buttonsFrame, clicked = lambda: PopUpDeleteAttentionPage.Apply())
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

        self.pushButtonNo = QPushButton(self.buttonsFrame, clicked = lambda : PopUpDeleteAttentionPage.CloseWindow())
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

        PopUpDeleteAttentionPage.setCentralWidget(self.popUpDeleteAttentionPage)

        self.retranslateUi(PopUpDeleteAttentionPage)

        QMetaObject.connectSlotsByName(PopUpDeleteAttentionPage)
    # setupUi

    def retranslateUi(self, PopUpDeleteAttentionPage):
        PopUpDeleteAttentionPage.setWindowTitle(QCoreApplication.translate("PopUpDeleteAttentionPage", u"Your Vacancy", None))
        self.title.setText(QCoreApplication.translate("PopUpDeleteAttentionPage", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b, \u0447\u0442\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0443\u0434\u0430\u043b\u0438\u0442\u044c?", None))
        self.pushButtonYes.setText(QCoreApplication.translate("PopUpDeleteAttentionPage", u"\u0414\u0430", None))
        self.pushButtonNo.setText(QCoreApplication.translate("PopUpDeleteAttentionPage", u"\u041d\u0435\u0442", None))
    # retranslateUi