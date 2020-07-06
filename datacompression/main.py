import argparse
import sys
from progress.bar import IncrementalBar
from datacompression.compression import encode, decode


def main():
    # Build argument parser
    parser = argparse.ArgumentParser(
        description="Do various data compression techniques")
    parser.add_argument(
        '-f', '--file', dest='infile', nargs='?',
        type=argparse.FileType('rb'), default=sys.stdin,
        help="The input data for data compression.")
    parser.add_argument(
        '-o', '--output', dest='outfile', nargs='?',
        type=argparse.FileType('wb'), default=sys.stdout,
        help="Path to the compression output.")
    args = parser.parse_args()

    # Read input data
    data = bytearray()
    if args.infile is sys.stdin:
        # From stdin
        for line in args.infile:
            data += line.encode()
    else:
        # From file, opened in binary mode
        for line in args.infile:
            data += line

    sys.stderr.write(f"Consuming {len(data)} Bytes\n")

    # Workflow steps
    workflow = [
        (encode, 'bwt', "BWT encoding"),
        (encode, 'rle', "RLE encoding"),
        (encode, 'mtf', "MTF encoding"),
        (decode, 'mtf', "MTF decoding"),
        (decode, 'rle', "RLE decoding"),
        (decode, 'bwt', "BWT decoding")
    ]

    # Process all work steps
    for step in workflow:
        bar = IncrementalBar(step[2], max=len(data),
                             suffix='%(index)d/%(max)d Bytes [%(elapsed)ds]')
        data = step[0](data, step[1], bar)
        bar.finish()

    # Write output data
    sys.stderr.write(f"Output {len(data)} Bytes:\n")
    if args.outfile is sys.stdout:
        args.outfile.write(data.decode())
        args.outfile.flush()
    else:
        args.outfile.write(data)
        args.outfile.flush()


if __name__ == "__main__":
    main()
