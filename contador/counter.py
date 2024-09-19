import flet as ft  # Importa a biblioteca Flet para criar a interface gráfica.

# Função principal do aplicativo, onde a interface e a lógica são definidas
def main(page: ft.Page):
    # Define o título da janela do aplicativo
    page.title = "Flet counter example"
    # Alinha o conteúdo da página verticalmente ao centro
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Cria um campo de texto para exibir o valor do contador, inicializando-o em "0"
    # O valor do texto será alinhado à direita, e o campo terá uma largura de 100 pixels
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    # Função chamada ao clicar no botão de diminuir (ícone de remover)
    def minus_click(e):
        # Converte o valor atual do campo de texto em inteiro, subtrai 1, e atualiza o valor do campo
        txt_number.value = str(int(txt_number.value) - 1)
        # Atualiza a interface da página para refletir a mudança
        page.update()

    # Função chamada ao clicar no botão de aumentar (ícone de adicionar)
    def plus_click(e):
        # Converte o valor atual do campo de texto em inteiro, soma 1, e atualiza o valor do campo
        txt_number.value = str(int(txt_number.value) + 1)
        # Atualiza a interface da página para refletir a mudança
        page.update()

    # Adiciona uma linha (ft.Row) contendo os botões e o campo de texto à página
    page.add(
        ft.Row(
            [
                # Botão de ícone para diminuir o contador (ícone de remover)
                # Quando clicado, chama a função minus_click
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                
                # Campo de texto que exibe o valor atual do contador (txt_number)
                txt_number,
                
                # Botão de ícone para aumentar o contador (ícone de adicionar)
                # Quando clicado, chama a função plus_click
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            # Alinha os itens da linha horizontalmente ao centro
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Inicia o aplicativo, chamando a função main como ponto de entrada
ft.app(main)
