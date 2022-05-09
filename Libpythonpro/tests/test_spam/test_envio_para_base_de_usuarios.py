from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
import pytest

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome = 'Mateus', email = 'mateus.schemer@gmail.com'),
            Usuario(nome = 'Karin', email = 'karin,luccas@hotmail.com')
        ],
        [
            Usuario(nome = 'Mateus', email = 'mateus.schemer@gmail.com')
        ]
    ]
)
def test_qde_spam (sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mateus.schemer@gmail.com',
        'Curso Python',
        'Confira as novidades'
    )
    assert len(usuarios) == enviador.qde_emails_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qde_emails_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qde_emails_enviados += 1


def test_parametros_de_spam (sessao):
    usuario = Usuario(nome = 'Mateus', email = 'mateus.schemer@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'karin.luccas@hotmail.com',
        'Curso Python',
        'Confira as novidades'
    )
    assert enviador.parametros_de_envio == (
        'karin.luccas@hotmail.com',
        'mateus.schemer@gmail.com',
        'Curso Python',
        'Confira as novidades'
    )