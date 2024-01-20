import streamlit as st 
from streamlit_option_menu import option_menu
import requests
from PIL import Image
import base64

# """### gif from url"""
# st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

st.title('Hello')
# st.set_page_config(layout="wide")

def load_lottineurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# lottie_coder =load_lottineurl("https://giphy.com/gifs/KeepCoding-code-coding-keepcoding-ACzsN9dhQuOZ6RYXcM")
# image = Image.open("C:\Users\Abhi\OneDrive\Desktop\portfolio\spam.png")
st.write("#")
st.subheader("Hey Guys:wave:")
st.title("Abhiraj Sachan")
st.subheader("My linkdin profile")
st.write("[Link](https://www.linkedin.com/in/abhiraj-sachan-542799222/)")
st.write('---')
st.subheader("My Blogs at medium")
st.write("[Link](https://medium.com/@abhirajj701)")
st.write('-----')
st.subheader("My kaggle")
st.write("[Link](https://www.kaggle.com/abhirajsac)")
st.write('-----')
st.subheader("My Github ")
st.write("[Link](https://github.com/abhiraj-sac)")
st.write('-----')
st.subheader("My Leetcode Profile")
st.write("[Link](https://leetcode.com/)")

with st.container():
    selected = option_menu(
       menu_title = None,
       options = ['About','Projects','Contact','blogs'],
       icons =['person','code-slash','chat-left-text-fill'],
       orientation =  'horizontal' 
    )
if selected == 'About':
    with st.container():
        col1,col2  =st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am ABhiraj sachan")
            st.title("Machine learning")
        with col2:
            html_code="""
            <img src="https://cdn.dribbble.com/users/2401141/screenshots/5487982/media/9a946a4bf36643b0b9c7ece0eb478f83.gif" width="250" height="250"/>
            """ 
            st.markdown(html_code, unsafe_allow_html=True)
            #  st.image(, width =100)
    st.write('-----')
    with st.container():
        col3,col4 =st.columns(2)
        with col3:
         html_code="""
         <img src="https://cdn.rentechdigital.com/common_files/blogs/machine-learning-swipecart-blog-img-01-31-08-2022.gif" width="250" height="250"/>
         """ 
         st.markdown(html_code, unsafe_allow_html=True)        
        with col4:
         st.write("""Meet Abhiraj, an enthusiastic and dedicated machine learning student with a fervent passion for the ever-evolving field of artificial intelligence. Currently immersed in the journey of mastering machine learning, [Your Name] exhibits a profound curiosity and determination to explore the depths of this transformative technology.
        Armed with a strong foundation in Data Structures and Algorithms,The marriage of SQL expertise with his proficiency in Python, including object-oriented programming (OOP) principles, showcases  holistic approach to data science and machine learning projects. """)
         
         
if selected =="Projects":
    with st.container():
        st.header("My Project")
        st.write("##")
        cols5,cols6,col7 =st.columns((1,3,1))
        with cols5:
            # st.Image(image)
        # st.write("SMS_SPAM_DETECTS")
         st.subheader("To view all projects, can visit")
         st.write("[Link](https://github.com/abhiraj-sac)")    
        with cols6:
            st.header("SMS_SPAM_DETECTS")
            st.write("""The sms spam trapper is a end to end machine learning project, which is deployed in Render.All steps are included in this projects which are:-
            Collecting Data: As you know, machines initially learn from the data that you give them. ...
            Preparing the Data: After you have your data, you have to prepare it. ...
            Choosing a Model: ...
            Training the Model: ...
            Evaluating the Model: ...
            Parameter Tuning: ...
            Making Predictions.
            I have vs code for making a python application.The sms spam trapper is a end to end machine learning project, which is deployed in Render.All steps are included in this projects which are:- Collecting Data: As you know, machines initially learn from the data that you give them. ... Preparing the Data: After you have your data, you have to prepare it. ... Choosing a Model: ... Training the Model: ... Evaluating the Model: ... Parameter Tuning: ... Making Predictions. I have vs code for making a python application.
            Skills: Pickles · Heroku · Random Forest · Scikit-Learn · Git · Matplotlib · NumPy · Pandas (Software)""")
            st.markdown("[visit Github][https://github.com/abhiraj-sac/Spam_detector-End-to-End-deployed-project]")
        with col7:
            st.header("Car price predictor")
            st.write("""
            The main aim of this project is to predict the price of used cars using various Machine Learning (ML) models.
            Steps Involved
            Data Cleaning which involves identifying all the null and missing values and removing the outliers
            The next process is Data Preprocessing which involves us normalising and standardize the dataset
            We then use the different Machine Learning models like Linear Regression, KNN
            We then need to compare the performance of any of the models used
            Now, gather insights and analyze the data based on the accuracy test""")
            st.markdown("[visit Github][https://github.com/abhiraj-sac/Spam_detector-End-to-End-deployed-project]")
        
if selected == 'Contact':
    st.header("Get my contact")
    st.write("##")
    st.write("##")

    contact_form ="""
   <form action="https://formsubmit.co/abhirajsachan706@email.com" method="POST">
     <input type="text" name="ABhiraj sachan" required>
     <input type="email" name="abhirajsachan706@email.com" required>
     <button type="submit">Send</button>
    </form>"""
    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form,unsafe_allow_html=True)
    # with right_col:
        # st.write("hello")   
if selected =="blogs":
    with st.container():
        st.header("My Project")
        st.write("##")
        cols5,cols6,cols7 =st.columns((1,1,1))
        # cols5, cols6, cols7 = st.beta_columns(3)
        with cols5:
            html_code="""
            <img src="https://media.tenor.com/iRB7vrvhPR4AAAAi/data-code.gif" width="200" height="200"/>
            """ 
            st.markdown(html_code, unsafe_allow_html=True)
            st.markdown("[check my all blogs.][https://medium.com/@abhirajj701]")
            st.text('')
        
        with cols6:
            st.header("From the vault:Python oops concepts on medium ")
            st.write("A blog about Python oops Concept from scratch to advance, Every topic is decorated with a related examples of code.")
            st.markdown("[visit my midium page for this Blog!][https://medium.com/@abhirajj701/python-oops-concept-c1abc5778b18]")
            st.text('')
        st.write('-----')
        with cols7:
            st.header("From the vault: Top 8 sql questions")
            st.write("A blog about questions of sql, every questions will trigger famous topics and tuted from scratch to advance, Every topic is decorated with a related examples of code.")
            st.markdown("[visit for][https://medium.com/@abhirajj701/top-8-sql-queries-sql-interview-questions-for-data-science-e791dff3ba4d]")
            st.text('')