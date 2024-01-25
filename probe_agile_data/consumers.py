# # fema/consumers.py

# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async
# from .models import city

# class CityConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def city_data(self, event):
#         data = event["data"]
#         await self.send(text_data=json.dumps({"data": data}))

# @sync_to_async
# def get_city_data():
#     # Fetch data from the database
#     cities = city.objects.all().values()
#     return list(cities)
