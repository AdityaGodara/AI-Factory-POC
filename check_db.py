import sqlite3
import bcrypt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # bcrypt requires bytes
    password_bytes = plain_password.encode('utf-8')[:72]
    hash_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hash_bytes)

def check_all():
    conn = sqlite3.connect('c:\\Program1\\AiFactory\\aifactory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, password_hash FROM users")
    for username, hashed in cursor.fetchall():
        print(f"Checking {username}...")
        try:
            # We don't know the password, but we can check if it parses
            # We can't verify unless we know the password, but let's check if it crashes
            # Actually just running checkpw with wrong password is fine.
            res = verify_password('wrongpassword', hashed)
            print(f"  Valid hash format: {username} (matched: {res})")
        except Exception as e:
            print(f"  Error on {username}: {e}")

check_all()
