def test_fixture(testdir):
    testdir.makepyfile(
        """
    import pytest

    def test_fixture(future_session_mock_from_boolean):

        assert future_session_mock_from_boolean is not None
    """
    )
    result = testdir.runpytest("--verbose")
    result.stdout.fnmatch_lines("test_fixture.py::test_fixture PASSED*")
