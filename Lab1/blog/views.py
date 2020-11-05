from django.shortcuts import render

#  stworzyłyśmy funkcję (def) nazwaną post_list, 
# która pobiera request i zwraca return wartość uzyskaną dzięki 
# wywołaniu innej funkcji render, która wyrenderuje (złoży w całość) szablon blog/post_list.html.

def post_list(request):
    return render(request, 'blog/post_list.html', {})