import pytest
from requests import *
@pytest.mark.parametrize("style", ['abap', 'colorful', 'dracula', 'igor'])
@pytest.mark.parametrize("language", ["abap", "apl", "bach"])
@pytest.mark.parametrize("lineos", ["True", "Faulse"])
def test_with_param(style, language, lineos):
    my_session = Session()
    my_session.auth = ("usov_svyatoslav_victorovic", "asdq1234515")
    ans = my_session.post(url='http://185.182.111.235/snippets/',
                          data={
                              'title': "doggie",
                              'code': 'husky',
                              'linenos': lineos,
                              "language": language,
                              "style": style

                          })
    assert ans.status_code == 201
