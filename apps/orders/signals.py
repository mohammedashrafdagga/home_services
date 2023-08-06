from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Tracking
from apps.notification.models import Notification


def get_descriptions(order):
    services_name = order.service.name
    data = {
    'قيد المراجعة': {
        'descriptions':f"The Order you request {services_name} is Under review",
        'image': r'tracking_images\review.png',
        'notification': f'You Are Creating New Order for {services_name}'
    },
    'قيد التنفيذ': {
        'descriptions':f"The implementation of the {services_name} has started",
        'image': r'tracking_images\under_work.png',
        'notification': f"we start the implementation the order for {services_name}"
        },
    'مكتمل': {
        'descriptions':f"The Order for {services_name} has been completed successfully",
        'image': r'tracking_images\complete.png',
        'notification': f"we finished implementation the order for {services_name}"
        },
    'مرفوض': {
         'descriptions':f"You order for {services_name} has rejected",
        'image': r'tracking_images\rejected.png',
        'notification': f"You order for {services_name} has rejected"
    }
    }
    return data[order.order_status]

# # when create Coed Activation that Mean Send Activation Code into User
@receiver(post_save, sender = Order)
def order_post_save(sender, instance, created, **kwargs):
    data = get_descriptions(order=instance)
    Tracking.objects.create(
        order = instance,
        status = instance.order_status,
        descriptions = data['descriptions'],
        icons = data['image']
    )
    Notification.objects.create(user = instance.user, message=data['notification'])
        