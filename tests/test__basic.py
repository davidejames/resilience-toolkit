

from retry_toolkit.simple import retry


def test__retry():

    @retry()
    def foo():
        pass

    foo()


