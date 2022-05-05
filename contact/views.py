from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from contact.serializers import EmailSerializer
from django.conf import settings

# Vista Email
@api_view(['POST'])
def contact_email(request):
    
    if request.method == 'POST':
        # Serializer
        email_serializer = EmailSerializer(data = request.data)
        #Validación
        if email_serializer.is_valid():
            # Extraer datos que vienen desde el frontend
            subject = request.data['subject']
            message = request.data['message']
            message_email = request.data['message_email']

            #print(message_email)
            # Enviar email
            send_mail(
                subject,# Asunto
                message + '\n' + message_email, # Cuerpo del correo
                EMAIL_HOST_USER, # Email de envio
                ['vilchesymurillo@gmail.com'], # Email que recibe los mensajes (en este caso es el mismo)
            )
            return Response({"message": "Email enviado"}, status=status.HTTP_200_OK)
        return Response({"message": "No se pudo enviar el correo"}, status=status.HTTP_400_BAD_REQUEST)
        

