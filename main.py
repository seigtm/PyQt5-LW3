# Laboratory work №3.
# Baranov Konstantin Pavlovich, IP-18-4.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class App(QMainWindow):  # Core application (main window) class.
    def __init__(self):
        super().__init__()

        # Init window UI.
        self.initUI()

        # Show window.
        self.show()

    def initUI(self):
        # Variables (window params).
        self._title = 'Laboratory work №3'
        self._left = 150
        self._top = 150
        self._width = 500
        self._height = 600
        self._font = QFont('Arial', 14, 14)

        # Set window title, geometry and font.
        self.setWindowTitle(self._title)
        self.setGeometry(self._left, self._top, self._width, self._height)
        self.setFont(self._font)

        # Add custom widget to the window.
        self.mainTabWidget = MyTabWidget(self)

        # Set tab widget as central widget.
        self.setCentralWidget(self.mainTabWidget)


class MyTabWidget(QWidget):  # My tab widget with tabs as tasks.
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # Init tab widget UI.
        self.initUI()

    def initUI(self):
        # Main layout (vertical).
        self.layout = QVBoxLayout(self)

        # Init tabs.
        self.initTabs()

        # Set the layout on the application's window.
        self.setLayout(self.layout)

    def initTabs(self):
        # Initialize tab screen.
        self.tabs = QTabWidget()
        self.tab1 = FirstTaskWidget(self)
        self.tab2 = SecondTaskWidget(self)
        self.tab3 = ThirdTaskWidget(self)
        self.tab4 = ForthTaskWidget(self)

        # Add tabs.
        self.tabs.addTab(self.tab1, 'First')
        self.tabs.addTab(self.tab2, 'Second')
        self.tabs.addTab(self.tab3, 'Third')
        self.tabs.addTab(self.tab4, 'Forth')

        # Add tabs to the widget layout.
        self.layout.addWidget(self.tabs)


class FirstTaskWidget(QWidget):  # First task.
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # Init first task widget UI.
        self.initUI()

    def initUI(self):
        # Set widget main layout (horizontal).
        self.layout = QHBoxLayout(self)

        # Create label for text (new note) input.
        self.inputLabel = QLabel('Input:')

        # Create line edit to input new notes.
        self.lineEdit = QLineEdit()

        # Create action buttons.
        self.addButton = QPushButton('Add')
        self.editButton = QPushButton('Edit')
        self.deleteButton = QPushButton('Delete')
        self.deleteAllButton = QPushButton('Delete all')

        # Create vertical spacer.
        self.verticalSpacer = QSpacerItem(
            20, 40,
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Expanding)

        # Create vertical layout and add widgets and spacer to it.
        self.leftVerticalLayout = QVBoxLayout()
        self.leftVerticalLayout.addWidget(self.inputLabel)
        self.leftVerticalLayout.addWidget(self.lineEdit)
        self.leftVerticalLayout.addWidget(self.addButton)
        self.leftVerticalLayout.addWidget(self.editButton)
        self.leftVerticalLayout.addWidget(self.deleteButton)
        self.leftVerticalLayout.addWidget(self.deleteAllButton)
        self.leftVerticalLayout.addSpacerItem(self.verticalSpacer)

        # Add left layout to main layout.
        self.layout.addLayout(self.leftVerticalLayout)

        # Create list widget.
        self.listWidget = QListWidget()

        # Add list widget to main layout.
        self.layout.addWidget(self.listWidget)

        # Connect slots and signals.
        self.addButton.clicked.connect(self.addListWidgetItem)
        self.editButton.clicked.connect(self.editListWidgetItem)
        self.deleteButton.clicked.connect(self.deleteListWidgetItem)
        self.deleteAllButton.clicked.connect(self.clearListWidget)

    # Slot on button 'add' clicked.
    def addListWidgetItem(self):
        # Get text from lineEdit.
        text = self.lineEdit.text()

        # Add this as new item to the list widget.
        self.listWidget.addItem(text)

    # Slot on button 'edit' clicked.
    def editListWidgetItem(self):
        # If nothing is selected in list widget.
        if self.listWidget.currentRow() == -1:
            return

        # Show input dialog.
        text, ok = QInputDialog().getText(
            self, 'Edit note', 'Enter new note text:', QLineEdit.Normal)

        # If text is not empty and ok button clicked.
        if ok and text:
            self.listWidget.currentItem().setText(text)

    # Slot on button 'delete' clicked.
    def deleteListWidgetItem(self):
        # Delete list widget item at the current row index.
        self.listWidget.takeItem(self.listWidget.currentRow())

    # Slot on button 'delete all' clicked.
    def clearListWidget(self):
        self.listWidget.clear()


