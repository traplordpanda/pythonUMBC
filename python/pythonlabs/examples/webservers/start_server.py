#!/usr/bin/env python3
from server import configure_server, display_server_info


def main():
    try:
        server = configure_server()
    except Exception as e:
        print("Unable to start server:", e)
        return
    try:
        display_server_info(server.server_port)
        server.serve_forever()
    except (Exception, KeyboardInterrupt) as e:
        print("\n", "Exception:", e, "Shutting Down Server", sep="\n")
        server.shutdown()


if __name__ == "__main__":
    main()
