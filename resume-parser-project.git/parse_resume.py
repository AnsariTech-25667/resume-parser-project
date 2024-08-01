import openai
import json

# Set your OpenAI API key
openai.api_key = 'OPENAI_API_KEY'

def parse_resume(resume_text):
    prompt = (
        "Parse the following resume into JSON format. Include fields such as 'name', 'education', 'skills', 'experience', and 'projects'.\n\n"
        "Resume:\n"
        f"{resume_text}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    parsed_json = response.choices[0].message['content'].strip()
    return json.loads(parsed_json)

if __name__ == "__main__":
    resume_text = """
    Ansari Maaz 
    ENTC undergrad 
    VIT Pune ENTC grad with a strong foundation in Deep Learning, NLP, and Python. Proficient in PyTorch, cloud platforms, and version control with Git. Skilled in advanced ML techniques, including Prompt Engineering and LLM tools like LangChain and LlamaIndex. Driven to innovate in AI and machine learning, bringing enthusiasm and technical expertise to deliver impactful solutions. 
     https://www.hackerrank.com/profile/maazansari25667 
     http://github.com/AnsariTech-25667 
     https://www.linkedin.com/in/ansari-maaz-06193a231/ 
     maaz.ansari211@vit.edu 
     9511670380 
    EDUCATION 
    Vishwakarma Institute of Technology 
    Bachelor of Electronics and Telecommunications 
    Pune, India 
    Expected 2025 
    SKILLS 
    Technical Skills – Python, C++, PyTorch, NLP, LLM Tools (LangChain, LlamaIndex), Git/GitHub, Cloud Platforms (AWS, Azure), SQL. 
    Soft Skills - Strong Verbal and Written Skills, Collaboration Abilities, Troubleshooting, Solution-Oriented, Organizational Skills, Analytical Reasoning, Innovation. 
    Professional Development 
    "Deploying a Python Data Analytics web app on Heroku" (Coursera) - Learned to build and deploy data analysis applications using Python, Streamlit, and Heroku. 
    Certifications 
    “Learning Power BI Desktop" (LinkedIn Learning) - Strengthened data visualization and business intelligence skills using Microsoft Power BI. 
    “Tableau Essential Training” (LinkedIn Learning) - Enhanced data visualization capabilities through Tableau. 
    “Learning Data Analytics: 1 Foundations” (LinkedIn Learning) - Gained a foundation in data analysis concepts and tools, including data collection, cleaning, and visualization. 
    Internship Experience: 
    Developer Intern| InternPixel, Bengaluru, Karnataka 
    Feb 2024 - Mar 2024 | Remote 
    During my internship at InternPixel, I created multiple engaging web interfaces using HTML, CSS, JavaScript, and React. I designed a user-centric platform with Figma, achieving responsive and cross-browser compatibility. This improved the platform’s aesthetic and functionality. Additionally, I tackled complex challenges like performance optimization and API integration, demonstrating my proficiency in web development and ability to deliver impactful, user-friendly digital solutions. 
    Publications: Ansari Maaz. (2024). Precision Robotics Arm System based on computer vision. International Journal of Intelligent Systems and Applications in Engineering (IJISAE). (Scopus Indexed) Available at: https://ijisae.org/index.php/IJISAE/article/view/6136 
    PROJECTS 
    MERN Stack Social Media Platform:- 
    Crafted 'Vinsta,' a dynamic social media platform on the advanced MERN stack, inspired by Facebook, Instagram, and Twitter. Boasting user authentication, real-time interactions, and a dynamic news feed, 'Vinsta' offers seamless experiences. Leveraging MongoDB, Express.js, React, and Node.js, it reflects my expertise in full-stack development, user-centric design, and cutting-edge technology. 'Vinsta' demonstrates my dedication to innovation and delivering impactful digital solutions, marking a milestone in my journey as a developer. 
    Mobile Book Library Application:- React Native Project:- 
    Built a cutting-edge React Native mobile application showcasing expertise in UI/UX design, API integration (Open Library), and efficient navigation (React Navigation). This user-friendly application features real-time search and a book status toggle, highlighting my commitment to technical proficiency and user-centric design. 
    Ethereum Smart Contract for Secure Fund Locking:- Developed a robust Ethereum smart contract using Solidity and JavaScript for secure fund locking, employing Hardhat for seamless testing and deployment. Utilized Mocha and Chai for comprehensive unit testing, ensuring security and efficiency. Implemented time-based fund locking and withdrawal mechanisms, demonstrating proficiency in blockchain development, smart contracts, and leveraging advanced frameworks for streamlined workflows. 
    A Three-Layer Privacy Preserving Cloud Storage:- 
    Developed a three-layer privacy-preserving cloud storage system integrating Caesar Cipher encryption, FTP-based file uploads, and MySQL for data integrity. Utilized modular design for seamless user authentication and secure document management. Implemented robust encryption algorithms, dynamic file splitting, and MAC address-based verification to ensure data confidentiality, efficient cloud interaction, and reliable storage. This comprehensive solution exemplifies advanced data security and cloud technology integration.
    """
    result = parse_resume(resume_text)
    print(json.dumps(result, indent=4))
