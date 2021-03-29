# Color(Green) all Call(s) in Listing Window.
# https://ghidra.re/ghidra_docs/api/ghidra/program/model/symbol/FlowType.html#isCall()
# @author : Harshil Patel
# @category : Tools

from java.awt import Color


call_count = 0
CALL_COLOR = Color(190, 255, 143) # Green

#get all memory ranges
addr_ranges = currentProgram.getMemory().getAddressRanges()

for addr_range in addr_ranges:
    insts = currentProgram.getListing().getInstructions(addr_range.getMinAddress(), True)
    for inst in insts:
        flow_type = inst.getFlowType()
        addr = inst.getAddress()
        if flow_type.isCall():
            print("0x{} : {}".format(addr, inst))
            setBackgroundColor(addr, CALL_COLOR)
            call_count += 1

print('[*] Total Call(s) : {}'.format(call_count))
