# The MIT License (MIT)
#
# Copyright (c) 2018 Jonah Yolles-Murphy for Makers Anywhere! 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`TGFONT01`
====================================================

CircuitPython pixel graphics drawing library.

* Author(s): Jonah Yolles-Murphy
Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""
"""
letter format:
    { 'character_here' : bytearray(b',WIDTH,HEIGHT,right-most-data,more-bytes-here,left-most-data') ,} (replace the "," with backslashes!!)
    each byte:
            | lower most bit(lowest on display)
            V
     x0110100
      ^c
      | top most bit (highest on display)
Key format:
    keys of one length only represent one character. longer then one is either extended characters or special characters
"""
text_dict = {
'A' : bytearray(b'\x05\x08?DDD?') ,
'B' : bytearray(b'\x05\x08\x7fAII6') ,
'C' : bytearray(b'\x05\x08>AAA"') ,
'D' : bytearray(b'\x05\x08\x7fAA"\x1c') ,
'E' : bytearray(b'\x05\x08\x7fIIIA') ,
'F' : bytearray(b'\x05\x08\x7fHH@@') ,
'G' : bytearray(b'\x05\x08>AII.') ,
'H' : bytearray(b'\x05\x08\x7f\x08\x08\x08\x7f') ,
'I' : bytearray(b'\x05\x08AA\x7fAA') ,
'J' : bytearray(b'\x05\x08FA~@@') ,
'K' : bytearray(b'\x05\x08\x7f\x08\x08t\x03') ,
'L' : bytearray(b'\x05\x08\x7f\x01\x01\x01\x01') ,
'M' : bytearray(b'\x05\x08\x7f \x10 \x7f') ,
'N' : bytearray(b'\x05\x08\x7f \x1c\x02\x7f') ,
'O' : bytearray(b'\x05\x08>AAA>') ,
'P' : bytearray(b'\x05\x08\x7fHHH0') ,
'Q' : bytearray(b'\x05\x08>AEB=') ,
'R' : bytearray(b'\x05\x08\x7fHLJ1') ,
'S' : bytearray(b'\x05\x082III&') ,
'T' : bytearray(b'\x05\x08@@\x7f@@') ,
'U' : bytearray(b'\x05\x08~\x01\x01\x01~') ,
'V' : bytearray(b'\x05\x08p\x0e\x01\x0ep') ,
'W' : bytearray(b'\x05\x08|\x03\x04\x03|') ,
'X' : bytearray(b'\x05\x08c\x14\x08\x14c') ,
'Y' : bytearray(b'\x05\x08`\x10\x0f\x10`') ,
'Z' : bytearray(b'\x05\x08CEIQa') ,
'0' : bytearray(b'\x05\x08>EIQ>') ,
'1' : bytearray(b'\x05\x08\x11!\x7f\x01\x01') ,
'2' : bytearray(b'\x05\x08!CEI1') ,
'3' : bytearray(b'\x05\x08FAQiF') ,
'4' : bytearray(b'\x05\x08x\x08\x08\x08\x7f') ,
'5' : bytearray(b'\x05\x08rQQQN') ,
'6' : bytearray(b'\x05\x08\x1e)II\x06') ,
'7' : bytearray(b'\x05\x08@GHP`') ,
'8' : bytearray(b'\x05\x086III6') ,
'9' : bytearray(b'\x05\x080IIJ<') ,
')' : bytearray(b'\x05\x08\x00A>\x00\x00') ,
'(' : bytearray(b'\x05\x08\x00\x00>A\x00') ,
'[' : bytearray(b'\x05\x08\x00\x00\x7fA\x00') ,
']' : bytearray(b'\x05\x08\x00A\x7f\x00\x00') ,
'.' : bytearray(b'\x05\x08\x00\x03\x03\x00\x00') ,
"'" : bytearray(b'\x05\x08\x00\x000\x00\x00') ,
':' : bytearray(b'\x05\x08\x00\x0066\x00') ,
'?CHAR?' : bytearray(b'\x05\x08\x7f_RG\x7f') ,
'!' : bytearray(b'\x05\x08\x00{{\x00\x00') ,
'?' : bytearray(b'\x05\x08 @EH0') ,
',' : bytearray(b'\x05\x08\x00\x05\x06\x00\x00') ,
';' : bytearray(b'\x05\x08\x0056\x00\x00') ,
'/' : bytearray(b'\x05\x08\x01\x06\x080@') ,
'>' : bytearray(b'\x05\x08Ac6\x1c\x08') ,
'<' : bytearray(b'\x05\x08\x08\x1c6cA') ,
'%' : bytearray(b'\x05\x08af\x083C') ,
'@' : bytearray(b'\x05\x08&IOA>') ,
'#' : bytearray(b'\x05\x08\x14\x7f\x14\x7f\x14') ,
'$' : bytearray(b'\x05\x082I\x7fI&') ,
'&' : bytearray(b'\x05\x086IU"\x05') ,
'*' : bytearray(b'\x05\x08(\x10|\x10(') ,
'-' : bytearray(b'\x05\x08\x00\x08\x08\x08\x00') ,
'_' : bytearray(b'\x05\x08\x01\x01\x01\x01\x01') ,
'+' : bytearray(b'\x05\x08\x08\x08>\x08\x08') ,
'=' : bytearray(b'\x05\x08\x00\x14\x14\x14\x00') ,
'"' : bytearray(b'\x05\x08\x00p\x00p\x00') ,
'`' : bytearray(b'\x05\x08\x00\x00 \x10\x00') ,
'~' : bytearray(b'\x05\x08\x08\x10\x08\x04\x08') ,
' ' : bytearray(b'\x05\x08\x00\x00\x00\x00\x00') ,
'^' : bytearray(b'\x05\x08\x10 @ \x10') ,
'NONE' : bytearray(b'\x00\x08') ,
'BLANK' : bytearray(b'\x05\x08\x00\x00\x00\x00\x00') ,
'BATA0' : bytearray(b'\x0b\x08\x7fAAAAAAAA\x7f\x1c') ,
'BATA1' : bytearray(b'\x0b\x08\x7fA]AAAAAA\x7f\x1c') ,
'BATA2' : bytearray(b'\x0b\x08\x7fA]]AAAAA\x7f\x1c') ,
'BATA3' : bytearray(b'\x0b\x08\x7fA]]]AAAA\x7f\x1c') ,
'BATA4' : bytearray(b'\x0b\x08\x7fA]]]]AAA\x7f\x1c') ,
'BATA5' : bytearray(b'\x0b\x08\x7fA]]]]]AA\x7f\x1c') ,
'BATA6' : bytearray(b'\x0b\x08\x7fA]]]]]]A\x7f\x1c') ,
'BATACHRG' : bytearray(b'\x0b\x08\x7fAIYyOMIA\x7f\x1c') ,
'BATB0' : bytearray(b'\x0b\x08\x7fAAAAAAAA\x7f\x1c') ,
'FULL' : bytearray(b'\x05\x08\x7f\x7f\x7f\x7f\x7f') ,
'\n' : bytearray(b'\x05\x08\x00\x00\x00\x00\x00') ,
'DEGREESIGN' : bytearray(b'\x05\x08\x18$$\x18\x00') ,
}