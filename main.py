import streamlit as st
st.title('my first streamlit app')
name=st.text_input('이름을 입력해주세요:')
menu=st.selectbox('좋아하는 음식을 선택하세요',['막국수','돼지국밥', '순대국밥', '설렁탕', '들깨수제비'])
if st.button('LOL you got rickrolled'):
  st.write(f'안녕하세요, {name}님! 당신이 좋아하는 음식은 {menu}이군요. 정말 맛있겠네요! 반갑습니다! =) https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab <==')                 
