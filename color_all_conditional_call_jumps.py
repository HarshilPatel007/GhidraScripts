# Color(Pink) all Conditional Call(s) or Jump(s) in Listing Window.
# https://ghidra.re/ghidra_docs/api/ghidra/program/model/symbol/FlowType.html#isConditional()
# @author : Harshil Patel
# @category : Tools

from java.awt import Color


conditional_call_jump_count = 0
COLOR = Color(249, 143, 255) # Pink

#get all memory ranges
addr_ranges = currentProgram.getMemory().getAddressRanges()

for addr_range in addr_ranges:
    insts = currentProgram.getListing().getInstructions(addr_range.getMinAddress(), True)
    for inst in insts:
        flow_type = inst.getFlowType()
        addr = inst.getAddress()
        if flow_type.isConditional():
            print("0x{} : {}".format(addr, inst))
            setBackgroundColor(addr, COLOR)
            conditional_call_jump_count += 1

print('[*] Total Conditional Call(s) or Jump(s) : {}'.format(conditional_call_jump_count))
