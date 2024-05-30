#!/usr/bin/env python3
import aws_cdk as cdk

from richies_cdk.richies_pipeline_stack import RichiesPipelineStack

app = cdk.App()
RichiesPipelineStack(
    app,
    "RichiesPipelineStack",
    env=cdk.Environment(account="888418132247", region="eu-west-2")
)
app.synth()
