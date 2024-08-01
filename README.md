# Resume Parser with OpenAI Integration

## Project Overview

This project is a resume parser developed to efficiently extract and analyze information from resumes using OpenAI’s GPT models. Built with Python, this project utilizes a virtual environment to manage dependencies and ensure an isolated development environment.

## Technologies Used

- **Python**: The primary programming language for implementing the parser.
- **OpenAI API**: Provides advanced natural language processing capabilities for parsing resume data.
- **Virtual Environment (`venv`)**: Manages project dependencies and isolates the development environment.

## Setup Instructions

1. **Clone the Repository**:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and Activate a Virtual Environment**:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install Dependencies**:
   ```sh
   pip install openai
   ```

4. **Verify Installation**:
   Create a `test_openai.py` file with the following content to ensure the `openai` module is working:
   ```python
   import openai
   print("OpenAI module is working.")
   ```

   Run the script:
   ```sh
   python test_openai.py
   ```

## Project Details

- **Virtual Environment**: A Python virtual environment (`venv`) is utilized to maintain a clean and isolated setup, ensuring that the `openai` package and other dependencies are managed effectively.

- **OpenAI Integration**: The `openai` Python package is used to interact with OpenAI’s GPT models. This integration enables sophisticated parsing of resume text to extract key information such as skills, experience, and qualifications.

- **Script Functionality**: The `parse_resume.py` script is designed to leverage the OpenAI API for natural language processing tasks. It parses resumes and extracts relevant details, demonstrating practical use of AI for text analysis.

## Usage

1. **Activate the Virtual Environment**.
2. **Run the Resume Parsing Script** to process and extract information from resumes.

## Conclusion

This project highlights the application of modern AI technology for text analysis, demonstrating the integration of OpenAI's API with Python. The use of a virtual environment ensures a well-managed development process, showcasing an effective approach to handling dependencies and project requirements.
