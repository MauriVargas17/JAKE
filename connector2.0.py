import socket
import subprocess
import process_input from inference.py

def receive_data(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost', port))
        server_socket.listen()

        print(f"Waiting for connection on port {port}...")
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        with conn:
            while True:
                data = conn.recv(1024)                


                if not data:
                    break
                print(f":3 {data.decode('utf-8')}")
                # Emulate the command: echo 'data' | ./piper/piper --model ... --output_f>
                process_echo = subprocess.Popen(
                    ['echo', '-n', process_input(data.decode('utf-8'))],
                    stdout=subprocess.PIPE,
                    text=True
                )

                process_piper = subprocess.Popen(
                    ['./piper/piper', '--model', 'en-us-amy-low.onnx', '--output_file', 'welcome.wav'],
                    stdin=process_echo.stdout,
                    stdout=subprocess.PIPE,
                    text=True
                )

                # Print the output of the piper process (for demonstration purposes)
                output_piper = process_piper.communicate()[0]
                print(output_piper)

                # Play the generated 'welcome.wav' file using paplay
                subprocess.run(['paplay', 'welcome.wav'])

if __name__ == "__main__":
    receive_data(12346)  # Use the port you choose for communication