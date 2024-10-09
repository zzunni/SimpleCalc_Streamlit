import streamlit as st
import math

# Streamlit 앱 제목
st.title("Simple Calculator")

# 결과 변수 초기화
if 'result' not in st.session_state:
    st.session_state.result = ""

# 결과창 만들기 (key 값에 고유한 값 부여)
def display_result():
    st.text_input("Expression", st.session_state.result, key='display_result', disabled=True)

# 숫자 및 연산자 버튼 클릭 처리
def num_click(num):
    st.session_state.result += str(num)
    display_result()

# 연산자 버튼 클릭 처리
def operation_click(op):
    st.session_state.result += op
    display_result()

# 계산 실행
def calculate():
    try:
        expression = st.session_state.result.replace("^", "**")  # ^를 **로 변환
        result = eval(expression)
        st.session_state.result = str(result)
    except Exception as e:
        st.session_state.result = "Error"
    display_result()

# 마지막 입력값 삭제 (백스페이스)
def delete_last():
    st.session_state.result = st.session_state.result[:-1]
    display_result()

# 전체 초기화
def clear():
    st.session_state.result = ""
    display_result()

# 결과 화면 출력
display_result()

# 버튼 레이아웃
cols = st.columns(4)

with cols[0]:
    if st.button('7'):
        num_click(7)
with cols[1]:
    if st.button('8'):
        num_click(8)
with cols[2]:
    if st.button('9'):
        num_click(9)
with cols[3]:
    if st.button('÷'):  # '÷'로 표시
        operation_click('/')

with cols[0]:
    if st.button('4'):
        num_click(4)
with cols[1]:
    if st.button('5'):
        num_click(5)
with cols[2]:
    if st.button('6'):
        num_click(6)
with cols[3]:
    if st.button('×'):  # '×'로 표시
        operation_click('*')

with cols[0]:
    if st.button('1'):
        num_click(1)
with cols[1]:
    if st.button('2'):
        num_click(2)
with cols[2]:
    if st.button('3'):
        num_click(3)
with cols[3]:
    if st.button('-'):
        operation_click('-')

with cols[0]:
    if st.button('0'):
        num_click(0)
with cols[1]:
    if st.button('.'):
        num_click('.')
with cols[2]:
    if st.button('C'):
        clear()
with cols[3]:
    if st.button('+'):
        operation_click('+')

# 계산 버튼
if st.button('='):
    calculate()

# 지우기 버튼 (백스페이스)
if st.button('←'):
    delete_last()

# 추가 기능 버튼
with st.expander("Advanced Functions"):
    advanced_cols = st.columns(4)
    with advanced_cols[0]:
        if st.button('^2'):
            st.session_state.result += '**2'
            display_result()
    with advanced_cols[1]:
        if st.button('√'):
            st.session_state.result = f"sqrt({st.session_state.result})"
            display_result()
    with advanced_cols[2]:
        if st.button('π'):
            st.session_state.result += str(math.pi)
            display_result()
    with advanced_cols[3]:
        if st.button('sin'):
            st.session_state.result = f"sin({st.session_state.result})"
            display_result()

    with advanced_cols[0]:
        if st.button('cos'):
            st.session_state.result = f"cos({st.session_state.result})"
            display_result()
    with advanced_cols[1]:
        if st.button('tan'):
            st.session_state.result = f"tan({st.session_state.result})"
            display_result()
    with advanced_cols[2]:
        if st.button('ln'):
            st.session_state.result = f"log({st.session_state.result})"
            display_result()
