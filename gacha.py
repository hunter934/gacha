import random
import streamlit as st

st.title("UB48 @ Isshoni Tanoshimimashou 17")
st.header("GACHA GACHA BERHADIAH")
st.write("created by hunter934")

mylist200 = range(200)
mylist100 = range(100)
mylist50 = range(50)

def gacha(mylist):
    nums = random.choices(mylist, weights=None)
    st.write(nums)

button2000 = st.button("IDR 2000")
button5000 = st.button("IDR 5000")
button10000 = st.button("IDR 10000")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(button2000)
    if button2000:
        gacha(mylist200)

with col2:
    st.write(button5000)
    if button5000:
        gacha(mylist5000)

with col3:
    st.write(button10000)
    if button10000:
        gacha(mylist10000)
