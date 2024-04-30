from django.dispatch.dispatcher import Signal

send_email_communications = Signal(
    providing_args=[
        'title',
        'email'
    ]
)

