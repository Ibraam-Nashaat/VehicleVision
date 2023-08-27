import json
import base64
import boto3

ENDPOINT = "image-classification-2023-08-22-22-52-59-515"

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event["image_data"])

    # Create a SageMaker runtime client
    sagemaker_runtime = boto3.client("sagemaker-runtime")

    # Make a prediction using the InvokeEndpoint API
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType="application/x-image",
        Body=image
    )

    # Get the inferences from the response
    inferences = response["Body"].read()

    # Update the event with inferences and return
    event["inferences"] = inferences.decode('utf-8')
    return event



