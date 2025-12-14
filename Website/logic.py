def suggest_career(age, qualification, interest):
    suggestions = []

    if qualification == "Matric":
        if interest == "Medical":
            suggestions = [
                "Nursing Assistant",
                "Lab Technician",
                "Pharmacy Assistant",
                "Health Educator",
                "Dental Assistant",
                "Medical Receptionist",
                "First Aid Trainer",
                "Physiotherapy Assistant",
                "Home Health Aide",
                "Medical Records Clerk"
            ]
        elif interest == "IT":
            suggestions = [
                "Junior Web Developer",
                "Graphic Designer",
                "IT Support Technician",
                "Data Entry Operator",
                "Computer Hardware Technician",
                "App Tester",
                "Digital Marketing Assistant",
                "Social Media Manager",
                "SEO Assistant",
                "Freelance Programmer"
            ]
        elif interest == "Commerce":
            suggestions = [
                "Accounts Assistant",
                "Sales Executive",
                "Bank Teller",
                "Cashier",
                "Customer Support",
                "Marketing Assistant",
                "Retail Manager",
                "Business Analyst Trainee",
                "Insurance Agent",
                "Stock Clerk"
            ]
        elif interest == "Arts":
            suggestions = [
                "Graphic Designer",
                "Animator",
                "Content Writer",
                "Copywriter",
                "Interior Designer",
                "Fashion Designer",
                "Photography Assistant",
                "Video Editor",
                "Music Instructor",
                "Event Planner"
            ]
        else:
            suggestions = ["Career Counselor Consultation Recommended"]

    elif qualification == "Intermediate":
        if interest == "Medical":
            suggestions = [
                "Pharmacy Technician",
                "Lab Technician",
                "Nursing Diploma",
                "MBBS Path Guide",
                "Physiotherapy Assistant",
                "Medical Sales Representative",
                "Nutritionist Assistant",
                "Health Administration",
                "Radiology Technician",
                "Clinical Research Assistant"
            ]
        elif interest == "IT":
            suggestions = [
                "Web Developer",
                "App Developer",
                "Data Analyst",
                "UI/UX Designer",
                "Network Technician",
                "Cybersecurity Assistant",
                "Database Administrator",
                "Digital Marketing Specialist",
                "Software Tester",
                "Python Programmer"
            ]
        elif interest == "Commerce":
            suggestions = [
                "Business Administration",
                "Accounting",
                "Finance Analyst Trainee",
                "Banking Associate",
                "Marketing Coordinator",
                "Human Resources Assistant",
                "Entrepreneurship Path",
                "Retail Management",
                "Tax Consultant Assistant",
                "Insurance Advisor"
            ]
        elif interest == "Arts":
            suggestions = [
                "Graphic Designer",
                "Animator",
                "Content Writer",
                "Copywriter",
                "Interior Designer",
                "Fashion Designer",
                "Photography Assistant",
                "Video Editor",
                "Music Instructor",
                "Event Planner"
            ]
        else:
            suggestions = ["Career Counselor Consultation Recommended"]

    elif qualification == "Graduate":
        if interest == "Medical":
            suggestions = [
                "Pharmacist",
                "Doctor (MBBS/Path Guide)",
                "Clinical Researcher",
                "Medical Lab Specialist",
                "Nutritionist",
                "Physiotherapist",
                "Healthcare Management",
                "Medical Writer",
                "Radiologist Assistant",
                "Public Health Officer"
            ]
        elif interest == "IT":
            suggestions = [
                "Software Engineer",
                "Data Scientist",
                "AI/ML Specialist",
                "Web/App Developer",
                "UI/UX Designer",
                "Cloud Engineer",
                "Cybersecurity Analyst",
                "Business Intelligence Analyst",
                "Project Manager",
                "Digital Product Manager"
            ]
        elif interest == "Commerce":
            suggestions = [
                "Financial Analyst",
                "Accountant",
                "Business Consultant",
                "Marketing Manager",
                "HR Manager",
                "Entrepreneur",
                "Investment Analyst",
                "Tax Consultant",
                "Retail Manager",
                "Bank Manager"
            ]
        elif interest == "Arts":
            suggestions = [
                "Graphic Designer",
                "Animator",
                "Content Writer",
                "Copywriter",
                "Interior Designer",
                "Fashion Designer",
                "Photographer",
                "Video Editor",
                "Music Composer",
                "Event Manager"
            ]
        else:
            suggestions = ["Career Counselor Consultation Recommended"]

    else:
        suggestions = ["Career Counselor Consultation Recommended"]

    return suggestions



# def suggest_career(age, qualification, interest):
#     suggestions = []

