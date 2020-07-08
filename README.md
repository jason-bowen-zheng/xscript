> This is xscript v0.5, xIDE v0.0 Github repo

> English | [简体中文](./README-zh_cn.md)

# xscript v0.5
xscript is a tiny programming language written in python. Its core(`xscriptcore.py`) is very small.

`xIDE` is a xscript development toolkit

Visit [xscript Home page](https://jason-bowen-zheng.github.io/xscript) for more information.

# Install
1. Clone:
```shell
git clone https://github.com/jason-bowen-zheng/xscript
cd xscript
```

2. Download xscript and dependencies:
```shell
# May need root privileges
pip install -U colorama mkdocs prettytable
sudo make install
```

3. Test xscript:
```shell
make test
```

4. Upgrade xscript:
```shell
sudo make upgrade
```

# How to run my code?
On the directory `xscript`, input `./xscript <file> [args...]`

You can also read examples on `xscript/examples`.
