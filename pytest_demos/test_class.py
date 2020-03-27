import pytest
class TestClass():
    # @pytest.mark.aaa
    def test_one(self):
        print("test_one method")
        x = 'this'
        # assert 'h' in x
    def test_two(self):
        x = 'hello'
        # assert 'e' not in x

    def test_three(self):
        a = 'hello'
        b = 'hello world'
        # assert a not in b

if __name__ == '__main__':
    pytest.main(['-v','test_class.py::TestClass'])