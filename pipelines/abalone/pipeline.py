from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.parameters import ParameterString

def get_pipeline():
    return Pipeline(
        name="abalone-pipeline",
        parameters=[
            ParameterString(name="InputDataUrl", default_value="s3://dummy-url/")
        ],
        steps=[]
    )
