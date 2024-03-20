# Crie sua agenda de tarefas com Python

Este código implementa uma aplicação básica de lista de tarefas (to-do app) utilizando Tkinter, uma biblioteca do Python para o desenvolvimento de interfaces gráficas de usuário (GUI).

## Importação de Bibliotecas

- **Tkinter:** Utilizada para criar a interface gráfica.
- **Messagebox:** Usada para mostrar alertas e mensagens para o usuário.

## Funções da Aplicação

### `entertask()`
- **Propósito:** Adiciona novas tarefas.
- **Funcionamento:** Abre uma nova janela onde o usuário pode inserir uma tarefa. Se o usuário inserir texto, este é adicionado à lista na janela principal. Se nenhum texto for inserido, um aviso é exibido.
- **Encerramento:** Fecha a janela de entrada da tarefa após a inserção.

### `deletetask()`
- **Propósito:** Remove uma tarefa selecionada da lista.
- **Funcionamento:** Identifica a tarefa selecionada pelo usuário e a remove da lista.

### `markcompleted()`
- **Propósito:** Marca uma tarefa selecionada como concluída.
- **Funcionamento:** Adiciona um símbolo de verificação (✅) ao final do texto da tarefa selecionada e atualiza a lista com a tarefa modificada.

## Layout e Widgets da Aplicação

- **Janela Principal:** Configurada com um título e contém um quadro para a lista de tarefas e barra de rolagem.
- **Listbox:** Mostra a lista de tarefas. Permite a seleção de tarefas para exclusão ou marcação como completadas.
- **Scrollbar:** Permite a rolagem da lista se o número de tarefas exceder o tamanho da janela.
- **Botões:** Incluem funcionalidades para adicionar uma nova tarefa, excluir a tarefa selecionada e marcar uma tarefa como concluída.

## Execução da Aplicação

- Utiliza `window.mainloop()` para manter a interface gráfica aberta e responsiva ao usuário.

## Resumo da Funcionalidade

Permite ao usuário adicionar, remover e marcar tarefas como concluídas numa interface gráfica simplificada.



## Rodando projeto

Clone o projeto

```bash
  git clone https://github.com/python-brasil/Crie-sua-agenda-de-tarefas-com-Python.git
```

Rodandando o projeto

```bash
  python main.py
```

## Screenshot

![Crie sua  agenda de taferas com Python](https://github.com/python-brasil/Crie-sua-agenda-de-tarefas-com-Python/assets/126124866/793acf8d-67b5-4857-957d-45ffef345362)


## Infos de commits

- :package: novas funcionalidades
- :up: atualizações
- :ant: correções de bug
- :checkered_flag: release


## Nos acompanhe nas redes

- Instagram - [@python_brasil](https://www.instagram.com/python_brasil/)
- LinkedIn - [Comunidade Python Brasil](https://www.linkedin.com/company/comunidade-python-brasil)
- GitHub - [python-brasil](https://github.com/python-brasil)
- YouTube - [@Python_Brasil](https://www.youtube.com/@Python_Brasil)
- Pinterest - [Python Brasil](https://br.pinterest.com/pythonbrasil/)
- TikTok - [@python_brasil](https://www.tiktok.com/@python_brasil)
