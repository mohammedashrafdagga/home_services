from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Tracking



def get_descriptions(order):
    services_name = order.service.name
    data = {
    'قيد المراجعة': {
        'descriptions':f"الطلب لخدمة {services_name} قيد المراجعة الآن",
        'image': r'tracking_images\review.png'
    },
    'قيد التنفيذ': {
        'descriptions':f"الطلب لخدمة {services_name} قيد التنفيذ حالياً",
        'image': r'tracking_images\under_work.png'},
    'مكتمل': {
        'descriptions':f"الطلب لخدمة {services_name} أصبح مكتملاً الأن",
        'image': r'tracking_images\complete.png'},
    'مرفوض': {
         'descriptions':f"الطلب لخدمة {services_name} مرفوض",
        'image': r'tracking_images\rejected.png'
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
        