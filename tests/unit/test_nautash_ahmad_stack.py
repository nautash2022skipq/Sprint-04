import aws_cdk as core
import aws_cdk.assertions as assertions

from nautash_ahmad.nautash_ahmad_stack import NautashAhmadStack

# example tests. To run these tests, uncomment this file along with the example
# resource in nautash_ahmad/nautash_ahmad_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NautashAhmadStack(app, "nautash-ahmad")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
