import streamlit as st

# Title
st.title("OHM'S LAW")

# Function to calculate current using Ohm's law
def calc_ohmslaw(v, r):
    return v / r

# Create tabs
tab1, tab2 = st.tabs(["Calculate", "Explain"])

# Layout for "Calculate" tab
with tab1:
    # Create columns for input and result display
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Enter the values")
        # User input for voltage and resistance
        voltage = st.number_input("Enter voltage (V):", min_value=0.0)
        resistance = st.number_input("Enter resistance (R):", min_value=0.0)
        
    with col2:
        st.header("Result")
        # If valid inputs, calculate and display current
        if voltage > 0 and resistance > 0:
            current = calc_ohmslaw(voltage, resistance)
            st.write(f"The calculated current (I) is: {current:.2f} Amps")
        else:
            st.write("Please enter valid values for both voltage and resistance.")

# Layout for "Explain" tab
with tab2:
    st.header("What is Ohm's Law?")
    st.write("""
        Ohm's Law states that the current flowing through a conductor between two points 
        is directly proportional to the voltage across the two points and inversely proportional 
        to the resistance between them. The formula is:

        **I = V / R**

        Where:
        - I is the current in Amps (A)
        - V is the voltage in Volts (V)
        - R is the resistance in Ohms (Ω)
    """)
