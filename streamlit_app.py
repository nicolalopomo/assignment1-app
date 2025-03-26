import streamlit as st

st.title("User Feedback Form")

with st.form("feedback_form"):
  name = st.text_input("Your Name")
  rating = st.slider("Rate your satisfaction", 1, 5, 3)
  comments = st.text_area("Additional Comments")
  submit_button = st.form_submit_button("Submit")
  
if submit_button:
  st.write("## Feedback Summary")
  st.write(f"**Name:** {name}")
  st.write(f"**Satisfaction Rating:** {rating}")
  st.write(f"**Comments:** {comments}")
        
  if rating <= 2:
    st.warning("We're sorry to hear that! We'll work on improving.")
  elif rating >= 4:
    st.success("Thank you for your positive feedback!")


