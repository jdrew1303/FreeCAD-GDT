#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2016 Juan Vanyo Cerda <juavacer@inf.upv.es>             *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************
import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui,QtCore
from GDT import *

listOfIcons = [':/dd/icons/datumFeature.svg',':/dd/icons/datumSystem.svg',':/dd/icons/geometricTolerance.svg',':/dd/icons/annotationPlane.svg']

listOfCharacteristics = ['Straightness', 'Flatness', 'Circularity', 'Cylindricity', 'Profile of a line', 'Profile of a surface', 'Perpendicularity', 'Angularity', 'Parallelism', 'Symmetry', 'Position', 'Concentricity','Circular run-out', 'Total run-out']
listOfIconsOfCharacteristic = [':/dd/icons/Characteristic/straightness.svg', ':/dd/icons/Characteristic/flatness.svg', ':/dd/icons/Characteristic/circularity.svg', ':/dd/icons/Characteristic/cylindricity.svg', ':/dd/icons/Characteristic/profileOfALine.svg', ':/dd/icons/Characteristic/profileOfASurface.svg', ':/dd/icons/Characteristic/perpendicularity.svg', ':/dd/icons/Characteristic/angularity.svg', ':/dd/icons/Characteristic/parallelism.svg', ':/dd/icons/Characteristic/symmetry.svg', ':/dd/icons/Characteristic/position.svg', ':/dd/icons/Characteristic/concentricity.svg',':/dd/icons/Characteristic/circularRunOut.svg', ':/dd/icons/Characteristic/totalRunOut.svg']

listOfCharacteristics2 = ['','','','','','','','']
listOfIconsOfFeatureControlFrame = ['', ':/dd/icons/FeatureControlFrame/freeState.svg', ':/dd/icons/FeatureControlFrame/leastMaterialCondition.svg', ':/dd/icons/FeatureControlFrame/maximumMaterialCondition.svg', ':/dd/icons/FeatureControlFrame/projectedToleranceZone.svg', ':/dd/icons/FeatureControlFrame/regardlessOfFeatureSize.svg', ':/dd/icons/FeatureControlFrame/tangentPlane.svg', ':/dd/icons/FeatureControlFrame/unequalBilateral.svg']
listOfToolTips = ['Feature control frame', 'Free state', 'Least material condition', 'Maximum material condition', 'Projected tolerance zone', 'Regardless of feature size', 'Tangent plane', 'Unequal Bilateral']

textNameList = []
textDSList = []
primaryList = []
secondaryList = []
tertiaryList = []
comboList = []
characteristicList = []
toleranceValueList = []
featureControlFrameList = []
datumSystemList = []

class InventoryCommand:
    def __init__(self):
        self.iconPath = ':/dd/icons/inventory.svg'
        self.toolTip = 'Inventory of the elements of GD&T'

    def Activated(self):
        Gui.Control.showDialog( GDTGuiClass() )

    def GetResources(self):
        return {
            'Pixmap' : self.iconPath,
            'MenuText': self.toolTip,
            'ToolTip':  self.toolTip
            }

    def IsActive(self):
        if FreeCADGui.ActiveDocument:
            return True
        else:
            return False

