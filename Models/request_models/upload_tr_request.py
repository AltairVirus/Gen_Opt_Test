class UploadTRRequest:
    def __init__(self, group):
        self.params = {
            'plan': f'{group.MODEL.PLAN.id}',
            'modelId': f'{group.MODEL.PLAN.id}',
            'RuleGroupId': '58e95ef2-7b5b-44dc-9a44-6105a63e0f6b',
            'loadAllItemsToPlan': 'false',
            'userCorrections': f'{group.MODEL.UC.id}'
        }
