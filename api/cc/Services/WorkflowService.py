import logging
from cc.models import Workflow, Community, Task


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

    def GetByCommunity(self, communityId):
        list = Workflow.objects.filter(Community_id=communityId)
        return list
    
    def Create(self, request, id):
        data=Workflow.objects.create(Name=request.get("Name",u""), Description=request.get("Description",u""), Community_id=id)
        return data

    def Update(self, request, id):
        workflow = Workflow.objects.get(pk=id)
        if "Name" in request:
            workflow.Name = request.get("Name", u"")
        if "Description" in request:
            workflow.Description = request.get("Description", u"")
        workflow.save()
        return workflow
    
    def Delete(self, id):
        workflow = self.Detail(id)
        workflow.Deleted = 1
        workflow.save()
        tasks = Task.objects.filter(Workflow_id=id)
        for i in tasks:
            i.Deleted = 1
            i.save()
        return workflow

    def Detail(self, id):
        workflow = Workflow.objects.get(pk=id)
        return workflow
