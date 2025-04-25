import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    factors = {
        'Meter': 1,
        'Kilometer': 1000,
        'Mile': 1609.34,
        'Foot': 0.3048
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    factors = {
        'Kilogram': 1,
        'Gram': 0.001,
        'Pound': 0.453592,
        'Ounce': 0.0283495
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32

# Streamlit UI
st.title("🌐 Unit Converter")

category = st.selectbox("Choose a category", ["Length", "Weight", "Temperature"])

if category == "Length":
    units = ["Meter", "Kilometer", "Mile", "Foot"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", step=0.01)
    result = convert_length(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", step=0.01)
    result = convert_weight(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", step=0.01)
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")
