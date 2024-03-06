from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QTabWidget, QApplication, QComboBox, QLineEdit
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
'''NOTE: all instances of matrices used are in the format [a11,a21,a31,a12,a22,a32,a13,a23,a33]'''

class matrixUI(QMainWindow):
    def __init__(self):
        super(matrixUI,self).__init__()

        uic.loadUi('matrix.ui',self)

        self.d = dict()
        self.labels = dict()

        # First Column
        for i in range(111,134,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(211,234,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(311,334,10):
            exec('label_{} = self.findChild(QLabel,\'label_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(411,435,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(511,534,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(611,634,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        # Second Column
        for i in range(112,135,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(212,235,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(312,334,10):
            exec('label_{} = self.findChild(QLabel,\'label_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(412,435,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(512,535,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        # Third Column
        for i in range(113,134,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(213,234,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(313,334,10):
            exec('label_{} = self.findChild(QLabel,\'label_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(413,434,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        for i in range(513,534,10):
            exec('label_{} = self.findChild(QLineEdit,\'lineEdit_{}\')'.format(i,i))
            exec("self.d[i] = label_{}.text()".format(i))
            exec("self.labels[i] = label_{}".format(i))
            exec("print(label_{})".format(i))

        self.calcButton = self.findChild(QPushButton,'calcButton')
        self.calcButton2 = self.findChild(QPushButton,'calcButton2')
        self.calcButton3 = self.findChild(QPushButton,'calcButton3')
        self.OPcomboplus = self.findChild(QComboBox,'OPcomboplus')
        self.detlabel = self.findChild(QLabel,'detlabel')
        self.xlabel = self.findChild(QLabel,'xlabel')
        self.ylabel = self.findChild(QLabel,'ylabel')
        self.zlabel = self.findChild(QLabel,'zlabel')
        
        #self.label_111.setEditable(True)

        self.calcButton.clicked.connect(self.calc)
        self.calcButton2.clicked.connect(self.calc2)
        self.calcButton3.clicked.connect(self.calcSimEqn)

        print(self.OPcomboplus.currentText())
        #print(self.d)

        print('self.d is',self.d)
        print('self.labels is',self.labels)

    def calc(self):
        d = dict()
        d[111] = self.labels[111].text()
        d[121] = self.labels[121].text()
        d[131] = self.labels[131].text()

        d[112] = self.labels[112].text()
        d[122] = self.labels[122].text()
        d[132] = self.labels[132].text()

        d[113] = self.labels[113].text()
        d[123] = self.labels[123].text()
        d[133] = self.labels[133].text()

        d[211] = self.labels[211].text()
        d[221] = self.labels[221].text()
        d[231] = self.labels[231].text()

        d[212] = self.labels[212].text()
        d[222] = self.labels[222].text()
        d[232] = self.labels[232].text()

        d[213] = self.labels[213].text()
        d[223] = self.labels[223].text()
        d[233] = self.labels[233].text()
        print('outp is',d)

        dint = dict()
        try:
            for i in d:
                dint[i] = int(d[i])
            print(dint)
        except:
            print('error in inputting')
        if self.OPcomboplus.currentText() == '+':
            t311 = dint[111] + dint[211]
            t312 = dint[112] + dint[212]
            t313 = dint[113] + dint[213]
            t321 = dint[121] + dint[221]
            t322 = dint[122] + dint[222]
            t323 = dint[123] + dint[223]
            t331 = dint[131] + dint[231]
            t332 = dint[132] + dint[232]
            t333 = dint[133] + dint[233]
            self.labels[311].setText(str(t311))
            self.labels[312].setText(str(t312))
            self.labels[313].setText(str(t313))
            self.labels[321].setText(str(t321))
            self.labels[322].setText(str(t322))
            self.labels[323].setText(str(t323))
            self.labels[331].setText(str(t331))
            self.labels[332].setText(str(t332))
            self.labels[333].setText(str(t333))

        if self.OPcomboplus.currentText() == '-':
            t311 = dint[111] - dint[211]
            t312 = dint[112] - dint[212]
            t313 = dint[113] - dint[213]
            t321 = dint[121] - dint[221]
            t322 = dint[122] - dint[222]
            t323 = dint[123] - dint[223]
            t331 = dint[131] - dint[231]
            t332 = dint[132] - dint[232]
            t333 = dint[133] - dint[233]
            self.labels[311].setText(str(t311))
            self.labels[312].setText(str(t312))
            self.labels[313].setText(str(t313))
            self.labels[321].setText(str(t321))
            self.labels[322].setText(str(t322))
            self.labels[323].setText(str(t323))
            self.labels[331].setText(str(t331))
            self.labels[332].setText(str(t332))
            self.labels[333].setText(str(t333))

        if self.OPcomboplus.currentText() == '*':
            # First row
            t311 = dint[111]*dint[211] + dint[112]*dint[221] + dint[113]*dint[231]
            t312 = dint[111]*dint[212] + dint[112]*dint[222] + dint[113]*dint[232]
            t313 = dint[111]*dint[213] + dint[112]*dint[223] + dint[113]*dint[233]
            # Second row
            t321 = dint[121]*dint[211] + dint[122]*dint[221] + dint[123]*dint[231]
            t322 = dint[121]*dint[212] + dint[122]*dint[222] + dint[123]*dint[232]
            t323 = dint[121]*dint[213] + dint[122]*dint[223] + dint[123]*dint[233]
            # Third row
            t331 = dint[131]*dint[211] + dint[132]*dint[221] + dint[133]*dint[231]
            t332 = dint[131]*dint[212] + dint[132]*dint[222] + dint[133]*dint[232]
            t333 = dint[131]*dint[213] + dint[132]*dint[223] + dint[133]*dint[233]

            self.labels[311].setText(str(t311))
            self.labels[312].setText(str(t312))
            self.labels[313].setText(str(t313))
            self.labels[321].setText(str(t321))
            self.labels[322].setText(str(t322))
            self.labels[323].setText(str(t323))
            self.labels[331].setText(str(t331))
            self.labels[332].setText(str(t332))
            self.labels[333].setText(str(t333))

    def calc2(self):
        print('In calc2')
        d = dict()
        d[411] = self.labels[411].text()
        d[421] = self.labels[421].text()
        d[431] = self.labels[431].text()

        d[412] = self.labels[412].text()
        d[422] = self.labels[422].text()
        d[432] = self.labels[432].text()

        d[413] = self.labels[413].text()
        d[423] = self.labels[423].text()
        d[433] = self.labels[433].text()

        dint = dict()
        try:
            for i in d:
                dint[i] = int(d[i])
            print(dint)
        except:
            print('error in inputting')
        det = self.det3(dint[411],dint[421],dint[431],dint[412],dint[422],dint[432],dint[413],dint[423],dint[433])
        self.detlabel.setText(str(det))

    def calcSimEqn(self):
        try:
            d = dict()
            B = list()
            d[511] = self.labels[511].text()
            d[521] = self.labels[521].text()
            d[531] = self.labels[531].text()

            d[512] = self.labels[512].text()
            d[522] = self.labels[522].text()
            d[532] = self.labels[532].text()

            d[513] = self.labels[513].text()
            d[523] = self.labels[523].text()
            d[533] = self.labels[533].text()
            try:
                B.append(int(self.labels[611].text()))
                B.append(int(self.labels[621].text()))
                B.append(int(self.labels[631].text()))
            except:
                print('Error in B index')
        except:
            print('Error in d indexing')

        print('Properly till here')
        dint = dict()
        A = list()
        try:
            for i in d:
                dint[i] = int(d[i])
                A.append(int(d[i]))
            print(dint)
        except:
            print('error in inputting')
        a11,a21,a31,a12,a22,a32,a13,a23,a33 = A
        detA = self.det3(a11, a21, a31, a12, a22, a32, a13, a23, a33)
        if detA != 0:
            invA = self.inverse(a11, a21, a31, a12, a22, a32, a13, a23, a33)
            t11, t21, t31, t12, t22, t32, t13, t23, t33 = invA
            b11,b21,b31 = B
            X = self.multi3x3_3x1(t11,t21,t31,t12,t22,t32,t13,t23,t33,b11,b21,b31)
            x,y,z = X
            self.xlabel.setText('x = '+str(x))
            self.ylabel.setText('y = '+str(y))
            self.zlabel.setText('z = '+str(z))







    def det2(self, a11, a21, a12, a22):
        det = (a11*a22) - (a12*a21)
        return det # Returns a number

    def det3(self, a11, a21, a31, a12, a22, a32, a13, a23, a33):
        det = a11 * self.det2(a22,a32,a23,a33) - a12 * self.det2(a21,a31,a23,a33) + a13 * self.det2(a21,a31,a22,a32)
        return det # Returns a number

    def transpose(self,a11,a21,a31,a12,a22,a32,a13,a23,a33):
        trans = [a11,a12,a13,a21,a22,a23,a31,a32,a33]
        return trans # Returns as a list

    def adjoint(self,a11,a21,a31,a12,a22,a32,a13,a23,a33):
        # A --> Cofactors
        A11 = self.det2(a22,a32,a23,a33)
        A21 = -self.det2(a12,a32,a13,a33)
        A31 = self.det2(a12,a22,a13,a23)
        A12 = -self.det2(a21,a31,a23,a33)
        A22 = self.det2(a11,a31,a13,a33)
        A32 = -self.det2(a11,a21,a13,a23)
        A13 = self.det2(a21,a31,a22,a32)
        A23 = -self.det2(a11,a31,a12,a32)
        A33 = self.det2(a11,a21,a12,a22)
        adj = self.transpose(A11,A21,A31,A12,A22,A32,A13,A23,A33)
        return adj # Returns as a list

    def inverse(self,a11,a21,a31,a12,a22,a32,a13,a23,a33):
        det = self.det3(a11,a21,a31,a12,a22,a32,a13,a23,a33)
        adj = self.adjoint(a11,a21,a31,a12,a22,a32,a13,a23,a33)

        inv = list()
        for i in adj:
            ele = i*(1/det)
            inv.append(ele)
        return inv # Returns list

    def multi3x3_3x1(self,a11,a21,a31,a12,a22,a32,a13,a23,a33,b11,b21,b31):
        t11 = a11*b11+a12*b21+a13*b31
        t21 = a21*b11+a22*b21+a23*b31
        t31 = a31*b11+a32*b21+a33*b31
        prod = [t11,t21,t31]
        return prod



















app = QApplication(sys.argv)
UIWindow = matrixUI()
UIWindow.show()
app.exec_()

