import streamlit as st

def main():
    st.header('About Us')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### Ayan Srivastava
        **Role:** Machine Learning Developer

        An experienced software developer with expertise in Python, Machine Learning, and Web Development.
        """)

    with col2:
        st.markdown("""
        ### Aditi 
        **Role:** Designer
        
        A creative designer with a strong background in UI/UX design, graphic design, and digital marketing.
        """)

    with col3:
        # st.image("images/aditya_pic.jpg", caption="Person 3", use_column_width=True)
        st.markdown("""
        ### Person 3
        **Role:** Designer
   
        A creative designer with a strong background in UI/UX design, graphic design, and digital marketing.

        """)