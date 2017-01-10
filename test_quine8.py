
def test_loadia():
    from quine8_machine import Program, CPU,log

    program = Program()
    program.load("NOP")
    program.load("LOADI A",32)
    program.data[32] = 64
    program.data[64] = 10
    cpu = CPU(program)
    cpu.step()
    cpu.step()
    cpu.step()
    log(cpu)

    assert(cpu.a == 10 and cpu.b == 0 and cpu.Z_flag == False)
