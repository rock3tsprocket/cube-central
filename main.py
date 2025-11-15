from dotenv import load_dotenv
from os import getenv
from aiohttp import web, ClientSession
from datetime import datetime

load_dotenv()
webhook = getenv("webhook")
port = int(getenv("port"))
bindip = getenv("bindip")

async def alert(request):
    alert = getenv("alert")
    return web.Response(text=alert)

async def ping(request):
    ping_payload = await request.json()
    timestamp = datetime.now().isoformat()
    async with ClientSession() as session:
        async with session.post(webhook, json={
        "embeds": [
          {
            "title": "A bot has started up",
            "color": "7896063",
            "fields": [
              {
                "name": "Name",
                "value": ping_payload["name"],
                "inline": "true"
              },
              {
                "name": "Timestamp",
                "value": timestamp,
                "inline": "true"
              },
              {
                "name": "Slash Commands",
                "value": ping_payload["slash_commands"]
              },
              {
                "name": "Memory File Info",
                "value": f"File size: {ping_payload["memory_file_info"]["file_size_bytes"]}\nLine count: {ping_payload["memory_file_info"]["line_count"]}"
              }
            ],
             "footer": {
              "text": "Cube Central Alive Pings"
            }
          }
        ]
        }) as response:
            pass

    return web.json_response({"message": "Ping received successfully", "timestamp": timestamp})
    

app = web.Application()
app.add_routes([web.get('/alert', alert)])
app.add_routes([web.post('/ping', ping)])
app.add_routes([web.static('/', 'static')])
if __name__ == '__main__':
    web.run_app(app, host=bindip, port=port)
