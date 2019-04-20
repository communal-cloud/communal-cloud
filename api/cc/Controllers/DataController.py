import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from api.cc.Services.DataService import DataService


class DataController(APIView):
	__logger = logging.getLogger('DataController')
	__dataService = DataService.Instance()