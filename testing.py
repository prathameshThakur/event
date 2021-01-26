import streamlit as st
st.title('Inquisitive result Checker')
word = st.text_input("Enter the letter from participant")
press = st.button('show count')
count = 0
if press:
    for x in word:
        if x in 'Bioinformatics' or 'BIOINFORMATICS':
            count+=1

    st.success('The count of words is {}'.format(count))