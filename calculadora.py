from tkinter import *
import pyautogui

conta = "0"
historico = ""

#funções

def numeros(num):
    global conta, label
    if label['text'] == '0' or label['text'] == 'Erro':
        label['text'] = str(num)
        conta = str(num)
    elif len(label['text']) <= 28:
        label['text'] += str(num)
        conta += str(num)

def funcPonto(num = '.'):
    global conta, label 
    if conta[-1] == '.' or conta[-1] == '+' or conta[-1] == '-' or conta[-1] == '*' or conta[-1] == '/' or conta[-1] == '%' or conta[-1] == '(' or conta[-1] == ')' or conta == 'Erro' or len(label['text']) >= 23:
        return
    elif len(label['text']) <= 26:
        label['text'] += str(num)   
        conta += str(num)

def funcAbreParente(num = '('):
    global conta, label
    if label['text'] == '' or label['text'] == 'Erro':
        return
    elif label['text'][-1].isdigit():
        return
    elif len(label['text']) <= 24:
        if label['text'][-1] == '.':
            label['text'] += "0"
            conta += "0"
            label['text'] += str(num)
            conta += str(num)
        else:
            label['text'] += str(num)
            conta += str(num)

def funcFechaParente(num = ')'):
    global conta, label
    if conta[-1] == '.' or conta[-1] == '+' or conta[-1] == '-' or conta[-1] == '*' or conta[-1] == '/' or conta[-1] == '%' or conta[-1] == '(' or conta[-1] == ')' or conta == 'Erro':
        return
    elif conta.count('(') > conta.count(')') and len(label['text']) <= 28:
        label['text'] += str(num)
        conta += str(num)

def operador(num):
    global conta, label

    if conta[-1] in "+-*/%":
        conta = conta[:-1]
        label['text'] = label['text'][:-1]

    # Impede a inserção de dois operadores consecutivos
    if conta[-1] not in "+-*/%" and len(label['text']) <= 22:
    
        if num == '-':
            label['text'] += str(num)
            conta += str(num)
            return

        # Se o último caractere for um ponto, adiciona "0" antes do operador
        if label['text'][-1] == ".":
            label['text'] += "0"
            conta += "0"
            label['text'] += str(num)
            conta += str(num)
        else:
            label['text'] += str(num)
            conta += str(num)

        
def limpartudo(num = 'CE'):
     global conta, label
     label['text'] = '0'
     conta = '0'
     labelhistorico['text'] = ''

def resultado(num = '='):
    global conta, label
    if conta[-1] == '.' or conta[-1] == '+' or conta[-1] == '-' or conta[-1] == '*' or conta[-1] == '/' or conta[-1] == '%' or conta[-1] == '(' or conta == 'Erro':
        return
    
    try:
        if (conta.count('(') != conta.count(')')):
            for i in range(conta.count('(') - conta.count(')')):
                label['text'] = ')'
                conta += ')'
        resultado = ""
        resultado = eval(conta)
        label['text'] = str(resultado)
        historico = conta + " = " + str(resultado)
        labelhistorico['text'] = historico
        labelhistorico['text'] = historico
        conta = str(resultado)
    except:
        label['text'] = 'Erro'
        conta = 'Erro'

def on_key_press(event):
    key = event.char
    
    if key in "0123456789":
        numeros(key)
    elif key == "+":
        operador(key)
    elif key == "-":
        operador(key)
    elif key == "*":
        operador(key)
    elif key == "/":
        operador(key)
    elif key == ".":
        funcPonto()
    elif key == "=" or key == "\r":
        resultado()
    elif key == "c" or key == "C":
        limpartudo()
    elif key == "(":
        funcAbreParente()
    elif key == ")":
        funcFechaParente()

# abre a janela no tkinter
janela = Tk()
janela.title('Calculadora')
janela.geometry('300x450')
janela.configure(bg='light gray')

label2 = Label(janela, bg='light gray', width=10, height=2, anchor='e', padx=5)
label2.pack()

labelhistorico = Label(janela, text='', bg='black', fg='white', font='Arial 12 bold', width=25, height=2, anchor='e', padx=5)
labelhistorico.pack()

label = Label(janela, text='0', bg='black', fg='white', font='Arial 12 bold', width=25, height=2, anchor='e', padx=5)
label.pack()

label2 = Label(janela, bg='light gray', width=10, height=2, anchor='e', padx=5)
label2.pack()

frame = Frame(janela)
frame.pack()

#linha 1
n0 = Button(frame, text='0', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 0))
n0.grid(row=4, column=0)
ponto = Button(frame, text='.', font='Arial 12 bold', width=6, height=2, command=lambda: funcPonto(num = '.'))
ponto.grid(row=4, column=1)
soma = Button(frame, text='+', font='Arial 12 bold', width=6, height=2, command=lambda: operador(num = '+'))
soma.grid(row=4, column=2)
igual = Button(frame, text='=', bg="light blue", font='Arial 12 bold', width=6, height=2, command=lambda: resultado('='))
igual.grid(row=4, column=3)

#linha 2   
n1 = Button(frame, text='1', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 1))
n1.grid(row=3, column=0)
n2 = Button(frame, text='2', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 2))
n2.grid(row=3, column=1)
n3 = Button(frame, text='3', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 3))
n3.grid(row=3, column=2)
sub = Button(frame, text='-', font='Arial 12 bold', width=6, height=2, command=lambda: operador(num ='-'))
sub.grid(row=3, column=3)

#linha 3
n4 = Button(frame, text='4', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 4))
n4.grid(row=2, column=0)
n5 = Button(frame, text='5', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 5))
n5.grid(row=2, column=1)
n6 = Button(frame, text='6', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 6))
n6.grid(row=2, column=2)
mult = Button(frame, text='*', font='Arial 12 bold', width=6, height=2, command=lambda: operador(num = '*'))
mult.grid(row=2, column=3)

#linha 4
n7 = Button(frame, text='7', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 7))
n7.grid(row=1, column=0)
n8 = Button(frame, text='8', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 8))
n8.grid(row=1, column=1)
n9 = Button(frame, text='9', font='Arial 12 bold', width=6, height=2, command=lambda: numeros(num = 9))
n9.grid(row=1, column=2)
div = Button(frame, text='/', font='Arial 12 bold', width=6, height=2, command=lambda: operador(num ='/'))
div.grid(row=1, column=3)

#linha 5
abreParenteses = Button(frame, text='(', font='Arial 12 bold', width=6, height=2, command=lambda: funcAbreParente('('))
abreParenteses.grid(row=0, column=0)
fechaParenteses = Button(frame, text=')', font='Arial 12 bold', width=6, height=2, command=lambda: funcFechaParente(')'))
fechaParenteses.grid(row=0, column=1)
porcentagem = Button(frame, text='%', font='Arial 12 bold', width=6, height=2, command=lambda: operador(num = '%'))
porcentagem.grid(row=0, column=2)
limpar = Button(frame, text='CE', font='Arial 12 bold', width=6, height=2, command=lambda: limpartudo('CE'))
limpar.grid(row=0, column=3)

janela.bind("<KeyPress>", on_key_press)

janela.mainloop()