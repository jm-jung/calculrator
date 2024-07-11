from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self)
        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기만 가능하도록 수정
        self.btn1 = QPushButton("Message", self)
        self.btn2 = QPushButton("Clear", self)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1) # 'Message' 버튼 위치
        hbox.addWidget(self.btn2) # 'Clear' 버튼 위치
        
        vbox = QVBoxLayout() # 수직 레이아웃 위젯 생성 코드
        vbox.addWidget(self.te1) # 수직 레이아웃에 텍스트 에디트 위젯 추가
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl1) # 빈 공간 생성 코드
        
        self.setLayout(vbox) # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self): # 버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        self.te1.appendPlainText("Button clicked!")
        
    def clearMessage(self):
        self.te1.clear()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())