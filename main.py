from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq
import random as rd
import string as st
from hashlib import sha256

cor1='#f6eddc'
cor2='#e3e5d7'
cor3='#bdd6d2'
cor4='#a5c8ca'
cor5='#586875'

letrasm = st.ascii_lowercase
letrasM = st.ascii_uppercase
numeros = st.digits
caracteres = st.punctuation




tela_login = Tk()



class geradores():
    def Mmn2(self):
        valor=StringVar()
        self.Mmn = Toplevel()
        #config
        self.Mmn.configure(bg=cor1)
        self.Mmn.title('gerador de senhas Mmn')
        self.Mmn.resizable(False,False)
        self.Mmn.geometry('400x200')
        
        #frames
        self.frame_tela = Frame(self.Mmn, bg=cor4)
        self.frame_tela.place(relx=0, rely=0, relheight=0.3,relwidth=1)
        self.frame_baixo = Frame(self.Mmn,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_baixo.place(relx=0.02, rely=0.35, relheight=0.6,relwidth=0.96)
        #funções
        Mmn3 = letrasM + letrasm + numeros
        self.gerar_entry = Entry(self.frame_baixo)
        self.gerar_entry.place(relx=0.6, rely=0.53, relwidth=0.05)
        
        def gerar_senhaMmn():
            try:
                int(self.gerar_entry.get())
            except:
                messagebox.showerror(title='Erro ao gerar senha', message='Por favor colocar um número inteiro válido')
            if int(self.gerar_entry.get()) < 8 or int(self.gerar_entry.get()) > 16:
                messagebox.showinfo(title='Erro ao gerar senha', message='só se pode gerar senhas com 8 à 16 dígitos')
            else:
                senha = ''.join(rd.SystemRandom().choices(Mmn3, k= int(self.gerar_entry.get())))
                valor.set(senha)
                return senha
        #gadgets
        self.label_senha = Label(self.frame_tela, textvariable=valor, bg=cor5, fg='white', font="Ivy 16 bold")
        self.label_senha.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.bt_gerar = Button(self.frame_baixo,text='Gerar',command=gerar_senhaMmn)
        self.bt_gerar.place(relx=0.7, rely=0.5)

        self.label_gerar = Label(self.frame_baixo,text='Coloque o tamanho da senha entre 8 e 16:')
        self.label_gerar.place(relx=0.1,rely=0.2)
    def Mmc2(self):
        valor=StringVar()
        self.Mmc = Toplevel()
        #config
        self.Mmc.configure(bg=cor1)
        self.Mmc.title('gerador de senhas Mmc')
        self.Mmc.resizable(False,False)
        self.Mmc.geometry('400x200')
        
        #frames
        self.frame_tela = Frame(self.Mmc, bg=cor4)
        self.frame_tela.place(relx=0, rely=0, relheight=0.3,relwidth=1)
        self.frame_baixo = Frame(self.Mmc,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_baixo.place(relx=0.02, rely=0.35, relheight=0.6,relwidth=0.96)
        #funções
        Mmc3 = letrasM + letrasm + caracteres
        self.gerar_entry = Entry(self.frame_baixo)
        self.gerar_entry.place(relx=0.6, rely=0.53, relwidth=0.05)
        def gerar_senhaMmc():
            try:
                int(self.gerar_entry.get())
            except:
                messagebox.showerror(title='Erro ao gerar senha', message='Por favor colocar um número inteiro válido')
            if int(self.gerar_entry.get()) < 8 or int(self.gerar_entry.get()) > 16:
                messagebox.showinfo(title='Erro ao gerar senha', message='só se pode gerar senhas com 8 à 16 dígitos')
            else:
                senha = ''.join(rd.SystemRandom().choices(Mmc3, k= int(self.gerar_entry.get())))
                valor.set(senha)
                return senha
        #gadgets
        self.label_senha = Label(self.frame_tela, textvariable=valor, bg=cor5, fg='white', font="Ivy 16 bold")
        self.label_senha.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.bt_gerar = Button(self.frame_baixo,text='Gerar',command=gerar_senhaMmc)
        self.bt_gerar.place(relx=0.7, rely=0.5)

        self.label_gerar = Label(self.frame_baixo,text='Coloque o tamanho da senha entre 8 e 16:')
        self.label_gerar.place(relx=0.1,rely=0.2)
    def Mnc2(self):
        valor=StringVar()
        self.Mnc = Toplevel()
        #config
        self.Mnc.configure(bg=cor1)
        self.Mnc.title('gerador de senhas Mnc')
        self.Mnc.resizable(False,False)
        self.Mnc.geometry('400x200')
        
        #frames
        self.frame_tela = Frame(self.Mnc, bg=cor4)
        self.frame_tela.place(relx=0, rely=0, relheight=0.3,relwidth=1)
        self.frame_baixo = Frame(self.Mnc,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_baixo.place(relx=0.02, rely=0.35, relheight=0.6,relwidth=0.96)
        #funções
        Mnc3 = letrasM + numeros + caracteres
        self.gerar_entry = Entry(self.frame_baixo)
        self.gerar_entry.place(relx=0.6, rely=0.53, relwidth=0.05)
        def gerar_senhaMnc():
            try:
                int(self.gerar_entry.get())
            except:
                messagebox.showerror(title='Erro ao gerar senha', message='Por favor colocar um número inteiro válido')
                
            if int(self.gerar_entry.get()) < 8 or int(self.gerar_entry.get()) > 16:
                messagebox.showinfo(title='Erro ao gerar senha', message='só se pode gerar senhas com 8 à 16 dígitos')
            else:
                senha = ''.join(rd.SystemRandom().choices(Mnc3, k= int(self.gerar_entry.get())))
                valor.set(senha)
                return senha
        #gadgets
        self.label_senha = Label(self.frame_tela, textvariable=valor, bg=cor5, fg='white', font="Ivy 16 bold")
        self.label_senha.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.bt_gerar = Button(self.frame_baixo,text='Gerar',command=gerar_senhaMnc)
        self.bt_gerar.place(relx=0.7, rely=0.5)

        self.label_gerar = Label(self.frame_baixo,text='Coloque o tamanho da senha entre 8 e 16:')
        self.label_gerar.place(relx=0.1,rely=0.2)
    def mnc2(self):
        valor=StringVar()
        self.mnc = Toplevel()
        #config
        self.mnc.configure(bg=cor1)
        self.mnc.title('gerador de senhas mnc')
        self.mnc.resizable(False,False)
        self.mnc.geometry('400x200')
        
        #frames
        self.frame_tela = Frame(self.mnc, bg=cor4)
        self.frame_tela.place(relx=0, rely=0, relheight=0.3,relwidth=1)
        self.frame_baixo = Frame(self.mnc,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_baixo.place(relx=0.02, rely=0.35, relheight=0.6,relwidth=0.96)
        #funções
        mnc3 = letrasm + numeros + caracteres
        self.gerar_entry = Entry(self.frame_baixo)
        self.gerar_entry.place(relx=0.6, rely=0.53, relwidth=0.05)
        def gerar_senhamnc():
            try:
                int(self.gerar_entry.get())
            except:
                messagebox.showerror(title='Erro ao gerar senha', message='Por favor colocar um número inteiro válido')
            if int(self.gerar_entry.get()) < 8 or int(self.gerar_entry.get()) > 16:
                messagebox.showinfo(title='Erro ao gerar senha', message='só se pode gerar senhas com 8 à 16 dígitos')
            else:
                senha = ''.join(rd.SystemRandom().choices(mnc3, k= int(self.gerar_entry.get())))
                valor.set(senha)
                return senha
        #gadgets
        self.label_senha = Label(self.frame_tela, textvariable=valor, bg=cor5, fg='white', font="Ivy 16 bold")
        self.label_senha.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.bt_gerar = Button(self.frame_baixo,text='Gerar',command=gerar_senhamnc)
        self.bt_gerar.place(relx=0.7, rely=0.5)

        self.label_gerar = Label(self.frame_baixo,text='Coloque o tamanho da senha entre 8 e 16:')
        self.label_gerar.place(relx=0.1,rely=0.2)
    def todos2(self):
        valor=StringVar()
        self.todos = Toplevel()
        #config
        self.todos.configure(bg=cor1)
        self.todos.title('gerador de senhas todos')
        self.todos.resizable(False,False)
        self.todos.geometry('400x200')
        
        #frames
        self.frame_tela = Frame(self.todos, bg=cor4)
        self.frame_tela.place(relx=0, rely=0, relheight=0.3,relwidth=1)
        self.frame_baixo = Frame(self.todos,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_baixo.place(relx=0.02, rely=0.35, relheight=0.6,relwidth=0.96)
        #funções
        todos3 = letrasm + numeros + caracteres + letrasM
        self.gerar_entry = Entry(self.frame_baixo)
        self.gerar_entry.place(relx=0.6, rely=0.53, relwidth=0.05)
        def gerar_senhatodos():
            try:
                int(self.gerar_entry.get())
            except:
                messagebox.showerror(title='Erro ao gerar senha', message='Por favor colocar um número inteiro válido')
            if int(self.gerar_entry.get()) < 8 or int(self.gerar_entry.get()) > 16:
                messagebox.showinfo(title='Erro ao gerar senha', message='só se pode gerar senhas com 8 à 16 dígitos')
            else:
                senha = ''.join(rd.SystemRandom().choices(todos3, k= int(self.gerar_entry.get())))
                valor.set(senha)
                return senha
        #gadgets
        self.label_senha = Label(self.frame_tela, textvariable=valor, bg=cor5, fg='white', font="Ivy 16 bold")
        self.label_senha.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.bt_gerar = Button(self.frame_baixo,text='Gerar',command=gerar_senhatodos)
        self.bt_gerar.place(relx=0.7, rely=0.5)

        self.label_gerar = Label(self.frame_baixo,text='Coloque o tamanho da senha entre 8 e 16:')
        self.label_gerar.place(relx=0.1,rely=0.2)


class funcao_gerador(geradores):
    def Mmn(self):
        self.Mmn2()
    def Mmc(self):
        self.Mmc2()
    def Mnc(self):
        self.Mnc2()
    def mnc(self):
        self.mnc2()
    def todos(self):
        self.todos2()


class tela_gerador(funcao_gerador):
    def tela_gera(self):
        self.telaGera = Toplevel()
        self.config_telaGera()
        self.frame_gera()
        self.gadgets_gera()
        self.telaGera.mainloop()
    def config_telaGera(self):
        self.telaGera.title('Gerador de senha')
        self.telaGera.geometry('500x300')
        self.telaGera.resizable(False,False)
        self.telaGera.configure(bg=cor1)
    def frame_gera(self):
        self.frame_gera1 = Frame(self.telaGera,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_gera1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
    def gadgets_gera(self):
        self.b_Mmn = Button(self.frame_gera1, text=f'Letras maiúsculas,\nminúsculas,\nnúmeros', font=('Ivy 10 bold'),command=self.Mmn)
        self.b_Mmn.place(relx=0.1, rely=0.15)
        self.b_Mmc = Button(self.frame_gera1, text=f'Letras maiúsculas,\nminúsculas,\ncaractéres especiais', font=('Ivy 10 bold'),command=self.Mmc)
        self.b_Mmc.place(relx=0.1, rely=0.55)
        self.b_Mnc = Button(self.frame_gera1, text=f'Letras maiúsculas,\nnúmeros,\ncaractéres especiais', font=('Ivy 10 bold'),command=self.Mnc)
        self.b_Mnc.place(relx=0.5, rely=0.15)
        self.b_mnc = Button(self.frame_gera1, text=f'Letras maiúsculas,\nminúsculas,\ncaractéres especiais', font=('Ivy 10 bold'),command=self.mnc)
        self.b_mnc.place(relx=0.5, rely=0.55)
        self.b_todos = Button(self.frame_gera1, text='Todos', font=('Ivy 10 bold'),command=self.todos)
        self.b_todos.place(relx=0.85, rely=0.4)


class funcao_gerenciador():
    def limpa_tela(self):
        self.id_entry.delete(0, END)
        self.app_entry.delete(0, END)
        self.nick_entry.delete(0, END)
        self.senha_entry.delete(0, END)
    def conecta_bd2(self):
        self.conn2 = sq.connect(f'{self.login_entry.get()}.db')
        self.cursor2 = self.conn2.cursor()
    def desconecta_bd2(self):
        self.conn2.close()
    def monta_tabelas2(self):
        self.conecta_bd2()
        
        self.cursor2.execute("""
            CREATE TABLE IF NOT EXISTS conta (
                cod INTEGER PRIMARY KEY,
                app CHAR(40) NOT NULL,
                nick CHAR(20),
                senha CHAR(16)
            );
        """)
        self.conn2.commit()
        self.desconecta_bd2()
    def variaveis(self):
        self.id = self.id_entry.get()
        self.app = self.app_entry.get()
        self.nick = self.nick_entry.get()
        self.senha = self.senha_entry.get()
    def add(self):
        self.variaveis()
        self.conecta_bd2()
        self.cursor2.execute(""" INSERT INTO conta (app, nick, senha)
            VALUES (?, ?, ?)""", (self.app, self.nick, self.senha))
        self.conn2.commit()
        self.desconecta_bd2()
        self.select_lista2()
        self.limpa_tela()
    def select_lista2(self):
        self.lista_contas.delete(*self.lista_contas.get_children())
        self.conecta_bd2()
        lista = self.cursor2.execute(""" SELECT cod, app, nick, senha FROM conta
            ORDER BY cod ASC; """)
        for i in lista:
            self.lista_contas.insert("", END, values=i)
        self.desconecta_bd2()
    def onDoubleClick(self, event):
        self.limpa_tela()
        self.lista_contas.selection()

        for n in self.lista_contas.selection():
            col1, col2, col3, col4 = self.lista_contas.item(n, 'values')
            self.id_entry.insert(END, col1)
            self.app_entry.insert(END, col2)
            self.nick_entry.insert(END, col3)
            self.senha_entry.insert(END, col4)
    def deletar(self):
        self.variaveis()
        self.conecta_bd2()
        self.cursor2.execute("""DELETE FROM conta WHERE cod = ? """, [self.id])
        self.conn2.commit()
        self.desconecta_bd2()
        self.limpa_tela()
        self.select_lista2()
    def editar(self):
        self.variaveis()
        self.conecta_bd2()
        self.cursor2.execute(""" UPDATE conta SET app = ?, nick = ?, senha = ?
            WHERE cod = ? """, (self.app, self.nick, self.senha, self.id))
        self.conn2.commit()
        self.desconecta_bd2()
        self.select_lista2()
        self.limpa_tela()
    def buscar(self):
        self.conecta_bd2()
        self.lista_contas.delete(*self.lista_contas.get_children())

        self.app_entry.insert(END, '%')
        app = self.app_entry.get()
        self.cursor2.execute(""" SELECT cod, app, nick, senha FROM conta
            WHERE app LIKE '%s' ORDER BY app ASC""" % app)
        buscarapp_contas = self.cursor2.fetchall()
        for i in buscarapp_contas:
            self.lista_contas.insert('', END, values=i)
        self.limpa_tela()
        self.desconecta_bd2()


class tela_gerenciador(funcao_gerenciador):
    def tela_geren(self):
        self.telaGeren = Toplevel()
        self.config_tela_geren()
        self.monta_tabelas2()
        self.frames_geren()
        self.gadgets_geren()
        self.lista_frame_geren2()
        self.select_lista2()
        self.telaGeren.mainloop()
    def config_tela_geren(self):
        self.telaGeren.geometry('700x500')
        self.telaGeren.resizable(False,False)
        self.telaGeren.title('Gerenciador de senhas')
        self.telaGeren.configure(bg=cor1)
    def frames_geren(self):
        self.frame_geren1 = Frame(self.telaGeren,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_geren1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_geren2 = Frame(self.telaGeren,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_geren2.place(relx=0.02, rely=0.51, relwidth=0.96, relheight=0.46)
    def gadgets_geren(self):
        self.b_buscar = Button(self.frame_geren1, text='Buscar', font=('Ivy 10 bold'),command=self.buscar)
        self.b_buscar.place(relx=0.2, rely=0.15, relwidth=0.1, relheight=0.1)
        self.b_limpar = Button(self.frame_geren1, text='Limpar', font=('Ivy 10 bold'),command=self.limpa_tela)
        self.b_limpar.place(relx=0.32, rely=0.15, relwidth=0.1, relheight=0.1)
        self.b_novo = Button(self.frame_geren1, text='Novo', font=('Ivy 10 bold'), command=self.add)
        self.b_novo.place(relx=0.6, rely=0.15, relwidth=0.1, relheight=0.1)
        self.b_excluir = Button(self.frame_geren1, text='Excluir', font=('Ivy 10 bold'),command=self.deletar)
        self.b_excluir.place(relx=0.72, rely=0.15, relwidth=0.1, relheight=0.1)
        self.b_editar = Button(self.frame_geren1, text='Editar', font=('Ivy 10 bold'),command=self.editar)
        self.b_editar.place(relx=0.84, rely=0.15, relwidth=0.1, relheight=0.1)

        self.lb_app = Label(self.frame_geren1, text='App/Site/Programa', font='verdana 10 bold')
        self.lb_app.place(relx=0.06, rely=0.35)
        self.lb_nick = Label(self.frame_geren1, text='Nick', font='verdana 10 bold')
        self.lb_nick.place(relx=0.06, rely=0.65)
        self.lb_senha = Label(self.frame_geren1, text='Senha', font='verdana 10 bold')
        self.lb_senha.place(relx=0.5, rely=0.65)
        self.lb_id = Label(self.frame_geren1, text='ID', font='verdana 12 bold',)
        self.lb_id.place(relx=0.06, rely=0.05)

        self.id_entry = Entry(self.frame_geren1)
        self.id_entry.place(relx=0.06, rely=0.16, relwidth= 0.12)
        self.app_entry = Entry(self.frame_geren1)
        self.app_entry.place(relx=0.06, rely=0.46, relwidth= 0.6)
        self.nick_entry = Entry(self.frame_geren1)
        self.nick_entry.place(relx=0.06, rely=0.76, relwidth= 0.3)
        self.senha_entry = Entry(self.frame_geren1)
        self.senha_entry.place(relx=0.5, rely=0.76, relwidth= 0.4)
    def lista_frame_geren2(self):
        self.lista_contas = ttk.Treeview(self.frame_geren2, height= 3, column=('col1', 'col2', 'col3', 'col4'))
        self.lista_contas.heading('#0', text='')
        self.lista_contas.heading('#1', text='Id')
        self.lista_contas.heading('#2', text='App')
        self.lista_contas.heading('#3', text='Nick')
        self.lista_contas.heading('#4', text='Senha')
        
        self.lista_contas.column('#0', width=1)
        self.lista_contas.column('#1', width=25)
        self.lista_contas.column('#2', width=250)
        self.lista_contas.column('#3', width=175)
        self.lista_contas.column('#4', width=125)

        self.lista_contas.place(relx=0.02, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrool_lista = Scrollbar(self.frame_geren2, orient='vertical')
        self.lista_contas.configure(yscroll=self.scrool_lista.set)
        self.scrool_lista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
        self.lista_contas.bind("<Double-1>", self.onDoubleClick)


class funcao_usuario(tela_gerenciador,tela_gerador):
    def gerenciador(self):
        self.tela_geren()
    def gerador(self):
        self.tela_gera()


class tela_usuario(funcao_usuario):
    def tela_usu(self):
        self.telausu = Toplevel()
        self.config_telausu()
        self.frames_usu()
        self.gadgets_usu()
        self.telausu.mainloop()
    def config_telausu(self):
        self.telausu.geometry('400x400')
        self.telausu.resizable(False,False)
        self.telausu.title('Tela do usuário')
        self.telausu.configure(bg=cor1)
    def frames_usu(self):
        self.frame_usu = Frame(self.telausu,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_usu.place(relx=0.05,rely=0.25, relwidth=0.9, relheight=0.7)
    def gadgets_usu(self):
        self.usuario = Label(self.telausu, text=f'Olá,{self.login_entry.get()}', font='Ivy 20 bold', fg=cor5, bg=cor1)
        self.usuario.place(relx=0.3,rely=0.1)


        self.bt_gerenciador = Button(self.frame_usu,text='Gerenciador', font='Ivy 12 bold', command=self.gerenciador)
        self.bt_gerenciador.place(relx=0.35, rely=0.3)
        self.bt_gerador = Button(self.frame_usu,text='Gerador', font='Ivy 12 bold',command=self.gerador)
        self.bt_gerador.place(relx=0.4, rely=0.5)


class funcao_cadastro():
    def limpa_cadas(self):
        self.username_entry.delete(0, END)
        self.senha_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sq.connect('contas.db')
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def cadastrar(self):
        self.username = self.username_entry.get()
        self.senha = self.senha_SQL
        self.conecta_bd()
        if (self.username == '' or self.senha == ''):
            messagebox.showinfo(title='Erro ao cadatrar', message='Um dos campos está incompleto')
        elif len(self.senha_entry.get()) < 8:
            messagebox.showinfo(title='Erro ao cadatrar', message='A senha tem que ter mais de 8 digítos')
        else:
            self.cursor.execute("""INSERT INTO contas (login, senha) 
                VALUES(?,?) """, (self.username, self.senha))
            self.conn.commit()

        self.desconecta_bd()
        self.limpa_cadas()
    

class tela_cadastro(funcao_cadastro):
    def tela_cadas(self):
        self.telaCadas = Toplevel()
        self.config_tela_cadas()
        self.frame_tela_cadas()
        self.gadgets_cadas()
        self.telaCadas.mainloop()
    def config_tela_cadas(self):
        self.telaCadas.geometry('400x600')
        self.telaCadas.resizable(False,False)
        self.telaCadas.title('Tela de cadastro')
        self.telaCadas.configure(bg=cor1)
    def frame_tela_cadas(self):
        self.frame_cadastro = Frame(self.telaCadas,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_cadastro.place(relx=0.05,rely=0.25, relwidth=0.9, relheight=0.7)
    def gadgets_cadas(self):
        self.titulo = Label(self.telaCadas, text=f'Gerenciador \n de senhas', justify= CENTER, font='Ivy 20 bold', fg=cor5, bg=cor1)
        self.titulo.place(relx=0.3,rely=0.1)

        self.username_label = Label(self.frame_cadastro, text='Nome do Usuário:',font='Ivy 16 bold', fg=cor5)
        self.username_label.place(relx=0.1, rely=0.05)
        self.username_entry = Entry(self.frame_cadastro)
        self.username_entry.place(relx=0.1, rely=0.12, relwidth=0.7)
        
        self.senha_label = Label(self.frame_cadastro, text='Senha:',font='Ivy 16 bold', fg=cor5)
        self.senha_label.place(relx=0.1, rely=0.3)
        self.senha_entry = Entry(self.frame_cadastro, show='*')
        self.senha_entry.place(relx=0.1, rely=0.37, relwidth=0.7)
        self.senha_codificada = sha256(self.senha_entry.get().encode())
        self.senha_SQL = self.senha_codificada.hexdigest()

        self.bt_cadastrar = Button(self.frame_cadastro,text='Cadastrar', font='Ivy 12 bold', command=self.cadastrar)
        self.bt_cadastrar.place(relx=0.36, rely=0.7)


class funcao_tela_login(tela_cadastro,tela_usuario):
    def conecta_bd(self):
        self.conn = sq.connect('contas.db')
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def monta_bd(self):
        self.conecta_bd()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contas (
                cod INTERGER PRIMARY KEY,
                login CHAR(20)NOT NULL,
                senha CHAR(16)NOT NULL
            );
        """)
        self.conn.commit()
        self.desconecta_bd()
    def entrar(self):
        self.login = self.login_entry.get()
        self.senha = self.senha_SQL
        self.conecta_bd()
        self.cursor.execute("""SELECT * FROM contas WHERE (login = ? and senha = ?)""", (self.login, self.senha))
        self.verificar = self.cursor.fetchone()
        try:
            if (self.login in self.verificar and self.senha in self.verificar):
                self.tela_usu()
        except:
            messagebox.showinfo(title='Login info', message='algum dado está incorreto ou você não está cadastrado!')
        self.desconecta_bd()
    def cadastro(self):
        self.tela_cadas()


class tela_de_login(funcao_tela_login):
    def __init__(self):
        self.tela_login = tela_login
        self.tela()
        self.frame_tela()
        self.gadgets()
        self.monta_bd()
        self.tela_login.mainloop()
    def tela(self):
        self.tela_login.geometry('400x600')
        self.tela_login.resizable(False,False)
        self.tela_login.title('Gerenciador de senhas')
        self.tela_login.configure(bg=cor1)
    def frame_tela(self):
        self.frame_login = Frame(self.tela_login,bd=4,highlightbackground=cor3,highlightthickness=3)
        self.frame_login.place(relx=0.05,rely=0.25, relwidth=0.9, relheight=0.7)
    def gadgets(self):
        self.titulo = Label(self.tela_login, text=f'Gerenciador \n de senhas', justify= CENTER, font='Ivy 20 bold', fg=cor5, bg=cor1)
        self.titulo.place(relx=0.3,rely=0.1)

        self.login_label = Label(self.frame_login, text='Login:',font='Ivy 16 bold', fg=cor5)
        self.login_label.place(relx=0.1, rely=0.05)
        self.login_entry = Entry(self.frame_login)
        self.login_entry.place(relx=0.1, rely=0.12, relwidth=0.7)
        
        self.senha_label = Label(self.frame_login, text='Senha:',font='Ivy 16 bold', fg=cor5)
        self.senha_label.place(relx=0.1, rely=0.3)
        self.senha_entry = Entry(self.frame_login, show='*')
        self.senha_entry.place(relx=0.1, rely=0.37, relwidth=0.7)
        self.senha_codificada = sha256(self.senha_entry.get().encode())
        self.senha_SQL = self.senha_codificada.hexdigest()

        self.bt_entrar = Button(self.frame_login,text='Entrar', font='Ivy 12 bold', command=self.entrar)
        self.bt_entrar.place(relx=0.4, rely=0.6)
        self.bt_cadastrar = Button(self.frame_login,text='Cadastrar', font='Ivy 12 bold', command=self.cadastro)
        self.bt_cadastrar.place(relx=0.36, rely=0.7)


tela_de_login()