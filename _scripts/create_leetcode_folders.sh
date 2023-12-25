#!/bin/bash

# This script creates a folder structure for programming problems,
# organized by difficulty, and copies a template Python file into the new folder.

# Get the directory of the script
script_dir="$(dirname "$(readlink -f "$0")")"

if [ $# -lt 2 ]; then
    echo "Usage: $0 <difficulty> <folder_name>" >&2
    exit 1
fi

difficulty=$1
folder_name=$2
folder_path="$script_dir/problems/${difficulty}/${folder_name}"
lowercase_folder_name=$(echo "$folder_name" | tr '[:upper:]' '[:lower:]')

# Function to convert a string to camel case
to_camel_case() {
    echo "$1" | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1'
}

# Camel case the folder name if the difficulty is "easy"
camelcase_folder_name=$(to_camel_case "$folder_name")

# Error handling - Check if the folder already exists
if [ -d "$folder_path" ]; then
    echo "Error: Folder $folder_path already exists." >&2
    exit 1
fi

# Create the folder
mkdir "$folder_path"

# Create ProgressionNote.md
touch "$folder_path/ProgressionNote.md"

# Path to your template .py file
template_py_file="$script_dir/.vscode/template.py"

# Copy template file to the new Python file
cp "$template_py_file" "$folder_path/${lowercase_folder_name}.py"

echo "Folder structure created successfully for ${difficulty}${folder_name} in $folder_path."
