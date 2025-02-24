import streamlit as st
import utils.data_loader as data_loader

# Set Streamlit page configuration (optional)
st.set_page_config(page_title="FFB Research", page_icon="📊", layout="wide")

data_loader.setup_state_main() # Create necessary state variables for boot

pages = [
    st.Page("pages/custom_scoring.py", title="Custom Scoring"),
    st.Page("pages/player_comparison.py", title="player comp"),
    st.Page("pages/player_details.py", title="Details WIP")

]

pg = st.navigation(pages)
pg.run()

