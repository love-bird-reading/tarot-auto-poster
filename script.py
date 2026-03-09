import os
import random
import google.generativeai as genai
import facebook

# Setup Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-3-flash-preview')

# Post Styles for Variety
styles = [
    "Daily Love Forecast",
    "Career Guidance Reading",
    "Yes or No Tarot Question",
    "Spiritual Message from Universe",
    "Zodiac Energy Update"
]

def generate_content():
    selected_style = random.choice(styles)
    prompt = f"Write a {selected_style} tarot post in Hindi (शुद्ध हिंदी फॉन्ट). Keep it mysterious and engaging. Mention one random tarot card. End with: 'Free personal reading ke liye download karein Love Bird Tarot App: [YOUR_APP_LINK]'. Add emojis."
    
    response = model.generate_content(prompt)
    return response.text

def post_to_facebook():
    # Facebook Page/Account Token (Isse hum baad mein set karenge)
    token = os.getenv("FB_ACCESS_TOKEN")
    graph = facebook.GraphAPI(token)
    
    groups = [
        "1CXTfmR2Ex", "1Cj58b2Ex6", "198Rfp56cB", "17zge5EiQx"
    ]
    
    message = generate_content()
    
    # Pick a random image from your 'images' folder
    image_folder = "./images"
    image_name = random.choice(os.listdir(image_folder))
    image_path = os.path.join(image_folder, image_name)

    for group_id in groups:
        try:
            with open(image_path, 'rb') as img:
                graph.put_photo(image=img, message=message, album_path=f"{group_id}/photos")
            print(f"Posted to group {group_id}")
        except Exception as e:
            print(f"Error posting to {group_id}: {e}")

if __name__ == "__main__":
    post_to_facebook()
