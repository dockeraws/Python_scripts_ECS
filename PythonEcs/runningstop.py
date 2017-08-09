
import boto3
import sys
client = boto3.client('ecs')
response1 = client.list_tasks(
    cluster=str(sys.argv[1]),
    desiredStatus='running'
)
tasks= response1['taskArns']
taskid= ''.join(tasks)
print taskid

response= client.stop_task(
    cluster=str(sys.argv[1]),
    task=taskid
)

print "running tasks are stoped"

