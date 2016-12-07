#defining PyQt libraries
from PyQt4.QtGui import *
from PyQt4.QtCore import *
 
#definin PyQt class
class calculator(QDialog):
 
    #we defined main window 
    #parents=none means it is main window
    def __init__(self,parents=None):
 
        #super starts the class
        super(calculator, self).__init__(parents)
 
        #create grid
        grid=QGridLayout()
 
        #we create to label for to tell enter first number
        #0,0 means line and column
        grid.addWidget(QLabel("Enter First Number:"),0,0)
 
        #QLineEdit is getting input
        self.firstNumber=QLineEdit()
 
        #with setInputMask you can limit to input
        self.firstNumber.setInputMask("0000.00")
 
        #0,1 still means line and column
        grid.addWidget(self.firstNumber,0,1)
 
        grid.addWidget(QLabel("Enter second number:"),1,0)
        self.secondNumber=QLineEdit()
        self.secondNumber.setInputMask("0000.00")
        grid.addWidget(self.secondNumber,1,1)
 
        grid.addWidget(QLabel("Select an operation "),2,1)
 
        #adding a button with QPushButton
        plus=QPushButton("+")
        plus.setToolTip('To add the numbers.')
 
        #connect means when user click a button calling a def
        grid.connect(plus, SIGNAL("pressed()"), self.addition )
 
        #plus,line, column, line weight, column weight
        grid.addWidget(plus,3,0,1,1)
 
        minus=QPushButton("-")
        minus.setToolTip('To subtract the second number from the first.')
        grid.connect(minus, SIGNAL("pressed()"), self.subtraction )
        grid.addWidget(minus,3,1,1,1)
 
        multi=QPushButton("*")
        multi.setToolTip('To multiply the numbers.')
        grid.connect(multi, SIGNAL("pressed()"),self.multiplication)
        grid.addWidget(multi,3,2,1,1)
 
        div=QPushButton("/")
        div.setToolTip('To divide the first number by the second.')
        grid.connect(div, SIGNAL("pressed()"),self.division )
        grid.addWidget(div,3,3,1,1)
 
        self.result=QLabel("Result")
        grid.addWidget(self.result,4,1)
 
        self.setLayout(grid)
        self.setWindowTitle("Parth's Calculator")
 
    #with connect function we calls this class def
    def addition(self):
 
        #firstNumber.text is first numbers string format
        #float() making strings float
        add=float(self.firstNumber.text()) + float(self.secondNumber.text())
        self.result.setText("%.2f"%add)
 
    def subtraction(self):
        minus=float(self.firstNumber.text()) - float(self.secondNumber.text())
        self.result.setText("%.2f"%minus)
 
    def multiplication(self):
        multi=float(self.firstNumber.text()) * float(self.secondNumber.text())
        self.result.setText("%.2f"%multi)
 
    def division(self):
        div=float(self.firstNumber.text()) / float(self.secondNumber.text())
        self.result.setText("%.2f"%div)

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Do you really want to quit me?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   
 
#QApplication starts qt
app=QApplication([])
 
window=calculator()
#we did visible to calculator
window.show()
#added a loop
#with loop application cathcing to inputs
app.exec_()