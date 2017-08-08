import boto3

client = boto3.client('ecs')
response = client.list_tasks(
    cluster='test-automation',
    desiredStatus='stopped'
)
print(id(response))
response = client.stop_task(
    cluster='test-automation',
    task='297346c0-336a-4839-bce8-0943957e3a9e'
)

print(response)

response = client.start_task(
    cluster='test-automation',
    taskDefinition='testapache',
    containerInstances=['2c3f3f0d-76db-42b2-8fdd-9edf1595e62e']

)
print(response)