class GDTGuiClass:

    def __init__(self):
        global textDSList, primaryList, secondaryList, tertiaryList, textNameList, inventory, comboList, characteristicList, toleranceValueList, featureControlFrameList, datumSystemList
        self.widgetsGDT = []
        primaryList = []
        secondaryList = []
        tertiaryList = []
        textNameList = []
        textDSList = []
        comboList = []
        characteristicList = []
        toleranceValueList = []
        featureControlFrameList = []
        datumSystemList = []
        for i in range(len(inventory)):
            if str(inventory[i][0]).find('1') == 0 or str(inventory[i][0]).find('2') == 0 or str(inventory[i][0]).find('3') == 0 or str(inventory[i][0]).find('4') == 0:
                self.widget = QtGui.QWidget()
                if len(inventory[i][1]) > 4:
                    textNameList.append((inventory[i][1])[:inventory[i][1].find(':')])
                else:
                    textNameList.append((inventory[i][1]))
                if inventory[i][0] == 2:
                    textDS=['','','']
                    separator = ' | '
                    pos = self.getPos(i, listDS)
                    if len(inventory[i]) > 2:
                        textDS[0] = inventory[inventory[i][2]][1]
                        if len(inventory[i]) > 3:
                            textDS[1] = inventory[inventory[i][3]][1]
                            if len(inventory[i]) > 4:
                                textDS[2] = inventory[inventory[i][4]][1]
                                inventory[i][1] = textNameList[i]+ ': ' + separator.join(textDS)
                                listDS[pos][1] = textNameList[i]+ ': ' + separator.join(textDS)
                            else:
                                inventory[i][1] = textNameList[i]+ ': ' + separator.join([textDS[0], textDS[1]])
                                listDS[pos][1] = textNameList[i]+ ': ' + separator.join([textDS[0], textDS[1]])
                        else:
                            inventory[i][1] = textNameList[i]+ ': ' + textDS[0]
                            listDS[pos][1] = textNameList[i]+ ': ' + textDS[0]
                    else:
                        inventory[i][1] = textNameList[i]
                        listDS[pos][1] = textNameList[i]
                self.widget.title = inventory[i][1]
                primaryList.append(None)
                secondaryList.append(None)
                tertiaryList.append(None)
                textDSList.append(['','',''])
                comboList.append(['','','','',''])
                characteristicList.append(0)
                toleranceValueList.append('0.0')
                featureControlFrameList.append(0)
                datumSystemList.append(None)
                if str(inventory[i][0]).find('3') == 0:
                    iconPath = listOfIconsOfCharacteristic[ inventory[i][2] ]
                else:
                    iconPath = listOfIcons[ inventory[i][0] - 1 ]
                self.widget.setWindowTitle( self.widget.title )
                self.widget.setWindowIcon( QtGui.QIcon( iconPath ) )
                self.widgetsGDT.append(self.widget)
                self.widgetsGDT[i].gdtID = inventory[i][0]
                self.parent = self.widgetsGDT[i]
                self.dialogWidgets = []
                vbox = QtGui.QVBoxLayout(self.parent)
                hbox = QtGui.QHBoxLayout(self.parent)

                if str(inventory[i][0]).find('1') == 0:
                    self.dialogWidgets.append(textLabelWidget_inv(Text = 'Datum feature:', Mask='>A', Parent = self.parent, IndexInv = i))

                if str(inventory[i][0]).find('2') == 0:
                    self.dialogWidgets.append(textLabelWidget_inv(Text = 'Name:', Mask='NNNn', Parent = self.parent, IndexInv = i))
                    self.dialogWidgets.append( groupBoxWidget_inv(Text='Constituents', List=[comboLabelWidget_inv(Text='Primary:',List=listDF, Parent = self.parent, IndexInv = i),comboLabelWidget_inv(Text='Secondary:',List=listDF, Parent = self.parent, IndexInv = i), comboLabelWidget_inv(Text='Tertiary:',List=listDF, Parent = self.parent, IndexInv = i)], Parent = self.parent, IndexInv = i) )

                if str(inventory[i][0]).find('3') == 0:
                    self.dialogWidgets.append(textLabelWidget_inv(Text = 'Name:', Mask='NNNn', Parent = self.parent, IndexInv = i))
                    self.dialogWidgets.append( comboLabelWidget_inv(Text='Characteristic:', List=listOfCharacteristics, Icons=listOfIconsOfCharacteristic, Parent = self.parent, IndexInv = i) )
                    self.dialogWidgets.append( textLabeCombolWidget_inv(Text='Tolerance value:', Mask='00.00', List=listOfCharacteristics2, Icons=listOfIconsOfFeatureControlFrame, ToolTip=listOfToolTips, Parent = self.parent, IndexInv = i) ) #http://doc.qt.io/qt-5/qlineedit.html#inputMask-prop
                    self.dialogWidgets.append( comboLabelWidget_inv(Text='Datum system:', List=listDS, Parent = self.parent, IndexInv = i) )

                if str(inventory[i][0]).find('4') == 0:
                    self.dialogWidgets.append(textLabelWidget_inv(Text = 'Name:', Mask='NNNn', Parent = self.parent, IndexInv = i))

                for widg in self.dialogWidgets:
                    w = widg.generateWidget()
                    if isinstance(w, QtGui.QLayout):
                        vbox.addLayout( w )
                    else:
                        vbox.addWidget( w )

                buttonModify = QtGui.QPushButton('Modify')
                buttonModify.clicked.connect(lambda aux = i: self.modifyFunc(aux))
                buttonDelate = QtGui.QPushButton('Delete')
                buttonDelate.clicked.connect(lambda aux = i: self.deleteFunc(aux))
                hbox.addStretch(1)
                hbox.addWidget( buttonModify )
                hbox.addWidget( buttonDelate )
                hbox.addStretch(1)
                vbox.addLayout(hbox)
                self.widget.setLayout(vbox)
        self.form = self.widgetsGDT

    def modifyFunc(self,i):
        global inventory, listDF, listDS, primaryList, secondaryList, tertiaryList, textNameList, characteristicList, toleranceValueList, featureControlFrameList, datumSystemList
        if self.widgetsGDT[i].gdtID == 1:
            prevName = inventory[i][1]
            inventory[i] = [ self.widgetsGDT[i].gdtID, textNameList[i], annotationPlane ]
            pos = self.getPos(i, listDF)
            listDF[pos] = [i, textNameList[i]]
            prevName = ' '+prevName
            for j in range(len(listDS)):
                if prevName in listDS[j][1]:
                    listDS[j][1] = listDS[j][1].replace(prevName, ' '+textNameList[i])
                    inventory[listDS[j][0]][1] = listDS[j][1]
        elif self.widgetsGDT[i].gdtID == 2:
            pos = self.getPos(i, listDS)
            separator = ' | '
            if textDSList[i][0] <> '':
                if textDSList[i][1] <> '':
                    if textDSList[i][2] <> '':
                        listDS[pos] = [ i, textNameList[i] + ': ' + separator.join(textDSList[i]) ]
                        inventory[i] = [ self.widgetsGDT[i].gdtID, textNameList[i] + ': ' + separator.join(textDSList[i]), primaryList[i], secondaryList[i], tertiaryList[i] ]
                    else:
                        listDS[pos] = [ i, textNameList[i] + ': ' + separator.join([textDSList[i][0], textDSList[i][1]]) ]
                        inventory[i] = [ self.widgetsGDT[i].gdtID, textNameList[i] + ': ' + separator.join([textDSList[i][0], textDSList[i][1]]), primaryList[i], secondaryList[i] ]
                else:
                    listDS[pos] = [ i, textNameList[i] + ': ' + textDSList[i][0] ]
                    inventory[i] = [ self.widgetsGDT[i].gdtID, textNameList[i] + ': ' + textDSList[i][0], primaryList[i] ]
            else:
                listDS[pos] = [ i, textNameList[i] ]
                inventory[i] = [ self.widgetsGDT[i].gdtID, textNameList[i] ]
        elif self.widgetsGDT[i].gdtID == 3:
            inventory[i] = [ self.widgetsGDT[i].gdtID, textNameList[i], characteristicList[i], toleranceValueList[i], featureControlFrameList[i], datumSystemList[i], annotationPlane ]
        elif self.widgetsGDT[i].gdtID == 4:
            inventory[i] = [ self.widgetsGDT[i].gdtID, textNameList[i], annotationPlane ]
        else:
            pass
        FreeCADGui.Control.closeDialog()
        Gui.Control.showDialog( GDTGuiClass() )

    def getPos(self, actualValue, List):
        for i in range(len(List)):
            if List[i][0] == actualValue:
                return i

    def deleteFunc(self,i):
        global inventory
        if self.widgetsGDT[i].gdtID == 1:
            FreeCAD.Console.PrintMessage('DF')
        elif self.widgetsGDT[i].gdtID == 2:
            FreeCAD.Console.PrintMessage('DS')
        elif self.widgetsGDT[i].gdtID == 3:
            FreeCAD.Console.PrintMessage('GT')
        elif self.widgetsGDT[i].gdtID == 4:
            FreeCAD.Console.PrintMessage('AP')
        else:
            pass

    def reject(self): #close button
        FreeCADGui.Control.closeDialog()

    def getStandardButtons(self): #http://forum.freecadweb.org/viewtopic.php?f=10&t=11801
        return 0x00200000 #close button

