import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='shark') #here shark is an emoji , we can put any image link within icon '' also .
mymenu = st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://img.freepik.com/free-photo/3d-illustration-blue-purple-futuristic-sci-fi-techno-lights-cool-background_181624-57587.jpg?w=2000')  #the function that we wanna see first on webpage has to
#be written first
st.title('Futuro Technologies')
st.header('By Siddhartha Sen')
st.text('This is a tutorial on Streamlit Library')
if(mymenu=='Home'):
    st.markdown('<center><h1>Welcome</h1></center>',unsafe_allow_html=True)
#st.image('data:image/jpeg;base64,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')
    st.video('https://www.youtube.com/watch?v=qCn22As86xw')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name = st.text_input('Enter Name')
        dob = st.date_input('Choose Date of Birth')
        marks = st.slider('Choose Marks') # Slider for sliding and chosing marks
        k = st.form_submit_button("Submit Form")
        if k:
            st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','hello this is the downloaded data','onlei.txt') #text data getting downloaded here
# emoji 'random' can also be placed for different emoji every time .
# sidebar is a function . selectbox is a dropdown . selectbox name is My Menu.
