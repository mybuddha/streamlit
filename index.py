import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)






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

