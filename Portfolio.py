import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
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
    st.subheader("Fullstack Developer")

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
    st.write("Experienced Fullstack Developer with a passion for creating innovative web applications. Skilled in Python, JavaScript, and cloud computing. Committed to delivering high-quality solutions to meet business needs.")

    # Education
    st.header("Education")
    st.markdown("Bachelor In Information Technology, KCA UNIVERSITY")
    st.markdown("J A N  2009 - D E C E M B ER  2011")

    # Additional Certifications
    st.header("Additional Certifications")
    st.markdown("1. CCNA, ZETECH")
    st.markdown("2. MYSQL, EDX STANFORD (Feb 2023 - July 2023)")
    st.markdown("3. Python Data Science, EDX HARVARD (January 2023 - June 2023)")

    # Work Experience
    st.header("Work Experience")
    st.subheader("Fullstack Developer at BIO HAZARD NBO")
    st.write("Jan 2021 - Present")
    st.write("Developed and maintained web applications.")
    st.write("Collaborated with cross-functional teams to deliver projects")
    
    # GitHub Contributions
    st.header("GitHub Contributions (Line Chart)")

    # Create a sample data frame for the line chart (replace this with your actual data)
    github_data = {
        "Year": [2019, 2020, 2021, 2022, 2023],
        "Contributions": [100, 300, 500, 700, 600]
    }
    github_df = pd.DataFrame(github_data)

    fig_line = px.line(github_df, x="Year", y="Contributions", title="GitHub Contributions Over Time")
    st.plotly_chart(fig_line)

    # Skills
    st.header("Skills")
    st.write("Programming Languages: Python, JavaScript")
    st.write("Cloud Computing: AWS")
    st.write("Databases: MySQL, MongoDB")
    st.write("Version Control: Git")

    # Projects
    st.header("Projects")
    st.subheader("E-commerce Website")
    st.write("Developed a full-stack e-commerce website using React and Node.js.")
    st.write("Implemented payment processing and user authentication.")
    st.subheader("Portfolio Website")
    st.write("Created a personal portfolio website using HTML, CSS, and JavaScript.")
    st.write("Showcased my work and skills through a user-friendly interface.")

    # Key Achievements
    st.header("Key Achievements")
    st.markdown("1. Increased website traffic by 30% through SEO optimization.")
    st.markdown("2. Successfully led a team of developers in delivering a critical project on time.")
    st.markdown("3. Received the 'Employee of the Month' award in June 2022.")

    # Certifications and Awards
    st.header("Certifications and Awards")
    st.markdown("1. AWS Cloud Quest Data Analytics Certification")
    st.markdown("2. AWS Cloud Quest Solutions Architect Certification")
    st.markdown("3. Google Analytics Certification")

    # Online Portfolio
    st.header("Online Portfolio")
    st.markdown("Visit my online portfolio to explore my projects and work in more detail: [Portfolio](https://yourportfolio.com)")

    # Code Samples
    st.header("Code Samples")
    # You can provide code snippets or links to specific code examples on GitHub.

    # Testimonials
    st.header("Testimonials")
    # If available, you can add testimonials from colleagues or clients.

    # Awards and Honors
    st.header("Awards and Honors")
    st.markdown("1. Employee of the Month (June 2022)")
    st.markdown("2. Best Web Developer Award (2021)")
    st.markdown("3. Outstanding Academic Achievement Award (2009)")

    # Professional Associations
    st.header("Professional Associations")
    st.markdown("1. Member of the Association of Fullstack Developers (AFD)")
    st.markdown("2. IEEE Computer Society Member")

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
    st.markdown("Link to [Research Paper](https://example.com/research-paper)")

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
    skills = ["Python", "JavaScript", "Data Analysis", "Machine Learning", "SQL"]
    proficiency = [90, 80, 85, 75, 90]

    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots()
    ax.bar(skills, proficiency, color='#2a3e72')
    plt.xticks(rotation=45)
    st.pyplot(fig, use_container_width=True)

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