class SecondTaskWidget(QLCDNumber):  # Second task.
    def __init__(self, parent):
        super(SecondTaskWidget, self).__init__(parent)

        # Set clock segment style (Filled/Flat/Outline).
        self.setSegmentStyle(QLCDNumber.Filled)

        # Create a timer.
        self.timer = QTimer(self)
        # Connect it to slot 'showTime'.
        self.timer.timeout.connect(self.showTime)
        # Update the timer every second.
        self.timer.start(1000)

        # Colorize clock.
        self.colorizeQLCD()

        self.showTime()

    def showTime(self):
        time = QTime.currentTime()
        timeText = time.toString('hh:mm')

        # Make colon appear and vanish every other second (pseudo-animation).
        if (time.second() % 2) == 0:
            # timeText[:2] is hours, timeText[3:] is minutes.
            timeText = timeText[:2] + ' ' + timeText[3:]

        self.display(timeText)

    def colorizeQLCD(self):
        # Get current palette.
        palette = self.palette()
        # Foreground color.
        palette.setColor(palette.WindowText, QColor(185, 85, 255))
        # Set new palette.
        self.setPalette(palette)


class ThirdTaskWidget(QWidget):  # Third task.
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # Init third task widget UI.
        self.initUI()

    def initUI(self):
        # Set widget main layout (vertical).
        self.layout = QVBoxLayout(self)

        # Create calendar widget.
        self.calendar = QCalendarWidget()

        # Create date edit widget.
        self.dateEdit = QDateEdit()
        # Format examples: dd.MM.yy / dddd, dd MMMM yyyy
        self.dateEdit.setDisplayFormat('MMM dd yyyy')

        # Connect calendar and date edit together.
        self.calendar.clicked.connect(self.dateEdit.setDate)
        self.dateEdit.dateChanged.connect(self.calendar.setSelectedDate)

        # Set current date.
        self.dateEdit.setDate(QDate().currentDate())

        # Add widgets to the layout.
        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.dateEdit)


class ForthTaskWidget(QWidget):  # Forth task.
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # Prices for different seat classes.
        self.prices = [300, 200, 100]

        # Init forth task widget UI.
        self.initUI()

    def initUI(self):
        # Set widget main layout (vertical).
        self.layout = QGridLayout(self)

        # Create header label.
        self.headerLabel = QLabel('Booking form')
        self.headerLabel.setAlignment(Qt.AlignCenter)

        # Create calendar widget.
        self.calendar = QCalendarWidget()
        self.calendar.setSelectedDate(QDate().currentDate())

        # Create people number label.
        self.peopleNumLabel = QLabel('Number of people:')

        # Create people number spin box.
        self.peopleNumSpinBox = QSpinBox()

        # Create seat class label.
        self.classLabel = QLabel('Seat class:')

        # Create seat class combo box.
        self.classComboBox = QComboBox()
        classes = ['First', 'Second', 'Third']
        self.classComboBox.addItems(classes)

        # Create calculate button.
        self.calculateButton = QPushButton('Calculate the tariff')
        self.calculateButton.clicked.connect(self.calculateTariff)

        # Create info label.
        self.infoLabel = QLabel()

        # Add widgets to the layout.
        self.layout.addWidget(self.headerLabel, 0, 0, 1, 2)
        self.layout.addWidget(self.calendar, 1, 0, 1, 2)
        self.layout.addWidget(self.peopleNumLabel, 2, 0, 1, 1)
        self.layout.addWidget(self.peopleNumSpinBox, 2, 1, 1, 1)
        self.layout.addWidget(self.classLabel, 3, 0, 1, 1)
        self.layout.addWidget(self.classComboBox, 3, 1, 1, 1)
        self.layout.addWidget(self.calculateButton, 4, 0, 1, 2)
        self.layout.addWidget(self.infoLabel, 5, 0, 1, 2)

    def calculateTariff(self):
        # Clear previous text from info label.
        self.infoLabel.clear()

        if self.peopleNumSpinBox.value() == 0:
            return

        # Get data from user inputs.
        date = self.calendar.selectedDate().toString('yyyy-MM-dd')
        peopleNum = self.peopleNumSpinBox.value()
        seatClass = self.classComboBox.currentText()
        seatPrice = self.prices[self.classComboBox.currentIndex()]
        totalPrice = seatPrice * peopleNum

        # Construct result string.
        resultString = 'Date: {}, Number of people: {},\nSelected seat class: {},\nPrice for one seat: {}$, Total price: {}$'.format(
            date, peopleNum, seatClass, seatPrice, totalPrice)

        # Set info label text.
        self.infoLabel.setText(resultString)


# Main function.
if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())
