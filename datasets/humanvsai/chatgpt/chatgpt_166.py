def create_load_balancer_dict():
    load_balancer_dict = {
        "name": "my-load-balancer",
        "port": 80,
        "protocol": "http",
        "algorithm": "round_robin",
        "health_check": {
            "protocol": "http",
            "port": 80,
            "path": "/health",
            "interval": 30,
            "timeout": 5,
            "healthy_threshold": 3,
            "unhealthy_threshold": 5
        },
        "instances": [
            {
                "id": "i-04438fb7f11f9f6d7",
                "ip_address": "10.0.0.1"
            },
            {
                "id": "i-0a9fbb8d7c7995f5e",
                "ip_address": "10.0.0.2"
            }
        ]
    }
    return load_balancer_dict
