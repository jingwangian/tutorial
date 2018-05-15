#!/usr/bin/env python3

from unittest.mock import patch, MagicMock


class MySupClass:
    def on_command(self, command):
        print("MySupClass:on_command {}".format(command))


class MyClass1:
    number = 100
    name = 'ian'

    def on_command(self, command):
        super().on_command(command)
        print("MyClass1 on_command: {}".format(command))


with patch('builtins.super') as myclass_super:
    mock = MagicMock()
    # myclass_super.return_value = mock.on_command

    c1 = MyClass1()

    c1.on_command("task command")

    print(mock.mock_calls)
    print(mock.on_command.method_calls)

    print(myclass_super.mock_calls)

    myclass_super().on_command.assert_called_with('task command')
