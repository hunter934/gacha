import random
import streamlit as st

st.title("UB48 @ Isshoni Tanoshimimashou 17")
st.header("GACHA GACHA BERHADIAH")
st.write("GRAND PRIZE PHOTOBOOK, CD original, towel, photopack")

mylist200 = range(200)
mylist100 = range(100)
mylist50 = range(50)

def gacha(mylist):
    nums = random.choices(mylist, weights=None)
    strnums = str(nums)
    if st.header(strnums) == "0":
        st.header(strnums)

col1, col2, col3 = st.columns(3)
button = st.button("ROLL")

with col1:
    button2000 = st.button("ROLL")
    st.write("IDR 2000")
    st.write(button)
    if button2000:
        gacha(mylist200)

with col2:
    button5000 = st.button("ROLL")
    st.write("IDR 5000")
    st.write(button)
    if button5000:
        gacha(mylist100)

with col3:
    button10000 = st.button("ROLL")
    st.write("IDR 10000")
    st.write(button)
    if button10000:
        gacha(mylist50)
