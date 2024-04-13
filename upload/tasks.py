from celery import shared_task
from secureuploader.celery import app
from django.utils import timezone
from django.core.mail import send_mail

# ....
from .models import UploadedFile

def send_emails_to_users(users_emails:list):

    sending_mail = send_mail(
        'File Delete',
        'Here is the message.',
        'from@example.com',
        [users_emails],
        fail_silently=False,
    )
    print("Email Sent to " + str(len(users_emails)) + " users")
    return sending_mail


@app.task
def your_periodic_task():
    ninety_days_ago = timezone.now() - timezone.timedelta(dasy=90)
    print(ninety_days_ago)
    old_files = UploadedFile.objects.filter(created_at__lte=ninety_days_ago)
    
    users_emails = []

    for obj in old_files:
        users_emails.append(obj.ref_user.email)
        obj.delete()
        print(f"Deleted file {obj.file.name}")

    # Optionally, send notification to the user
    send_emails_to_users(users_emails)

    
