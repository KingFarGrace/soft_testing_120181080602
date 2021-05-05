from homework_3_15 import dictionary
import pytest


class Test_Dictionary:

    def setup(self):
        dictionary.dictionary['test'] = ['测试', '考试']
        dictionary.dictionary['hello'] = ['你好']
        dictionary.dictionary['world'] = ['世界']

    def test_add_word(self):
        print(dictionary.add_word('java', ['爪哇', '一种语言']))

    def test_del_word(self):
        assert dictionary.del_word('python') is False
        assert dictionary.del_word('hello') is True

    def test_get_word(self):
        assert dictionary.get_word('python') is None
        assert dictionary.get_word('test') == ['测试', '考试']
        assert dictionary.get_word('hello') == ['你好']

    def test_revise_word(self):
        assert dictionary.revise_word('python', 'java') is False
        assert dictionary.revise_word('hello', 'hi') is True

    def test_add_paras(self):
        assert dictionary.add_paras('test', ['测验', '考验']) == ['测试', '考试', '测验', '考验']
        assert dictionary.add_paras('python', ['一种语言']) == ['一种语言']
