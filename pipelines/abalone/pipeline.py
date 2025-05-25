from sagemaker.workflow.pipeline import Pipeline

def get_pipeline(region=None, role=None, default_bucket=None, pipeline_name="DemoPipeline", base_job_prefix="demo"):
    return Pipeline(
        name=pipeline_name,
        parameters=[],
        steps=[],
        sagemaker_session=None
    )
