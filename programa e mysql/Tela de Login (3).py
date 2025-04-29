import customtkinter as ctk

#Validação
def validção_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    #Dados corretos (Fixos)
    if usuario == 'Fulano' and senha == '12345678':
        resultado_login.configure(text='Login feito com sucesso!',text_color='green')
    else:
        resultado_login.configure(text='Senha ou usuario Incorretos, tente novamente!',text_color='red')
        


#Aparencia
ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Tela de Login')
app.geometry('300x400')

#Usuario
label_usuario = ctk.CTkLabel(app,text='Usuario:',font=("Arial", 16, "bold"))
label_usuario.pack(pady=20)

campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu Usuario')
campo_usuario.pack(pady=1)

#Senha
label_senha = ctk.CTkLabel(app,text='Senha:',font=("Arial", 16, "bold"))
label_senha.pack(pady=20)

campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua Senha',show='*')
campo_senha.pack(pady=1)

#Botão
botão_login = ctk.CTkButton(app,text='Continuar',command=validção_login)
botão_login.pack(pady=30)

#Campo de resposta de login
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=20)


app.mainloop()
