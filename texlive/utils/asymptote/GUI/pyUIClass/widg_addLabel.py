# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/windows/widg_addLabel.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(599, 35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 35))
        Form.setMaximumSize(QtCore.QSize(16777215, 35))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtLabelText = QtWidgets.QLineEdit(Form)
        self.txtLabelText.setObjectName("txtLabelText")
        self.horizontalLayout.addWidget(self.txtLabelText)
        self.btnAdvancedEdit = QtWidgets.QPushButton(Form)
        self.btnAdvancedEdit.setMaximumSize(QtCore.QSize(25, 25))
        self.btnAdvancedEdit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdvancedEdit.setIcon(icon)
        self.btnAdvancedEdit.setFlat(True)
        self.btnAdvancedEdit.setObjectName("btnAdvancedEdit")
        self.horizontalLayout.addWidget(self.btnAdvancedEdit)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cmbAlign = QtWidgets.QComboBox(Form)
        self.cmbAlign.setObjectName("cmbAlign")
        self.cmbAlign.addItem("")
        self.cmbAlign.addItem("")
        self.cmbAlign.addItem("")
        self.cmbAlign.addItem("")
        self.cmbAlign.addItem("")
        self.cmbAlign.addItem("")
        self.cmbAlign.addItem("")
        self.cmbAlign.addItem("")
        self.cmbAlign.addItem("")
        self.cmbAlign.addItem("")
        self.horizontalLayout.addWidget(self.cmbAlign)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.cmbFontSize = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbFontSize.sizePolicy().hasHeightForWidth())
        self.cmbFontSize.setSizePolicy(sizePolicy)
        self.cmbFontSize.setEditable(True)
        self.cmbFontSize.setObjectName("cmbFontSize")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.cmbFontSize.addItem("")
        self.horizontalLayout.addWidget(self.cmbFontSize)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.txtShiftX = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtShiftX.sizePolicy().hasHeightForWidth())
        self.txtShiftX.setSizePolicy(sizePolicy)
        self.txtShiftX.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txtShiftX.setObjectName("txtShiftX")
        self.horizontalLayout.addWidget(self.txtShiftX)
        self.txtShiftY = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtShiftY.sizePolicy().hasHeightForWidth())
        self.txtShiftY.setSizePolicy(sizePolicy)
        self.txtShiftY.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txtShiftY.setObjectName("txtShiftY")
        self.horizontalLayout.addWidget(self.txtShiftY)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.txtLabelText.setToolTip(_translate("Form", "Number of Sides"))
        self.txtLabelText.setPlaceholderText(_translate("Form", "Text"))
        self.label.setText(_translate("Form", "Align"))
        self.cmbAlign.setItemText(0, _translate("Form", "Center"))
        self.cmbAlign.setItemText(1, _translate("Form", "N"))
        self.cmbAlign.setItemText(2, _translate("Form", "E"))
        self.cmbAlign.setItemText(3, _translate("Form", "W"))
        self.cmbAlign.setItemText(4, _translate("Form", "S"))
        self.cmbAlign.setItemText(5, _translate("Form", "NW"))
        self.cmbAlign.setItemText(6, _translate("Form", "NE"))
        self.cmbAlign.setItemText(7, _translate("Form", "SW"))
        self.cmbAlign.setItemText(8, _translate("Form", "SE"))
        self.cmbAlign.setItemText(9, _translate("Form", "Custom"))
        self.label_3.setText(_translate("Form", "Font Size"))
        self.cmbFontSize.setItemText(0, _translate("Form", "-"))
        self.cmbFontSize.setItemText(1, _translate("Form", "8"))
        self.cmbFontSize.setItemText(2, _translate("Form", "9"))
        self.cmbFontSize.setItemText(3, _translate("Form", "10"))
        self.cmbFontSize.setItemText(4, _translate("Form", "11"))
        self.cmbFontSize.setItemText(5, _translate("Form", "12"))
        self.cmbFontSize.setItemText(6, _translate("Form", "14"))
        self.cmbFontSize.setItemText(7, _translate("Form", "18"))
        self.cmbFontSize.setItemText(8, _translate("Form", "24"))
        self.cmbFontSize.setItemText(9, _translate("Form", "48"))
        self.cmbFontSize.setItemText(10, _translate("Form", "72"))
        self.label_2.setText(_translate("Form", "Custom Align"))
        self.txtShiftX.setPlaceholderText(_translate("Form", "Shift X"))
        self.txtShiftY.setPlaceholderText(_translate("Form", "Shift Y"))

import icons_rc
