class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("Государственный язык Бразилии", "Португальский", "Испанский", "Украинский", "Русский"))

question_list.append(Question("Как переводиться universe", 'вселенная', 'одежда', 'очки', 'мышка'))
question_list.append(Question('Сколько струн в гитаре', '6', '4', '2', '8'))
question_list.append(Question('Чему равен алгебраический корень 4', '+-2', '4', '2', '8'))
question_list.append(Question('Как звали колдуна из властелина колец, с которым дружил Фродо', 'Гендальф', 'Дамблдор', 'Вульфрик', 'Гардас'))
question_list.append(Question('Как зовут главного героя игры hollow knight', 'маленький призрак', 'полый рыцарь', 'пустотный странник', 'опустевший сосуд'))
question_list.append(Question('Как звали крысу Рона из Гарри Поттера', 'Короста', 'Шимли', 'Кона', 'Грызунья'))
question_list.append(Question('Как по английски пишется феникс', 'phoenix', 'foenyx', 'phenix', 'fenix'))
question_list.append(Question('Чему равен арифметический корень 16', '4', '+-4', '8', '2'))

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    quet.setText("Следующий вопрос")
    pushbutton.setText("Следующий вопрос")


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    pushbutton.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_answer1.setChecked(False)
    rbtn_answer2.setChecked(False)
    rbtn_answer3.setChecked(False)
    rbtn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout,QGroupBox, QButtonGroup
 
app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
#создание виджетов главного окна
 
main_win.setWindowTitle("Memory Card")
rbtn_answer1 = QRadioButton("Энцы")
rbtn_answer2 = QRadioButton("Смурфы")
rbtn_answer3 = QRadioButton("Чульмцы")
rbtn_answer4 = QRadioButton("Алеуты")
answers = [rbtn_answer1, rbtn_answer2, rbtn_answer3, rbtn_answer4]

def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    quet.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно!")
def next_question():
    main_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
    print("Всего вопросов", main_win.total)
    print("Правильных ответов:", main_win.score)
    print("Рейтинг", main_win.score/main_win.total * 100, "%")
def click_OK():
    if pushbutton.text() == "Ответить":
        check_answer()
    else:
        next_question()

RadioGroupBox = QGroupBox("Варианты ответов")
AnsGroupBox = QGroupBox("Результат теста")
RadioGroup = QButtonGroup()
quet = QLabel("Какой национальности не существует?")
pushbutton = QPushButton("Ответить")

RadioGroup.addButton(rbtn_answer1)
RadioGroup.addButton(rbtn_answer2)
RadioGroup.addButton(rbtn_answer3)
RadioGroup.addButton(rbtn_answer4)
 
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_answer1)
layout_ans2.addWidget(rbtn_answer2)
layout_ans3.addWidget(rbtn_answer3)
layout_ans3.addWidget(rbtn_answer4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
lain1 = QHBoxLayout()
lain2 = QHBoxLayout()
lain3 = QHBoxLayout()
 
lain1.addWidget(quet, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
lain2.addWidget(RadioGroupBox)
 
lain3.addStretch(1)
lain3.addWidget(pushbutton, stretch=2)
lain3.addStretch()
 
lb_Result = QLabel("Ты прав или нет?")
lb_Correct = QLabel("ответ будет тут!")
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = Qt.AlignHCenter )
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
RadioGroupBox.setLayout(layout_ans1)
 
lain1.addWidget(quet, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
 
lain2.addWidget(RadioGroupBox)
lain2.addWidget(AnsGroupBox)
 
lain3.addStretch(1)
lain3.addWidget(pushbutton, stretch=2)
lain3.addStretch(1)
 
layout_card = QVBoxLayout()
layout_card.addLayout(lain1, stretch=2)
layout_card.addLayout(lain2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(lain3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
main_win.setLayout(layout_card)

main_win.total = 0 
main_win.score = 0
q = Question('Выбор перевод слова "переменная"', ' variable', 'variation', 'link', 'bad')
ask(q)
pushbutton.clicked.connect(click_OK)
main_win.show()
app.exec_()
print("Всего вопросов", main_win.total)
print("Правильных ответов:", main_win.score)
print("Рейтинг", main_win.total/main_win.score * 100, "%")


