import pandas as pd
import os
from werkzeug.security import generate_password_hash, check_password_hash

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.csv")

def load_users():
    if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
        return pd.DataFrame(columns=["Username", "Email", "Password"])
    return pd.read_csv(CSV_PATH)

def save_users(df):
    df.to_csv(CSV_PATH, index=False)

def register_user(username, email, password):
    df = load_users()
    if (df['Username'] == username).any():
        return "Username already exists"
    if (df['Email'] == email).any():
        return "Email already registered"

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = pd.DataFrame([[username, email, hashed_password]], columns=["Username", "Email", "Password"])
    df = pd.concat([df, new_user], ignore_index=True)
    save_users(df)
    return "success"

def verify_login(identifier, password):
    df = load_users()
    user = df[(df['Username'] == identifier) | (df['Email'] == identifier)]
    
    if user.empty:
        return False
    
    hashed_password = user.iloc[0]['Password']
    return check_password_hash(hashed_password, password)
