import streamlit as st

st.title("MY First Stramlit project")
st.write("It is a simple web app built on Streamlet.")

name = st.text_input("Name:")
if name:
    st.write(f"Wel Come ,{name}!")

if st.button("Click"):
    st.success("You pressed the button!")

# ڈیٹا ویژولائزیشن
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

st.write("📊Data visualization:")
st.bar_chart(data.set_index('Category'))
