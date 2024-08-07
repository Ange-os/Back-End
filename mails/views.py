from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}"

        email_message = EmailMessage(
            subject=f'Mensaje de {name}',
            body=full_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_RECIPIENNT],
            reply_to=[email]
        )

        email_message.send()
        response = JsonResponse({'status': 'Correo enviado exitosamente'}, status=200)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    response = JsonResponse({'status': 'Método no permitido'}, status=405)
    response["Access-Control-Allow-Origin"] = "*"
    return response