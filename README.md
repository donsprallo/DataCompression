# DataCompression
Various data compression techniques

---

# Installation

The installation is very simple. You only need an installed Python interpreter
(version > 3.6) and Git.

```bash
    # Clone the repository to your local machine
    git clone https://github.com/donsprallo/DataCompression.git

    # Then run the setup
    python -m pip install ./DataCompression
```

> **Note:**
> The repository may be made available on PyPi in the future.

---

# Usage
The program is used exclusively via a CLI. It reads without further the data
from the standard input, performs the compression or the decompression and
outputs the result on the standard output.

```bash
    > echo "KORREKT" | pycompress encode bwt
    Consuming 8 Bytes
    bwt encoding |████████████████████████████████| 8/8 Bytes [0s]
    Output 12 Bytes:
    TREKROK
```

This example shows how to read a file and write the result to another file.

```bash
    # In a Windows environment using pipes
    > type your_file | pycompress -o encoded.txt encode rle

    # In a Linux environment using pipes
    > cat your_file | pycompress -o encoded.txt encode rle

    # About command line arguments
    > pycompress -f your_file -o encoded.txt encode rle
```

## Linking compression stages

It is possible to perform several steps with one process one after the other, without using pipes.

```bash
    # Encoding the file 'your_file' with the methods bwt > rle > mtf
    > pycompress -f your_file -o encode.txt encode bwt rle mtf

    # The created file can now be decoded again in reverse order
    > pycompress -f encode.txt -o decode.txt decode mtf rle bwt
```