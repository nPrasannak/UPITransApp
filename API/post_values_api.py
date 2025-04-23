from google.cloud import aiplatform


def post_call(data):
    aiplatform.init(project="focus-infusion-457122-c8", location="us-central1")

    endpoint = aiplatform.Endpoint(
        endpoint_name="projects/focus-infusion-457122-c8/locations/us-central1/endpoints/7448273185973207040")

    response = endpoint.predict(instances=[data])
    return response
