import argparse
from pathlib import Path
from compression import encode, decode


def main():
    # Build argument parser
    parser = argparse.ArgumentParser(
        description="Do various data compression techniques")
    parser.add_argument('-f', '--file', dest='input_file', type=Path,
                        required=True,
                        help="The input data for data compression.")
    parser.add_argument('-o', '--output', dest='output_file',
                        type=Path, default=r'out.txt',
                        help="Path to the compression output.")
    args = parser.parse_args()

    # Read input file
    input_bytes = str()
    with open(args.input_file, "r") as ifile:
        for line in ifile:
            input_bytes += line

    # Encode input string into bytes
    data = input_bytes.encode('ascii')
    print(f"--- Testdaten --- {len(data)} Byte ---")

    # Work steps
    workflow = [
        (encode, 'bwt', "--- BWT coded ---"),
        (encode, 'rle', "--- RLE coded ---"),
        (encode, 'mtf', "--- MTF coded ---"),
        (decode, 'mtf', "--- MTF decoded ---"),
        (decode, 'rle', "--- RLE decoded ---"),
        (decode, 'bwt', "--- BWT decoded ---")
    ]

    # Process all work steps
    for step in workflow:
        data = step[0](data, step[1])
        print(step[2], f"{len(data)} Byte(s) ---")

    # Write data to output
    with open(args.output_file, "wb") as ofile:
        ofile.write(data)


if __name__ == "__main__":
    main()
