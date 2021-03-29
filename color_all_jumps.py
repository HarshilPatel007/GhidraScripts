# Color(Red) all Jump(s) in Listing Window.
# https://ghidra.re/ghidra_docs/api/ghidra/program/model/symbol/FlowType.html#isJump()
# @author : Harshil Patel
# @category : Tools

from java.awt import Color


jump_count = 0
JUMP_COLOR = Color(255, 143, 143) # Red

#get all memory ranges
addr_ranges = currentProgram.getMemory().getAddressRanges()

for addr_range in addr_ranges:
    insts = currentProgram.getListing().getInstructions(addr_range.getMinAddress(), True)
    for inst in insts:
        flow_type = inst.getFlowType()
        addr = inst.getAddress()
        if flow_type.isJump():
            print("0x{} : {}".format(addr, inst))
            setBackgroundColor(addr, JUMP_COLOR)
            jump_count += 1

print('[*] Total Jump(s) : {}'.format(jump_count))
