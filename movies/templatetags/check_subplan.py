from atexit import register
from django import template
from movies.models import Subscription,SubPlan
from django.contrib.auth.models import User
import datetime
from datetime import date

register=template.Library()
@register.simple_tag
def check_user_sub_plan(user_id,plan_id):
    user=User.objects.get(id=user_id)
    plan=SubPlan.objects.get(id=plan_id)
    check_subplan=Subscription.objects.filter(user=user,plan=plan).count()
    if check_subplan > 0:
        return True
    else:
        return False

@register.simple_tag
def check_validity(user_id,plan_id):
    expired=False
    remaining_days=None
    subscription_validity=None
    # user=request.user
    # if request.user.is_authenticated:
    user=User.objects.get(id=user_id)
    subplan=SubPlan.objects.get(id=plan_id)
    check_package=Subscription.objects.filter(user=user,plan=subplan).count()

    if check_package > 0:
        subscription=Subscription.objects.filter(user=user,plan=subplan).order_by('-id').first()
        today=date.today()
        subscription_date=subscription.reg_date
        remaining_days=(today-subscription_date).days
        subscription_validity=subscription.plan.validity_days
        if remaining_days > subscription_validity:
            expired=True
    else:
        expired=False

    return expired



