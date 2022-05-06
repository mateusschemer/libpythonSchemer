from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Mateus')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuarios (sessao):
    usuarios = [Usuario(nome='Mateus'), Usuario(nome='Karin')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()



