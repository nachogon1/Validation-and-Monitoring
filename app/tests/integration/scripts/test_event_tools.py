from click.testing import CliRunner
from loguru import logger
from loguru_caplog import loguru_caplog as caplog


def test_validate_json():
    from scripts.event_tools import validate_json

    runner = CliRunner()
    result = runner.invoke(
        validate_json, ["--file", "/app/app/tests/mock_data/mock_input.json"]
    )
    assert result.exit_code == 0

    result = runner.invoke(
        validate_json, ["--file", "/app/app/tests/mock_data/mock_input2.json"]
    )
    assert result.exit_code == 1


def test_generate_report(caplog):
    from scripts.event_tools import generate_report

    runner = CliRunner()
    result = runner.invoke(
        generate_report,
        ["--file", "/app/app/tests/mock_data/mock_input.json"],
        obj=logger,
    )
    assert result.exit_code == 0
    assert caplog.messages == [
        "Event submission_success cooccur with 1 events at 01/30/2018."
    ]
