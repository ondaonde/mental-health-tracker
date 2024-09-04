from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306207796',
        'name': 'Najwa Zarifa',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
