![logo](/home/shinji/school/503/pounesolve/assets/pounesolve.png)

<div align="center">
	<img alt="Version" src="https://img.shields.io/badge/version-1.0-blue" />
	<img alt="Binary support" src="https://img.shields.io/badge/binary%20support-i386%2Famd64-success" />
</div>



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



### Shellcode exploit

To obtain a shell

```
python3 pounesolve.py shellcode -s tests/shellcode/babyshell1/babyshell
```

To read a specific file

```bash
python3 pounesolve.py shellcode -r tests/shellcode/flag.txt tests/shellcode/babyshell1/babyshell
```



### Overwrite exploit

Exploit an address return overwrite

```bash
python pounesolve.py overwrite -t "ret2win" tests/overwrite/ret2win/ret2win
```

This exploit to be successful need to have a `flag.txt` in the current directory
