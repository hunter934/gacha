import random
import streamlit as st
from PIL import Image

pic = Image.open('ub48.PNG')
st.image(pic, width=200)
st.title("UB48 @ Isshoni Tanoshimimashou 17")
st.header("GACHA GACHA BERHADIAH")
st.write("GRAND PRIZE PHOTOBOOK, CD original, towel, photopack, etc")

mylist200 = range(200)
mylist100 = range(100)
mylist50 = range(50)

def gacha(mylist):
    nums = random.choices(mylist, weights=None)
    strnums = str(nums)
    if st.header(strnums) == "0":
        st.header(strnums)

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Angka 1-200")
    button2000 = st.button("IDR 2,000")
    st.write(button2000)
    if button2000:
        gacha(mylist200)
    elif button2000=None:
        st.write(" ")

with col2:
    st.write("Angka 1-100")
    button5000 = st.button("IDR 5,000")
    st.write(button5000)
    if button5000:
        gacha(mylist100)
    elif button5000=None:
        st.write(" ")

with col3:
    st.write("Angka 1-50")
    button10000 = st.button("IDR 10,000")
    st.write(button10000)
    if button10000:
        gacha(mylist50)
    elif button10000=None:
        st.write(" ")
