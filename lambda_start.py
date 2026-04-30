import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances_to_start = []

    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:AutoStart', 'Values': ['True']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances_to_start.append(instance['InstanceId'])

    if instances_to_start:
        ec2.start_instances(InstanceIds=instances_to_start)
        return f"Started instances: {instances_to_start}"
    
    return "No instances to start"
