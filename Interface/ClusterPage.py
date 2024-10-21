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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QListView, QListWidget, QListWidgetItem, QMainWindow,
                               QPushButton, QScrollBar, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
import Logo
import Icons


class Ui_ClusterPage(object):
    def setupUi(self, ClusterPage):
        if not ClusterPage.objectName():
            ClusterPage.setObjectName(u"ClusterPage")
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
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
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

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButtonMore = QPushButton(self.cluster)
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
        self.pushButtonRedact_4 = QPushButton(self.cluster_4)
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

        self.pushButtonDelete_4 = QPushButton(self.cluster_4)
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

        self.listWidget_4 = QListWidget(self.cluster_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setMinimumSize(QSize(302, 260))
        self.listWidget_4.setMaximumSize(QSize(302, 260))
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
        self.listWidget_4.setPalette(palette11)
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

        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.pushButtonMore_4 = QPushButton(self.cluster_4)
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
        self.pushButtonRedact_2 = QPushButton(self.cluster_2)
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

        self.pushButtonDelete_2 = QPushButton(self.cluster_2)
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

        self.listWidget_2 = QListWidget(self.cluster_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMinimumSize(QSize(302, 260))
        self.listWidget_2.setMaximumSize(QSize(302, 260))
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
        self.listWidget_2.setPalette(palette15)
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

        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.pushButtonMore_2 = QPushButton(self.cluster_2)
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
        self.pushButtonRedact_3 = QPushButton(self.cluster_3)
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

        self.pushButtonDelete_3 = QPushButton(self.cluster_3)
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

        self.listWidget_3 = QListWidget(self.cluster_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setMinimumSize(QSize(302, 260))
        self.listWidget_3.setMaximumSize(QSize(302, 260))
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
        self.listWidget_3.setPalette(palette19)
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

        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.pushButtonMore_3 = QPushButton(self.cluster_3)
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
        self.pushButtonRedact_5 = QPushButton(self.cluster_5)
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

        self.pushButtonDelete_5 = QPushButton(self.cluster_5)
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

        self.listWidget_5 = QListWidget(self.cluster_5)
        QListWidgetItem(self.listWidget_5)
        QListWidgetItem(self.listWidget_5)
        QListWidgetItem(self.listWidget_5)
        QListWidgetItem(self.listWidget_5)
        QListWidgetItem(self.listWidget_5)
        QListWidgetItem(self.listWidget_5)
        QListWidgetItem(self.listWidget_5)
        QListWidgetItem(self.listWidget_5)
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setMinimumSize(QSize(302, 260))
        self.listWidget_5.setMaximumSize(QSize(302, 260))
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
        self.listWidget_5.setPalette(palette23)
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

        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.pushButtonMore_5 = QPushButton(self.cluster_5)
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
        self.pushButtonRedact_6 = QPushButton(self.cluster_6)
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

        self.pushButtonDelete_6 = QPushButton(self.cluster_6)
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

        self.listWidget_6 = QListWidget(self.cluster_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        self.listWidget_6.setObjectName(u"listWidget_6")
        self.listWidget_6.setMinimumSize(QSize(302, 260))
        self.listWidget_6.setMaximumSize(QSize(302, 260))
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
        self.listWidget_6.setPalette(palette27)
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

        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.pushButtonMore_6 = QPushButton(self.cluster_6)
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
        ClusterPage.setWindowTitle(QCoreApplication.translate("ClusterPage", u"Your Vacancy", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("ClusterPage",
                                                           u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e",
                                                           None))
        self.pushButton_2.setText(
            QCoreApplication.translate("ClusterPage", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u044b", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.title_2.setText(
            QCoreApplication.translate("ClusterPage", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u044b", None))
        self.findInput.setText("")
        self.findInput.setPlaceholderText(QCoreApplication.translate("ClusterPage",
                                                                     u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0430",
                                                                     None))
        self.pushButtonFind.setText("")
        self.pushButtonAdd.setText("")
        self.textAdd.setText(QCoreApplication.translate("ClusterPage",
                                                        u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043a\u043b\u0430\u0441\u0442\u0435\u0440",
                                                        None))
        self.clusterName.setText(
            QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonRedact.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.vacancy.setText(
            QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ClusterPage",
                                                              u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c",
                                                              None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("ClusterPage",
                                                               u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440",
                                                               None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("ClusterPage",
                                                               u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435",
                                                               None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("ClusterPage",
                                                               u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430",
                                                               None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("ClusterPage",
                                                               u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436",
                                                               None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(
            QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("ClusterPage",
                                                               u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440",
                                                               None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("ClusterPage",
                                                               u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442",
                                                               None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButtonMore.setText(QCoreApplication.translate("ClusterPage",
                                                               u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451",
                                                               None))
        self.clusterName_4.setText(
            QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_4.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonRedact_4.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_4.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonDelete_4.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.vacancy_4.setText(
            QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))

        __sortingEnabled1 = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        ___qlistwidgetitem8 = self.listWidget_4.item(0)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("ClusterPage",
                                                               u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c",
                                                               None));
        ___qlistwidgetitem9 = self.listWidget_4.item(1)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("ClusterPage",
                                                               u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440",
                                                               None));
        ___qlistwidgetitem10 = self.listWidget_4.item(2)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435",
                                                                None));
        ___qlistwidgetitem11 = self.listWidget_4.item(3)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430",
                                                                None));
        ___qlistwidgetitem12 = self.listWidget_4.item(4)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436",
                                                                None));
        ___qlistwidgetitem13 = self.listWidget_4.item(5)
        ___qlistwidgetitem13.setText(
            QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None));
        ___qlistwidgetitem14 = self.listWidget_4.item(6)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440",
                                                                None));
        ___qlistwidgetitem15 = self.listWidget_4.item(7)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442",
                                                                None));
        self.listWidget_4.setSortingEnabled(__sortingEnabled1)

        self.pushButtonMore_4.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451",
                                                                 None))
        self.clusterName_2.setText(
            QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_2.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonRedact_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_2.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonDelete_2.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.vacancy_2.setText(
            QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))

        __sortingEnabled2 = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem16 = self.listWidget_2.item(0)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c",
                                                                None));
        ___qlistwidgetitem17 = self.listWidget_2.item(1)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440",
                                                                None));
        ___qlistwidgetitem18 = self.listWidget_2.item(2)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435",
                                                                None));
        ___qlistwidgetitem19 = self.listWidget_2.item(3)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430",
                                                                None));
        ___qlistwidgetitem20 = self.listWidget_2.item(4)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436",
                                                                None));
        ___qlistwidgetitem21 = self.listWidget_2.item(5)
        ___qlistwidgetitem21.setText(
            QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None));
        ___qlistwidgetitem22 = self.listWidget_2.item(6)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440",
                                                                None));
        ___qlistwidgetitem23 = self.listWidget_2.item(7)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442",
                                                                None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled2)

        self.pushButtonMore_2.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451",
                                                                 None))
        self.clusterName_3.setText(
            QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_3.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonRedact_3.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_3.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonDelete_3.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.vacancy_3.setText(
            QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))

        __sortingEnabled3 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem24 = self.listWidget_3.item(0)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c",
                                                                None));
        ___qlistwidgetitem25 = self.listWidget_3.item(1)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440",
                                                                None));
        ___qlistwidgetitem26 = self.listWidget_3.item(2)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435",
                                                                None));
        ___qlistwidgetitem27 = self.listWidget_3.item(3)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430",
                                                                None));
        ___qlistwidgetitem28 = self.listWidget_3.item(4)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436",
                                                                None));
        ___qlistwidgetitem29 = self.listWidget_3.item(5)
        ___qlistwidgetitem29.setText(
            QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None));
        ___qlistwidgetitem30 = self.listWidget_3.item(6)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440",
                                                                None));
        ___qlistwidgetitem31 = self.listWidget_3.item(7)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442",
                                                                None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled3)

        self.pushButtonMore_3.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451",
                                                                 None))
        self.clusterName_5.setText(
            QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_5.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonRedact_5.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_5.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonDelete_5.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.vacancy_5.setText(
            QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))

        __sortingEnabled4 = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        ___qlistwidgetitem32 = self.listWidget_5.item(0)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c",
                                                                None));
        ___qlistwidgetitem33 = self.listWidget_5.item(1)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440",
                                                                None));
        ___qlistwidgetitem34 = self.listWidget_5.item(2)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435",
                                                                None));
        ___qlistwidgetitem35 = self.listWidget_5.item(3)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430",
                                                                None));
        ___qlistwidgetitem36 = self.listWidget_5.item(4)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436",
                                                                None));
        ___qlistwidgetitem37 = self.listWidget_5.item(5)
        ___qlistwidgetitem37.setText(
            QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None));
        ___qlistwidgetitem38 = self.listWidget_5.item(6)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440",
                                                                None));
        ___qlistwidgetitem39 = self.listWidget_5.item(7)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442",
                                                                None));
        self.listWidget_5.setSortingEnabled(__sortingEnabled4)

        self.pushButtonMore_5.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451",
                                                                 None))
        self.clusterName_6.setText(
            QCoreApplication.translate("ClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact_6.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonRedact_6.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_6.setText("")
        #if QT_CONFIG(shortcut)
        self.pushButtonDelete_6.setShortcut("")
        #endif // QT_CONFIG(shortcut)
        self.vacancy_6.setText(
            QCoreApplication.translate("ClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))

        __sortingEnabled5 = self.listWidget_6.isSortingEnabled()
        self.listWidget_6.setSortingEnabled(False)
        ___qlistwidgetitem40 = self.listWidget_6.item(0)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c",
                                                                None));
        ___qlistwidgetitem41 = self.listWidget_6.item(1)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440",
                                                                None));
        ___qlistwidgetitem42 = self.listWidget_6.item(2)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435",
                                                                None));
        ___qlistwidgetitem43 = self.listWidget_6.item(3)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u0441\u0430\u043b\u043e\u043d\u0430",
                                                                None));
        ___qlistwidgetitem44 = self.listWidget_6.item(4)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436",
                                                                None));
        ___qlistwidgetitem45 = self.listWidget_6.item(5)
        ___qlistwidgetitem45.setText(
            QCoreApplication.translate("ClusterPage", u"\u041a\u0430\u0441\u0441\u0438\u0440", None));
        ___qlistwidgetitem46 = self.listWidget_6.item(6)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440",
                                                                None));
        ___qlistwidgetitem47 = self.listWidget_6.item(7)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("ClusterPage",
                                                                u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442",
                                                                None));
        self.listWidget_6.setSortingEnabled(__sortingEnabled5)

        self.pushButtonMore_6.setText(QCoreApplication.translate("ClusterPage",
                                                                 u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451",
                                                                 None))
    # retranslateUi
