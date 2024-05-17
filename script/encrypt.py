import json
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

files = ["user_stats.json"]


def encrypt_aes(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode("utf-8"), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted_data).decode("utf-8")


def encrypt_data(data):
    key = bytes(
        [
            57,
            114,
            107,
            120,
            67,
            80,
            108,
            106,
            83,
            77,
            49,
            71,
            86,
            81,
            104,
            87,
            119,
            49,
            114,
            49,
            114,
            75,
            79,
            72,
            71,
            99,
            99,
            98,
            50,
            105,
            74,
            53,
        ]
    )
    iv = bytes([0] * 16)

    try:
        encrypted_data = encrypt_aes(key, iv, data)
        return encrypted_data
    except Exception as ex:
        print(f"Error during encryption: {ex}")
        return None


def main():
    for file in files:
        # Load user_stats.json to get the initial "data" value
        try:
            with open(f"temp/data/{file}", "r") as f:
                user_stats = json.load(f)
        except FileNotFoundError:
            print(f"Error: File {file} not found.")
            continue
        except json.JSONDecodeError as e:
            print(f"Error: Could not decode JSON from {file}. Error: {e}")
            continue

        # Get the current "data" value
        data_value = user_stats.get("data", "")
        if not isinstance(data_value, str) or not data_value:
            print(f"Error: No valid data found to encrypt in {file}.")
            continue

        # Encrypt the data
        encrypted_result = encrypt_data(data_value)
        if encrypted_result is None:
            print(f"Error: Failed to encrypt data in file {file}.")
            continue

        # Update the "data" value with encrypted result
        user_stats["data"] = encrypted_result

        try:
            with open(f"temp/data/{file}", "w") as f:
                json.dump(user_stats, f, indent=4)
        except IOError as e:
            print(f"Error: Could not write to file {file}. Error: {e}")


if __name__ == "__main__":
    main()
