<div align="center">
	<img alt="Logo" src="assets/pounesolve.png" />
</div>
<div align="center">
	<img alt="Version" src="https://img.shields.io/badge/version-1.0-blue" />
	<img alt="Binary support" src="https://img.shields.io/badge/binary%20support-i386%2Famd64-success" />
</div>


This tool was created to ease the exploitation of basic binary for the following exploits: `overwrite return address`, `shellcode`.

In fact, binary exploitation challenges in CTF can be repetitive and just differ by the offset where the input modify the program behavior. 



## Installation

```bash
python3 -m venv .
source bin/activate
pip install -r requirements.txt
```



## Usage


The tool is using coredump of binary to exploit them. These coredump are not always activated, to be sure, use this command:

```bash
echo "core" | sudo tee /proc/sys/kernel/core_pattern
```

### Dépendances

pwntools



### Shellcode exploit

#### Usage

```bash
usage: main.py [-h] [-s] [-r file] [binary]

Generate executable code and send it

positional arguments:
  binary                Binary to exploit

options:
  -h, --help            show this help message and exit
  -s, --shell           Get a shell
  -r file, --read file  Read specified file
```



#### Demo

To obtain a shell

```
python3 main.py shellcode -s tests/shellcode/babyshell1/babyshell
```

To read a specific file

```bash
python3 main.py shellcode -r tests/shellcode/flag.txt tests/shellcode/babyshell1/babyshell
```



### Overwrite exploit

#### Usage

```bash
usage: main.py [-h] [-t TARGET] [binary]

Overwrite a return address to access specific part of the binary

positional arguments:
  binary                Binary to exploit

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET    Function to reach may be function name or address
```



#### Demo

Exploit an address return overwrite

```bash
python main.py overwrite -t "ret2win" tests/overwrite/ret2win/ret2win
```

This exploit to be successful need to have a `flag.txt` in the current directory
