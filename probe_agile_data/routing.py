# # routing.py

# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from probe_agile_data.consumers import CityConsumer

# application = ProtocolTypeRouter({
#     "websocket": URLRouter(
#         [
#             path("ws/city/", CityConsumer.as_asgi()),
#         ]
#     ),
# })
