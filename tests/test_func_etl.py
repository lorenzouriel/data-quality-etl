from app.etl import configuracao, extract, transformation, load

def test_config():
    assert configuracao() == 'senha postgres'
    