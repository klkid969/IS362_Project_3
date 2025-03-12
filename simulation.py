import sys
import csv
import queue

class Request:
    def __init__(self, arrival_time, file_requested, processing_time):
        self.arrival_time = int(arrival_time)
        self.file_requested = file_requested
        self.processing_time = int(processing_time)
        self.start_time = None  # Time when the request starts being processed
        self.finish_time = None # Time when the request finishes being processed.

class Server:
    def __init__(self):
        self.queue = queue.Queue()
        self.current_request = None
        self.time_remaining = 0

    def is_busy(self):
        return self.current_request is not None

    def start_next(self, current_time):
        if not self.queue.empty():
            self.current_request = self.queue.get()
            self.time_remaining = self.current_request.processing_time
            self.current_request.start_time = current_time

    def tick(self):
        if self.current_request is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_request.finish_time = self.current_request.start_time + self.current_request.processing_time
                self.current_request = None

def simulateOneServer(filename):
    requests =
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            requests.append(Request(*row))

    server = Server()
    current_time = 0
    request_index = 0
    wait_times =

    while request_index < len(requests) or server.is_busy() or not server.queue.empty():
        # Add incoming requests
        while request_index < len(requests) and requests[request_index].arrival_time == current_time:
            server.queue.put(requests[request_index])
            request_index += 1

        # Start processing the next request
        if not server.is_busy():
            server.start_next(current_time)

        # Process the current request
        server.tick()

        # Calculate wait times
        if server.current_request and server.current_request.finish_time:
            wait_times.append(server.current_request.finish_time - server.current_request.arrival_time - server.current_request.processing_time)

        current_time += 1

    if wait_times:
        average_wait_time = sum(wait_times) / len(wait_times)
        return average_wait_time
    else:
        return 0

def simulateManyServers(filename, num_servers):
    requests =
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            requests.append(Request(*row))

    servers = [Server() for _ in range(num_servers)]
    current_time = 0
    request_index = 0
    wait_times =
    server_index = 0

    while request_index < len(requests) or any(server.is_busy() or not server.queue.empty() for server in servers):
        # Add incoming requests
        while request_index < len(requests) and requests[request_index].arrival_time == current_time:
            servers[server_index].queue.put(requests[request_index])
            server_index = (server_index + 1) % num_servers
            request_index += 1

        # Start processing the next request
        for server in servers:
            if not server.is_busy():
                server.start_next(current_time)

        # Process the current request
        for server in servers:
            server.tick()

        # Calculate wait times
        for server in servers:
            if server.current_request and server.current_request.finish_time:
                wait_times.append(server.current_request.finish_time - server.current_request.arrival_time - server.current_request.processing_time)

        current_time += 1

    if wait_times:
        average_wait_time = sum(wait_times) / len(wait_times)
        return average_wait_time
    else:
        return 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python simulation.py <filename> [<servers>]")
        sys.exit(1)
    filename = sys.argv[1]
    servers = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    if servers == 1:
        average_wait_time = simulateOneServer(filename)
        print(f"Average wait time for one server: {average_wait_time}")
    else:
        average_wait_time = simulateManyServers(filename, servers)
        print(f"Average wait time for {servers} servers: {average_wait_time}")

if __name__ == "__main__":
    main()