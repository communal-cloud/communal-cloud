import logging
from cc.models import Workflow, Community


class WorkflowService(object):
    __instance = None
    __logger = logging.getLogger('WorkflowService')

    @staticmethod
    def Instance():
        if WorkflowService.__instance is None:
            WorkflowService()
        return WorkflowService.__instance

    def __init__(self):
        if WorkflowService.__instance is not None:
            raise Exception("WorkflowService is a singleton, use 'WorkflowService.Instance()'")
        WorkflowService.__instance = self

    def Create(self, request, id):
        community=Community.objects.get(pk=id)
        data=Workflow.objects.create(Name=request.data.get("Name",u""), Description=request.data.get("Description",u""), Community_id=community)
        return data

    def Update(self, request, id):
        workflow = Workflow.objects.get(pk=id)
        if "Name" in request:
            workflow.Name = request.get("Name", u"")
        if "Description" in request:
            workflow.Description = request.get("Description", u"")
        workflow.save()
        return workflow

    def Detail(self, id):
        workflow = Workflow.objects.get(pk=id)
        return workflow
