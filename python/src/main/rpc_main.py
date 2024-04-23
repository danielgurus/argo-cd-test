from fastapi import FastAPI
import os
from google.cloud import pubsub_v1

app = FastAPI()


@app.get("/launch_function_a")
async def launch_function_a():
    print("Launch Function A Invoked!")

    try:
        publisher = pubsub_v1.PublisherClient()
        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id='collaboration-01',  #os.getenv('GOOGLE_CLOUD_PROJECT'),
            topic='FUNCTION_A',  # Set this to something appropriate.
        )
        # publisher.create_topic(name=topic_name)
        future = publisher.publish(topic_name, b'{ "caller": "launch_function_a" }')
        future.result()
        return {"message": f"Connected to PubSub. Published message to FUNCTION_A."}
    except Exception as e:
        return {"message": "Could not connect to PudSub. Error: " + str(e)}


@app.get("/launch_function_b")
async def launch_function_b():
    print("Launch Function B Invoked!")
    try:
        publisher = pubsub_v1.PublisherClient()
        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id='collaboration',  # os.getenv('GOOGLE_CLOUD_PROJECT'),
            topic='FUNCTION_B',  # Set this to something appropriate.
        )
        # publisher.create_topic(name=topic_name)
        future = publisher.publish(topic_name, b'{ "caller": "launch_function_b" }')
        future.result()
        return {"message": f"Connected to PubSub. Published message to FUNCTION_B."}
    except Exception as e:
        return {"message": "Could not connect to PudSub. Error: " + str(e)}
