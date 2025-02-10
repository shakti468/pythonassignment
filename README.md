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
 python .\question1.py
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
## Screenshot

## Code:
![image](https://github.com/user-attachments/assets/c4787446-2ceb-4fc7-8919-6385be7d7cf3)



## Output:
![image](https://github.com/user-attachments/assets/cee8ef26-f0c7-405e-bfc3-2c6011dc6e7d)




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
python .\question2.py
```

### Example Output
```
Monitoring CPU usage...
Current CPU usage: 9.7%
Current CPU usage: 27.7%
Current CPU usage: 18.4%
Current CPU usage: 18.8%

Monitoring stopped by user.
```

## Screenshot

## Code:
![image](https://github.com/user-attachments/assets/8d7b360a-03de-4b69-8962-1907a814596b)

## Output:
![image](https://github.com/user-attachments/assets/304a482c-d29a-458f-9408-6dcfe4f958a3)




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
python backup.py F:\Source F:\Destination
```

#### Output:
```
Backed up 'file1.txt' to 'F:\Destination\file1.txt'
Backed up 'file2.txt' to 'F:\Destination\file2.txt'
```

## Screenshot

## Code:
![image](https://github.com/user-attachments/assets/bef9f69b-5475-425a-b2fe-f96983f656cd)

#### Output:
![image](https://github.com/user-attachments/assets/cd7b7391-9a93-41a1-a460-88a1f9c925d2)



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

