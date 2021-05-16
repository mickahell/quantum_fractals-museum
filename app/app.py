# App control
import streamlit as st
import home
import perso_fractal

PAGES = {
    "Home": home,
    "Creation": perso_fractal,
}
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Which page do you want to see", list(PAGES.keys()))
page = PAGES[selection]
page.app()
