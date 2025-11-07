import re

def is_valid_email(email):
    # Regular Expression Pattern
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # re.match checks if the email fits the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


if __name__ == "__main__":
    print("📧 Email ID Validator 📧")
    print("="*30)

    n = int(input("How many emails do you want to check? "))

    for _ in range(n):
        email = input("\nEnter email address: ").strip()
        if is_valid_email(email):
            print(f"✅ '{email}' is a valid email ID.")
        else:
            print(f"❌ '{email}' is NOT a valid email ID.")
