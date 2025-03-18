# ml/views.py
import pickle
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sentiment_analysis_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        with open('sentiment_model.pkl', 'rb') as f:
            vectorizer, clf = pickle.load(f)
        X = vectorizer.transform([text])
        sentiment = clf.predict(X)[0]
        return JsonResponse({'sentiment': sentiment})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
