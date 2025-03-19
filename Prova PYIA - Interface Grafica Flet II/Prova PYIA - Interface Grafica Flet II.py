import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nome = ft.TextField(label="Nome")
    email = ft.TextField(label="Email")
    mensagem = ft.TextField(label="Mensagem", multiline=True)
    confirmacao = ft.Text(visible=False)
    
    def enviar_formulario(e):
        if nome.value and email.value and mensagem.value:
            confirmacao.value = "Formulário enviado com sucesso!"
            confirmacao.visible = True
            nome.value = ""
            email.value = ""
            mensagem.value = ""
            page.update()
    
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_formulario)
    
    page.add(nome, email, mensagem, botao_enviar, confirmacao)

ft.app(target=main)
