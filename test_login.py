import asyncio
import httpx
import subprocess
import time

async def main():
    # Start server
    server = subprocess.Popen(["uvicorn", "backend.main:app", "--port", "8000"])
    time.sleep(3) # wait for server to start

    try:
        async with httpx.AsyncClient() as client:
            # 1. Register a new user
            query = """
            mutation {
                register(username: "testuser1234", password: "password123", role: "PM") {
                    token
                }
            }
            """
            print("Registering...")
            res = await client.post("http://localhost:8000/graphql", json={"query": query})
            print("Register:", res.json())

            # 2. Login as the new user
            query2 = """
            mutation {
                login(username: "testuser1234", password: "password123") {
                    token
                }
            }
            """
            print("Logging in new user...")
            res = await client.post("http://localhost:8000/graphql", json={"query": query2})
            print("Login new:", res.json())

            # 3. Try logging into an existing user? 
            # We don't know the exact username, but wait, the bug said "I cannot login to the id I created yesterday"
            # Maybe the database has an older user?
            
    finally:
        server.terminate()
        server.wait()

if __name__ == "__main__":
    asyncio.run(main())