class textLabelWidget_inv:
    def __init__(self, Text='Label', Mask = None, Parent = None, IndexInv = 0):
        self.Text = Text
        self.Mask = Mask
        self.parent = Parent
        self.indexInv = IndexInv

    def generateWidget( self ):
        self.lineEdit = QtGui.QLineEdit(self.parent)
        if self.Mask <> None:
            self.lineEdit.setInputMask(self.Mask)
        self.lineEdit.setText(inventory[self.indexInv][1])
        self.text = inventory[self.indexInv][1]
        self.lineEdit.textChanged.connect(lambda Txt = self.text, aux = self.indexInv: self.valueChanged(Txt, aux))
        return GDTDialog_hbox_inv(self.Text, self.lineEdit, parent = self.parent)

    def valueChanged(self, argGDT, i):
        global textNameList
        textNameList[i] = argGDT.strip()

class comboLabelWidget_inv:
    def __init__(self, Text='Label', List=[[0,'']], Icons=None, ToolTip = None, Parent = None, IndexInv = 0):
        self.Text = Text
        self.List = List
        self.Icons = Icons
        self.ToolTip = ToolTip
        self.parent = Parent
        self.IndexInv = IndexInv

    def generateWidget( self ):
        global comboList
        if self.Text == 'Primary:':
            self.k=0
        elif self.Text == 'Secondary:':
            self.k=1
        elif self.Text == 'Tertiary:':
            self.k=2
        elif self.Text == 'Characteristic:':
            self.k=3
        elif self.Text == 'Datum system:':
            self.k=4
        else:
            self.k=5
        comboList[self.IndexInv][self.k] = QtGui.QComboBox(self.parent)
        for i in range(len(self.List)):
            if self.Icons <> None:
                if isinstance(self.List[len(self.List)-1], list):
                    comboList[self.IndexInv][self.k].addItem( QtGui.QIcon(self.Icons[i]), self.List[i][1] )
                else:
                    comboList[self.IndexInv][self.k].addItem( QtGui.QIcon(self.Icons[i]), self.List[i] )
            else:
                if isinstance(self.List[len(self.List)-1], list):
                    comboList[self.IndexInv][self.k].addItem( self.List[i][1] )
                else:
                    comboList[self.IndexInv][self.k].addItem( self.List[i] )
        if self.ToolTip <> None:
            comboList[self.IndexInv][self.k].setToolTip( self.ToolTip[0] )
        self.updateCurrentItem(self.IndexInv)
        if self.Text == 'Secondary:' and comboList[self.IndexInv][self.k].currentIndex() == 0 or self.Text == 'Tertiary:' and comboList[self.IndexInv][self.k].currentIndex() == 0:
            comboList[self.IndexInv][self.k].setEnabled(False)
        self.comboIndex = comboList[self.IndexInv][self.k].currentIndex()
        if self.k == 2:
            self.updateItemsEnabled(self.IndexInv, self.k)
            if comboList[self.IndexInv][0].currentIndex() <> 0:
                comboList[self.IndexInv][1].setEnabled(True)
                if comboList[self.IndexInv][1].currentIndex() <> 0:
                    comboList[self.IndexInv][2].setEnabled(True)
        comboList[self.IndexInv][self.k].activated.connect(lambda comboIndex = self.comboIndex, IndexInv = self.IndexInv: self.updateDate(comboIndex, IndexInv))

        return GDTDialog_hbox_inv(self.Text, comboList[self.IndexInv][self.k], parent = self.parent)

    def updateCurrentItem(self, IndexInv):
        global textDSList, primaryList, secondaryList, tertiaryList, comboList, characteristicList, datumSystemList
        if self.Text == 'Primary:':
            if len(inventory[IndexInv]) > 2:
                actualValue = inventory[inventory[IndexInv][2]][1]
                pos = self.getPos(actualValue)
                comboList[IndexInv][self.k].setCurrentIndex(pos)
            textDSList[IndexInv][0] = comboList[IndexInv][self.k].currentText()
            primaryList[IndexInv] = self.List[comboList[IndexInv][self.k].currentIndex()][0]
        elif self.Text == 'Secondary:':
            if len(inventory[IndexInv]) > 3:
                actualValue = inventory[inventory[IndexInv][3]][1]
                pos = self.getPos(actualValue)
                comboList[IndexInv][self.k].setCurrentIndex(pos)
            textDSList[IndexInv][1] = comboList[IndexInv][self.k].currentText()
            secondaryList[IndexInv] = self.List[comboList[IndexInv][self.k].currentIndex()][0]
        elif self.Text == 'Tertiary:':
            if len(inventory[IndexInv]) > 4:
                actualValue = inventory[inventory[IndexInv][4]][1]
                pos = self.getPos(actualValue)
                comboList[IndexInv][self.k].setCurrentIndex(pos)
            textDSList[IndexInv][2] = comboList[IndexInv][self.k].currentText()
            tertiaryList[IndexInv] = self.List[comboList[IndexInv][self.k].currentIndex()][0]
        elif self.Text == 'Characteristic:':
            pos = inventory[IndexInv][2]
            comboList[IndexInv][self.k].setCurrentIndex(pos)
            characteristicList[IndexInv] = comboList[IndexInv][self.k].currentIndex()
        elif self.Text == 'Datum system:':
            if inventory[IndexInv][5] <> None:
                actualValue = inventory[inventory[IndexInv][5]][1]
                pos = self.getPos(actualValue)
                comboList[IndexInv][self.k].setCurrentIndex(pos)
            datumSystemList[IndexInv] = self.List[comboList[IndexInv][self.k].currentIndex()][0]

    def getPos(self, actualValue):
        for i in range(len(self.List)):
            if self.List[i][1] == actualValue:
                return i

    def updateDate(self, comboIndex, IndexInv):
        global textDSList, primaryList, secondaryList, tertiaryList, characteristic, datumSystem, comboList, characteristicList, datumSystemList
        if self.ToolTip <> None:
            comboList[IndexInv][self.k].setToolTip( self.ToolTip[comboList[IndexInv][self.k].currentIndex()] )
        if self.Text == 'Primary:':
            textDSList[IndexInv][0] = comboList[IndexInv][self.k].currentText()
            primaryList[IndexInv] = self.List[comboList[IndexInv][self.k].currentIndex()][0]
            if comboList[IndexInv][self.k].currentIndex() <> 0:
                comboList[IndexInv][1].setEnabled(True)
            else:
                comboList[IndexInv][1].setEnabled(False)
                comboList[IndexInv][2].setEnabled(False)
                comboList[IndexInv][1].setCurrentIndex(0)
                comboList[IndexInv][2].setCurrentIndex(0)
                textDSList[IndexInv][1] = ''
                textDSList[IndexInv][2] = ''
                secondaryList[IndexInv] = None
                tertiaryList[IndexInv] = None
            self.updateItemsEnabled(IndexInv, self.k)
        elif self.Text == 'Secondary:':
            textDSList[IndexInv][1] = comboList[IndexInv][self.k].currentText()
            secondaryList[IndexInv] = self.List[comboList[IndexInv][self.k].currentIndex()][0]
            if comboList[IndexInv][self.k].currentIndex() <> 0:
                comboList[IndexInv][2].setEnabled(True)
            else:
                comboList[IndexInv][2].setEnabled(False)
                comboList[IndexInv][2].setCurrentIndex(0)
                textDSList[IndexInv][2] = ''
                tertiaryList[IndexInv] = None
            self.updateItemsEnabled(IndexInv, self.k)
        elif self.Text == 'Tertiary:':
            textDSList[IndexInv][2] = comboList[IndexInv][self.k].currentText()
            tertiaryList[IndexInv] = self.List[comboList[IndexInv][self.k].currentIndex()][0]
            self.updateItemsEnabled(IndexInv, self.k)
        elif self.Text == 'Characteristic:':
            characteristicList[IndexInv] = comboList[IndexInv][self.k].currentIndex()
        elif self.Text == 'Datum system:':
            datumSystemList[IndexInv] = self.List[comboList[IndexInv][self.k].currentIndex()][0]

    def updateItemsEnabled(self, IndexInv, comboIndex):
        comboIndex0 = comboIndex
        comboIndex1 = (comboIndex+1) % 3
        comboIndex2 = (comboIndex+2) % 3

        for i in range(comboList[IndexInv][comboIndex0].count()):
            comboList[IndexInv][comboIndex0].model().item(i).setEnabled(True)
        if comboList[IndexInv][comboIndex1].currentIndex() <> 0:
            comboList[IndexInv][comboIndex0].model().item(comboList[IndexInv][comboIndex1].currentIndex()).setEnabled(False)
        if comboList[IndexInv][comboIndex2].currentIndex() <> 0:
            comboList[IndexInv][comboIndex0].model().item(comboList[IndexInv][comboIndex2].currentIndex()).setEnabled(False)
        for i in range(comboList[IndexInv][comboIndex1].count()):
            comboList[IndexInv][comboIndex1].model().item(i).setEnabled(True)
        if comboList[IndexInv][comboIndex0].currentIndex() <> 0:
            comboList[IndexInv][comboIndex1].model().item(comboList[IndexInv][comboIndex0].currentIndex()).setEnabled(False)
        if comboList[IndexInv][comboIndex2].currentIndex() <> 0:
            comboList[IndexInv][comboIndex1].model().item(comboList[IndexInv][comboIndex2].currentIndex()).setEnabled(False)
        for i in range(comboList[IndexInv][comboIndex2].count()):
            comboList[IndexInv][comboIndex2].model().item(i).setEnabled(True)
        if comboList[IndexInv][comboIndex0].currentIndex() <> 0:
            comboList[IndexInv][comboIndex2].model().item(comboList[IndexInv][comboIndex0].currentIndex()).setEnabled(False)
        if comboList[IndexInv][comboIndex1].currentIndex() <> 0:
            comboList[IndexInv][comboIndex2].model().item(comboList[IndexInv][comboIndex1].currentIndex()).setEnabled(False)

