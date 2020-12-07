from django.test import TestCase
from django.utils import timezone

import datetime

from accounts.models import User
from api.models import ChatMessage
from api import admin



class TestSlack(TestCase):

    """Model
    username = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images',blank=True, null=True)
    icon =models.CharField(max_length=1000)
    good = models.IntegerField(null=True, blank=True, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    """
    
    def test_chatmessage(self):

        saved_messages = ChatMessage.objects.all()
        self.assertFalse(saved_messages.count(), 0)

        testchat = ChatMessage.objects.create(
            username = "hogehgoe",
            nickname = "hogehgoe",
            text = "test",
            image = "test.png",
            thumbnail = "test.png",
            icon = "test",
            good = 0,
            created_date = datetime.datetime(2020, 11, 12, 9, 55, 28)
        )
        testMessage = testchat.text
        self.assertTrue("test", testMessage)