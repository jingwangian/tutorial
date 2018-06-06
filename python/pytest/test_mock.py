#!/usr/bin/env python3

from mock import Mock, MagicMock, call


class MySupClass:
    def on_command(command):
        print("MySupClass:on_command %s", command)


class MyClass1:
    number = 100
    name = 'ian'

    def on_command(command):
        super().on_command('task run')
        print("MyClass1 %s", command)


def fun2(*arg, **karg):
    return "fun2"
# mock = Mock(spec=MyClass1)

# print(dir(mock))
# print(type(mock))
# print(isinstance(mock, MyClass1))
# print(mock.name)


mock = MagicMock()
p = mock.Process1

mock.state.st_size = 100

mock.fun1.return_value = "fun1_invoked"
mock.fun2 = fun2
# mock.state.state.create_task.return_value = task_info

c1 = MyClass1()

p(c1, 'context')
p.items_of_interested()

print(p.method_calls)
print(mock.mock_calls)
print(mock.method_calls)
mock.Process1.assert_called_with(c1, 'context')

print(mock.state.st_size)

print(mock.fun1('a', 100))

print(mock.fun2('a', 100))


mock.fun3.side_effect = [1, 2, 3]
print(mock.fun3('a'))
print(mock.fun3('b'))
