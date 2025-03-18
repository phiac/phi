import os
# from dotenv import load_dotenv
# Load environment variables from .env file (if using dotenv)
# load_dotenv()

# from decouple import config
import logging

import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
import nltk
# nltk.download('punkt_tab')
# nltk.download('wordnet')
# nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from datetime import datetime
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
import wikipedia
from django.contrib.auth.models import User
from django.http import HttpResponse
from transformers import TFDistilBertForQuestionAnswering, DistilBertTokenizer
# import tensorflow as tf

# Load pre-trained model and tokenizer
# model = TFDistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')
# tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased-distilled-squad')

# Example question and context
question = "What is the capital of France?"
context = "The capital of France is Paris."

# Preprocess inputs
# inputs = tokenizer(question, context, return_tensors="tf")

# Get predictions
# outputs = model(**inputs)

# # Extract answer
# answer_start_scores, answer_end_scores = outputs.start_logits, outputs.end_logits

# # Compute answer
# answer_start = tf.argmax(answer_start_scores, axis=1).numpy()[0]
# answer_end = tf.argmax(answer_end_scores, axis=1).numpy()[0] + 1

# # Convert to text
# answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs.input_ids[0][answer_start:answer_end]))

# print(f"Answer: {answer}")


# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def user_details(request):
    return Response({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email
    })

