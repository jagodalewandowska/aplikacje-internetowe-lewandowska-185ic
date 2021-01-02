from celery import shared_task

# definicja nowej funkcji
@shared_task
def adding_task(x, y):
    return x + y