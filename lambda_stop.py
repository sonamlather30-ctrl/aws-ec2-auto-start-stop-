import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances_to_stop = []

    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:AutoStop', 'Values': ['True']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances_to_stop.append(instance['InstanceId'])

    if instances_to_stop:
        ec2.stop_instances(InstanceIds=instances_to_stop)
        return f"Stopped instances: {instances_to_stop}"
    
    return "No instances to stop"
