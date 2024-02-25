from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import os

def image_list_topK(path):
    static_path = os.path.join('pages/static', 'topK')
    image_files = [f for f in os.listdir(static_path) if f.endswith('.png')]
    return JsonResponse({'images': image_files})

def image_list_per_member(path):
    static_path = os.path.join('pages/static', 'analysis_per_member_of_parliament')
    image_files = [f for f in os.listdir(static_path) if f.endswith('.png')]
    return JsonResponse({'images': image_files})

def image_list_per_party(path):
    static_path = os.path.join('pages/static', 'analysis_per_party')
    image_files = [f for f in os.listdir(static_path) if f.endswith('.png')]
    return JsonResponse({'images': image_files})

def image_list_in_time_per_member(path):
    static_path = os.path.join('pages/static', 'in_time_analysis_per_member')
    image_files = [f for f in os.listdir(static_path) if f.endswith('.png')]
    return JsonResponse({'images': image_files})

def image_list_in_time_per_party(path):
    static_path = os.path.join('pages/static', 'in_time_analysis_per_party')
    image_files = [f for f in os.listdir(static_path) if f.endswith('.png')]
    return JsonResponse({'images': image_files})

def image_list_similarity_graph(path):
    static_path = os.path.join('pages/static', 'similarity_graph')
    image_files = [f for f in os.listdir(static_path) if f.endswith('.png')]
    return JsonResponse({'images': image_files})

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def in_time_analysis(request):
    template = loader.get_template('in-time-analysis.html')
    return HttpResponse(template.render())

def top_k(request):
    template = loader.get_template('top-k.html')
    return HttpResponse(template.render())

def lsi_analysis(request):
    template = loader.get_template('lsi_analysis.html')
    return HttpResponse(template.render())

def speech_similarity(request):
    template = loader.get_template('speech_similarity.html')
    return HttpResponse(template.render())

def suprise_analysis(request):
    template = loader.get_template('suprise_analysis.html')
    return HttpResponse(template.render())

def sidebar(request):
    template = loader.get_template('sidebar.html')
    return HttpResponse(template.render())

@csrf_exempt
def call_service(request):
    # Perform the action or call the service here
    # Replace this with your actual service logic
    # For example, returning a JSON response when the button is clicked:
    data = {'message': 'Service called successfully!'}
    return JsonResponse(data)

# @csrf_exempt
# def top_k_pairs(request):
#     try:
#         #k_value = 5  # You can adjust this based on your requirements
        
#         # Call the function from your Top_k module
#         result_data = get_top_k_data()

#         # For demonstration purposes, let's assume you're returning a JSON response
#         return JsonResponse(result_data)

#     except Exception as e:
#         return JsonResponse({'error': str(e)})