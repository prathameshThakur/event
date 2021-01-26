import streamlit as st
st.title('Inquisitive result Checker')
word = st.text_input("Enter the letter from participant")
press = st.button('show count')
count = 0
if press:
    for x in word:
        if x in ['b','i','o','i','n','f','o','r','m','a','t','i','c','s','B','I','O','I','N','F','O','R','M','A','T','I','C','S']:
            count+=1

    st.success('The count of words is {}'.format(count))