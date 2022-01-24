import pwn
import os
import utils

class Binary:
    def __init__(self, path):
        self.posix_path = path
        self.path = str(path)

        utils.check_binary(self)

        self.ELF = pwn.ELF(self.path)

        self.architecture_setup()

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
            sys.exit(1)

    def get_overflow_offset(self):
        process = pwn.process(self.path)
        process.sendline(pwn.cyclic(400, n=4))
        process.wait()

        overflow_offset = -1

        try:
            core = process.corefile

            registers_value = [
                getattr(core, self.sp_register).to_bytes(self.register_size, byteorder='little'),
                getattr(core, self.pc_register).to_bytes(self.register_size, byteorder='little'),
                core.read(getattr(core, self.sp_register), self.register_size),
                core.read(getattr(core, self.pc_register), self.register_size)
            ]

            os.remove(core.path)

            for value in registers_value:
                overflow_offset = pwn.cyclic_find(value)

                if overflow_offset != -1:
                    break

            return overflow_offset

        except Exception as e:
            os.remove(core.path)
