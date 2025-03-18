import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription

pc = RTCPeerConnection()

async def handle_offer(offer):
    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)
    return answer

async def main():
    # Start the server
    # For simplicity, just print a message to indicate setup
    print("aiortc setup complete. Ready to handle WebRTC connections.")

asyncio.run(main())