#     if qualification == "Matric":
#         if interest == "Medical":
#             suggestions = [
#                 "Nursing Assistant",
#                 "Lab Technician",
#                 "Pharmacy Assistant",
#                 "Health Educator",
#                 "Dental Assistant",
#                 "Medical Receptionist",
#                 "First Aid Trainer",
#                 "Physiotherapy Assistant",
#                 "Home Health Aide",
#                 "Medical Records Clerk"
#             ]
#         elif interest == "IT":
#             suggestions = [
#                 "Junior Web Developer",
#                 "Graphic Designer",
#                 "IT Support Technician",
#                 "Data Entry Operator",
#                 "Computer Hardware Technician",
#                 "App Tester",
#                 "Digital Marketing Assistant",
#                 "Social Media Manager",
#                 "SEO Assistant",
#                 "Freelance Programmer"
#             ]
#         elif interest == "Commerce":
#             suggestions = [
#                 "Accounts Assistant",
#                 "Sales Executive",
#                 "Bank Teller",
#                 "Cashier",
#                 "Customer Support",
#                 "Marketing Assistant",
#                 "Retail Manager",
#                 "Business Analyst Trainee",
#                 "Insurance Agent",
#                 "Stock Clerk"
#             ]
#         else:
#             suggestions = ["Career Counselor Consultation Recommended"]

#     elif qualification == "Intermediate":
#         if interest == "Medical":
#             suggestions = [
#                 "Pharmacy Technician",
#                 "Lab Technician",
#                 "Nursing Diploma",
#                 "MBBS Path Guide",
#                 "Physiotherapy Assistant",
#                 "Medical Sales Representative",
#                 "Nutritionist Assistant",
#                 "Health Administration",
#                 "Radiology Technician",
#                 "Clinical Research Assistant"
#             ]
#         elif interest == "IT":
#             suggestions = [
#                 "Web Developer",
#                 "App Developer",
#                 "Data Analyst",
#                 "UI/UX Designer",
#                 "Network Technician",
#                 "Cybersecurity Assistant",
#                 "Database Administrator",
#                 "Digital Marketing Specialist",
#                 "Software Tester",
#                 "Python Programmer"
#             ]
#         elif interest == "Commerce":
#             suggestions = [
#                 "Business Administration",
#                 "Accounting",
#                 "Finance Analyst Trainee",
#                 "Banking Associate",
#                 "Marketing Coordinator",
#                 "Human Resources Assistant",
#                 "Entrepreneurship Path",
#                 "Retail Management",
#                 "Tax Consultant Assistant",
#                 "Insurance Advisor"
#             ]
#         else:
#             suggestions = ["Career Counselor Consultation Recommended"]

#     elif qualification == "Graduate":
#         if interest == "Medical":
#             suggestions = [
#                 "Pharmacist",
#                 "Doctor (MBBS/Path Guide)",
#                 "Clinical Researcher",
#                 "Medical Lab Specialist",
#                 "Nutritionist",
#                 "Physiotherapist",
#                 "Healthcare Management",
#                 "Medical Writer",
#                 "Radiologist Assistant",
#                 "Public Health Officer"
#             ]
#         elif interest == "IT":
#             suggestions = [
#                 "Software Engineer",
#                 "Data Scientist",
#                 "AI/ML Specialist",
#                 "Web/App Developer",
#                 "UI/UX Designer",
#                 "Cloud Engineer",
#                 "Cybersecurity Analyst",
#                 "Business Intelligence Analyst",
#                 "Project Manager",
#                 "Digital Product Manager"
#             ]
#         elif interest == "Commerce":
#             suggestions = [
#                 "Financial Analyst",
#                 "Accountant",
#                 "Business Consultant",
#                 "Marketing Manager",
#                 "HR Manager",
#                 "Entrepreneur",
#                 "Investment Analyst",
#                 "Tax Consultant",
#                 "Retail Manager",
#                 "Bank Manager"
#             ]
#         else:
#             suggestions = ["Career Counselor Consultation Recommended"]

#     else:
#         suggestions = ["Career Counselor Consultation Recommended"]

#     return suggestions



# def suggest_career(age, qualification, interest):
#     if qualification == "Intermediate" and interest == "Medical":
#         return "Pharmacist 💊, Lab Technician 🧪, MBBS (Proper Path)"
    
#     elif qualification == "Matric" and interest == "IT":
#         return "Web Developer 💻, App Developer 📱"
    
#     elif qualification == "Graduate" and interest == "Commerce":
#         return "Accountant 📊, Business Analyst 📈"
    
#     else:
#         return "Career Counselor se baat karein 📞"
