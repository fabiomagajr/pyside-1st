from PySide6.QtWidgets import QApplication, QPushButton, QWidget,QVBoxLayout
import sys

app=QApplication(sys.argv)
botao=QPushButton("TExto do botao")
botao.setStyleSheet('font-size: 40px; color: red;')
botao.show()
central_widget = QWidget()
layout=QVBoxLayout()
central_widget.setLayout(layout)
layout.addWidget(botao)
central_widget.show()
app.exec()




