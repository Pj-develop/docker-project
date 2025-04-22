import google.generativeai as genai

genai.configure(api_key="AIzaSyDlv95Vd8NtDI3LVIlq_C0WWk2y8eUbxpM")
model = genai.GenerativeModel('gemini-pro')

def fact(user_input):
    
    data= user_input

    prompt="The following is a conversation with an AI Assistand for AI Legal Decision assistant for India specially for Rajasthan. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nOUTPUT: I am an AI Legal Decision System created by Team : Hackstormers. How can I help you today?\nHuman: {} ?".format(data)
    responseAI = model.generate_content(prompt)
    print(responseAI.text)
    return responseAI.text

fact("hello")
