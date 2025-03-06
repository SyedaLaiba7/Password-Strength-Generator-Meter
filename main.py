import streamlit as st
import random
import string
import re  # For regex-based password analysis

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Uppercase & lowercase letters

    if use_digits:
        characters += string.digits  # Include numbers (0-9)

    if use_special:
        characters += string.punctuation  # Include special characters (!@#$%^&*)

    return "".join(random.choice(characters) for _ in range(length))


# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback


# Streamlit UI
st.title("🔐 Password Strength Generator & Meter")

# User input for password generation
length = st.slider("Select password length:", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include numbers")
use_special = st.checkbox("Include special characters")

# Generate password button
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

    # Check password strength
    score, feedback = check_password_strength(password)

    # Display strength results
    st.subheader("🔒 Password Strength Analysis")
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")

    # Display feedback for improvement
    for tip in feedback:
        st.write(tip)

# User input to check their own password strength
st.subheader("🔍 Test Your Own Password")
user_password = st.text_input("Enter a password to check its strength", type="password")

if user_password:
    score, feedback = check_password_strength(user_password)

    # Display password strength
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")

    for tip in feedback:
        st.write(tip)
