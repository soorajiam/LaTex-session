from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your own OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')

available_open_ai_models = [
    "gpt-3.5-turbo",
    "gpt-3.5",
    "gpt-4",
    "gpt-4-turbo",
    "gpt-4o",
    "gpt-4o-mini"
]

your_name = 'John_Doe'

job = input("Enter the job folder name: ")

# Function to read content from a file


def read_file_content(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

def call_openai_api(prompt, model):
    client = OpenAI(api_key=api_key)
    message = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=message,
    temperature=0.2,
    max_tokens=4000,
    frequency_penalty=0.0)
    return response

def write_file_content(file_path: str, content: str):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing file: {str(e)}")
        return False


# Read the .tex file and text file
cv_file = read_file_content('main_cv.tex')  # Replace with your .tex file path
cl_file = read_file_content('main_cover_letter.txt')  # Replace with your text file path

jd_file = read_file_content('job/'+job+'job_description.txt')

# Check if both files were successfully read
if cv_file is not None and cl_file is not None:
    # Combine the contents of both files into a single prompt
    print("Choose the model to use: \n")
    for i, model in enumerate(available_open_ai_models):
        print(f"{i+1}. {model}")
    if len(available_open_ai_models) == 1:
        model_to_use = available_open_ai_models[0]
    else:
        model_to_use = available_open_ai_models[int(input("Enter the model number: ")) -1]
        if model_to_use not in available_open_ai_models:
            print("Invalid model. Exiting...")
            exit()
    # RESUME
    prompt = f"""
    I have to apply for a job with the following job description:- \n{jd_file}
    \n\nMy current Resume is the following:\n{cv_file} 
    \n You have to ensure that this resume will pass the ATS to secure an interview.
      Rewrite my Resume to match the job description which aligns with my experience. 
     try not to change roles.
        rewrite my experience while keeping the task meaning same. 
        Only respond with the LaTeX File. Do not add any other text.
        Do not wrap the latex content in any formatting like ''' or ``` or any other.
        """

    print(prompt)

    # Call the GPT-4 API
    response = call_openai_api(prompt,model_to_use)

    cv_file_response = 'job/'+job+"/"+your_name+"_cv.tex"

    write_file_content(cv_file_response, response.choices[0].message.content)

    prompt = f"""I have to apply for a job with the following job description:- 
    \n{jd_file}\n\nMy current Cover letter is the following:
    \n{cl_file} \n
Rewrite my Cover letter to match the job description which aligns with my experience. 
     try not to change roles.
        rewrite my experience while keeping the task meaning same. 
      """

    print(prompt)

    # Call the GPT-4 API
    response = call_openai_api(prompt, model_to_use)
    print(response)
    print(response.choices[0].message.content)

    cv_file_response = 'job/'+job+"/"+your_name+"_cover_letter.txt"

    write_file_content(cv_file_response, response.choices[0].message.content)
        # Print the generated response
    # print(response.choices[0].text)
else:
    print("File reading failed. Make sure both files exist.")
