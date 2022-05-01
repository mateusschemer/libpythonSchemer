from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None

def test_remetente():
    enviador=Enviador()
    resultado=enviador.enviar(
        'mateus.schemer@gmail.com',
        'karin.luccas@hotmail.com',
        'Teste teste',
        'teste python'
    )
    assert 'mateus.schemer@gmail.com' in resultado