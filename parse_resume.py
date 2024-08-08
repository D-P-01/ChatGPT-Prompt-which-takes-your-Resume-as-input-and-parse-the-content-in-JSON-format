import openai

# Replace 'your-api-key' with your actual API key from OpenAI
openai.api_key = 'your-api-key'

def parse_resume(resume_text):
    prompt = f"""
    You are an AI language model. I will provide you with the text content of a resume. Please parse the resume and format it into a JSON structure with the following fields:
    - Name
    - Contact Information (Email, Phone, Address)
    - Summary
    - Work Experience (Job Title, Company Name, Dates, Description)
    - Education (Degree, Institution, Dates, Description)
    - Skills
    - Certifications
    - Projects
    - Languages
    - Interests

    Please ensure the JSON structure is clear and properly nested where appropriate. Provide the output in JSON format.

    Here is the resume:
    {resume_text}
    """

    response = openai.Completion.create(
      engine="text-davinci-003",  # or another GPT-3 engine
      prompt=prompt,
      max_tokens=1500,
      temperature=0.5,
    )

    return response.choices[0].text.strip()

# Your resume text input
resume_text = """
Dhananjay Pawal
7666588873 
Pune, India 
dhananjaypawal03@gmail.com

Summary:
An enthusiast and passionate Artificial Intelligence and Data Science engineering graduate looking for opportunities to showcase knowledge and gain the experience by solving real-world problems. And to hone organizational skills and teamwork abilities.

Skills:
- C++
- MySQL
- JavaScript
- OOPs
- Data Structures
- Problem Solving
- DBMS
- Machine Learning
- HTML
- CSS
- Python
- C#
- Java
- .Net

Languages:
- English (Full Professional Proficiency)
- Marathi (Full Professional Proficiency)
- Hindi (Full Professional Proficiency)

Interests:
- Eager to learn and adapt to new technologies and methodologies.
- Cricket
- Badminton

Education:
B.Tech (Artificial Intelligence and Data Science) (CGPA: 8.7)
Vishwakarma Institute Of Technology, Pune
2020 - 2024

Personal Projects:
AgroCare: A Plant Disease Diagnosis and Solution System (May-2024)
- Developed an application predicting over 30+ crop diseases and offering solutions for these plant diseases.
- Employed a design thinking approach to create an intuitive solution.
- Created a user-friendly interface for farmers to easily upload images of affected crops and receive accurate disease predictions.
- Utilized CNN, Numpy, Pandas, ResNet34 model, and transfer learning, achieving an accuracy of 92%.

Fake Product Detection using Blockchain (January-2024)
- Developed an application to distinguish between counterfeit and non-counterfeit products.
- Implemented QR code scanning and generation of products with unique hash using SHA256, ownership transfer features to prevent fake copies of the product.
- Used Ganache as a local blockchain.
- Applied experience with MySQL, Web3, MetaMask, PHP, HTML, CSS, JavaScript, and Ganache.

VitBot: A College Enquiry Chatbot (November-2023)
- Created VitBot with a primary focus on enhancing the user experience for individuals seeking information about the college.
- Implemented an end-to-end chatbot portal capable of efficiently retrieving the needed information about the college.
- Trained this chatbot with 3000+ queries.
- Utilized HTML, CSS, and JavaScript to create a user-friendly frontend and developed and trained VitBot using the ChatterBot library.

Work Experience:
AI Intern
Accurate Industrial Controls
06/2024 - Present, Pune, India
- Developed and implemented C# and .NET code for capturing images in required formats for data collection and model training in the gas leakage detection project.
- Led data collection efforts and established a data preprocessing pipeline to ensure high-quality input for model training.
- Built an autoencoder-based model to accurately detect gas leaks, contributing to the project’s overall success.

Certificates:
- Python programming completion certificate.
- SQL completion certificate from Hackerrank.
- Complete Web Development Bootcamp 2023.

Achievements:
- Published paper in IEEE Explore on Simulation of CPU Scheduling Algorithms for Efficient Execution of Process.
- Authored paper in ICJA Journal on Pattern Matching in File System.
- Proposed a paper in SPICON conference on Human Following Robot.
"""

json_output = parse_resume(resume_text)
print(json_output)
