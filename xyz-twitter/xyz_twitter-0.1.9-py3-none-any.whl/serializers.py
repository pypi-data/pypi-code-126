# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from xyz_restful.mixins import IDAndStrFieldSerializerMixin
from rest_framework import serializers
from . import models


class UserSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ()
        read_only_fields = ('user', )


class TweetSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    user_name = serializers.CharField(label='用户', source='user.__str__', read_only=True)
    class Meta:
        model = models.Tweet
        exclude = ()
        read_only_fields = ('questions_count', )

