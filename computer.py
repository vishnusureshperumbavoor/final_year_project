import pandas as pd
import streamlit as st
from joblib import load
st.set_page_config(
    page_title="Computer Department",
    page_icon=" "
)

def main():
    model = load('nba_accreditation.json')
    html_temp="""
        <div style="background-color:lightblue;padding:16px">
            <h2 style="color:black;text-align:center;">NBA Accreditation probablilty of Computer Department</h2>
        </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.markdown("##### CURRICULUM \n ")

    p1 = st.radio(
    "Is the curriculum covering topics such as programming languages, data structures, algorithms, computer organization, operating systems and computer networks?",
    ('Yes', 'No'))
    if p1 == 'Yes':
        p1 = 1
    else:
        p1 = 0

    st.markdown("##### FACULTY \n ")
    p2 = st.radio(
    "Does the faculties have strong background in teaching, research and industry experience?",
    ('Yes', 'No'))
    if p2 == 'Yes':
        p2 = 1
    else:
        p2 = 0

    st.markdown("##### INFRASTURCTURE \n ")
    p3 = st.radio(
    "Does the college have well-equipped laboratories, library and computing facilities?",
    ('Yes', 'No'))
    if p3 == 'Yes':
        p3 = 1
    else:
        p3 = 0

    st.markdown("##### STUDENT SUPPORT \n ")
    p4 = st.radio(
    "Does the college have counseling services, academic advising and career guidance for the students?",
    ('Yes', 'No'))
    if p4 == 'Yes':
        p4 = 1
    else:
        p4 = 0

    st.markdown("##### LEARNING OUTCOMES \n ")
    p5 = st.radio(
    "Does the learning outcomes include technical skills, problem-solving abilities, communication skills and teamwork skills?",
    ('Yes', 'No'))
    if p5 == 'Yes':
        p5 = 1
    else:
        p5 = 0

    st.markdown("##### CONTINUOUS IMPROVEMENT \n ")
    p6 = st.radio(
    "Does the institution take regular feedback from students, faculty and employers?",
    ('Yes', 'No'))
    if p6 == 'Yes':
        p6 = 1
    else:
        p6 = 0

    data = pd.DataFrame({
        'curriculum':p1,
        'faculty':p2,
        'infrastructure':p3,
        'student_support':p4,
        'learning_outcomes':p5,
        'continuous_improvement':p6
    },index=[0])

    try:
        if st.button('Predict'):
            pred = model.predict(data)
            #st.balloons()
            st.success("Your college has a chance of {:.2f}% to get accredited".format(pred[0]))
    except:
        st.warning("You can't cultivate crops in this land")


    
if __name__ == "__main__":
    main()