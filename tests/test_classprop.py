#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `classprop` package."""

import typing

import pytest

from classprop import classprop


@pytest.fixture  # type: ignore
def response() -> None:
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    pass
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response: typing.Any) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    pass
