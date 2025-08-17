import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QFormLayout, QHBoxLayout, 
                             QLineEdit, QLabel, QRadioButton, QButtonGroup, QCheckBox, 
                             QTextEdit, QPushButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用户注册")
        self.setGeometry(100, 100, 500, 600)
        self.setup_ui()
        self.apply_styles()
        
    def setup_ui(self):
        # 主布局
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        
        # 标题
        title_label = QLabel("用户注册")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("title")
        main_layout.addWidget(title_label)
        
        # 表单布局
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setVerticalSpacing(15)
        
        # 用户名
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("请输入用户名")
        form_layout.addRow("用户名:", self.username_input)
        
        # 密码
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("请输入密码")
        self.password_input.setEchoMode(QLineEdit.Password)
        form_layout.addRow("密码:", self.password_input)
        
        # 确认密码
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("请再次输入密码")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        form_layout.addRow("确认密码:", self.confirm_password_input)
        
        # 性别
        gender_layout = QHBoxLayout()
        self.gender_group = QButtonGroup(self)
        
        self.male_radio = QRadioButton("男")
        self.male_radio.setChecked(True)
        self.female_radio = QRadioButton("女")
        
        self.gender_group.addButton(self.male_radio, 1)
        self.gender_group.addButton(self.female_radio, 2)
        
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        gender_layout.addStretch()
        
        form_layout.addRow("性别:", gender_layout)
        
        # 爱好
        hobbies_layout = QHBoxLayout()
        self.hobby_sports = QCheckBox("运动")
        self.hobby_travel = QCheckBox("旅游")
        self.hobby_reading = QCheckBox("阅读")
        self.hobby_gaming = QCheckBox("游戏")
        
        hobbies_layout.addWidget(self.hobby_sports)
        hobbies_layout.addWidget(self.hobby_travel)
        hobbies_layout.addWidget(self.hobby_reading)
        hobbies_layout.addWidget(self.hobby_gaming)
        
        form_layout.addRow("爱好:", hobbies_layout)
        
        # 个性签名
        self.signature_input = QTextEdit()
        self.signature_input.setPlaceholderText("请输入您的个性签名...")
        self.signature_input.setMaximumHeight(80)
        form_layout.addRow("个性签名:", self.signature_input)
        
        # 择偶要求分组框
        partner_group = QGroupBox("择偶要求")
        partner_layout = QHBoxLayout()
        
        # 身高要求
        height_layout = QVBoxLayout()
        height_label = QLabel("身高要求(cm):")
        self.min_height_input = QLineEdit()
        self.min_height_input.setPlaceholderText("最低")
        self.max_height_input = QLineEdit()
        self.max_height_input.setPlaceholderText("最高")
        
        height_inputs = QHBoxLayout()
        height_inputs.addWidget(self.min_height_input)
        height_inputs.addWidget(QLabel("-"))
        height_inputs.addWidget(self.max_height_input)
        
        height_layout.addWidget(height_label)
        height_layout.addLayout(height_inputs)
        
        # 收入要求
        income_layout = QVBoxLayout()
        income_label = QLabel("收入要求(万/年):")
        self.min_income_input = QLineEdit()
        self.min_income_input.setPlaceholderText("最低")
        self.max_income_input = QLineEdit()
        self.max_income_input.setPlaceholderText("最高")
        
        income_inputs = QHBoxLayout()
        income_inputs.addWidget(self.min_income_input)
        income_inputs.addWidget(QLabel("-"))
        income_inputs.addWidget(self.max_income_input)
        
        income_layout.addWidget(income_label)
        income_layout.addLayout(income_inputs)
        
        partner_layout.addLayout(height_layout)
        partner_layout.addSpacing(20)
        partner_layout.addLayout(income_layout)
        partner_group.setLayout(partner_layout)
        
        # 注册按钮
        register_button = QPushButton("注册")
        register_button.clicked.connect(self.print_registration_info)
        
        # 添加到主布局
        main_layout.addLayout(form_layout)
        main_layout.addWidget(partner_group)
        main_layout.addWidget(register_button, alignment=Qt.AlignCenter)
        main_layout.addStretch(1)
        
        self.setLayout(main_layout)
    
    def apply_styles(self):
        # 设置样式
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f8ff;
                font-family: 'Microsoft YaHei';
            }
            QLabel#title {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 20px;
            }
            QLineEdit, QTextEdit {
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                padding: 8px;
                background-color: white;
            }
            QLineEdit:focus, QTextEdit:focus {
                border: 1px solid #3498db;
            }
            QGroupBox {
                border: 1px solid #bdc3c7;
                border-radius: 6px;
                margin-top: 10px;
                padding: 10px;
                font-weight: bold;
                background-color: #e8f4fc;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 5px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 12px 30px;
                font-size: 16px;
                font-weight: bold;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c6ea4;
            }
            QLabel {
                font-weight: bold;
                color: #2c3e50;
            }
            QCheckBox, QRadioButton {
                color: #2c3e50;
            }
        """)
    
    def print_registration_info(self):
        # 收集用户信息
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        
        # 检查密码是否匹配
        if password != confirm_password:
            QMessageBox.warning(self, "密码错误", "两次输入的密码不一致！")
            return
            
        gender = "男" if self.male_radio.isChecked() else "女"
        
        hobbies = []
        if self.hobby_sports.isChecked(): hobbies.append("运动")
        if self.hobby_travel.isChecked(): hobbies.append("旅游")
        if self.hobby_reading.isChecked(): hobbies.append("阅读")
        if self.hobby_gaming.isChecked(): hobbies.append("游戏")
        hobbies_str = "、".join(hobbies) if hobbies else "无"
        
        signature = self.signature_input.toPlainText()
        
        min_height = self.min_height_input.text()
        max_height = self.max_height_input.text()
        height_range = f"{min_height}-{max_height} cm" if min_height or max_height else "未填写"
        
        min_income = self.min_income_input.text()
        max_income = self.max_income_input.text()
        income_range = f"{min_income}-{max_income} 万/年" if min_income or max_income else "未填写"
        
        # 创建信息字符串
        info = f"""
        ========== 用户注册信息 ==========
        用户名: {username}
        密码: {'*' * len(password)}
        性别: {gender}
        爱好: {hobbies_str}
        个性签名: {signature if signature else "未填写"}
        身高要求: {height_range}
        收入要求: {income_range}
        ================================
        """
        
        # 打印到控制台
        print(info)
        
        # 显示成功消息
        QMessageBox.information(self, "注册成功", "用户信息已成功提交！")
        
        # 清空表单（可选）
        # self.clear_form()

    def clear_form(self):
        # 清空表单的方法
        self.username_input.clear()
        self.password_input.clear()
        self.confirm_password_input.clear()
        self.male_radio.setChecked(True)
        self.hobby_sports.setChecked(False)
        self.hobby_travel.setChecked(False)
        self.hobby_reading.setChecked(False)
        self.hobby_gaming.setChecked(False)
        self.signature_input.clear()
        self.min_height_input.clear()
        self.max_height_input.clear()
        self.min_income_input.clear()
        self.max_income_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())