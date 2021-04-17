from libpyhonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'gelhen@gmail.com',
        'gelhen@gmail.com',
        'Cursos PythonPro',
        'Teste envio e-mail'
    )
    assert 'gelhen@gmail.com' in resultado