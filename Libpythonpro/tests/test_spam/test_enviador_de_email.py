import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailIvalido


def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com', 'mateus.schemer@gmail.com']
)
def test_remetente(destinatario):
    enviador=Enviador()
    resultado=enviador.enviar(
        destinatario,
        'karin.luccas@hotmail.com',
        'Teste teste',
        'teste python'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'mateus']
)
def test_remetente_invalido(remetente):
    enviador=Enviador()
    with pytest.raises(EmailIvalido):
         enviador.enviar(
            remetente,
            'karin.luccas@hotmail.com',
            'Teste teste',
            'teste python'
         )
