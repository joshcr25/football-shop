from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406395291',
        'name': 'Josh Christmas Rommlynn',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)