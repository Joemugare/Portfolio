import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Set the Matplotlib backend to 'Agg' to work with Streamlit
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import plotly.express as px
import pandas as pd
from streamlit_lottie import st_lottie


# Set page configuration as the first Streamlit command
st.set_page_config(page_title="Portfolio ", page_icon="📄", layout="wide")

# Define custom CSS styles for improved aesthetics
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .st-bm {
        background-color: #2a3e72;
        color: white;
    }
    .st-at {
        background-color: #f0f2f6;
        color: #2a3e72;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    # Header with Photo
    st.title("Joseph Mugare Portfolio")
    st.subheader("Data Analyst/Fullstack Developer")

    # Add Lottie animation from the provided URL
    animation_url = "https://lottie.host/e8dbe450-ca62-4516-8646-b646e8bef5a1/rTmqdL4mNv.json"
    st_lottie(animation_url, speed=1, height=300, key="lottie")  # Customize the animation height and speed



    # Contact Information
    st.header("Contact Information")
    st.markdown("📧 Email: joemugare@gmail.com")
    st.markdown("📞 Phone: +254720957180")
    st.markdown("🌐 LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/joseph-mugare/)")
    st.markdown("📁 GitHub: [GitHub Profile](https://github.com/joemugare)")
    st.markdown("📺 YouTube: [YouTube Channel](https://www.youtube.com/user/joemugare)")

    # Summary or Objective Section
    st.header("Summary")
    st.write("Experienced Data Analyst and Fullstack Developer with a passion for crafting innovative web applications. Proficient in Python, JavaScript, and adept in cloud computing technologies. Committed to delivering high-quality solutions that precisely align with business objectives.")

    # Education
    st.header("Education")
    st.markdown("Bachelor In Information Technology, KCA UNIVERSITY")
    st.markdown("JAN  2009 - DECEMBER  2011")

    # Additional Certifications
    st.header("Additional Certifications")
    st.markdown("1. CCNA, ZETECH")
    st.markdown("2. MYSQL, EDX STANFORD (Feb 2023 - July 2023)")
    st.markdown("3. Python Data Science, EDX HARVARD (January 2023 - June 2023)")
    st.markdown("4. CS50's Introduction to Computer Science, Harvard University (March 2024)")
    st.markdown("5. MIT Computer Science and Programming Using Python, Massachusetts Institute of Technology (January 2024)")
    st.markdown("6. MIT Computational Thinking and Data Science, Massachusetts Institute of Technology (March 2024)")


    # Work Experience
    st.header("Work Experience")
    st.subheader("Fullstack Developer at BIO HAZARD NBO")
    st.write("Jan 2021 - Present")
    st.write("Responsible for designing, developing, and maintaining web applications.")
    st.write("Collaborated closely with cross-functional teams to ensure seamless project delivery.")

    # GitHub Contributions
    st.header("GitHub Contributions (Line Chart)")

    # Create a sample data frame for the line chart (replace this with your actual data)
    github_data = {
        "Year": [2019, 2020, 2021, 2022, 2023,2024],
        "Contributions": [100, 350, 550, 600, 600,800]
    }
    github_df = pd.DataFrame(github_data)

    fig_line = px.line(github_df, x="Year", y="Contributions", title="GitHub Contributions Over Time")
    st.plotly_chart(fig_line)  

    # Add the Skills animation under the "Skills" section
    st.header("Skills")
    animation_url1 = "https://lottie.host/81923711-4d08-4098-9c30-4df1491579ac/bDnigl2A7X.json"
    st_lottie(animation_url1, speed=1, height=300, key="lottie_animation_skills")

    st.write("Programming Languages: Python, JavaScript")
    st.write("Machine Learning: Scikit-learn, TensorFlow, Keras")
    st.write("Cloud Computing: AWS")
    st.write("Databases: MySQL, MongoDB")
    st.write("Version Control: Git")


    
    # Add the Project animation under the "Skills" section
    st.header("Projects")
    animation_url = "https://lottie.host/c69a85a4-cc7e-472d-921b-851566ade1d4/EySROHiYry.json"
    st_lottie(animation_url, speed=1, height=300, key="lottie_animation_projects")

    st.subheader("E-commerce Website")
    st.write("Developed a full-stack e-commerce website using React and Node.js.")
    st.write("Implemented payment processing, user authentication, and product recommendation system.")

    st.subheader("Portfolio Website")
    st.write("Created a personal portfolio website using HTML, CSS, and JavaScript.")
    st.write("Utilized responsive design principles for optimal viewing across devices.")
    st.write("Implemented dynamic content loading and smooth transitions for improved user experience.")

    # Key Achievements
    st.header("Key Achievements")
    st.markdown("1. Implemented a machine learning-based recommendation system, resulting in a 20% increase in user engagement.")
    st.markdown("2. Designed and deployed a scalable cloud infrastructure using AWS, reducing operational costs by 15%.")
    st.markdown("3. Led the development of a data-driven dashboard, providing actionable insights for decision-makers.")


    # Certifications and Awards
    st.header("Certifications and Awards")
    st.markdown("1. AWS Cloud Quest Data Analytics Certification")
    st.markdown("2. AWS Cloud Quest Solutions Architect Certification")
    st.markdown("3. Google Analytics Certification")
    st.markdown("4. Microsoft Certified: Azure AI Engineer Associate")
    st.markdown("5. Coursera: Deep Learning Specialization")
    st.markdown("6. IBM Data Science Professional Certificate")


    # Code Samples
    st.header("Code Samples")
    ("https://youtube-trends-joe.streamlit.app/")

    # Testimonials
    st.header("Testimonials")

    st.subheader("Alvin, Senior Network Adimn Liquid Telecom:")
    st.write("Working with Mugare has been an absolute pleasure. His deep understanding of machine learning concepts coupled with their proficiency in coding has been instrumental in delivering successful projects. I highly recommend him for any data science role.")

    st.subheader("Virender, Director London Distillers Kenya:")
    st.write("Joseph is a highly skilled full-stack developer with a keen eye for detail. They have a knack for problem-solving and consistently deliver high-quality solutions. It's been a privilege to work alongside him.")

    st.subheader("Anne Nderitu :")
    st.write("I engaged Joseph for a web development project, and I was thoroughly impressed with their professionalism and expertise. He went above and beyond to ensure that the final product exceeded my expectations. I wouldn't hesitate to work with him again in the future.")


    # Awards and Honors
    st.header("Awards and Honors")
    st.markdown("1. Employee of the Month (June 2022)")
    st.markdown("3. Outstanding Academic Achievement Award (2009)")
    st.markdown("4. Innovation Award for Machine Learning Project (2023)")
    st.markdown("5. Top Performer in Cloud Computing Hackathon (2020)")
    st.markdown("6. Leadership Excellence Award for Project Management (2018)")


    # Professional Associations
    st.header("Professional Associations")
    st.markdown("1. Member of the Association of Fullstack Developers (AFD)")
    st.markdown("2. IEEE Computer Society Member")
    st.markdown("3. ACM - Association for Computing Machinery Member")
    st.markdown("4. Data Science Society Member")
    st.markdown("5. Cloud Native Computing Foundation (CNCF) Member")
    st.markdown("6. International Web Developers Association (IWDA) Member")

    # Volunteer Work
    st.header("Volunteer Work")
    st.subheader("Tech for Good Charity")
    st.write("Volunteered as a web developer to support charitable causes.")
    st.subheader("Local Youth Mentorship Program")
    st.write("Mentored young individuals interested in technology and programming.")

    # Publications or Research
    st.header("Publications and Research")
    st.subheader("Research Paper: 'Machine Learning in Healthcare'")
    st.write("Published in the International Journal of Data Science and Healthcare.")
    

    # Languages and Technologies
    st.header("Languages and Technologies")
    st.markdown("1. Python (Proficient)")
    st.markdown("2. JavaScript (Proficient)")
    st.markdown("3. AWS (Certified)")
    st.markdown("4. MySQL (Proficient)")
    st.markdown("5. MongoDB (Intermediate)")
    st.markdown("6. Git (Proficient)")

    # Interests and Hobbies
    st.header("Interests and Hobbies")
    st.write("1. Hiking and Outdoor Adventures")
    st.write("2. Photography and Travel")
    st.write("3. Cooking and Culinary Exploration")

    # References
    st.header("References")
    st.markdown("Available upon request. Please feel free to contact me for references.")

    # Badges
    st.header("Badges")
    badge_paths = ["aws-cloud-quest-data-analytics.png", "aws-cloud-quest-solutions-architect.png", "google analytic cert.png"]
    badge_images = [Image.open(path) for path in badge_paths]

    # Create a horizontal layout for badges using st.columns
    badge_columns = st.columns(len(badge_images))
    for i, badge_image in enumerate(badge_images):
        with badge_columns[i]:
            st.image(badge_image, caption=f"Badge {i + 1} (PNG)", use_column_width=False, width=200)

    # Skills Proficiency Bar Chart
    st.header("Skills Proficiency")
    skills = ["Python", "JavaScript", "Data Analysis", "Machine Learning", "SQL", "HTML/CSS", "React.js", "Node.js"]
    proficiency = [90, 80, 85, 75, 90, 85, 80, 75]

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.barh(skills, proficiency, color='skyblue')
    ax.set_xlabel('Proficiency (%)')
    ax.set_title('Skills Proficiency')
    st.pyplot(fig)


    # Downloadable PDF
    st.header("Downloadable PDF")
    pdf_filename = "digital_resume.pdf"

    def generate_pdf():
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 700, "Digital Resume")
        c.drawString(100, 680, "Joseph Mugare")
        c.drawString(100, 660, "Software Engineer")
        c.showPage()
        c.save()

    if st.button("Download PDF"):
        generate_pdf()
        with open(pdf_filename, "rb") as pdf_file:
            st.success("Download your PDF [here](data:application/pdf;base64,%s)" % pdf_file.read().encode("base64").decode())

if __name__ == '__main__':
    main()
