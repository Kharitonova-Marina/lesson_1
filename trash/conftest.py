# в этом файле всегда фикстуры
# фикстура обозночается @

import random
import pytest


@pytest.fixture()
def random_int():
    return random.randint(5, 10)


