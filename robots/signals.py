from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from robots.models import Robot
from orders.models import Order


@receiver(post_save, sender=Robot)
def send_notification_when_robot_available(sender, instance, created, **kwargs):
    if instance.available:
        orders = Order.objects.filter(robot_serial=instance.serial, notified=False)

        for order in orders:
            send_mail(
                subject=f"Робот {instance.model} {instance.version} теперь в наличии",
                message=f"Добрый день!\n\n"
                        f"Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}. \n"
                        f"Этот робот теперь в наличии. Если вам подходит этот вариант, пожалуйста, свяжитесь с нами.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[order.customer.email],
            )

            order.notified = True
            order.save()
