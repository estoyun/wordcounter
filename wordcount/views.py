from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'wordcount/index.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    # 총 단어수 세는 기능 구현
    word_list = full_text.split()
    # 각 단어별로 나온 횟수 세는 기능 구현
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1
    
    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})