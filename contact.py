import streamlit as st
from firebase_admin import firestore
from firebase_setup import initialize_firebase

firebase_app = initialize_firebase()
if firebase_app is None:
    # Firebase app already initialized, use the existing app
    pass
else:
    # Use firebase_app for Firebase operations in this module
    pass
db = firestore.client()
# Function to store feedback data in Firestore
def store_feedback_data(email, username, feedback_text):
    try:
        feedback_ref = db.collection('feedbacks').document()
        feedback_ref.set({
            'email': email,
            'username': username,
            'feedback_text': feedback_text
        })
        st.success('Feedback submitted successfully!')
    except Exception as e:
        st.error(f"Error submitting feedback: {e}")

def apps():
    st.title('Feedback Form')
    
    if 'useremail' in st.session_state:
        st.write(f"Email: {st.session_state.useremail}")
        username = st.session_state.username  # Assuming you have stored username in session state
        
        feedback_text = st.text_area('Your Feedback:', height=100)
        if st.button('Submit Feedback'):
            # Store the feedback data in Firestore
            store_feedback_data(st.session_state.useremail, username, feedback_text)

if __name__ == "__main__":
    apps()
