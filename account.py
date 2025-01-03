import streamlit as st
from firebase_admin import firestore, auth
import re
from firebase_setup import initialize_firebase

firebase_app = initialize_firebase()
if firebase_app is None:
    # Firebase app already initialized, use the existing app
    pass
else:
    # Use firebase_app for Firebase operations in this module
    pass
db = firestore.client()

# Function to store user information in Firestore
def store_user_data(email, username, password):
    try:
        user_ref = db.collection('users').document(email)
        user_ref.set({
            'username': username,
            'useremail': email,
            'password': password
        })
        st.success('Account created successfully!')
        st.markdown('Please login using your email and password')
        st.balloons()
    except Exception as e:
        st.error(f"Error creating user: {e}")

# Function to validate email format
def is_valid_email(email):
    return '@' in email

# Function to validate password format
def is_valid_password(password):
    # At least 8 characters
    if len(password) < 8:
        return False
    
    # At least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # At least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # At least one digit
    if not re.search(r'\d', password):
        return False
    
    # At least one special character
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    
    return True

# Function to handle user signup
def signup():
    st.title('Sign Up Page')

    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')
    username = st.text_input("Enter your unique username")

    if st.button('Create my account'):
        if not email or not password or not username:
            st.warning('Please fill in all the mandatory fields.')
        elif not is_valid_email(email):
            st.warning('Invalid email format. Please enter a valid email address.')
        elif not is_valid_password(password):
            st.warning('Password should have at least 8 characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character.')
        else:
            try:
                # Create a new user in Firebase Authentication
                user = auth.create_user(email=email, password=password, display_name=username)
                store_user_data(email, username, password)  # Store user data in Firestore
            except Exception as e:
                st.error(f"Error creating user: {e}")

# Function to handle user login
def login():
    st.title('Login Page')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if not email or not password:
            st.warning('Please fill in all the mandatory fields.')
        elif not is_valid_email(email):
            st.warning('Invalid email format. Please enter a valid email address.')
        else:
            try:
                user = auth.get_user_by_email(email)
                # Password validation
                if is_valid_password(password):
                    st.session_state.username = user.uid
                    st.session_state.useremail = user.email
                    st.success('Login successful!')
                else:
                    st.warning('Invalid password. Please try again.')
            except:
                st.warning('Login Failed')

# Streamlit app function
def apps():
    st.title('Welcome to :violet[Waste Classifier] :sunglasses:')

    choice = st.sidebar.radio('Page Navigation', ['Login', 'Sign Up'])

    if choice == 'Login':
        login()
    elif choice == 'Sign Up':
        signup()

if __name__ == "__main__":
    apps()
