# App control
import streamlit as st
import home
import perso_fractal

st.set_page_config(page_title="Fractals Museum", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

PAGES = {
    "Home": home,
    "Creation": perso_fractal,
}
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Which page do you want to see", list(PAGES.keys()))
page = PAGES[selection]
page.app()
