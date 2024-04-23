from fastapi import FastAPI

app = FastAPI()


@app.get("/connect_gcs")
async def connect_gcs():
    try:
        from google.cloud import storage
        storage_client = storage.Client()
        buckets = list(storage_client.list_buckets())
        return {"message": f"Connected to GCS. Found {len(buckets)} buckets."}
    except Exception as e:
        print(e)
        return {"message": "Could not connect to GCS. Error: " + str(e)}


@app.get("/connect_hazelcast")
async def connect_hazelcast():
    try:
        from hazelcast import HazelcastClient
        client = HazelcastClient(
            # cluster_name='cognetto-local',
            cluster_members=["127.0.0.1:8080"],  #, "172.17.0.3:5701"],
            lifecycle_listeners=[lambda state: print("Cache lifecycle event >>>", state)]
        )
        return {"message": f"Connected to Hazelcast. Cluster ID: {client.cluster.id}"}
    except Exception as e:
        return {"message": "Could not connect to Hazelcast. Error: " + str(e)}
