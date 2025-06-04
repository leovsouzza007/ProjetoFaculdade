from tkinter import *

co1 = "#feffff" 
co2 = "#38576b"  
co3 = "#ECEFF1"  
co4 = "#FFAB40"  
fundo = "#3b3b3b"  
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.configure(bg=co1)

frame_tela = Frame(janela, width=235, height=50, bg=co2)
frame_tela.grid(row=0, column=0)

frame_quadros = Frame(janela, width=235, height=260, bg=fundo)
frame_quadros.grid(row=1, column=0)

todos_valores = ""
valor_texto = StringVar()

app_tela = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat",
                 anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg='#37474F', fg=co1)
app_tela.place(x=0, y=0)

def entrar_valor(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    try:
        resultado = str(eval(todos_valores))
        valor_texto.set(resultado)
        todos_valores = ""
    except:
        valor_texto.set("Erro")
        todos_valores = ""

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")



