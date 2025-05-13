import pandas as pd
import os

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.csv")

def load_users():
    if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
        # File doesn't exist or is empty → return empty DataFrame with headers
        return pd.DataFrame(columns=["Username", "Email", "Password"])
    return pd.read_csv(CSV_PATH)

def save_users(df):
    df.to_csv(CSV_PATH, index=False)

def register_user(username, email, password):
    df = load_users()
    if (df['Username'] == username).any() or (df['Email'] == email).any():
        return "Username or email already exists"
    new_user = pd.DataFrame([[username, email, password]], columns=["Username", "Email", "Password"])
    df = pd.concat([df, new_user], ignore_index=True)
    save_users(df)
    return "success"

def verify_login(identifier, password):
    df = load_users()
    match = df[((df['Username'] == identifier) | (df['Email'] == identifier)) & (df['Password'] == password)]
    return not match.empty
