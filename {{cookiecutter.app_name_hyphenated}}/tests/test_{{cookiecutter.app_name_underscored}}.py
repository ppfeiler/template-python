from unittest.mock import MagicMock, patch
from {{ cookiecutter.app_name_underscored }}.app import run


@patch("builtins.print")
def test_run(mock_print: MagicMock) -> None:
    run()
    mock_print.assert_called_once_with("Hello World from {{cookiecutter.app_name_hyphenated}}")
