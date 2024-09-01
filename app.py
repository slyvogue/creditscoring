import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from pathlib import Path
from PIL import Image
import Dashboard
from Prediction import app as prediction_app 

#  load the logo
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
logo = current_dir / "image.jpeg"
logo = Image.open(logo)

# Set page configurations
st.set_page_config(
    page_title="Credit Score Analysis",
    page_icon="📊", 
    layout="wide",
    initial_sidebar_state="expanded",
)


# Importing data
df = pd.read_csv('combined_dataset.csv')  # Adjusted for credit score dataset

# Set style for menu options in the sidebar
style = {
        "nav-link": {"font-family": "Monospace, Arial", "--hover-color": "SkyBlue"},
        "nav-link-selected": {"background-color": "rgb(10, 0, 124)", "font-family": "Monospace , Arial"},
    }

# The main class of the application
class MultiPage:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            st.title('Credit Score Analysis')
            st.image(logo, width=300)
        with st.sidebar:
            app = option_menu(None,
                              options=['Dashboard', 'Predict Credit Score'],
                              icons=["bar-chart-line-fill", "shield-fill-check", "envelope-fill"],
                              styles=style,
                              default_index=0,
                              )

        if app == 'Dashboard':
            Dashboard.app(df,st)
        if app == 'Predict Credit Score':
            prediction_app()  # Call the prediction app from prediction.py

# Run the multipage App
MultiPage().run()
