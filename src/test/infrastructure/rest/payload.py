def create_testcase_payload(project_id='77dba7a4-6dc7-46e0-aaf1-e956696506bd'):
    return {
        'project_id': project_id,
        'name': 'my testcase',
        'start': {
            'componentId': '3c2755da-e15e-4072-a1e0-0046c7588dd0',
            'type': 'start',
            'node': 'primary'
        },
        'end': {
            'componentId': 'd5ab2ffb-ab5d-4048-838e-1296be40d1f8'
        },
        'steps': [
            {
                'name': 'step 1',
                'componentId': '3c2755da-e15e-4072-a1e0-0046c7588dd0',
                'type': 'output'
            },
            {
                'name': 'step 2',
                'componentId': 'd5ab2ffb-ab5d-4048-838e-1296be40d1f8',
                'type': 'output'
            }
        ]
    }
