# Demo program to show how to generate an ASCII table as PDF,
# using the xtopdf tooklit for PDF creation from Python. 
# By: http://code.activestate.com/recipes/579043-printing-an-ascii-table-to-pdf/

# Practicing coding by analyzing other programs code and doing it all over.
# By Codart


import sys
from PDFWriter import PDFWriter

# Header info
column_names = ['DEC', 'OCT', 'HEX', 'BIN', 'Symbol', 'Description']
column_sizes = [4, 6, 3, 10, 7, 20]

# ASCII control character
ascii_chars = \
"""
0    000    00    00000000    NUL              Null char
1    001    01    00000001    SOH             Start of Heading
2    002    02    00000010    STX             Start of Text
3    003    03    00000011    ETX             End of Text
4    004    04    00000100    EOT             End of Transmission
5    005    05    00000101    ENQ             Enquiry
6    006    06    00000110    ACK             Acknowledgment
7    007    07    00000111    BEL             Bell
8    010    08    00001000    BS             Back Space
9    011    09    00001001    HT    	         Horizontal Tab
10    012    0A    00001010    LF    
         Line Feed
11    013    0B    00001011    VT             Vertical Tab
12    014    0C    00001100    FF             Form Feed
13    015    0D    00001101    CR    
         Carriage Return
14    016    0E    00001110    SO             Shift Out / X-On
15    017    0F    00001111    SI             Shift In / X-Off
16    020    10    00010000    DLE             Data Line Escape
17    021    11    00010001    DC1             Device Control 1 (oft. XON)
18    022    12    00010010    DC2             Device Control 2
19    023    13    00010011    DC3             Device Control 3 (oft. XOFF)
20    024    14    00010100    DC4             Device Control 4
21    025    15    00010101    NAK             Negative Acknowledgement
22    026    16    00010110    SYN             Synchronous Idle
23    027    17    00010111    ETB             End of Transmit Block
24    030    18    00011000    CAN             Cancel
25    031    19    00011001    EM             End of Medium
26    032    1A    00011010    SUB             Substitute
27    033    1B    00011011    ESC             Escape
28    034    1C    00011100    FS    
         File Separator
29    035    1D    00011101    GS    
         Group Separator
30    036    1E    00011110    RS    
         Record Separator
31    037    1F    00011111    US             Unit Separator
"""

# Create and set some of the fiels of a PDF witer
p = PDFWriter("ASCII-Table.pdf")
p.setFont("Courier", 12)
p.setHeader("ASCII Characters - 0 to 31")
p.setFooter("Generated by xtopdf: http://slid.es/vasudevram/xtopdf")

#write the column headings to output
column_headings = [str(val).ljust(column_sizes[idx])\
	for idx, val in enumerate(column_names)]
p.writeLine(' '.join(column_headings))

#Split the string into lines
for line in ascii_chars.split('\n')[1:-1]:

	#space-delimited fields
	l = line.split()
	l2 = l[0:5] + [' '.join(l[6:])]
	l3 = [str(val).ljust(column_sizes[idx]) \
		for idx, val in enumerate(l2)]
	p.writeLine(' '.join(l3))

p.close()










