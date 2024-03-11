from app.etl import configuracao, extract, load, transformation


def test_config():
    assert configuracao() == 'senha postgres'
