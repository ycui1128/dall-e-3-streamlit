import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from openai import OpenAI  # OpenAI Python library to make API calls


# Streamlit 页面标题
st.title("DALL-E-3 image generation")

# 用户输入框
api_key = st.text_input("input OpenAI API-key", type="password")
prompt_text = st.text_input("input prompt text:")

def generate_image(prompt):

    # imports
    
    client = OpenAI(api_key=api_key)
    # create an image

    # set the prompt

    # call the OpenAI API
    response  = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality="standard",
        response_format="url",
    )
    print(response)

    # if response.status != 200:
    #     st.error(f"API error: {response.errors}")
    #     return None

    # save the image    
    generated_image_url = response.data[0].url  # extract image URL from response
    return  generated_image_url

# Streamlit 按钮，当用户点击时触发生成图片操作
if st.button("Generated images"):
    # TODO: 调用 DALL-E 的代码，传入 prompt_text，获取生成的图片
    # 示例代码（需要替换为实际的 DALL-E 调用代码）
    image_url = generate_image(prompt_text)

    # 显示生成的图片
    if image_url:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Couldn't create images, please retry")


    