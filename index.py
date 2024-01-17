import streamlit as st
from stramlit_option_menu import option_menu

st.write("""
# Uber pickups in **NYC** *app*!'
""")
# 1. as Sidebar menu
with st.sidebar:
  selected = option_menu(
    menu_title="Main Menu", #required
    option=["Home", "Projects", "Contact"]
  )
  st.title(f"You have selected {selected}")
if selected == "Home":
  st.title(f"You have selected {selected}")
if selected == "Projects":
  st.title(f"You have selected {selected}")
if selected == "Contact":
  st.title(f"You have selected {selected}")

