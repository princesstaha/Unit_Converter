import streamlit as st

# Title and Introduction
st.title("Unit Converter")
st.write("Welcome to the Unit Converter App! Convert units of length, weight, or temperature easily.")

# Unit Type Selection
unit_type = st.selectbox("Select conversion type:", ["Length", "Weight", "Temperature"])

# Conversion Logic
def convert_length(value, from_unit, to_unit):
    length_units = {"meters": 1, "kilometers": 0.001, "feet": 3.28084, "miles": 0.000621371}
    return value * length_units[to_unit] / length_units[from_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274}
    return value * weight_units[to_unit] / weight_units[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

# Input Fields and Result
if unit_type == "Length":
    from_unit = st.selectbox("From unit:", ["meters", "kilometers", "feet", "miles"])
    to_unit = st.selectbox("To unit:", ["meters", "kilometers", "feet", "miles"])
    value = st.number_input("Enter the value to convert:", min_value=0.0, step=1.0)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")

elif unit_type == "Weight":
    from_unit = st.selectbox("From unit:", ["grams", "kilograms", "pounds", "ounces"])
    to_unit = st.selectbox("To unit:", ["grams", "kilograms", "pounds", "ounces"])
    value = st.number_input("Enter the value to convert:", min_value=0.0, step=1.0)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")

elif unit_type == "Temperature":
    from_unit = st.selectbox("From unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter the value to convert:", step=1.0)
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value:.2f} {from_unit} is equal to {result:.2f} {to_unit}.")