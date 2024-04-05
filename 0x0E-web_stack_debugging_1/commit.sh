#!/bin/bash

# Check if at least one filename is provided
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <file1> [<file2> ...]"
    exit 1
fi

# Commit message
message="Initial commit"

# Initialize Git repository if not already initialized
#if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
#   git init
#fi

# Add files to staging area
git add "$@"

# Commit files with the message
git commit -m "$message"

# Push
git push

