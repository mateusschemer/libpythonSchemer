from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam


def test_envio_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_email(
        'mateus.schemer@gmail.com',
        'Curso Python',
        'Confira as novidades'
    )
