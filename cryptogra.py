import streamlit as st
from cryptography.fernet import Fernet

def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

def encrypt_phrase(phrase, key):
    """Encrypt the phrase using the provided key."""
    cipher = Fernet(key)
    return cipher.encrypt(phrase.encode())

def decrypt_phrase(encrypted_phrase, key):
    """Decrypt the encrypted phrase using the provided key."""
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_phrase).decode()

# Streamlit app
st.title("Seed Phrase Encryption and Decryption")

st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose an action", ["Generate Key", "Encrypt Seed Phrase", "Decrypt Seed Phrase"])

if option == "Generate Key":
    st.subheader("Generate an Encryption Key")
    if st.button("Generate Key"):
        key = generate_key()
        st.write(f"Generated Key: {key.decode()}")

elif option == "Encrypt Seed Phrase":
    st.subheader("Encrypt a Seed Phrase")
    phrase = st.text_input("Enter seed phrase to encrypt")
    key = st.text_input("Enter encryption key (or generate a new one)", type="password")
    if st.button("Encrypt"):
        if not key:
            st.error("Please provide an encryption key or generate a new one.")
        else:
            try:
                key = key.encode()
                encrypted_phrase = encrypt_phrase(phrase, key)
                st.write(f"Encrypted Seed Phrase: {encrypted_phrase.decode()}")
                st.write(f"Encryption Key: {key.decode()}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

elif option == "Decrypt Seed Phrase":
    st.subheader("Decrypt an Encrypted Seed Phrase")
    encrypted_phrase = st.text_area("Enter encrypted seed phrase")
    key = st.text_input("Enter encryption key", type="password")
    if st.button("Decrypt"):
        try:
            encrypted_phrase = encrypted_phrase.encode()
            key = key.encode()
            decrypted_phrase = decrypt_phrase(encrypted_phrase, key)
            st.write(f"Decrypted Seed Phrase: {decrypted_phrase}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
