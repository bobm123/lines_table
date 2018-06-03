#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `lines_table` package."""

import pytest

from click.testing import CliRunner

from lines_table import lines_table
from lines_table import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'lines_table.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

def test_fie_to_di():
    """Test feet-inch-eights to decimal inch conversion."""

    # 0 feet, 0 inches, 1/8 inch
    assert lines_table.fie_to_di('0-0-1') == .125

    # 0 feet, 1 inch, 2/8
    assert lines_table.fie_to_di('0-1-2') == 1.25

    # 1 foot, 2 inch, 3/8
    assert lines_table.fie_to_di('1-2-3') == 14.375

    # No coversion needed
    assert lines_table.fie_to_di(3.14) == 3.14
