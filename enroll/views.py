from django.shortcuts import render
from django.db.models import Count
from .models import Student

def home(request):
    # Aggregate counts based on course and gender
    course_gender_counts = Student.objects.values('course', 'gender').annotate(count=Count('gender'))

    # Extract data for rendering in the template
    labels = []
    counts = []

    for item in course_gender_counts:
        label = f"{item['course']} - {item['gender']}"
        labels.append(label)
        counts.append(item['count'])

    context = {
        'labels': labels,
        'counts': counts,
    }

    return render(request, 'index.html', context)
