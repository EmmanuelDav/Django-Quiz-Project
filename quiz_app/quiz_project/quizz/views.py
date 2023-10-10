from django.shortcuts import render

def index(request):
    question = 'What is the most widely used Python framework?'
    options = ['Django', 'Flask', 'Pyramid']
    
    context = {
        'question': question,
        'options': options,
    }
    return render(request, 'index.html', context)

def form_view(request):
    if request.method == "POST":
       result = request.POST.get("answer")
       context = {"result": result }
    return render(request, "result.html", context)

