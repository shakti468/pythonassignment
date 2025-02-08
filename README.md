# Pythonassignment

This repository contains three essential Python scripts for DevOps engineers to ensure security, system health, and data safety:

1. **Password Strength Checker** - Validates the strength of user passwords.
2. **CPU Usage Monitor** - Continuously monitors CPU usage and raises alerts if it exceeds a predefined threshold.
3. **Backup Script** - Copies files from a source directory to a destination while ensuring unique filenames.

## 1. Password Strength Checker

### Description
A Python script that checks the strength of a given password based on the following criteria:
- At least 8 characters long
- Contains both uppercase and lowercase letters
- Includes at least one numeric digit (0-9)
- Contains at least one special character (!@#$%^&* etc.)

### Usage
Run the script and enter a password when prompted:
```sh
python password_checker.py
```

### Example Input and Output
#### Input:
```
Enter a password to check its strength: Pass@123
```
#### Output:
```
Strong password
```

#### Input:
```
Enter a password to check its strength: weakpass
```
#### Output:
```
Weak password! Please provide a password that has at least 8 characters, uppercase & lowercase letters, a digit, and a special character.
```

## 2. CPU Usage Monitor

### Description
A Python script that continuously monitors CPU usage and raises an alert if it exceeds a predefined threshold (e.g., 80%).

### Prerequisites
Install `psutil` if not already installed:
```sh
pip install psutil
```

### Usage
Run the script:
```sh
python cpu_monitor.py
```

### Example Output
```
Monitoring CPU usage...
Current CPU usage: 45%
Current CPU usage: 78%
Alert! CPU usage exceeds threshold: 85%
Alert! CPU usage exceeds threshold: 90%
```

## 3. Backup Script

### Description
A Python script that copies all files from a source directory to a destination directory. If a file with the same name already exists in the destination, it appends a timestamp to avoid overwriting.

### Usage
Run the script with the source and destination directories as arguments:
```sh
python backup.py /path/to/source /path/to/destination
```

### Example Input and Output
#### Command:
```sh
python backup.py ./source ./backup
```

#### Output:
```
Backed up 'file1.txt' to './backup/file1.txt'
File 'file2.txt' already exists in destination. Renaming...
Backed up 'file2.txt' to './backup/file2_20250208_123456.txt'
```

If the source directory does not exist, an error is displayed:
```
Error: Source directory './source' does not exist.
```

## Error Handling
- The scripts handle common errors, such as missing directories or invalid input.
- The CPU monitor includes exception handling to prevent crashes during runtime.

## 🤝 Contributing
Contributions are welcome! If you'd like to contribute, follow these steps:
1. **Fork** the repository.
2. Create a **feature branch**:
   ```sh
   git checkout -b feature-branch
   ```
3. **Commit your changes**:
   ```sh
   git commit -m 'Add feature'
   ```
4. **Push to the branch**:
   ```sh
   git push origin feature-branch
   ```
5. **Create a Pull Request** for review.

## 📜 License
This project is open-source and available under the MIT License.

