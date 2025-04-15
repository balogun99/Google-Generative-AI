import os
import json
import google.generativeai as genai
# from PIL import Image

# getting the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

# load the API Key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# configuring google.generativeai with API Key
genai.configure(api_key=GOOGLE_API_KEY)

# function to load the chatbot model
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemma-3-27b-it")
    return gemini_pro_model

# function for image captioning
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result

# function for embedding text
# def embedding_model_response(input_text):
#     embedding_model = "models/text-embedding-004"
#     embedding = genai.embed_content(model=embedding_model,
#                                     content=input_text,
#                                     task_type="retrieval_document")
#
#     embedding_list = embedding["embedding"]
#     return  embedding_list

def gemma_response(user_prompt):
    gemma_response_model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-1219")
    response = gemma_response_model.generate_content(user_prompt)
    result = response.text
    return result

# def generate_image_with_gemini(user_prompt: str, image_path: str = None, num_images: int = 1):
#     """
#     Generates images based on a text prompt using the Gemini API.
#
#     Args:
#         prompt: The text prompt to generate the image from.
#         image_path: Optional path to an image to influence the generation (multimodal).
#         num_images: The number of images to generate (default is 1).
#
#     Returns:
#         A list of PIL.Image objects if successful, None otherwise.
#     """
#     genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
#
#     model = genai.GenerativeModel('gemini-pro-vision' if image_path else 'gemini-2.0-flash-exp-image-generation')
#
#     contents = [prompt]
#     if image_path:
#         try:
#             image = Image.open(image_path)
#             contents.append(image)
#         except FileNotFoundError:
#             print(f"Error: Image not found at {image_path}")
#             return None
#
#     try:
#         response = model.generate_content(
#             contents=contents,
#             generation_config={
#                 "num_generation_trials": num_images, # Number of images to try to generate
#             }
#         )
#         images = []
#         for candidate in response.candidates:
#             if candidate.parts and hasattr(candidate.parts[0], 'image'):
#                 images.append(candidate.parts[0].image)
#             elif candidate.parts and hasattr(candidate.parts[0], 'text'):
#                 print(f"Warning: Model returned text instead of image: {candidate.parts[0].text}")
#         return images
#     except Exception as e:
#         print(f"Error generating image: {e}")
#         return None
#
# if __name__ == '__main__':
#     # Set your API key as an environment variable
#     # export GEMINI_API_KEY="YOUR_API_KEY"
#
#     prompt = "A futuristic cityscape at sunset"
#     generated_images = generate_image_with_gemini(prompt, num_images=2)
#
#     if generated_images:
#         for i, img in enumerate(generated_images):
#             img.save(f"generated_image_{i+1}.png")
#             print(f"Generated image saved as generated_image_{i+1}.png")
#
#     # Example using an image to influence the generation
#     image_prompt = "Transform this into a cartoon style"
#     input_image_path = "path/to/your/input_image.jpg" # Replace with your image path
#     edited_images = generate_image_with_gemini(image_prompt, image_path=input_image_path)
#
#     if edited_images:
#         for i, img in enumerate(edited_images):
#             img.save(f"edited_image_{i+1}.png")
#             print(f"Edited image saved as edited_image_{i+1}.png")
