

class Program:
    def __init__(self):
        self.data = [0 for i in range(32)]
        self.pc = 0
    def load(self,*args):
        for a in args:
            self.data[self.pc] = a
            self.pc = self.pc + 1

program = Program()
program.load("NOP")
# program.load("LOAD A", 30)
# program.load("LOAD B", 31)
program.load("JMP", 0)
program.data[30] = 2
program.data[31] = 6

class CPU:
    def __init__(self,program):
        self.pc = 0
        self.Z_flag = False
        self.Eq_flag = False
        self.G_flag = False
        self.L_flag = False
        self.JSP = 0
        self.JSP_enabled = False

        self.a = 0
        self.b = 0
        self.program = program
    def step(self):
        current_instruction = self.program.data[self.pc]
        print "current_instruction", current_instruction
        if current_instruction == "NOP":
            self.pc = self.pc + 1
        elif current_instruction == "LOAD A":
            # need the operand from the next instruction
            operand = self.program.data[self.pc+1]
            print "LOAD A", operand
            self.a = self.get_memory_value_at(operand)
            self.pc = self.pc + 2
        elif current_instruction == "LOAD B":
            operand = self.program.data[self.pc+1]
            print "LOAD B", operand
            self.b = self.get_memory_value_at(operand)
            self.pc = self.pc + 2
        elif current_instruction == "LOADI A":
            operand = self.program.data[self.pc+1]
            address = self.get_memory_value_at(operand)
            self.a = self.get_memory_value_at(address)
            print "LOADI A",operand
            self.pc = self.pc + 2
        elif current_instruction == "ADD A B":
            tmp1=self.a
            tmp2 = self.b
            self.a = tmp1 + tmp2
            self.pc = self.pc + 1
        elif current_instruction == "ISZERO A":
            self.Z_flag = False
            if self.a == 0:
                self.z = True
            self.pc = self.pc + 1
        elif current_instruction == "ISZERO B":
            self.z = False
            if self.b == 0:
                self.Z_flag = True
            self.pc = self.pc + 1
        elif current_instruction == "JMP":
            operand = self.program.data[self.pc+1]
            print "JMP",operand
            self.pc = operand
    def get_memory_value_at(self, operand):
        try:
            return self.program.data[operand]
        except IndexError:
            print "ERROR: invalid memory operand"
    def __str__(self):
        ts = "pc: {} a: {} b: {}".format(self.pc, self.a, self.b)
        return ts

cpu = CPU(program)
cpu.step()
cpu.step()
cpu.step()
print cpu
