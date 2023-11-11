from unittest.mock import patch, Mock

import pytest

from exfiltrieve.__main__ import execute_cmd

@patch("subprocess.Popen.communicate")
def test_execute_cmd(comm):
    input = {'SUPUSERS': {'cmd': "do something", 'msg': 'Super Users Found:', 'results': []}, 'WHOAMI': {'cmd': 'whoami', 'msg': 'Current User', 'results': []}}
    expected = {'SUPUSERS': {'cmd': "do something", 'msg': 'Super Users Found:', 'results': ["1","2"]}, 'WHOAMI': {'cmd': 'whoami', 'msg': 'Current User', 'results': ["3","4"]}}

    comm.side_effect = [[b"1\n2", None], [b"3\n4", None]]

    actual  = execute_cmd(input)
    assert actual == expected

@pytest.mark.skip("Not covered in source yet")
def test_execute_cmd_failure():
    pass

