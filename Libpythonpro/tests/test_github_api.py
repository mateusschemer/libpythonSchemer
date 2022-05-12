from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = "https://avatars.githubusercontent.com/u/102181255?v=4"
    resp_mock.json.return_value = {
        "login": "mateusschemer", "id": 102181255,
        "avatar_url": url
    }
    get_mock = mocker.patch('pythonlibSchemer.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url




def test_buscar_avatar(avatar_url):
    avatar_url = avatar_url()
    url = github_api.buscar_avatar('mateusschemer')
    assert avatar_url== url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('mateusschemer')
    assert 'https://avatars.githubusercontent.com/u/102181255?v=4' == url