from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Mateus', email= 'mateus.schemer@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuarios (sessao):
    usuarios = [Usuario(nome='Mateus', email='mateus.schemer@gmail.com'),
                Usuario(nome='Karin', email='karin.luccas.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()



