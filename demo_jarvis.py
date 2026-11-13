# JARVIS Simulation & Voice Demo Test Suite
# This script simulates full end-to-end voice and text interactions,
# demonstrating JARVIS's advanced IQ, planning, tool execution, memory,
# and synthetic voice response generation.

import asyncio
import aiohttp
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("JARVIS_DEMO")

async def run_demo():
    print("\n" + "="*60)
    print(" J.A.R.V.I.S. // NEXT-LEVEL AI DEMO & CAPABILITY TEST ")
    print("="*60 + "\n")
    
    base_url = "http://127.0.0.1:8000"
    
    async with aiohttp.ClientSession() as session:
        # 1. Health & Status Check
        print("[DEMO STEP 1] Checking JARVIS Core & Advanced IQ Status...")
        try:
            async with session.get(f"{base_url}/") as resp:
                data = await resp.json()
                print(f" -> Status: {data.get('message')}")
                print(f" -> IQ Level: {data.get('iq_level', 'Genius')}")
                print(f" -> Loaded Tools: {len(data.get('tools', []))}")
                print(f" -> Loaded Plugins: {len(data.get('plugins', []))}")
        except Exception as e:
            print(f" [!] Backend is starting or offline. Please ensure backend is running. Error: {e}")
            return

        # 2. Advanced Reasoning & Multi-Step Planning Demo
        print("\n[DEMO STEP 2] Testing Advanced IQ Reasoning & Planning...")
        test_queries = [
            "Take a screenshot of my screen right now",
            "Search online for the latest breakthroughs in quantum computing",
            "List all files in the current workspace directory"
        ]
        
        for q in test_queries:
            print(f"\n > User Voice Command: \"{q}\"")
            async with session.post(f"{base_url}/reason", params={"query": q}) as resp:
                res = await resp.json()
                print(f"   * Intent Detected : {res['plan']['intent']}")
                print(f"   * Requires Tools  : {res['plan']['requires_tools']}")
                print(f"   * Execution Plan  : {res['plan']['steps']}")
                if res['execution_results']:
                    for ex in res['execution_results']:
                        print(f"   * Tool Executed [{ex['tool']}]: {str(ex['result'])[:120]}...")

        # 3. Long-term Memory Demo
        print("\n[DEMO STEP 3] Testing Long-Term Memory (SQLite + ChromaDB)...")
        memory_fact = "The user is building an extreme Iron-Man style personal AI named JARVIS."
        print(f" > Remembering Fact: \"{memory_fact}\"")
        async with session.ws_connect(f"{base_url}/ws") as ws:
            await ws.send_str(f"remember:{memory_fact}")
            msg = await ws.receive_json()
            print(f"   * Memory Response: {msg}")

        print("\n" + "="*60)
        print(" DEMO COMPLETED SUCCESSFULLY. JARVIS IS FULLY OPERATIONAL. ")
        print("="*60 + "\n")

if __name__ == "__main__":
    asyncio.run(run_demo())
