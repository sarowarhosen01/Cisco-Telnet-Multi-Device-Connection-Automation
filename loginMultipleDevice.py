import asyncio
import telnetlib3

host_ip_address = [
    "192.168.10.11",
    "192.168.10.12",
    "192.168.10.13",
    "192.168.10.14"
]

USERNAME = "admin"
PASSWORD = "cisco123"

async def main(host, USERNAME, PASSWORD):
    reader, writer = await telnetlib3.open_connection(host, 23)
    try:
        # Send username
        writer.write(USERNAME + "\n")
        await writer.drain()
        await asyncio.sleep(1)
        
        # Send password
        writer.write(PASSWORD + "\n")
        await writer.drain()
        await asyncio.sleep(1)
        
        # Send enable command
        writer.write("enable\n")
        await writer.drain()
        await asyncio.sleep(1)
        
        # Send enable password
        writer.write("cisco123\n")
        await writer.drain()
        await asyncio.sleep(1)
        
        # Send show version command
        writer.write("show version\n")
        await writer.drain()
        await asyncio.sleep(2)  # Give more time for command to execute
        
        # Send exit command
        writer.write("exit\n")
        await writer.drain()
        await asyncio.sleep(0.5)
        
        # Read output
        output = await reader.read()
        if output:
            print(f"\n=== Output from {host} ===")
            print(output)
            print("=" * 80)

    except asyncio.TimeoutError:
        print(f"Timeout waiting for device response from {host}")
    except ConnectionRefusedError:
        print(f"Connection refused from {host}. Is Telnet enabled?")
    except Exception as e:
        print(f"Error connecting to {host}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    for host in host_ip_address:
        asyncio.run(main(host, USERNAME, PASSWORD))
