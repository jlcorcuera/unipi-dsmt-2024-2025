# Hands-on session 1: FedLang, a Middleware Support to Federated Learning Experiments + Pyrlang

## Prerequisites

Make sure you have installed:

- [Python 3.11](https://www.python.org/downloads/), You can use pyenv also.
- [Term](https://github.com/Pyrlang/Term)
- [Pyrlang](https://github.com/Pyrlang/Pyrlang)


## Exercises:

### Exercise slide 22:

In one terminal, execute the following command:

```bash
python exercise_02.py
```

Start a new Erlang node:

```bash
erl -name test_erlang_node@127.0.0.1 -setcookie "abcde"
```

Send a message to the Pyrlang node:

```erlang
{nodeMailBox, 'pyrlang_node2@127.0.0.1'}!{self(), "Message from Erlang."}.
```


### Exercise slide 23:

In one terminal, execute the following command:

```bash
python exercise_03.py
```

Start a new Erlang node:

```bash
erl -name test_erlang_node@127.0.0.1 -setcookie "abcde"
```

Send a message to the Pyrlang node:

```erlang
{nodeMailBox, 'pyrlang_node3@127.0.0.1'}!{self(), [1, 45, 784, 6]}.
```


### Exercise slide 24:

In one terminal, execute the following command:

```bash
python exercise_04a.py &
python exercise_04b.py &
```

Start a new Erlang node:

```bash
erl -name test_erlang_node@127.0.0.1 -setcookie "abcde"
```

Run the following code inside the Erlang node:

```erlang
{nodeMailBox, 'pyrlang_node4a@127.0.0.1'}!{self()}.
receive M -> M end.
{PY1, Data} = M.
{nodeMailBox, 'pyrlang_node4b@127.0.0.1'}!{self(), Data}.
receive U -> U end.
```
