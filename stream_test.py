import asyncio
import json
import websockets

async def main():
    # Target the exposed server container WebSocket port and path
    uri = "ws://127.0.0.1:3001/ws/sensing"
    print(f"Connecting to RuView WebSocket: {uri}...")
    
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected successfully to RuView Streaming Core!")
            
            while True:
                message = await websocket.recv()
                data = json.loads(message)
                
                presence = data.get("presence_detected", False)
                count = data.get("person_count", 0)
                
                vitals = data.get("vitals", {})
                breathing = vitals.get("breathing_bpm", 0.0)
                
                print(f"Room Presence: {presence} | "
                      f"Estimated Count: {count} | "
                      f"Breathing Rate: {breathing:.1f} BPM")
                      
    except Exception as e:
        print(f"Connection dropped or failed to bind: {e}")

if __name__ == "__main__":
    asyncio.run(main())
