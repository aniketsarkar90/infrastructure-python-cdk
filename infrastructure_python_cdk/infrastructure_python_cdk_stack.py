from aws_cdk import core as cdk
from aws_cdk import aws_ec2 as ec2

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class InfrastructurePythonCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # create a vpc         
        # specify the cidr (255 ip's available)
        # max 2 availability zone like the diagram
        # subnet config - 1 private and 1 public
            # this will deply 2 set of public and private subnets in each availability zones 
            # cdk will take care of all the nat provisioning (private route table pointing to nat gateway and) and routing of internet gateway (public subnet pointing to igw)
        vpc = ec2.Vpc(self, 'PythonInfraVPC', 
            cidr='10.1.0.0/16', 
            max_azs=2,
            subnet_configuration = [ 
                {'cidrMask': 24, 'name': 'Web', 'subnetType': ec2.SubnetType.PUBLIC},
                {'cidrMask': 24, 'name': 'Application', 'subnetType': ec2.SubnetType.PRIVATE}
        ])

