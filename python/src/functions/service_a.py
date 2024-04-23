import httpx as httpx


def service_a():
    base_path = 'http://localhost:8000'  # whatever the cloud URL is
    print("Service A Invoked!")
    response = httpx.get(base_path + '/launch_function_b')
    print(response.content)


if __name__ == '__main__':
    service_a()
