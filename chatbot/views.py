from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatLog, FAQ
from .nlp_engine import get_best_match, get_gemini_response

def chat_home(request):
    return render(request, 'chatbot/index.html')

def get_response(request):
    if request.method == 'POST':
        user_query = request.POST.get('message', '').strip()
        
        if not user_query:
            return JsonResponse({'response': "Please type something!"})

        # Initialize history in session if not exists
        if 'chat_history' not in request.session:
            request.session['chat_history'] = []

        # Step 1: Try local database match
        answer, score = get_best_match(user_query)
        
        if answer:
            response_text = answer
            source = "local"
        else:
            # Step 2: Fallback to Gemini with history
            # Gemini expects [{'role': 'user', 'parts': [...]}, {'role': 'model', 'parts': [...]}]
            formatted_history = []
            for entry in request.session['chat_history'][-6:]: # Keep last 3 exchanges
                formatted_history.append({'role': 'user', 'parts': [entry['user']]})
                formatted_history.append({'role': 'model', 'parts': [entry['bot']]})

            response_text = get_gemini_response(user_query, history=formatted_history)
            source = "gemini"

        # Step 3: Update session history
        request.session['chat_history'].append({'user': user_query, 'bot': response_text})
        request.session.modified = True

        # Step 4: Log the chat in DB
        ChatLog.objects.create(user_query=user_query, bot_response=response_text)

        return JsonResponse({
            'response': response_text,
            'source': source,
            'score': float(score)
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
