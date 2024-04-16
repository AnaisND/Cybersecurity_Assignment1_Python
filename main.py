import json
import re


def find_matches(input_str):
    email_regex = r'\bemail\b'
    password_regex = r'\bpassword\b'
    at_symbol_regex = r'@'

    email_pattern = re.compile(email_regex, re.IGNORECASE)
    password_pattern = re.compile(password_regex, re.IGNORECASE)
    at_symbol_pattern = re.compile(at_symbol_regex)

    print("Matches for 'email':")
    for match in email_pattern.finditer(input_str):
        print("Found 'email' at index", match.start())

    print("\nMatches for '@':")
    for match in at_symbol_pattern.finditer(input_str):
        print("Found '@' at index", match.start())

    print("\nMatches for 'password':")
    for match in password_pattern.finditer(input_str):
        print("Found 'password' at index", match.start())


def email_matches(input_str):
    email_regex = r'\bemail\b'
    at_symbol_regex = r'@'

    email_pattern = re.compile(email_regex, re.IGNORECASE)
    at_symbol_pattern = re.compile(at_symbol_regex)

    if email_pattern.search(input_str) or at_symbol_pattern.search(input_str):
        return True
    return False


def password_matches(input_str):
    password_regex = r'\bpassword\b'

    password_pattern = re.compile(password_regex, re.IGNORECASE)

    if password_pattern.search(input_str):
        return True
    return False


def json_to_string(json_data):
    try:
        # Convert JSON data to a string
        json_string = json.dumps(json_data)
        return json_string
    except Exception as e:
        print(f"Error converting JSON to string: {e}")
        return None


def readFile(filePath):
    try:
        with open(filePath, 'r') as file:
            if filePath.endswith(".txt"):
                return file.read()
            elif filePath.endswith(".json"):
                content = json.load(file)
                return json_to_string(content)
    except FileNotFoundError:
        print(f"File '{filePath}' not found.")
    except Exception as e:
        print(f"Error reading file '{filePath}': {e}")

    return ""


filePath1 = "file.txt"
filePath2 = "file.json"
filePath3 = "file_noPII.txt"
filePath4 = "file_noPII.json"

content1 = readFile(filePath1)
content2 = readFile(filePath2)
content3 = readFile(filePath3)
content4 = readFile(filePath4)

#Testing the matching method:
# find_matches(content1)
# find_matches(content2)
# find_matches(content3)
# find_matches(content4)

#Testing the boolean methods:
# print(email_matches(content1))
# print(password_matches(content1))
#
# print(email_matches(content2))
# print(password_matches(content2))
#
# print(email_matches(content3))
# print(password_matches(content3))
#
# print(email_matches(content4))
# print(password_matches(content4))