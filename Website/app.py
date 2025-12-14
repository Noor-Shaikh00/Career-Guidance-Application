import streamlit as st
from logic import suggest_career
from whatsapp import send_whatsapp
from database import create_db, save_student

# Create DB if not exists
create_db()

# Streamlit page settings
st.set_page_config(page_title="Career Guidance 🎓", layout="centered")
st.title("🎓 Career Guidance System")
st.write("Fill the form to get career suggestions sent directly to your WhatsApp")

# Form Fields
name = st.text_input("👤 Name")
age = st.number_input("🎂 Age", 10, 50)
qualification = st.selectbox("📚 Qualification", ["Matric", "Intermediate", "Graduate"])
interest = st.selectbox("❤️ Interest", ["Medical", "IT", "Commerce", "Arts"])
phone = st.text_input("📱 WhatsApp Number (92xxxxxxxxxx)")

if st.button("🔍 Get Career Suggestions"):
    if name and phone:
        # Get suggestions list
        career_suggestions = suggest_career(age, qualification, interest)

        # Save student info to DB
        save_student(name, age, qualification, interest, phone, career_suggestions)

        # Format message for WhatsApp
        suggestions_msg = "\n".join([f"{i+1}. {s}" for i, s in enumerate(career_suggestions)])
        final_msg = f"Hello {name}, here are your career suggestions based on your info:\n\n{suggestions_msg}\n\nBest of luck! 🎯"

        # Send WhatsApp to student
        send_whatsapp(final_msg, phone)

        # Send lead info to admin
        admin_msg = f"New Career Lead 🎓\nName: {name}\nAge: {age}\nQualification: {qualification}\nInterest: {interest}\nPhone: {phone}\nSuggested Careers:\n{suggestions_msg}"
        send_whatsapp(admin_msg, "923132272190")

        # Show simple success message on website
        st.success("✅ Career suggestions sent to your WhatsApp successfully!")
    else:
        st.error("❌ Please fill all fields")



# import streamlit as st
# from logic import suggest_career
# from database import create_db, save_student
# from whatsapp import send_whatsapp

# st.set_page_config(page_title="Career Guidance 🎓", layout="centered")

# create_db()

# st.title("🎓 Career Guidance System")
# st.write("Fill the form to get career guidance")

# name = st.text_input("👤 Name")
# age = st.number_input("🎂 Age", 10, 50)
# qualification = st.selectbox(
#     "📚 Qualification",
#     ["Matric", "Intermediate", "Graduate"]
# )
# interest = st.selectbox(
#     "❤️ Interest",
#     ["Medical", "IT", "Commerce", "Arts"]
# )
# phone = st.text_input("📱 WhatsApp Number (92xxxxxxxxxx)")

# if st.button("🔍 Get Career Suggestion"):
#     if name and phone:
#         career = suggest_career(age, qualification, interest)

#         save_student(name, age, qualification, interest, phone, career)

#         admin_msg = f"""
# New Career Lead 🎓
# Name: {name}
# Age: {age}
# Qualification: {qualification}
# Interest: {interest}
# Phone: {phone}
# Career: {career}
# """
#         send_whatsapp(admin_msg, "923303917931")
#         send_whatsapp("Thanks! Our counselor will contact you soon 😊", phone)

#         st.success(f"✅ Suggested Career: {career}")
#     else:
#         st.error("❌ Please fill all fields")
