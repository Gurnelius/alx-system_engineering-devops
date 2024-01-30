#!/bin/bash

# Check if the input file is provided as a command-line argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file '$input_file' not found."
    exit 1
fi

# Read input text from the file
input_text=$(cat "$input_file")

# Extract text after "File:"
file_names=$(echo "$input_text" | grep -oP 'File:\s*\K[^\n]*')

# Create files with content
for file_name in $file_names; do
    touch "$file_name"
    echo "#!/usr/bin/env ruby" > "$file_name"
    echo 'puts ARGV[0].scan(/127.0.0.[0-9]/).join' >> "$file_name"
    chmod u+x $file_name
    echo "Created file: $file_name"
done