class groupBoxWidget_inv:
    def __init__(self, Text='Label', List=[], Parent = None, IndexInv = 0):
        self.Text = Text
        self.List = List
        self.parent = Parent
        self.indexInv = IndexInv

    def generateWidget( self ):
        self.group = QtGui.QGroupBox(self.Text,self.parent)
        vbox = QtGui.QVBoxLayout(self.parent)
        for l in self.List:
            vbox.addLayout(l.generateWidget())
        self.group.setLayout(vbox)
        return self.group

class textLabeCombolWidget_inv:
    def __init__(self, Text='Label', Mask=None, List=[''], Icons=None, ToolTip = None, Parent = None, IndexInv = 0):
        self.Text = Text
        self.Mask = Mask
        self.List = List
        self.Icons = Icons
        self.ToolTip = ToolTip
        self.parent = Parent
        self.indexInv = IndexInv

    def generateWidget( self ):
        self.combo = QtGui.QComboBox(self.parent)
        for i in range(len(self.List)):
            if self.Icons <> None:
                self.combo.addItem( QtGui.QIcon(self.Icons[i]), self.List[i] )
            else:
                self.combo.addItem( self.List[i] )
        pos = inventory[self.indexInv][4]
        self.combo.setCurrentIndex(pos)
        if self.ToolTip <> None:
           self.combo.setToolTip( self.ToolTip[self.combo.currentIndex()] )
        self.updateDate()
        self.combo.activated.connect(self.updateDate)
        hbox = QtGui.QHBoxLayout(self.parent)
        self.lineEdit = QtGui.QLineEdit(self.parent)
        if self.Mask <> None:
            self.lineEdit.setInputMask(self.Mask)
        self.lineEdit.setText(inventory[self.indexInv][3])
        self.text = inventory[self.indexInv][3]
        toleranceValueList[self.indexInv] = self.text
        self.valueChanged(self.text, self.indexInv)
        self.lineEdit.textChanged.connect(lambda Txt = self.text, aux = self.indexInv: self.valueChanged(Txt, aux))
        textGDT = self.text.strip()
        hbox.addLayout( GDTDialog_hbox(self.Text,self.lineEdit) )
        hbox.addStretch(1)
        hbox.addWidget(self.combo)
        return hbox

    def updateDate(self):
        global featureControlFrameList
        if self.ToolTip <> None:
            self.combo.setToolTip( self.ToolTip[self.combo.currentIndex()] )
        if self.Text == 'Tolerance value:':
            featureControlFrameList[self.indexInv] = self.combo.currentIndex()

    def valueChanged(self, argGDT, i):
        global toleranceValueList
        toleranceValueList[i] = argGDT.strip()

def GDTDialog_hbox_inv( label, inputWidget, parent):
    hbox = QtGui.QHBoxLayout( parent )
    hbox.addWidget( QtGui.QLabel(label) )
    if inputWidget <> None:
        hbox.addStretch(1)
        hbox.addWidget(inputWidget)
    return hbox

FreeCADGui.addCommand('dd_inventory', InventoryCommand())
