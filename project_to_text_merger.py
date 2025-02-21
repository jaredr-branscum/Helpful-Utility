import os
import argparse

def combine_files(directory=".", output_filename="combined_files.txt", ignore_list=None):
    """Combines files, handles optional directory, ignores program & output, recursively adds files, and recursively ignores."""

    if ignore_list is None:
        ignore_list = []

    try:
        with open(output_filename, "w", encoding="utf-8") as outfile:
            for root, dirs, files in os.walk(directory):
                dirs[:] = [d for d in dirs if d not in ignore_list]  # Recursive directory ignore

                for item in files:
                    filepath = os.path.join(root, item)

                    if any(ignored in filepath for ignored in ignore_list) or item == os.path.basename(__file__) or item == output_filename:
                        continue

                    try:
                        with open(filepath, "r", encoding="utf-8") as infile:
                            outfile.write(f"------------------------------\n")
                            outfile.write(f"Filename: {item}\n")
                            outfile.write(f"Path: {filepath}\n")
                            outfile.write(f"------------------------------\n")
                            file_contents = infile.read()
                            outfile.write(file_contents)
                            outfile.write("\n\n")

                    except Exception as e:
                        print(f"Error reading file {item}: {e}")
                        outfile.write(f"Error reading file {item}: {e}\n")
                        outfile.write("------------------------------\n")

        print(f"Combined file created: {output_filename}")

    except Exception as e:
        print(f"Error creating combined file: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine files in a directory.")
    parser.add_argument("directory", nargs="?", default=".", help="The directory to process (defaults to current).")
    parser.add_argument("-o", "--output", default="combined_files.txt", help="Output filename.")
    parser.add_argument("-i", "--ignore", nargs="+", help="List of files/directories to ignore.", default=[])

    args = parser.parse_args()

    combine_files(args.directory, args.output, args.ignore)