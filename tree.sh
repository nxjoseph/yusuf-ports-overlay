#!/bin/sh

# Initialize README.md with a header
header="# These are ports in that FreeBSD overlay"
printf "%s\n\n" "$header" > README.md  # Add one newline after the header

# Define the base directory to check against
base_dir="/usr/ports"

# Temporary file to hold the port entries
temp_file=$(mktemp)

# Find directories, excluding .git and files directories
find . -mindepth 2 -type d | grep -Ev ".git|files" | while read dir; do
    # Check if Makefile exists in the current directory
    if [ -f "$dir/Makefile" ]; then
        # Extract the line starting with COMMENT= and format it for README.md
        comment=$(grep '^COMMENT=' "$dir/Makefile")
        if [ -n "$comment" ]; then
            # Check if the corresponding directory exists in /usr/ports
            relative_dir=${dir#./}  # Remove leading './' from directory path
            official_dir="$base_dir/$relative_dir"

            if [ -d "$official_dir" ]; then
                prefix="[OFFICIAL]"
            else
                prefix="[UNOFFICIAL]"
            fi

            # Format output as "official/unofficial example/dir: $COMMENT"
            printf "%s: %s\n" "$prefix $relative_dir" "${comment#COMMENT=}" >> "$temp_file"
        fi
    fi
done

# Sort the temporary file and output each line to README.md with an extra newline after each entry
{
    sort -k1,1 "$temp_file" | while read line; do
        echo "$line"  # Output the sorted line
        echo ""       # Add an extra newline after each entry
    done | sed '$d'  # Remove the last newline added by echo after the last entry
} >> README.md  # Append to README.md

# Clean up temporary file
rm "$temp_file"
