from orders.models import Order, OrderArtworkRate
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from django.utils.timezone import make_aware
from artworks.models import Artwork
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

def my_scheduled_job():
    artworksBaclInLessThan = OrderArtworkRate.objects.filter(return_date__lte=make_aware(datetime.now() + timedelta(days=15)), return_date__gte=make_aware(datetime.now()))
    arrBackSoon = []
    for a in artworksBaclInLessThan:
        art = Artwork.objects.get(id=a.artwork_id)
        art.returnDate = a.return_date
        arrBackSoon.append(art)
    subject = 'Retour des oeuvres de la semaine'
    data = { 'artworks': arrBackSoon }
    html_message = render_to_string('./mails/artworksBackThisWeek.html', data)
    plain_message = strip_tags(html_message)
    from_email = 'plateforme@ltk.com'
    to = 'admin@admin.com'
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)