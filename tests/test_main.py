from unittest.mock import patch, Mock

import pytest

from exfiltrieve.__main__ import execute_cmd

import subprocess
def test_execute_cmd():
    with (patch("subprocess.Popen") as popen):
        input = {'SUPUSERS': {'cmd': "grep -v -E '^#' /etc/passwd | awk -F: '$3 == 0{print $1}'", 'msg': 'Super Users Found:', 'results': []}, 'WHOAMI': {'cmd': 'whoami', 'msg': 'Current User', 'results': []}}
        expected = {'SUPUSERS': {'cmd': "grep -v -E '^#' /etc/passwd | awk -F: '$3 == 0{print $1}'", 'msg': 'Super Users Found:', 'results': ["1","2"]}, 'WHOAMI': {'cmd': 'whoami', 'msg': 'Current User', 'results': ["3","4"]}}

        process_mock = Mock(name="process")
        comm = Mock(name="communication",side_effect = [[b"1\n2", None], [b"3\n4", None]])

        process_mock.communicate = comm
        popen.return_value =process_mock

        actual  = execute_cmd(input)
        assert actual == expected