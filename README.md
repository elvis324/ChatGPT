

# ChatGPT 

 作为 OpenAI 开发的一种大型自然语言处理模型，ChatGPT 可以根据用户输入生成相应的文本回复，还会关联上下文，非常智能

###  OpenAI官网 https://openai.com/(https://openai.com/)
 
  <img width="535" alt="image" src="https://user-images.githubusercontent.com/57925514/218942962-25ca437c-3140-4977-b4dc-9e13bbec18f6.png">
  
###  ChatGPT官网 https://chat.openai.com/auth/login(https://chat.openai.com/auth/login)
  <img width="522" alt="image" src="https://user-images.githubusercontent.com/57925514/218943331-01cd5299-3d7c-421b-aafb-c86e66d3cf6c.png">

####  如何使用Python调用ChatGPT
 
　　1、获取 API Key

　　 首先，需要在 OpenAI 官网注册账号并获取 API Key，该 Key 用于访问 OpenAI的
    API。如果获取到了 API Key，在不翻墙的情况下，也可以使用。

　　2、安装 OpenAI 库

　　通过 pip 安装 OpenAI 库：

　　pip install openai

　　3、创建代码

　　下面是一段 Python 代码，演示如何通过调用 OpenAI API 来实现与 ChatGPT 的交互：
  ```
　　import openai

　　# 设置 API Key

　　openai.api_key = "your_api_key"

　　# 设置请求参数

　　model_engine = "text-davinci-002"

　　prompt = " Python 调用 ChatGPT"

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

　　4、运行代码
  
```
　　现在，我们运行代码，观察 ChatGPT的响应：

　　可以通过更改代码中的请求参数，如提示、模型、温度等，来调整 ChatGPT 的响应。需要注意的是，OpenAI 的 API 有请求限制，因此请确保在开发和测试过程中合理使用 API。在使用 ChatGPT 进行语言处理时，你可以使用多种语言技巧，例如对话管理、语境分析等，来提高应用的质量。
  