# Set your API key
def query_perplexity(prompt, model="mistral-7b-instruct"):
    """
    Sends a query to Perplexity AI using the pplx-api.
    """
    api_key = os.environ['PERPLEXITY_API_KEY']
    url = "https://api.perplexity.ai/chat/completions"

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Authorization': f"Bearer {api_key}",
    }

    data = {
        "model": model,
        "stream": False,
        "max_tokens": 1024,
        "frequency_penalty": 1,
        "temperature": 0.0,
        "messages": [
            {"role": "system", "content": "Be precise and concise in your responses."},
            {"role": "user", "content": prompt},
        ],
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


# qa_pipeline = pipeline('question-answering')

# Configure Wikipedia library
wikipedia.set_lang("en")

def process_command(command):
    tokens = command.lower().split()
    if 'time' in tokens:
        return "tell_time"
    elif 'date' in tokens:
        return "tell_date"
    else:
        return "ask_general"

def get_dynamic_context(query):
    try:
        search_results = wikipedia.search(query)
        if not search_results:
            print("No Wikipedia search results found.")  # Debugging log
            return None
        page_title = search_results[0]
        summary = wikipedia.summary(page_title, sentences=5)
        print(f"Wikipedia Summary Found: {summary}")  # Debugging log
        return summary
    except Exception as e:
        print(f"Wikipedia Error: {str(e)}")  # Debugging log
        return None


def respond_to_command(intent, query):
    if intent == "tell_time":
        # Return current time
        return "Current time is: " + datetime.now().strftime("%I:%M %p")
    elif intent == "tell_date":
        # Return today's date
        return "Today's date is: " + datetime.now().strftime("%B %d, %Y")
    elif intent == "ask_general":
        # Use Wikipedia for general queries
        dynamic_context = get_dynamic_context(query)
        if dynamic_context:
            try:
                answer = qa_pipeline(question=query, context=dynamic_context)
                return answer['answer']
            except Exception as e:
                print(f"QA Pipeline Error: {str(e)}")  # Debugging log
                return f"Error processing your query: {str(e)}"
        else:
            return f"No relevant information found for '{query}'."
    else:
        # Handle unknown intents
        return "Sorry, I didn't understand that command."


class IgnoreMigrationMessages(logging.Filter):
    def filter(self, record):
        return 'migrations' not in record.getMessage()

# Apply the filter to your handlers
logger = logging.getLogger(__name__)

# Django API Endpoint
@api_view(['POST'])
def process_voice(request):
    if not request.user.is_authenticated:
        return Response({'error': 'Unauthorized'}, status=401)

    # audio_data = request.FILES['audio']
    # result = voice_processor.process(audio_data)
    # return Response({'transcription': result})


    if request.method == 'POST':
        query = request.POST.get('query')
        if not query:
            logger.error("No query provided.")
            return JsonResponse({'error': 'Please enter a query.'})

        intent = process_command(query)
        logger.info(f"Intent Identified: {intent}")

        response = respond_to_command(intent, query)
        logger.debug(f"Generated Response: {response}")

        return JsonResponse({'response': response})

    # Render form for GET requests
    return render(request, 'process_voice.html')


import numpy as np

def validate_mdp_input(states, actions, transition_probabilities, rewards):
    num_states = len(states)
    num_actions = len(actions)

    # Validate transition probabilities
    if len(transition_probabilities) != num_states:
        raise ValueError(f"Transition probabilities must have {num_states} states, but got {len(transition_probabilities)}.")
    for s in range(num_states):
        if len(transition_probabilities[s]) != num_actions:
            raise ValueError(f"State {s} must have {num_actions} actions in transition probabilities.")
        for a in range(num_actions):
            if len(transition_probabilities[s][a]) != num_states:
                raise ValueError(f"State {s}, Action {a} must have {num_states} probabilities.")

    # Validate rewards
    if len(rewards) != num_states:
        raise ValueError(f"Rewards must have {num_states} states, but got {len(rewards)}.")
    for s in range(num_states):
        if len(rewards[s]) != num_actions:
            raise ValueError(f"State {s} must have {num_actions} actions in rewards.")
        for a in range(num_actions):
            if len(rewards[s][a]) != num_states:
                raise ValueError(f"State {s}, Action {a} must have {num_states} rewards.")

def debug_mdp_input(transition_probabilities, rewards):
    print("Transition Probabilities:")
    for s, state_probs in enumerate(transition_probabilities):
        print(f"State {s}:")
        for a, action_probs in enumerate(state_probs):
            print(f"  Action {a}: {action_probs}")

    print("\nRewards:")
    for s, state_rewards in enumerate(rewards):
        print(f"State {s}:")
        for a, action_rewards in enumerate(state_rewards):
            print(f"  Action {a}: {action_rewards}")

            debug_mdp_input(transition_probabilities, rewards)

def value_iteration(states, actions, transition_probabilities, rewards, gamma=0.9, theta=1e-6):
    value_table = np.zeros(len(states))
    policy = np.zeros(len(states), dtype=int)

    while True:
        delta = 0
        for s in range(len(states)):
            action_values = []
            for a in range(len(actions)):
                print(f"State {s}, Action {a}")
                print(f"Transition Probabilities: {transition_probabilities[s][a]}")
                print(f"Rewards: {rewards[s][a]}")

                # Check dimensions
                if len(transition_probabilities[s][a]) != len(states):
                    raise ValueError(f"Mismatch in transition probabilities dimensions for state {s}, action {a}.")
                if len(rewards[s][a]) != len(states):
                    raise ValueError(f"Mismatch in rewards dimensions for state {s}, action {a}.")

                value = sum(
                    transition_probabilities[s][a][s_next] *
                    (rewards[s][a][s_next] + gamma * value_table[s_next])
                    for s_next in range(len(states))
                )
                action_values.append(value)
            max_value = max(action_values)
            delta = max(delta, abs(max_value - value_table[s]))
            value_table[s] = max_value
            policy[s] = np.argmax(action_values)
        if delta < theta:
            break

    return policy, value_table



import json



def machine_learning_view(request):
    if request.method == 'POST':
        try:
            # Parse input data from JSON
            transition_probabilities = json.loads(request.POST.get('transition_probabilities'))
            rewards = json.loads(request.POST.get('rewards'))

            # Validate input format
            if not isinstance(transition_probabilities, list) or not isinstance(rewards, list):
                return JsonResponse({'error': 'Invalid input format. Must be nested lists.'})

            # Validate dimensions
            states = [0, 1, 2]
            actions = [0, 1]
            validate_mdp_input(states, actions, transition_probabilities, rewards)

        except (TypeError, ValueError) as e:
            return JsonResponse({'error': str(e)})

        # Call the value iteration function
        try:
            policy, values = value_iteration(states, actions, transition_probabilities, rewards)
        except Exception as e:
            return JsonResponse({'error': str(e)})
        except (TypeError, ValueError) as e:
            return JsonResponse({'error': str(e)})

        # Call the value iteration function
        try:
            policy, values = value_iteration(states, actions, transition_probabilities, rewards)
        except Exception as e:
            return JsonResponse({'error': str(e)})

        # Return results as JSON response
        return JsonResponse({'policy': policy.tolist(), 'values': values.tolist()})

    # Handle GET request: Render the HTML page
    elif request.method == 'GET':
        return render(request, 'machine_learning.html')

    # Handle other HTTP methods (optional)
    else:
        return JsonResponse({'error': 'Unsupported HTTP method.'}, status=405)

# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_selection import train_test_split
# from nltk.corpus import movie_reviews

# from nltk.corpus import stopwords

import pickle

# Ensure necessary NLTK resources are downloaded
# nltk.download('movie_reviews')
# nltk.download('punkt')
# nltk.download('stopwords')

# Prepare data
# negids = movie_reviews.fileids('neg')
# posids = movie_reviews.fileids('pos')

# negfeats = [(movie_reviews.raw(fileid), 'neg') for fileid in negids]
# posfeats = [(movie_reviews.raw(fileid), 'pos') for fileid in posids]

# # Combine datasets
# labeled_file_names = negfeats + posfeats

# # Tokenize and remove stopwords
# stop_words = set(stopwords.words('english'))

# def preprocess_text(text):
#     tokens = word_tokenize(text)
#     tokens = [t for t in tokens if t.isalpha() and t.lower() not in stop_words]
#     return ' '.join(tokens)

# labeled_file_names = [(preprocess_text(text), label) for text, label in labeled_file_names]

# # Split data into training and testing sets
# train_data, test_data = train_test_split(labeled_file_names, test_size=0.2, random_state=42)

# train_texts = [text for text, _ in train_data]
# train_labels = [label for _, label in train_data]

# test_texts = [text for text, _ in test_data]
# test_labels = [label for _, label in test_data]

# # Vectorize text data
# vectorizer = CountVectorizer()
# X_train = vectorizer.fit_transform(train_texts)
# y_train = train_labels

# # Train the model
# clf = MultinomialNB()
# clf.fit(X_train, y_train)

# # Save the model for later use
# with open('sentiment_model.pkl', 'wb') as f:
#     pickle.dump((vectorizer, clf), f)


from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.sessions.models import Session
# views.py

from .forms import CustomLoginForm

import jwt
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_http_methods
from datetime import  timedelta

@require_http_methods(["POST"])
def login_jwt(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)  # Log the user in using Django's auth system
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, settings.SECRET_KEY, algorithm='HS256')

        response = JsonResponse({'token': token})
        response.set_cookie('jwt', token, domain='.yourdomain.com')
        return response
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm
    redirect_authenticated_user = True

# views.py
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # Redirect to login after registration

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth.forms import UserCreationForm

#     return render(request, 'register.html', {'form': form})

def send_otp(request):
    # Generate OTP and send via SMS
    user = request.user
    # otp = generate_otp()  # Implement OTP generation logic
    # send_sms(user.phone_number, otp)  # Implement SMS sending logic
    return HttpResponse("OTP sent successfully.")

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if verify_otp(otp):  # Implement OTP verification logic
            return render(request, 'password_reset.html')
    return HttpResponse("Invalid OTP.")

def password_reset_with_phone(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        user = request.user
        user.set_password(new_password)
        user.save()
        return HttpResponse("Password reset successfully.")
