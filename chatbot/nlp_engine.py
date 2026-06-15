import os
import google.generativeai as genai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import FAQ
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

# The genai config is now handled inside the function to ensure the API key is always fresh from environment/settings

def get_best_match(user_query):
    faqs = FAQ.objects.all()
    if not faqs.exists():
        return None, 0

    questions = [faq.question for faq in faqs]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions + [user_query])
    
    # Calculate similarity
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    best_index = similarities.argmax()
    best_score = similarities[0][best_index]
    
    # Lowered threshold slightly for better matching
    if best_score > 0.3: 
        return faqs[int(best_index)].answer, best_score
    
    return None, best_score

def get_gemini_response(user_query, history=None):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or "your_gemini_api_key" in api_key:
        return "System Note: Please set a valid GEMINI_API_KEY in your .env file to enable universal answers."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-flash-latest')
        
        # System instructions specialized for SKASC
        system_instruction = (
            "You are the official AI Assistant for Sri Krishna Arts and Science College (SKASC), Coimbatore. "
            "Your goal is to help prospective and current students with information about SKASC. "
            "Key facts: Sugunapuram, Coimbatore; Motto: 'Igniting Minds, Shaping Up a Bright Future'; Ranked #50 NIRF 2025; 1st in Swachh Campus. "
            "Always be polite, professional, and act as a proud representative of SKASC. "
            "If the user says 'yes' or 'tell me more' to a previous suggestion, follow up on that specific topic."
        )
        
        # Convert history format if provided
        chat_session = model.start_chat(history=history or [])
        
        # Send query with system context prepended if it's the first message
        full_query = f"{system_instruction}\n\nUser Question: {user_query}" if not history else user_query
        
        response = chat_session.send_message(full_query)
        return response.text
    except Exception as e:
        print(f"Gemini Error Details: {e}")
        return f"I'm sorry, I encountered an error while trying to think: {str(e)[:100]}"
