# Importar bibliotecas
from tkinter import *
from tkinter import messagebox

# Função para inserir a tarefa na caixa de listagem
def entertask():
    # Uma nova janela aparecerá para receber informações
    input_text = ''
    def add():
        input_text = entry_task.get(1.0, 'end-1c')
        if input_text == '':
            messagebox.showwarning(title='Warning!', message='Please Enter some Text')
        else:
            listbox_task.insert(END, input_text)
        # Fechar a janela 1
        root1.destroy()
    root1 = Tk()
    root1.title('Add task')
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text='Add task', command=add)
    button_temp.pack()
    root1.mainloop()


# função para facilitar a tarefa de exclusão da caixa de listagem
def deletetask():
    # Seleciona o item selecionado e depois o exclu
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

# Executa isso para marcar como concluído
def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    # Armazena o texto do item selecionado em uma string
    temp_marked = listbox_task.get(marked)
    # Atualizar isso
    temp_marked = temp_marked + '✅'
    # Exclua-o e depois insira-o
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


# Criando a janela inicial
window = Tk()

# Dando um título
window.title('DataFlair To_Do_APP')

# Widget de quadro para conter a caixa de listagem e a barra de rolagem
frame_task = Frame(window)
frame_task.pack()

# Para manter itens em uma caixa de listagem
listbox_task = Listbox(frame_task, bg='black', fg='white', height=15, width=50, font='Helvetica')
listbox_task.pack(side=LEFT)

# Scrolldown caso a lista total exceda o tamanho da janela fornecida
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)


# Widget de botão
entry_button = Button(window, text='Add task', width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text='Delete selected task', width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text='Mark as completed', width=50, command=markcompleted)
mark_button.pack(pady=3)


window.mainloop()
