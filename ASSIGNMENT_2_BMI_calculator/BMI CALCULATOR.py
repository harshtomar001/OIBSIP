import sys

from  PyQt5.QtWidgets import (QApplication , QWidget, QVBoxLayout,QHBoxLayout,QDesktopWidget , QMainWindow,

                              QLabel,QLineEdit, QPushButton)
from PyQt5.QtCore import Qt




class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("BMI CALCULATOR")
        self.resize(1000,1000,)
        self.center()

        label=QLabel("BMI Calculator",self)
        label.setGeometry(100,0,300,60)

        label.setStyleSheet("color:blue;" "background-color:black;"
                            "font-size:40px;"
                            "border-radius:8px;"
                            "padding:30px;"
                            "font-weight:bold;"
                            "margin:10px;")

        label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label, alignment=Qt.AlignHCenter | Qt.AlignTop)

        label1=QLabel("Enter your Weight:")
        label1.setFixedWidth(400)

        label1.setStyleSheet("background-color:#43a7b0;""font-size:30px;"
                             "width:50px;"
                             "padding:10px;"
                             "margin:8px;"
                             "height:40px;"
                             "border-radius:8px;")

        label1.setAlignment(Qt.AlignCenter)
        self.line_edit=QLineEdit(self)
        self.line_edit.resize(40,40)
        self.line_edit.setPlaceholderText("in kg")
        self.line_edit.setFixedWidth(170)
        self.line_edit.setStyleSheet("background-color:#ace3e8;""font-size:25px;"
                                     "height:40px;"
                                     "border-radius:8px;"
                                     "padding:10px;"
                                     "text-align:center;"
                                     )


        layout_weight=QHBoxLayout()
        layout_weight.addWidget(label1)
        layout_weight.addSpacing(10)
        layout_weight.addWidget(self.line_edit)
        layout_weight.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.addLayout(layout_weight)



        label2 = QLabel("Enter your Height: ")
        label2.setAlignment(Qt.AlignCenter)
        label2.setFixedWidth(380)
        label2.setStyleSheet("font-size:30px;"
                             "padding:10px;"
                             "background-color:#43a7b0;"
                             "border-radius:8px;")

        self.line_edit_1 = QLineEdit(self)
        self.line_edit_1.setFixedWidth(170)
        self.line_edit_1.setPlaceholderText("in cm")
        self.line_edit_1.setStyleSheet("background-color:#ace3e8;"
                                       "height:40px;"
                                       "border-radius:8px;"
                                       "padding:10px;"
                                       "font-size:25px;")

        layout_height = QHBoxLayout()
        layout_height.addWidget(label2)
        layout_height.addSpacing(10)
        layout_height.addWidget(self.line_edit_1)
        layout_height.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.addLayout(layout_height)


        self.button=QPushButton("Calculate BMI")
        self.button.setFixedWidth(250)
        self.button.setStyleSheet("background-color:#e6986c;"
                                  "border-radius:8px;"
                                  "padding:10px;"
                                  "font-size:30px;"
                                  "font-weight:bold;"
                                  "font-style:italic;"
                                  )

        layout_button = QHBoxLayout()
        layout_button.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout_button.addWidget(self.button)

        self.button.clicked.connect(self.on_click)


        layout.addLayout(layout_button)

        self.label_3=QLabel(" ")

        layout_info=QHBoxLayout()
        layout_info.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout_info.addWidget(self.label_3)
        layout.addLayout(layout_info)
        container = QWidget(self)
        container.setStyleSheet("background-color:#a6a6a6")
        container.setLayout(layout)

        self.setCentralWidget(container)


    def center(self):
        # Get the geometry of the screen
        screen_geometry = QDesktopWidget().availableGeometry()
        # Get the geometry of the window
        window_geometry = self.frameGeometry()
        # Calculate the center point of the screen
        center_point = screen_geometry.center()
        # Move the window's rectangle to the screen center
        window_geometry.moveCenter(center_point)
        # Move the top-left of the window to the calculated position
        self.move(window_geometry.topLeft())

    def on_click(self):
        weight=self.line_edit.text()
        heigth=self.line_edit_1.text()
        try:

            weight=abs(float(weight))
            height=abs(float(heigth))
            if weight>300:
                self.label_3.setStyleSheet('color:red;'
                                           "font-size:40px;"
                                           "font-weight:bold;"
                                           )
                self.label_3.setText("Too much Weight")
                return
            if height>300:
                self.label_3.setStyleSheet('color:red;'
                                           "font-size:40px;"
                                           "font-weight:bold;"
                                           )
                self.label_3.setText("Too much Height")
                return
            height=height/100

            bmi=weight/(height*height)
            overview=""
            if bmi>=30:
                overview="Obese"
            elif bmi>=25:
                overview="Overweight"
            elif bmi>=18.5:
                overview="Healthy Weight"
            else:
                overview="Underweight"

            self.label_3.setStyleSheet('color:#e823d8;'
                               "font-size:40px;"
                               "font-weight:bold;"
                               "text-decoration:underline;")

            self.label_3.setText(f"BMI: {bmi:.2f}\n\n{overview}")

        except ValueError:
            # print("Invalid Value Provided")
            self.label_3.setStyleSheet('color:red;'
                                       "font-size:40px;"
                                       "font-weight:bold;"
                                       )
            self.label_3.setText("Invalid Value Provided")
        except ZeroDivisionError:
            self.label_3.setText("Height can't be zero")
            self.label_3.setStyleSheet('color:red;'
                                       "font-size:40px;"
                                       "font-weight:bold;"
                                       )


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ =="__main__":
    main()