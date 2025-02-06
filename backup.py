import os
import shutil
import sys
from datetime import datetime

# Function to append timestamp to a filename if file already exists
def get_unique_filename(destination, filename):
    base_name, extension = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}{extension}"

# Function to copy files from source to destination
def backup_files(source, destination):
    # Check if source directory exists
    if not os.path.exists(source):
        print(f"Error: Source directory '{source}' does not exist.")
        return

    # Check if destination directory exists
    if not os.path.exists(destination):
        print(f"Error: Destination directory '{destination}' does not exist.")
        return

    # Loop through all files in the source directory
    for filename in os.listdir(source):
        source_file = os.path.join(source, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(source_file):
            # Set the destination file path
            destination_file = os.path.join(destination, filename)

            # If file already exists in the destination, make the filename unique
            if os.path.exists(destination_file):
                print(f"File '{filename}' already exists in destination. Renaming...")
                destination_file = os.path.join(destination, get_unique_filename(destination, filename))

            try:
                # Copy the file to the destination
                shutil.copy2(source_file, destination_file)
                print(f"Backed up '{filename}' to '{destination_file}'")
            except Exception as e:
                print(f"Error copying '{filename}': {e}")

# Main function to parse command-line arguments
def main():
    # Check if command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    # Get source and destination directories from arguments
    source = sys.argv[1]
    destination = sys.argv[2]

    # Start the backup process
    backup_files(source, destination)

if __name__ == "__main__":
    main()
