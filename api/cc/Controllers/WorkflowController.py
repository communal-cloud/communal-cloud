import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from cc.Services.WorkflowService import WorkflowService


class WorkflowController(APIView):
	__logger = logging.getLogger('WorkflowController')
	__workflowService = WorkflowService.Instance()