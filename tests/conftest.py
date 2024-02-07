import pytest

@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")

@pytest.fixture(scope="module") # относится ко всем методам в файле. можно указать только в одном методе
def set_group():
    print("Enter system")
    yield
    print("Exit system")
