import os
import sys
import argparse
import configparser

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    patterns = config['Exclusions']['patterns'].strip().split('\n')
    return [pattern.strip() for pattern in patterns if pattern.strip()]

def should_ignore(path, ignore_patterns):
    return any(pattern in path for pattern in ignore_patterns)

def combine_files(input_dir, output_file, ignore_patterns):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(input_dir):
            dirs[:] = [d for d in dirs if not should_ignore(d, ignore_patterns)]
            for file in files:
                if not should_ignore(file, ignore_patterns):
                    filepath = os.path.join(root, file)
                    print(f"Processing: {filepath}")
                    try:
                        with open(filepath, "r", encoding="utf-8") as infile:
                            outfile.write(f"------------------------------\n")
                            outfile.write(f"Filename: {file}\n")
                            outfile.write(f"Path: {filepath}\n")
                            file_contents = infile.read()
                            outfile.write(file_contents)
                            outfile.write("\n\n")
                    except Exception as e:
                        print(f"Error processing {filepath}: {str(e)}")
                        outfile.write(f"Error reading file {filepath}: {e}\n")
                        outfile.write("------------------------------\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine files from a directory into a single output file, excluding specified patterns.")
    parser.add_argument("--input", default=".", help="Input directory containing files to combine")
    parser.add_argument("--output", default="combined_files.txt", help="Output file path")
    parser.add_argument("--config", default="exclusions.ini", help="Path to the exclusions configuration file")
    args = parser.parse_args()

    if not os.path.isdir(args.input):
        print(f"Error: Input directory '{args.input}' does not exist.")
        sys.exit(1)

    if not os.path.exists(args.config):
        print(f"Error: Configuration file '{args.config}' not found.")
        sys.exit(1)

    ignore_patterns = read_config(args.config)
    ignore_patterns.append(os.path.basename(args.config))  # Ignore the config file itself
    ignore_patterns.append(os.path.basename(args.output))  # Ignore the output file
    ignore_patterns.append(os.path.basename(__file__))  # Ignore the script itself

    combine_files(args.input, args.output, ignore_patterns)
    print(f"Files combined successfully. Output written to {args.output}")