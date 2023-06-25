import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox

class BackEnd():
    def connect_db(self):
        self.conn = sqlite3.connect('sistemaCadastro.db')
        self.cursor = self.conn.cursor()
        print('Banco de dados conectado')

    def disconnect_db(self):
        self.conn.close()
        print('Banco de dados desconectado')

    def create_table(self):
        self.connect_db()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                cPassword TEXT NOT NULL
            );
        ''')
        self.conn.commit()
        print('Tabela criada com sucesso!')
        self.disconnect_db()

    def register_user(self):
        self.username_register = self.username_register_entry.get()
        self.email_register = self.email_register_entry.get()
        self.password_register = self.password_register_entry.get()
        self.comfirm_register = self.confirm_register_entry.get()

        self.connect_db()

        self.cursor.execute('''
            INSERT INTO users (username, email, password, cPassword)
            VALUES (?, ?, ?, ?)''', (self.username_register, self.email_register, self.password_register, self.comfirm_register))
        
        try:
            if(self.username_register == '' or self.email_register == '' or self.password_register == '' or self.comfirm_register == ''):
                messagebox.showerror(title='Sistema de login', message='Preencha todos os campos!')
            elif(len(self.username_register) < 4):
                messagebox.showwarning(title='Sistema de login', message='O nome deve ter pelo menos 4 caracteres.')
            elif(len(self.email_register) < 12):
                messagebox.showwarning(title='Sistema de login', message='O e-mail deve ter pelo menos 12 caracteres.')
            elif(len(self.password_register) < 4):
                messagebox.showwarning(title='Sistema de login', message='A senha deve ter pelo menos 4 caracteres.')
            elif(self.password_register != self.comfirm_register):
                messagebox.showerror(title='Sistema de login', message='ERRO!!!\nAs senhas não são iguais.')
            else:
                self.conn.commit()
                messagebox.showinfo(title='Sistema de login', message=f'{self.username_register}\nOs seus dados foram cadastrados com sucesso!')
        except:
            messagebox.showerror(title='Sistema de login', message='Erro no prosessamento do seu cadastro!\nTente novamente!')



class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configuracoes_janela_principal()
        self.tela_login()
        self.create_table()


    #configurando tela principal
    def configuracoes_janela_principal(self):
        self.geometry('700x400')
        self.title('Sistema de Login')
        self.resizable(False, False)

    def tela_login(self):
        #titulo da plataforma
        self.title = ctk.CTkLabel(self, text='Faça seu login\nou Cadastre-se na nossa\nplataforma e acesse nossos serviços!', font=('Century Gothic ', 14, 'bold'))
        self.title.place(x=45, y=30)

        #trabalhando com as imagens
        self.img = PhotoImage(file='bg-login1.png')
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.place(x=10, y=100)

        #frame do formulario de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=360, y=30)

        #colocando widgets dentro do frame - formulario de login
        self.lb_title = ctk.CTkLabel(self.frame_login, text='Faça o seu login', font=('Century Gothic ', 22, 'bold'))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Nome', font=('Century Gothic ', 16, 'bold'), corner_radius=15, border_color='#1F6AA5')
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10)

        self.password_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Senha', font=('Century Gothic ', 16, 'bold'), corner_radius=15, border_color='#1F6AA5', show='*')
        self.password_login_entry.grid(row=2, column=0, padx=10, pady=10)

        self.ckeckboxPass_login_entry = ctk.CTkCheckBox(self.frame_login, text='Mostrar senha', font=('Century Gothic ', 14, 'bold'), corner_radius=20)
        self.ckeckboxPass_login_entry.grid(row=3, column=0, padx=10, pady=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text='fazer login'.upper(), font=('Century Gothic ', 16, 'bold'), corner_radius=15)
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)

        self.span = ctk.CTkLabel(self.frame_login, text='Se não tem uma conta cadastre-se agora\n no botão abaixo e acesse o nosso sistema!', font=('Century Gothic ', 12, 'bold'))
        self.span.grid(row=5, column=0, padx=10, pady=5)

        self.btn_register = ctk.CTkButton(self.frame_login, width=300, text='cadastre-se'.upper(), font=('Century Gothic ', 16, 'bold'), corner_radius=15, fg_color='green', hover_color='#005900', command=self.tela_cadastro)
        self.btn_register.grid(row=6, column=0, padx=10, pady=20)

    def tela_cadastro(self):
        #remover fomulario de login
        self.frame_login.place_forget()
        
        #frame do formulario de cadastro
        self.frame_register = ctk.CTkFrame(self, width=350, height=380)
        self.frame_register.place(x=360, y=30)

        #criando titulo
        self.lb_title = ctk.CTkLabel(self.frame_register, text='Faça seu cadastro', font=('Century Gothic ', 22, 'bold'))
        self.lb_title.grid(row=0, column=0, padx=10, pady=15)

        #widgets do formulario de cadastro
        self.username_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Nome', font=('Century Gothic ', 16, 'bold'), corner_radius=15, border_color='#1F6AA5')
        self.username_register_entry.grid(row=1, column=0, padx=10, pady=5)

        self.email_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='E-mail', font=('Century Gothic ', 16, 'bold'), corner_radius=15, border_color='#1F6AA5')
        self.email_register_entry.grid(row=2, column=0, padx=10, pady=5)

        self.password_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Senha', font=('Century Gothic ', 16, 'bold'), corner_radius=15, border_color='#1F6AA5', show='*')
        self.password_register_entry.grid(row=3, column=0, padx=10, pady=5)

        self.confirm_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Confirmar senha', font=('Century Gothic ', 16, 'bold'), corner_radius=15, border_color='#1F6AA5', show='*')
        self.confirm_register_entry.grid(row=4, column=0, padx=10, pady=5)

        self.ckeckboxPass_register_entry = ctk.CTkCheckBox(self.frame_register, text='Mostrar senha', font=('Century Gothic ', 14, 'bold'), corner_radius=20)
        self.ckeckboxPass_register_entry.grid(row=5, column=0, padx=10, pady=10)

        self.btn_save = ctk.CTkButton(self.frame_register, width=300, text='fazer cadastro'.upper(), font=('Century Gothic ', 16, 'bold'), corner_radius=15, fg_color='green', hover_color='#005900', command=self.register_user)
        self.btn_save.grid(row=6, column=0, padx=10, pady=5)

        self.btn_back = ctk.CTkButton(self.frame_register, width=300, text='voltar ao login'.upper(), font=('Century Gothic ', 16, 'bold'), corner_radius=15, fg_color='gray', hover_color='#303030', command=self.tela_login)
        self.btn_back.grid(row=7, column=0, padx=10, pady=15)

    def clean_register(self):
        self.username_register_entry.delete(0, END)
        self.email_register_entry.delete(0, END)
        self.password_register_entry.delete(0, END)
        self.confirm_register_entry.delete(0, END)

    def clean_login(self):
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

if __name__=='__main__':
    app = App()
    app.mainloop()