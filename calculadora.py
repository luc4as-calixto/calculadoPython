from tkinter import *

conta = "0"
historico = ""

#funções

def equação(num):
    global label, historico, conta, labelhistorico
    import re 

    partes = re.split(r'([\+\-\*/%])', conta)
    partes = [p.strip() for p in partes if p.strip()]
    
    if len(partes) < 3:
        return conta 

    n1 = float(partes[0])
    n2 = float(partes[2])
    sinal = partes[1]

    if sinal == "+":
        historico = str(n1 + n2)
    elif sinal == "-":
        historico = str(n1 - n2)
    elif sinal == "*":
        historico = str(n1 * n2)
    elif sinal == "/":
        historico = str(n1 / n2)
    elif sinal == "%":
        historico = str(n1 % n2)
    else:
        return conta  

    labelhistorico['text'] = historico
    label['text'] = historico + num 
    conta = historico 


def numeros(num):
    global conta, label
    if label['text'] == '0' or label['text'] == 'Erro':
        label['text'] = str(num)
        conta = ""
        conta += str(num)
    elif len(label['text']) <= 22:
        label['text'] += str(num)
        conta += str(num)
    elif conta[-1] == '.' or conta[-1] == '+' or conta[-1] == '-' or conta[-1] == '*' or conta[-1] == '/' or conta[-1] == '%' or conta[-1] == '(' or conta[-1] == ')' and len(label['text']) <= 28:
        label['text'] += str(num)
        conta += str(num)

def funcPonto(num = '.'):
    global conta, label 
    if conta[-1] == '.' or conta[-1] == '+' or conta[-1] == '-' or conta[-1] == '*' or conta[-1] == '/' or conta[-1] == '%' or conta[-1] == '(' or conta[-1] == ')' or conta == 'Erro' or len(label['text']) >= 23 or conta.count('.') > 0:
        return
    elif len(label['text']) <= 22:
        label['text'] += str(num)   
        conta += str(num)

def funcAbreParente(num = '('):
    global conta, label
    if label['text'] == '0' or len(label['text']) >= 20:
        label['text'] = ""
        label['text'] += str(num)
        conta = ""
        conta += str(num)
    elif len(label['text']) <= 22:
        label['text'] += str(num)
        conta += str(num)

def funcFechaParente(num = ')'):
    global conta, label
    if conta.count('(') > conta.count(')') or len(label['text']) >= 23:
        label['text'] += str(num)
        conta += str(num)

def operador(num):
    global conta, label
    if label['text'][-1] == '%' or label['text'][-1] == '+' or label['text'][-1] == '-' or label['text'][-1] == '*' or label['text'][-1] == '/' or label['text'][-1] == '(' or label['text'] == 'Erro' or len(label['text']) >= 25:
        return
    elif(conta.count('*') > 0) or (conta.count('/') > 0) or (conta.count('+') > 0) or (conta.count('-') > 0) or (conta.count('%') > 0):
        equação(num)   
    else:
        label['text'] += str(num)
        conta += str(num)
        
def limpartudo(num = 'CE'):
    global conta, label
    label['text'] = '0'
    conta = '0'

def resultado(num = '='):
    global conta, label
    try:
        label['text'] = str (eval(conta))
        conta = str(eval(conta))
    except:
        label['text'] = 'Erro'
        conta = '0'



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

janela.mainloop()
print(conta)