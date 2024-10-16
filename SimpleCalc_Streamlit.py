import streamlit as st
import math

# Initialize session state
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to update the expression
def update_expression(value):
    st.session_state.expression += str(value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except Exception as e:
        st.session_state.expression = "Error"

# Backspace function
def backspace_expression():
    st.session_state.expression = st.session_state.expression[:-1]
    
# Clear the expression
def clear_expression():
    st.session_state.expression = ""

# Streamlit app layout
st.title("Calculator")

# Display current expression
st.text_input("Expression", st.session_state.expression, key='display', disabled=True)

# Create buttons for digits and operations
col1, col2, col3 = st.columns(3)

with col1:
    st.button("1", on_click=update_expression, args=(1,))
    st.button("4", on_click=update_expression, args=(4,))
    st.button("7", on_click=update_expression, args=(7,))
    st.button(".", on_click=update_expression, args=("."))  # Decimal point button
    st.button("╇", on_click=update_expression, args=("+",))
    st.button("/", on_click=update_expression, args=("/"))

with col2:
    st.button("2", on_click=update_expression, args=(2,))
    st.button("5", on_click=update_expression, args=(5,))
    st.button("8", on_click=update_expression, args=(8,))
    st.button("0", on_click=update_expression, args=(0,))
    st.button("ㅡ", on_click=update_expression, args=("-",))
    st.button("C", on_click=clear_expression)
    

with col3:
    st.button("3", on_click=update_expression, args=(3,))
    st.button("6", on_click=update_expression, args=(6,))
    st.button("9", on_click=update_expression, args=(9,))
    st.button("⌫", on_click=backspace_expression)  # Backspace button
    st.button("X", on_click=update_expression, args=("*",))
    st.button("=", on_click=evaluate_expression)


# Engineering functions
st.subheader("Engineering Functions")
col4, col5, col6 = st.columns(3)

with col4:
    st.button("sin", on_click=update_expression, args=("math.sin(",))
    st.button("cos", on_click=update_expression, args=("math.cos(",))
    st.button("tan", on_click=update_expression, args=("math.tan(",))

with col5:
    st.button("log10", on_click=update_expression, args=("math.log10(",))
    st.button("ln", on_click=update_expression, args=("math.log(",))
    st.button("sqrt", on_click=update_expression, args=("math.sqrt(",))

with col6:
    st.button("pi", on_click=update_expression, args=(math.pi,)) 
    st.button("(", on_click=update_expression, args=("(",))
    st.button(")", on_click=update_expression, args=(")",))

# Provide a final button to evaluate the expression
if st.button("Evaluate"):
    evaluate_expression()
