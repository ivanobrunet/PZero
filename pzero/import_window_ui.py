# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImportOptionsWindow(object):
    def setupUi(self, ImportOptionsWindow):
        ImportOptionsWindow.setObjectName("ImportOptionsWindow")
        ImportOptionsWindow.resize(900, 818)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImportOptionsWindow.sizePolicy().hasHeightForWidth())
        ImportOptionsWindow.setSizePolicy(sizePolicy)
        ImportOptionsWindow.setMinimumSize(QtCore.QSize(900, 690))
        ImportOptionsWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ImportOptionsWindow.setBaseSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(ImportOptionsWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setBaseSize(QtCore.QSize(900, 600))
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dataView = QtWidgets.QTableView(self.centralwidget)
        self.dataView.setObjectName("dataView")
        self.horizontalLayout.addWidget(self.dataView)
        self.OptionsWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptionsWidget.sizePolicy().hasHeightForWidth())
        self.OptionsWidget.setSizePolicy(sizePolicy)
        self.OptionsWidget.setBaseSize(QtCore.QSize(0, 0))
        self.OptionsWidget.setObjectName("OptionsWidget")
        self.OptionsLayout = QtWidgets.QVBoxLayout(self.OptionsWidget)
        self.OptionsLayout.setObjectName("OptionsLayout")
        self.OptionsLabel = QtWidgets.QLabel(self.OptionsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptionsLabel.sizePolicy().hasHeightForWidth())
        self.OptionsLabel.setSizePolicy(sizePolicy)
        self.OptionsLabel.setObjectName("OptionsLabel")
        self.OptionsLayout.addWidget(self.OptionsLabel, 0, QtCore.Qt.AlignHCenter)
        self.ImportGroupBox = QtWidgets.QGroupBox(self.OptionsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImportGroupBox.sizePolicy().hasHeightForWidth())
        self.ImportGroupBox.setSizePolicy(sizePolicy)
        self.ImportGroupBox.setFlat(False)
        self.ImportGroupBox.setCheckable(False)
        self.ImportGroupBox.setObjectName("ImportGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ImportGroupBox)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PathlineEdit = QtWidgets.QLineEdit(self.ImportGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PathlineEdit.sizePolicy().hasHeightForWidth())
        self.PathlineEdit.setSizePolicy(sizePolicy)
        self.PathlineEdit.setMaxLength(32767)
        self.PathlineEdit.setClearButtonEnabled(False)
        self.PathlineEdit.setObjectName("PathlineEdit")
        self.horizontalLayout_3.addWidget(self.PathlineEdit)
        self.PathtoolButton = QtWidgets.QToolButton(self.ImportGroupBox)
        self.PathtoolButton.setObjectName("PathtoolButton")
        self.horizontalLayout_3.addWidget(self.PathtoolButton)
        self.OptionsLayout.addWidget(self.ImportGroupBox, 0, QtCore.Qt.AlignHCenter)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(14, -1, 21, 6)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.StartColLabel = QtWidgets.QLabel(self.OptionsWidget)
        self.StartColLabel.setObjectName("StartColLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.StartColLabel)
        self.StartColspinBox = QtWidgets.QSpinBox(self.OptionsWidget)
        self.StartColspinBox.setSingleStep(1)
        self.StartColspinBox.setProperty("value", 0)
        self.StartColspinBox.setObjectName("StartColspinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.StartColspinBox)
        self.EndColLabel = QtWidgets.QLabel(self.OptionsWidget)
        self.EndColLabel.setObjectName("EndColLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.EndColLabel)
        self.EndColspinBox = QtWidgets.QSpinBox(self.OptionsWidget)
        self.EndColspinBox.setProperty("value", 3)
        self.EndColspinBox.setObjectName("EndColspinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.EndColspinBox)
        self.HeaderRowLabel = QtWidgets.QLabel(self.OptionsWidget)
        self.HeaderRowLabel.setObjectName("HeaderRowLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.HeaderRowLabel)
        self.HeaderspinBox = QtWidgets.QSpinBox(self.OptionsWidget)
        self.HeaderspinBox.setProperty("value", 0)
        self.HeaderspinBox.setObjectName("HeaderspinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.HeaderspinBox)
        self.StartOnLabel = QtWidgets.QLabel(self.OptionsWidget)
        self.StartOnLabel.setObjectName("StartOnLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.StartOnLabel)
        self.StartRowspinBox = QtWidgets.QSpinBox(self.OptionsWidget)
        self.StartRowspinBox.setProperty("value", 0)
        self.StartRowspinBox.setObjectName("StartRowspinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.StartRowspinBox)
        self.EndOnLabel = QtWidgets.QLabel(self.OptionsWidget)
        self.EndOnLabel.setObjectName("EndOnLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.EndOnLabel)
        self.EndRowspinBox = QtWidgets.QSpinBox(self.OptionsWidget)
        self.EndRowspinBox.setMinimum(-1)
        self.EndRowspinBox.setMaximum(100)
        self.EndRowspinBox.setProperty("value", 100)
        self.EndRowspinBox.setObjectName("EndRowspinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.EndRowspinBox)
        self.SeparatoLabel = QtWidgets.QLabel(self.OptionsWidget)
        self.SeparatoLabel.setObjectName("SeparatoLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.SeparatoLabel)
        self.SeparatorcomboBox = QtWidgets.QComboBox(self.OptionsWidget)
        self.SeparatorcomboBox.setEditable(True)
        # self.SeparatorcomboBox.setPlaceholderText("")
        self.SeparatorcomboBox.setObjectName("SeparatorcomboBox")
        self.SeparatorcomboBox.addItem("")
        self.SeparatorcomboBox.addItem("")
        self.SeparatorcomboBox.addItem("")
        self.SeparatorcomboBox.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.SeparatorcomboBox)
        self.OptionsLayout.addLayout(self.formLayout)
        self.DataGroup = QtWidgets.QWidget(self.OptionsWidget)
        self.DataGroup.setObjectName("DataGroup")
        self.DataLayout = QtWidgets.QHBoxLayout(self.DataGroup)
        self.DataLayout.setObjectName("DataLayout")
        self.PreviewButton = QtWidgets.QPushButton(self.DataGroup)
        self.PreviewButton.setObjectName("PreviewButton")
        self.DataLayout.addWidget(self.PreviewButton)
        self.assignDataButton = QtWidgets.QPushButton(self.DataGroup)
        self.assignDataButton.setObjectName("assignDataButton")
        self.DataLayout.addWidget(self.assignDataButton)
        self.OptionsLayout.addWidget(self.DataGroup)
        self.ConfirmBox = QtWidgets.QDialogButtonBox(self.OptionsWidget)
        self.ConfirmBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.ConfirmBox.setCenterButtons(True)
        self.ConfirmBox.setObjectName("ConfirmBox")
        self.OptionsLayout.addWidget(self.ConfirmBox)
        self.horizontalLayout.addWidget(self.OptionsWidget)
        ImportOptionsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImportOptionsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        ImportOptionsWindow.setMenuBar(self.menubar)
        self.actionImport = QtWidgets.QAction(ImportOptionsWindow)
        self.actionImport.setObjectName("actionImport")

        self.retranslateUi(ImportOptionsWindow)
        QtCore.QMetaObject.connectSlotsByName(ImportOptionsWindow)

    def retranslateUi(self, ImportOptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        ImportOptionsWindow.setWindowTitle(_translate("ImportOptionsWindow", "Import options"))
        self.OptionsLabel.setText(_translate("ImportOptionsWindow", "Import options"))
        self.PathlineEdit.setPlaceholderText(_translate("ImportOptionsWindow", "file path..."))
        self.PathtoolButton.setText(_translate("ImportOptionsWindow", "..."))
        self.StartColLabel.setText(_translate("ImportOptionsWindow", "Start from column"))
        self.EndColLabel.setText(_translate("ImportOptionsWindow", "End on column"))
        self.HeaderRowLabel.setText(_translate("ImportOptionsWindow", "Header line"))
        self.StartOnLabel.setText(_translate("ImportOptionsWindow", "Start from line"))
        self.EndOnLabel.setText(_translate("ImportOptionsWindow", "End on line"))
        self.SeparatoLabel.setText(_translate("ImportOptionsWindow", "Separator"))
        self.SeparatorcomboBox.setCurrentText(_translate("ImportOptionsWindow", "<space>"))
        self.SeparatorcomboBox.setItemText(0, _translate("ImportOptionsWindow", "<space>"))
        self.SeparatorcomboBox.setItemText(1, _translate("ImportOptionsWindow", "<comma>"))
        self.SeparatorcomboBox.setItemText(2, _translate("ImportOptionsWindow", "<semi-col>"))
        self.SeparatorcomboBox.setItemText(3, _translate("ImportOptionsWindow", "<tab>"))
        self.PreviewButton.setText(_translate("ImportOptionsWindow", "Preview"))
        self.assignDataButton.setText(_translate("ImportOptionsWindow", "Assign data"))
        self.actionImport.setText(_translate("ImportOptionsWindow", "Import"))
