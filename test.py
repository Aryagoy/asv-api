import requests
import uuid

msg={'sender':'imu_serial', 'msg_type': 'asvprotobuf.sensor_pb2.Imu', 'receiver': 'imu_parser', 'freq': 20.003}
a=requests.post('http://localhost:8000/api/',json=msg)

print(a.json())
