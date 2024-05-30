import aws_cdk as core
import aws_cdk.assertions as assertions

from richies_cdk.richies_pipeline_stack import RichiesCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in richies_cdk/richies_pipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RichiesCdkStack(app, "richies-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
