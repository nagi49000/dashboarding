import streamlit as st
from data import get_data


n_new_coords = "10"


def click_button():
    st.session_state.coords = get_data(int(n_new_coords))


if "coords" not in st.session_state:
    click_button()


n_new_coords = st.text_input("Number of coords to fetch on update", "10")
st.button("Click to update coords", on_click=click_button)
st.map(st.session_state.coords)
