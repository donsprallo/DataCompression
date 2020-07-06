# DataCompression
Various data compression techniques

---

## Usage
The program is used exclusively via a CLI. It reads without further the data
from the standard input, performs the compression or the decompression and
outputs the result on the standard output.

```bash
echo ".ANANAS." | pycompress
Consuming 9 Bytes
BWT encoding |████████████████████████████████| 9/9 Bytes [0s]
RLE encoding |████████████████████████████████| 13/13 Bytes [0s]
MTF encoding |████████████████████████████████| 16/16 Bytes [0s]
MTF decoding |████████████████████████████████| 16/16 Bytes [0s]
RLE decoding |████████████████████████████████| 16/16 Bytes [0s]
BWT decoding |████████████████████████████████| 13/13 Bytes [0s]
Output 9 Bytes:
.ANANAS.
```

This example shows how to read a file and write the result to another file.

```bash
# In a Windows environment using pipes
type .\LICENSE | pycompress -o out.txt

# About command line arguments
pycompress -f .\LICENSE -o out.txt
```