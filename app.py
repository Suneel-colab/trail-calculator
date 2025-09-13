import streamlit as st

st.title("Weight Calculator")

mass = st.number_input("Mass (kg)", min_value=0.0, value=10.0, step=0.1, format="%.2f")
g = 9.81  # gravity (m/s^2)
weight_n = mass * g

st.write(f"Mass: {mass:.2f} kg")
st.write(f"Weight: {weight_n:.2f} N")