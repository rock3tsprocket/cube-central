from aiohttp import web
from datetime import datetime

async def alert(request):
    alert = "sample text"
    return web.Response(text=alert)

async def ping(request):
    ping_payload = await request.json())
    #TODO: webhook
    return web.json_response({"message": "Ping received successfully", "timestamp": datetime.now().isoformat()})
    

app = web.Application()
app.add_routes([web.get('/alert', alert)])
app.add_routes([web.post('/ping', ping)])

if __name__ == '__main__':
    web.run_app(app)
