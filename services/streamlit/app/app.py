import streamlit as st
from data import get_data


st.map(get_data())
