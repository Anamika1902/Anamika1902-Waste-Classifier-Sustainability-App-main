import streamlit as st

def apps():
    # st.write('hello')
    def about_us():
        
        st.write('hello')
    st.title("About Waste Classifier App")
    st.markdown(
        """
        Welcome to the Waste Classifier App! This application helps classify different types of waste using machine learning.
        """
    )

    st.subheader("Our Mission")
    st.write(
        "Our mission is to raise awareness about proper waste disposal and recycling by providing a user-friendly tool for waste classification."
    )

    st.subheader("How it Works")
    st.write(
        "The Waste Classifier App uses a machine learning model trained on various types of waste to accurately identify and categorize them. Users can upload images of waste items, and the app will provide information on the type of waste and how to dispose of it properly."
    )

    st.subheader("Meet the Team")
    st.write(
        "This app was developed by a dedicated team of developers and machine learning experts passionate about environmental sustainability."
    )
    
    st.subheader("Contact Us")
    st.write(
        "If you have any questions, suggestions, or feedback, feel free to reach out to us at wasteclass@email.com."
    )

def main():
    st.set_page_config(
        page_title="Waste Classifier App - About Us",
        page_icon="🌍",
        layout="wide",
    )
if __name__ == "__main__":
    
    apps()
