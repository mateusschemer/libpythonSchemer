from unittest.mock import Mock

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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mateus.schemer@gmail.com',
        'Curso Python',
        'Confira as novidades'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam (sessao):
    usuario = Usuario(nome = 'Mateus', email = 'mateus.schemer@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'karin.luccas@hotmail.com',
        'Curso Python',
        'Confira as novidades'
    )
    enviador.enviar.assert_called_once_with (
        'karin.luccas@hotmail.com',
        'mateus.schemer@gmail.com',
        'Curso Python',
        'Confira as novidades'
    )