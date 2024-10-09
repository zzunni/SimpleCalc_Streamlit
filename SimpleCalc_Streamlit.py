import streamlit as st

# Initialize session state for calculator
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to update the expression
def update_expression(value):
    st.session_state.expression += str(value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)  # Update expression with result
    except Exception as e:
        st.session_state.expression = "Error"

# Function to clear the expression
def clear_expression():
    st.session_state.expression = ""

# Calculator buttons
st.title("Calculator")

# Display current expression
st.write(f"Expression: {st.session_state.expression}")

# Number buttons
col1, col2, col3 = st.columns(3)

with col1:
    for i in range(1, 4):
        st.button(str(i), on_click=update_expression, args=(i,))
    st.button('0', on_click=update_expression, args=(0,))

with col2:
    for i in range(4, 7):
        st.button(str(i), on_click=update_expression, args=(i,))

with col3:
    for i in range(7, 10):
        st.button(str(i), on_click=update_expression, args=(i,))
    st.button("Clear", on_click=clear_expression)

# Operation buttons
st.button('+', on_click=update_expression, args=('+',))
st.button('-', on_click=update_expression, args=('-',))
st.button('*', on_click=update_expression, args=('*',))
st.button('/', on_click=update_expression, args=('/',))
st.button('=', on_click=evaluate_expression)
