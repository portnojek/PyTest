import logging as logger

def test_healthcheck_1():
    logger.info("Just running healthcheck 1.")

'''
żeby to poszło to trzeba aktywować środowisko wirtualne jakby widoczne w głównym katalogu:

utworzyć foldery:python_package - główny, python_package - src, python_package - tests. Wszędzie powinien utworzyć się plik __init__.py
utworzyć w głównym katalogu plik setup.py z pozycją: packages=find_packages()
(venv_pyapi_py3) T:\dev\Python\course-api-testing
potem wykonać komendę: python setup.py install - powinny utworzyć się dwa foldery - build i dist

i już. Jeśli wszystko jest poprawnie skonfigurowane to powinno elegancko pójść.

'''