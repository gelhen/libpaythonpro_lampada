from libpyhonpro.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['gelhen@gmail.com', 'ti@tozzoalimentos.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'gelhen@gmail.com',
        'Cursos PythonPro',
        'Teste envio e-mail'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'gelhen']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'gelhen@gmail.com',
            'Cursos PythonPro',
            'Teste envio e-mail'
        )
