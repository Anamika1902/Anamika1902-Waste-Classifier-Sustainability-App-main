import streamlit as st
from streamlit_option_menu import option_menu
import home
import account
import app
import opentest
import contact
import about

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            selected_app = option_menu(
                menu_title='Waste Classifier ',
                options=['Home', 'Account', 'Application','ChatBox', 'Contact', 'About'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'robot','chat-fill', 'info-circle-fill'],
                menu_icon='bi bi-recycle',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        for app_info in self.apps:
            if selected_app == app_info["title"]:
                app_info["function"]()

if __name__ == "__main__":
    multi_app = MultiApp()

    multi_app.add_app("Home", home.apps)
    multi_app.add_app("Account", account.apps)
    multi_app.add_app("Application", app.apps)
    multi_app.add_app("ChatBox", opentest.apps)
    multi_app.add_app("Contact", contact.apps)
    multi_app.add_app("About", about.apps)

    multi_app.run()
