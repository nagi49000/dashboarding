import streamlit as st
from app.data import get_data


def app():
    st.session_state.n_new_coords = "10"

    def click_button():
        st.session_state.coords = get_data(int(st.session_state.n_new_coords))

    if "coords" not in st.session_state:
        click_button()

    st.session_state.n_new_coords = st.text_input(
        "Number of coords to fetch on update", "10", key="n_new_coords_textbox"
    )
    st.button(
        "Click to update coords", on_click=click_button, key="update_coords_button"
    )
    st.map(st.session_state.coords)
