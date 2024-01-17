import streamlit as st
from streamlit_option_menu import option_menu

# 1. as Sidebar menu
with st.sidebar:
  selected = option_menu(
    menu_title="Main Menu", #required
    option=["Home", "Projects", "Contact"]
  )

if selected == "Home":
  st.title(f"You have selected {selected}")
if selected == "Projects":
  st.title(f"You have selected {selected}")
if selected == "Contact":
  st.title(f"You have selected {selected}")
