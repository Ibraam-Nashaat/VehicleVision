import json

THRESHOLD = 0.70  

def lambda_handler(event, context):
    # Grab the inferences from the event
    inferences = json.loads(event["inferences"])  # Assuming inferences are stored as JSON

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(confidence >= THRESHOLD for confidence in inferences)

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        return {
            'statusCode': 200,
            'body': json.dumps(event)
        }
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

