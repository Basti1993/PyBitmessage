# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Mon Sep 02 16:49:54 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName(_fromUtf8("settingsDialog"))
        settingsDialog.resize(567, 343)
        self.gridLayout = QtGui.QGridLayout(settingsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(settingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tabWidgetSettings = QtGui.QTabWidget(settingsDialog)
        self.tabWidgetSettings.setObjectName(_fromUtf8("tabWidgetSettings"))
        self.tabUserInterface = QtGui.QWidget()
        self.tabUserInterface.setEnabled(True)
        self.tabUserInterface.setObjectName(_fromUtf8("tabUserInterface"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tabUserInterface)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.checkBoxStartOnLogon = QtGui.QCheckBox(self.tabUserInterface)
        self.checkBoxStartOnLogon.setObjectName(_fromUtf8("checkBoxStartOnLogon"))
        self.gridLayout_5.addWidget(self.checkBoxStartOnLogon, 0, 0, 1, 2)
        self.checkBoxStartInTray = QtGui.QCheckBox(self.tabUserInterface)
        self.checkBoxStartInTray.setObjectName(_fromUtf8("checkBoxStartInTray"))
        self.gridLayout_5.addWidget(self.checkBoxStartInTray, 1, 0, 1, 2)
        self.checkBoxMinimizeToTray = QtGui.QCheckBox(self.tabUserInterface)
        self.checkBoxMinimizeToTray.setChecked(True)
        self.checkBoxMinimizeToTray.setObjectName(_fromUtf8("checkBoxMinimizeToTray"))
        self.gridLayout_5.addWidget(self.checkBoxMinimizeToTray, 2, 0, 1, 1)
        self.checkBoxShowTrayNotifications = QtGui.QCheckBox(self.tabUserInterface)
        self.checkBoxShowTrayNotifications.setObjectName(_fromUtf8("checkBoxShowTrayNotifications"))
        self.gridLayout_5.addWidget(self.checkBoxShowTrayNotifications, 3, 0, 1, 2)
        self.checkBoxPortableMode = QtGui.QCheckBox(self.tabUserInterface)
        self.checkBoxPortableMode.setObjectName(_fromUtf8("checkBoxPortableMode"))
        self.gridLayout_5.addWidget(self.checkBoxPortableMode, 4, 0, 1, 1)
        self.PortableModeDescription = QtGui.QLabel(self.tabUserInterface)
        self.PortableModeDescription.setWordWrap(True)
        self.PortableModeDescription.setObjectName(_fromUtf8("PortableModeDescription"))
        self.gridLayout_5.addWidget(self.PortableModeDescription, 5, 0, 1, 3)
        self.checkBoxWillinglySendToMobile = QtGui.QCheckBox(self.tabUserInterface)
        self.checkBoxWillinglySendToMobile.setObjectName(_fromUtf8("checkBoxWillinglySendToMobile"))
        self.gridLayout_5.addWidget(self.checkBoxWillinglySendToMobile, 6, 0, 1, 3)
        self.labelSettingsNote = QtGui.QLabel(self.tabUserInterface)
        self.labelSettingsNote.setText(_fromUtf8(""))
        self.labelSettingsNote.setWordWrap(True)
        self.labelSettingsNote.setObjectName(_fromUtf8("labelSettingsNote"))
        self.gridLayout_5.addWidget(self.labelSettingsNote, 7, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(self.tabUserInterface)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.languageComboBox = QtGui.QComboBox(self.groupBox)
        self.languageComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.languageComboBox.setObjectName(_fromUtf8("languageComboBox"))
        self.languageComboBox.addItem(_fromUtf8(""))
        self.languageComboBox.addItem(_fromUtf8(""))
        self.languageComboBox.addItem(_fromUtf8(""))
        self.languageComboBox.addItem(_fromUtf8(""))
        self.languageComboBox.addItem(_fromUtf8(""))
        self.languageComboBox.addItem(_fromUtf8(""))
        self.languageComboBox.addItem(_fromUtf8(""))
        self.languageComboBox.addItem(_fromUtf8(""))
        self.languageComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.languageComboBox)
        self.gridLayout_5.addWidget(self.groupBox, 7, 2, 2, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 8, 1, 1, 1)
        self.tabWidgetSettings.addTab(self.tabUserInterface, _fromUtf8(""))
        self.tabNetworkSettings = QtGui.QWidget()
        self.tabNetworkSettings.setObjectName(_fromUtf8("tabNetworkSettings"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabNetworkSettings)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox1 = QtGui.QGroupBox(self.tabNetworkSettings)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox1)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.lineEditTCPPort = QtGui.QLineEdit(self.groupBox1)
        self.lineEditTCPPort.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEditTCPPort.setObjectName(_fromUtf8("lineEditTCPPort"))
        self.gridLayout_3.addWidget(self.lineEditTCPPort, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox1, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tabNetworkSettings)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBoxProxyType = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxProxyType.setObjectName(_fromUtf8("comboBoxProxyType"))
        self.comboBoxProxyType.addItem(_fromUtf8(""))
        self.comboBoxProxyType.addItem(_fromUtf8(""))
        self.comboBoxProxyType.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBoxProxyType, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.lineEditSocksHostname = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditSocksHostname.setObjectName(_fromUtf8("lineEditSocksHostname"))
        self.gridLayout_2.addWidget(self.lineEditSocksHostname, 1, 2, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 4, 1, 1)
        self.lineEditSocksPort = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditSocksPort.setObjectName(_fromUtf8("lineEditSocksPort"))
        self.gridLayout_2.addWidget(self.lineEditSocksPort, 1, 5, 1, 1)
        self.checkBoxAuthentication = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxAuthentication.setObjectName(_fromUtf8("checkBoxAuthentication"))
        self.gridLayout_2.addWidget(self.checkBoxAuthentication, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)
        self.lineEditSocksUsername = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditSocksUsername.setEnabled(False)
        self.lineEditSocksUsername.setObjectName(_fromUtf8("lineEditSocksUsername"))
        self.gridLayout_2.addWidget(self.lineEditSocksUsername, 2, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 4, 1, 1)
        self.lineEditSocksPassword = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditSocksPassword.setEnabled(False)
        self.lineEditSocksPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEditSocksPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditSocksPassword.setObjectName(_fromUtf8("lineEditSocksPassword"))
        self.gridLayout_2.addWidget(self.lineEditSocksPassword, 2, 5, 1, 1)
        self.checkBoxSocksListen = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxSocksListen.setObjectName(_fromUtf8("checkBoxSocksListen"))
        self.gridLayout_2.addWidget(self.checkBoxSocksListen, 3, 1, 1, 4)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 70, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 2, 0, 1, 1)
        self.tabWidgetSettings.addTab(self.tabNetworkSettings, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(203, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_6.addWidget(self.label_9, 1, 1, 1, 1)
        self.lineEditTotalDifficulty = QtGui.QLineEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTotalDifficulty.sizePolicy().hasHeightForWidth())
        self.lineEditTotalDifficulty.setSizePolicy(sizePolicy)
        self.lineEditTotalDifficulty.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEditTotalDifficulty.setObjectName(_fromUtf8("lineEditTotalDifficulty"))
        self.gridLayout_6.addWidget(self.lineEditTotalDifficulty, 1, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(203, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 3, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_6.addWidget(self.label_11, 3, 1, 1, 1)
        self.lineEditSmallMessageDifficulty = QtGui.QLineEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSmallMessageDifficulty.sizePolicy().hasHeightForWidth())
        self.lineEditSmallMessageDifficulty.setSizePolicy(sizePolicy)
        self.lineEditSmallMessageDifficulty.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEditSmallMessageDifficulty.setObjectName(_fromUtf8("lineEditSmallMessageDifficulty"))
        self.gridLayout_6.addWidget(self.lineEditSmallMessageDifficulty, 3, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_6.addWidget(self.label_12, 4, 0, 1, 3)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_6.addWidget(self.label_10, 2, 0, 1, 3)
        self.tabWidgetSettings.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 3)
        spacerItem5 = QtGui.QSpacerItem(102, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 1, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_7.addWidget(self.label_13, 1, 1, 1, 1)
        self.lineEditMaxAcceptableTotalDifficulty = QtGui.QLineEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditMaxAcceptableTotalDifficulty.sizePolicy().hasHeightForWidth())
        self.lineEditMaxAcceptableTotalDifficulty.setSizePolicy(sizePolicy)
        self.lineEditMaxAcceptableTotalDifficulty.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEditMaxAcceptableTotalDifficulty.setObjectName(_fromUtf8("lineEditMaxAcceptableTotalDifficulty"))
        self.gridLayout_7.addWidget(self.lineEditMaxAcceptableTotalDifficulty, 1, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(102, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem6, 2, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_7.addWidget(self.label_14, 2, 1, 1, 1)
        self.lineEditMaxAcceptableSmallMessageDifficulty = QtGui.QLineEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditMaxAcceptableSmallMessageDifficulty.sizePolicy().hasHeightForWidth())
        self.lineEditMaxAcceptableSmallMessageDifficulty.setSizePolicy(sizePolicy)
        self.lineEditMaxAcceptableSmallMessageDifficulty.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEditMaxAcceptableSmallMessageDifficulty.setObjectName(_fromUtf8("lineEditMaxAcceptableSmallMessageDifficulty"))
        self.gridLayout_7.addWidget(self.lineEditMaxAcceptableSmallMessageDifficulty, 2, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 147, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem7, 3, 1, 1, 1)
        self.tabWidgetSettings.addTab(self.tab_2, _fromUtf8(""))
        self.tabNamecoin = QtGui.QWidget()
        self.tabNamecoin.setObjectName(_fromUtf8("tabNamecoin"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tabNamecoin)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem8, 2, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.tabNamecoin)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_8.addWidget(self.label_16, 0, 0, 1, 3)
        self.label_17 = QtGui.QLabel(self.tabNamecoin)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_8.addWidget(self.label_17, 2, 1, 1, 1)
        self.lineEditNamecoinHost = QtGui.QLineEdit(self.tabNamecoin)
        self.lineEditNamecoinHost.setObjectName(_fromUtf8("lineEditNamecoinHost"))
        self.gridLayout_8.addWidget(self.lineEditNamecoinHost, 2, 2, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem9, 3, 0, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem10, 4, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.tabNamecoin)
        self.label_18.setEnabled(True)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_8.addWidget(self.label_18, 3, 1, 1, 1)
        self.lineEditNamecoinPort = QtGui.QLineEdit(self.tabNamecoin)
        self.lineEditNamecoinPort.setObjectName(_fromUtf8("lineEditNamecoinPort"))
        self.gridLayout_8.addWidget(self.lineEditNamecoinPort, 3, 2, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem11, 8, 1, 1, 1)
        self.labelNamecoinUser = QtGui.QLabel(self.tabNamecoin)
        self.labelNamecoinUser.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNamecoinUser.setObjectName(_fromUtf8("labelNamecoinUser"))
        self.gridLayout_8.addWidget(self.labelNamecoinUser, 4, 1, 1, 1)
        self.lineEditNamecoinUser = QtGui.QLineEdit(self.tabNamecoin)
        self.lineEditNamecoinUser.setObjectName(_fromUtf8("lineEditNamecoinUser"))
        self.gridLayout_8.addWidget(self.lineEditNamecoinUser, 4, 2, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem12, 5, 0, 1, 1)
        self.labelNamecoinPassword = QtGui.QLabel(self.tabNamecoin)
        self.labelNamecoinPassword.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNamecoinPassword.setObjectName(_fromUtf8("labelNamecoinPassword"))
        self.gridLayout_8.addWidget(self.labelNamecoinPassword, 5, 1, 1, 1)
        self.lineEditNamecoinPassword = QtGui.QLineEdit(self.tabNamecoin)
        self.lineEditNamecoinPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEditNamecoinPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditNamecoinPassword.setObjectName(_fromUtf8("lineEditNamecoinPassword"))
        self.gridLayout_8.addWidget(self.lineEditNamecoinPassword, 5, 2, 1, 1)
        self.labelNamecoinTestResult = QtGui.QLabel(self.tabNamecoin)
        self.labelNamecoinTestResult.setText(_fromUtf8(""))
        self.labelNamecoinTestResult.setObjectName(_fromUtf8("labelNamecoinTestResult"))
        self.gridLayout_8.addWidget(self.labelNamecoinTestResult, 7, 0, 1, 2)
        self.pushButtonNamecoinTest = QtGui.QPushButton(self.tabNamecoin)
        self.pushButtonNamecoinTest.setObjectName(_fromUtf8("pushButtonNamecoinTest"))
        self.gridLayout_8.addWidget(self.pushButtonNamecoinTest, 7, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_21 = QtGui.QLabel(self.tabNamecoin)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout.addWidget(self.label_21)
        self.radioButtonNamecoinNamecoind = QtGui.QRadioButton(self.tabNamecoin)
        self.radioButtonNamecoinNamecoind.setObjectName(_fromUtf8("radioButtonNamecoinNamecoind"))
        self.horizontalLayout.addWidget(self.radioButtonNamecoinNamecoind)
        self.radioButtonNamecoinNmcontrol = QtGui.QRadioButton(self.tabNamecoin)
        self.radioButtonNamecoinNmcontrol.setObjectName(_fromUtf8("radioButtonNamecoinNmcontrol"))
        self.horizontalLayout.addWidget(self.radioButtonNamecoinNmcontrol)
        self.gridLayout_8.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.tabWidgetSettings.addTab(self.tabNamecoin, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidgetSettings, 0, 0, 1, 1)
#this line existed before
#my new implementation starts here
        self.tabResendingMessagesAdjustment=QtGui.QWidget()
        self.tabResendingMessagesAdjustment.setObjectName(_fromUtf8("tabResendingMessagesAdjustment"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tabResendingMessagesAdjustment)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_19 = QtGui.QLabel(self.tabResendingMessagesAdjustment)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_9.addWidget(self.label_19, 0, 0, 1, 0)
        spacerItem13 = QtGui.QSpacerItem(102, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem13, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_20 = QtGui.QLabel(self.tabResendingMessagesAdjustment)
        self.label_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_9.addWidget(self.label_20, 2, 0, 1, 1)
        self.lineEditHours = QtGui.QLineEdit(self.tabResendingMessagesAdjustment)
        self.lineEditHours.setMaximumSize(QtCore.QSize(33, 16777))
        self.lineEditHours.setObjectName(_fromUtf8("lineEditHours"))
        self.gridLayout_9.addWidget(self.lineEditHours, 2, 1, 1, 1)
        self.label_22 = QtGui.QLabel(self.tabResendingMessagesAdjustment)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_9.addWidget(self.label_22, 2, 2, 1, 1)
        self.lineEditDays = QtGui.QLineEdit(self.tabResendingMessagesAdjustment)
        self.lineEditDays.setMaximumSize(QtCore.QSize(33, 16777))
        self.lineEditDays.setObjectName(_fromUtf8("lineEditDays"))
        self.gridLayout_9.addWidget(self.lineEditDays, 2, 3, 1, 1)
        self.label_23 = QtGui.QLabel(self.tabResendingMessagesAdjustment)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_9.addWidget(self.label_23, 2, 4, 1, 1)
        self.lineEditMonths = QtGui.QLineEdit(self.tabResendingMessagesAdjustment)
        self.lineEditMonths.setMaximumSize(QtCore.QSize(33, 16777))
        self.lineEditMonths.setObjectName(_fromUtf8("lineEditMonths"))
        self.gridLayout_9.addWidget(self.lineEditMonths, 2, 5, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(20, 147, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem15, 3, 1, 1, 1)
        self.tabWidgetSettings.addTab(self.tabResendingMessagesAdjustment, _fromUtf8(""))
        #my new implementation stops here, it wasn't line here 
        self.retranslateUi(settingsDialog)
        self.tabWidgetSettings.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), settingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), settingsDialog.reject)
        QtCore.QObject.connect(self.checkBoxAuthentication, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEditSocksUsername.setEnabled)
        QtCore.QObject.connect(self.checkBoxAuthentication, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEditSocksPassword.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)
        settingsDialog.setTabOrder(self.tabWidgetSettings, self.checkBoxStartOnLogon)
        settingsDialog.setTabOrder(self.checkBoxStartOnLogon, self.checkBoxStartInTray)
        settingsDialog.setTabOrder(self.checkBoxStartInTray, self.checkBoxMinimizeToTray)
        settingsDialog.setTabOrder(self.checkBoxMinimizeToTray, self.checkBoxShowTrayNotifications)
        settingsDialog.setTabOrder(self.checkBoxShowTrayNotifications, self.lineEditTCPPort)
        settingsDialog.setTabOrder(self.lineEditTCPPort, self.comboBoxProxyType)
        settingsDialog.setTabOrder(self.comboBoxProxyType, self.lineEditSocksHostname)
        settingsDialog.setTabOrder(self.lineEditSocksHostname, self.lineEditSocksPort)
        settingsDialog.setTabOrder(self.lineEditSocksPort, self.checkBoxAuthentication)
        settingsDialog.setTabOrder(self.checkBoxAuthentication, self.lineEditSocksUsername)
        settingsDialog.setTabOrder(self.lineEditSocksUsername, self.lineEditSocksPassword)
        settingsDialog.setTabOrder(self.lineEditSocksPassword, self.checkBoxSocksListen)
        settingsDialog.setTabOrder(self.checkBoxSocksListen, self.buttonBox)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Settings", None))
        self.checkBoxStartOnLogon.setText(_translate("settingsDialog", "Start Bitmessage on user login", None))
        self.checkBoxStartInTray.setText(_translate("settingsDialog", "Start Bitmessage in the tray (don\'t show main window)", None))
        self.checkBoxMinimizeToTray.setText(_translate("settingsDialog", "Minimize to tray", None))
        self.checkBoxShowTrayNotifications.setText(_translate("settingsDialog", "Show notification when message received", None))
        self.checkBoxPortableMode.setText(_translate("settingsDialog", "Run in Portable Mode", None))
        self.PortableModeDescription.setText(_translate("settingsDialog", "In Portable Mode, messages and config files are stored in the same directory as the program rather than the normal application-data folder. This makes it convenient to run Bitmessage from a USB thumb drive.", None))
        self.checkBoxWillinglySendToMobile.setText(_translate("settingsDialog", "Willingly include unencrypted destination address when sending to a mobile device", None))
        self.groupBox.setTitle(_translate("settingsDialog", "Interface Language", None))
        self.languageComboBox.setItemText(0, _translate("settingsDialog", "System Settings", "system"))
        self.languageComboBox.setItemText(1, _translate("settingsDialog", "English", "en"))
        self.languageComboBox.setItemText(2, _translate("settingsDialog", "Esperanto", "eo"))
        self.languageComboBox.setItemText(3, _translate("settingsDialog", "Français", "fr"))
        self.languageComboBox.setItemText(4, _translate("settingsDialog", "Deutsch", "de"))
        self.languageComboBox.setItemText(5, _translate("settingsDialog", "Español", "es"))
        self.languageComboBox.setItemText(6, _translate("settingsDialog", "Русский", "ru"))
        self.languageComboBox.setItemText(7, _translate("settingsDialog", "Pirate English", "en_pirate"))
        self.languageComboBox.setItemText(8, _translate("settingsDialog", "Other (set in keys.dat)", "other"))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabUserInterface), _translate("settingsDialog", "User Interface", None))
        self.groupBox1.setTitle(_translate("settingsDialog", "Listening port", None))
        self.label.setText(_translate("settingsDialog", "Listen for connections on port:", None))
        self.groupBox_2.setTitle(_translate("settingsDialog", "Proxy server / Tor", None))
        self.label_2.setText(_translate("settingsDialog", "Type:", None))
        self.comboBoxProxyType.setItemText(0, _translate("settingsDialog", "none", None))
        self.comboBoxProxyType.setItemText(1, _translate("settingsDialog", "SOCKS4a", None))
        self.comboBoxProxyType.setItemText(2, _translate("settingsDialog", "SOCKS5", None))
        self.label_3.setText(_translate("settingsDialog", "Server hostname:", None))
        self.label_4.setText(_translate("settingsDialog", "Port:", None))
        self.checkBoxAuthentication.setText(_translate("settingsDialog", "Authentication", None))
        self.label_5.setText(_translate("settingsDialog", "Username:", None))
        self.label_6.setText(_translate("settingsDialog", "Pass:", None))
        self.checkBoxSocksListen.setText(_translate("settingsDialog", "Listen for incoming connections when using proxy", None))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabNetworkSettings), _translate("settingsDialog", "Network Settings", None))
        self.label_8.setText(_translate("settingsDialog", "When someone sends you a message, their computer must first complete some work. The difficulty of this work, by default, is 1. You may raise this default for new addresses you create by changing the values here. Any new addresses you create will require senders to meet the higher difficulty. There is one exception: if you add a friend or acquaintance to your address book, Bitmessage will automatically notify them when you next send a message that they need only complete the minimum amount of work: difficulty 1. ", None))
        self.label_9.setText(_translate("settingsDialog", "Total difficulty:", None))
        self.label_11.setText(_translate("settingsDialog", "Small message difficulty:", None))
        self.label_12.setText(_translate("settingsDialog", "The \'Small message difficulty\' mostly only affects the difficulty of sending small messages. Doubling this value makes it almost twice as difficult to send a small message but doesn\'t really affect large messages.", None))
        self.label_10.setText(_translate("settingsDialog", "The \'Total difficulty\' affects the absolute amount of work the sender must complete. Doubling this value doubles the amount of work.", None))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tab), _translate("settingsDialog", "Demanded difficulty", None))
        self.label_15.setText(_translate("settingsDialog", "Here you may set the maximum amount of work you are willing to do to send a message to another person. Setting these values to 0 means that any value is acceptable.", None))
        self.label_13.setText(_translate("settingsDialog", "Maximum acceptable total difficulty:", None))
        #my new implementation starts here,it wasn't line here
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabResendingMessagesAdjustment), _translate("settingsDialog", "Adjusting time period for resending messages", None))
        self.label_19.setText(_translate("settingsDialog", "<html><head/><body><p>If you send a message to someone and he is offline for more than two days, Bitmessage  will send the message again after an additional two days. This will be continued with exponential backoff forever. Messages  will continue to be sent after 4, 8,16 days and so on until the receiver get them. </p><p> Here you can adjust Bitmessage to stop trying to send messages after X hours/days/months. This time period needs to be longer than 5 days.</p></body></html>", None))
        self.label_20.setText(_translate("settingsDialog", "Time in hours/days/months:", None))
        self.label_22.setText(_translate("settingsDialog", "/", None))
        self.label_23.setText(_translate("settingsDialog", "/", None))
        #my new implementation stops here, it wasn't line here
        self.label_14.setText(_translate("settingsDialog", "Maximum acceptable small message difficulty:", None))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tab_2), _translate("settingsDialog", "Max acceptable difficulty", None))
        self.label_16.setText(_translate("settingsDialog", "<html><head/><body><p>Bitmessage can utilize a different Bitcoin-based program called Namecoin to make addresses human-friendly. For example, instead of having to tell your friend your long Bitmessage address, you can simply tell him to send a message to <span style=\" font-style:italic;\">test. </span></p><p>(Getting your own Bitmessage address into Namecoin is still rather difficult).</p><p>Bitmessage can use either namecoind directly or a running nmcontrol instance.</p></body></html>", None))
        self.label_17.setText(_translate("settingsDialog", "Host:", None))
        self.label_18.setText(_translate("settingsDialog", "Port:", None))
        self.labelNamecoinUser.setText(_translate("settingsDialog", "Username:", None))
        self.labelNamecoinPassword.setText(_translate("settingsDialog", "Password:", None))
        self.pushButtonNamecoinTest.setText(_translate("settingsDialog", "Test", None))
        self.label_21.setText(_translate("settingsDialog", "Connect to:", None))
        self.radioButtonNamecoinNamecoind.setText(_translate("settingsDialog", "Namecoind", None))
        self.radioButtonNamecoinNmcontrol.setText(_translate("settingsDialog", "NMControl", None))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabNamecoin), _translate("settingsDialog", "Namecoin integration", None))

