import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiohttp import web

# Create a peer connection
pc = RTCPeerConnection()

# Handle offer from client
async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params['sdp'], type=params['type'])
    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)
    return web.Response(
        content_type='application/json',
        text=json.dumps({'sdp': pc.localDescription.sdp, 'type': pc.localDescription.type})
    )

# Start the server
async def main():
    app = web.Application()
    app.router.add_post('/offer', offer)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    print("Server started at http://localhost:8080")

asyncio.run(main())
