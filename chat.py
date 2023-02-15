import openai

　　# 设置 API Key

　　openai.api_key = "your_api_key"

　　# 设置请求参数

　　model_engine = "text-davinci-002"

　　prompt = "Python 调用 ChatGPT"

　　completions = openai.Completion.create(

　　 engine=model_engine,

　　 prompt=prompt,

　　 max_tokens=1024,

　　 n=1,

　　 stop=None,

　　 temperature=0.5,

　　)

　　# 获取 ChatGPT 的回复

　　message = completions.choices[0].text

　　print(message)
