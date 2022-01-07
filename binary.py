import pwn, os, utils

class Binary:
    def __init__(self, path):
        self.posix_path = path
        self.path = str(path)

        utils.check_binary(self)

        self.ELF = pwn.ELF(self.path)

        # setup architecture
        self.architecture_setup()

    # architecture_setup {{{
    def architecture_setup(self):
        if self.ELF.arch == 'amd64':
            self.sp_register = 'rsp'
            self.pc_register = 'rip'
            self.register_size = 8

            self.packing = 'p64'
        elif self.ELF.arch == 'i386':
            self.sp_register = 'esp'
            self.pc_register = 'eip'
            self.register_size = 4

            self.packing = 'p32'
        else:
            Logger.error('Architecture unrecognized')
            exit(1)
    # }}}

    # get_overflow_offset {{{
    def get_overflow_offset(self):
        process = pwn.process(self.path)
        process.sendline(pwn.cyclic(10, n=4))
        process.wait()

        try:
            core = process.corefile

            overflow_offset = pwn.cyclic_find(getattr(core, self.sp_register).to_bytes(self.register_size, byteorder='little'), n=4)

            # overwrite may be on program counter and not stack pointer
            if overflow_offset == -1:
                overflow_offset = pwn.cyclic_find(getattr(core, self.pc_register).to_bytes(self.register_size, byteorder='little'), n=4)

            os.remove(core.path)

            return overflow_offset

        except Exception as e:
            print(e)
            os.remove(core.path)
    # }}}
