def test_check_math():
    assert 7*7 == 49

def test_check_78():
    assert 7*8 == 56

class User:
    def __init__(self) -> None:
        self.name = 'Viktor'
        self.second_name = 'Sokol'

user = User()
def text_remove_name():
    user.name = ''
    assert user.name ==''
def text_name():
    assert user_name == 'Viktor'

def test_second_name():
    assert user.second_name() == 'Sokol'
    
