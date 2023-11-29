from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from gui import Ui_MainWindow
from math import *
from typing import List

class Calc_Logic(QMainWindow, Ui_MainWindow):
    """
    A class representing the calculator's logic and functionality.
    """

    def __init__(self) -> None:
        """
        Initializes the calculator's logic and user interface.
        """
        super().__init__()
        self.setupUi(self)

        self.__curnum: str = ''  # Current number being entered
        self.__allinput: List[float] = []  # List of all input numbers and operators
        self.__equationActive: bool = True  # Indicates whether a new equation is being started

        # Connect button clicks to respective functions
        self.percentButton.clicked.connect(self.__percentFunction)
        self.fractionButton.clicked.connect(self.__fractionFunction)
        self.sevenButton.clicked.connect(self.__inputSeven)
        self.foutButton.clicked.connect(self.__inputFour)
        self.oneButton.clicked.connect(self.__inputOne)
        self.flipsignButton.clicked.connect(self.__flipCurSign)
        self.zeroButton.clicked.connect(self.__inputZero)
        self.eightButton.clicked.connect(self.__inputEight)
        self.clearButton.clicked.connect(self.__clearFunction)
        self.squareButton.clicked.connect(self.__squareFunction)
        self.fiveButton.clicked.connect(self.__inputFive)
        self.twoButton.clicked.connect(self.__inputTwo)
        self.decimalButton.clicked.connect(self.__inputDecimal)
        self.nineButton.clicked.connect(self.__inputNine)
        self.piButton.clicked.connect(self.__inputPi)
        self.squarerootButton.clicked.connect(self.__squarerootFunction)
        self.sixButton.clicked.connect(self.__inputSix)
        self.threeButton.clicked.connect(self.__inputThree)
        self.equalsButton.clicked.connect(self.__sumFunction)
        self.multiplicationButton.clicked.connect(self.__multiplicationFunction)
        self.backButton.clicked.connect(self.__backspaceFunction)
        self.divisionButton.clicked.connect(self.__divisionFunction)
        self.subtractionButton.clicked.connect(self.__subtractionFunction)
        self.additionButton.clicked.connect(self.__additionFunction)

    def __inputZero(self) -> None:
        """
        Appends the digit '0' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '0'
            self.updateView()

    def __inputOne(self) -> None:
        """
        Appends the digit '1' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '1'
            self.updateView()

    def __inputTwo(self) -> None:
        """
        Appends the digit '2' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '2'
            self.updateView()

    def __inputThree(self) -> None:
        """
        Appends the digit '3' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '3'
            self.updateView()

    def __inputFour(self) -> None:
        """
        Appends the digit '4' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '4'
            self.updateView()

    def __inputFive(self) -> None:
        """
        Appends the digit '5' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '5'
            self.updateView()

    def __inputSix(self) -> None:
        """
        Appends the digit '6' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '6'
            self.updateView()

    def __inputSeven(self) -> None:
        """
        Appends the digit '7' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '7'
            self.updateView()

    def __inputEight(self) -> None:
        """
        Appends the digit '8' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '8'
            self.updateView()

    def __inputNine(self) -> None:
        """
        Appends the digit '9' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '9'
            self.updateView()

    def __inputPi(self) -> None:
        """
        Appends the mathematical constant 'π' to the current number.
        """
        if self.__equationActive:
            self.__curnum = str(float(self.__curnum) * pi)
            self.updateView() 
        
    def __inputDecimal(self) -> None:
        """
        Appends the decimal symbol '.' to the current number.
        """
        if self.__equationActive:
            self.__curnum += '.' 
            self.updateView()

    def __flipCurSign(self) -> None:
        """
        Changes the sign of the current number.
        """
        if self.__equationActive:
        
          if self.__curnum[0] == '-':
            self.__curnum = self.__curnum[1:]  # Remove the first character ('-')
          else:
            self.__curnum = '-' + self.__curnum  # Add the first character ('-')

        self.updateView() 

    def __percentFunction(self) -> None:
        """
        Converts the current number to a percentage.
        """
        tempnum = float(self.__curnum) / 100
        for i in range(len(self.__curnum)):
            self.__backspaceFunction()
        self.__curnum = tempnum
        self.updateView()

    def __fractionFunction(self) -> None:
        """
        Converts the current number to its reciprocal.
        """
        tempnum = 1 / float(self.__curnum)
        for i in range(len(str(self.__curnum))):
            self.__backspaceFunction()
        self.__curnum = tempnum
        self.updateView()

    def __squareFunction(self) -> None:
        """
        Squares the current number.
        """
        __tempnum = self.__curnum
        for i in range(len(self.__curnum)):
          self.__backspaceFunction()
        self.__curnum = str(pow(float(__tempnum), 2))
        self.updateView()
        
        

    def __squarerootFunction(self) -> None:
        """
        Calculates the square root of the current number.
        """
        __tempnum = self.__curnum
        for i in range(len(self.__curnum)):
            self.__backspaceFunction()
        self.__curnum = str(sqrt(float(__tempnum)))
        self.updateView()
        

    def __multiplicationFunction(self) -> None:
        """
        Appends the multiplication operator '*' to the input list and initiates a new equation.
        """
        if self.__equationActive:
            try:
                self.__allinput.append(float(self.__curnum))
                self.__curnum = ''
                self.__allinput.append('×')
                self.updateView()
            except Exception as e:
                print(e)
    def __divisionFunction(self) -> None:
        """
        Appends the division operator '/' to the input list and initiates a new equation.
        """
        if self.__equationActive:
            try:
                self.__allinput.append(float(self.__curnum))
                self.__curnum = ''
                self.__allinput.append('÷')
                self.updateView()
            except Exception as e:
                print(e)

    def __subtractionFunction(self) -> None:
        """
        Appends the subtraction operator '-' to the input list and initiates a new equation.
        """
        if self.__equationActive:
            try:
                self.__allinput.append(float(self.__curnum))
                self.__curnum = ''
                self.__allinput.append('-')
                self.updateView()
            except Exception as e:
                print(e)

    def __additionFunction(self) -> None:
        """
        Appends the addition operator '+' to the input list and initiates a new equation.
        """
        if self.__equationActive:
            try:
                self.__allinput.append(float(self.__curnum))
                self.__curnum = ''
                self.__allinput.append('+')
                self.updateView()
            except Exception as e:
                print(e)

    def __sumFunction(self) -> None:
        """
        Evaluates the mathematical expression and displays the result.
        """
        if self.__equationActive:
            self.__allinput.append(float(self.__curnum))
            self.__curnum = ''
            self.updateView()
            self.__domath() # Evaluate the expression
            self.updateView()  # Display the result
            self.__equationActive = False  # Reset equation active flag
            
    def __domath(self) -> float:
        """
        Performs the mathematical operations in the input list from left to right.
        """
        try:
            while True:
                operator_index = -1  # Initialize operator index as not found

                # Handle multiplication
                if '×' in self.__allinput:
                    operator_index = self.__allinput.index('×')  # Find the first multiplication operator
                    self.__allinput[operator_index - 1] *= self.__allinput[operator_index + 1]  # Perform multiplication
                    del self.__allinput[operator_index]  # Remove the used operator
                    del self.__allinput[operator_index]  # Remove the used operand

                # Handle division
                elif '÷' in self.__allinput:
                    operator_index = self.__allinput.index('÷')  # Find the first division operator
                    self.__allinput[operator_index - 1] /= self.__allinput[operator_index + 1]  # Perform division
                    del self.__allinput[operator_index]  # Remove the used operator
                    del self.__allinput[operator_index]  # Remove the used operand

                # Handle addition
                elif '+' in self.__allinput:
                    operator_index = self.__allinput.index('+')  # Find the first addition operator
                    self.__allinput[operator_index - 1] += self.__allinput[operator_index + 1]  # Perform addition
                    del self.__allinput[operator_index]  # Remove the used operator
                    del self.__allinput[operator_index]  # Remove the used operand

                # Handle subtraction
                elif '-' in self.__allinput:
                    operator_index = self.__allinput.index('-')  # Find the first subtraction operator
                    self.__allinput[operator_index - 1] -= self.__allinput[operator_index + 1]  # Perform subtraction
                    del self.__allinput[operator_index]  # Remove the used operator
                    del self.__allinput[operator_index]  # Remove the used operand

                # If no operators found, break out of the loop
                if operator_index == -1:
                    break

            return self.__allinput[0]  # Return the final result

        except Exception as e:
            print("Error:", e)
            return None  # Return None in case of error

    def __clearFunction(self) -> None:
        """
        Clears all input and resets the equation.
        """
        self.__curnum = ''
        self.__allinput = []
        self.CalculatorViewBox.setPlainText('')
        self.__equationActive = True

    def __backspaceFunction(self) -> None:
      """
      Removes the last character from the current number and updates the display accordingly.
      """
      if len(str(self.__curnum)) >= 0:
        self.__curnum = self.__curnum[:-1]
      self.updateView()
        
            
    def updateView(self) -> None:
        """
        Updates the calculator's display with the provided text.
        """
        
        self.CalculatorViewBox.setPlainText('')
        for i in self.__allinput:
          self.CalculatorViewBox.setPlainText(self.CalculatorViewBox.toPlainText() + str(i))
        self.CalculatorViewBox.setPlainText(self.CalculatorViewBox.toPlainText() + str(self.__curnum))