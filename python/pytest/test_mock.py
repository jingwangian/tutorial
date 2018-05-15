#!/usr/bin/env python3

from unittest.mock import Mock, MagicMock, call


class MySupClass:
    def on_command(command):
        print("MySupClass:on_command %s", command)


class MyClass1:
    number = 100
    name = 'ian'

    def on_command(command):
        super().on_command('task run')
        print("MyClass1 %s", command)


# mock = Mock(spec=MyClass1)

# print(dir(mock))
# print(type(mock))
# print(isinstance(mock, MyClass1))
# print(mock.name)

mock = MagicMock()
p = mock.Process1

# mock.state.state.create_task.return_value = task_info

c1 = MyClass1()

p(c1, 'context')
p.items_of_interested()

print(p.method_calls)
print(mock.mock_calls)
print(mock.method_calls)
mock.Process1.assert_called_with(c1, 'context')
# mock.Process1.items_of_interested.assert_called()
