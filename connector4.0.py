import socket
import subprocess
from cooking_pal import process_input

def receive_data(port):
    data_decoded = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost', port))
        server_socket.listen()

        print(f"Waiting for connection on port {port}...")
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        with conn:
            while True:
                data = conn.recv(512)


                if not data:
                    break
                d = data.decode('utf-8').strip()
                print(f"R:{d}")
                if not d.endswith("]"):
                    print(f"---concatenating---")
                    data_decoded += " " + d
                    continue
                else:
                    print("---new---")
                    if "jake" in data_decoded.lower() or "drake" in data_decoded.lower():
                        print(f"D:{data_decoded}")

                        # Emulate the command: echo 'data' | ./piper/piper --model ... --output_f>
                        response = process_input(data_decoded) 
                        process_echo = subprocess.Popen(
                            ['echo', '-n', response],
                            stdout=subprocess.PIPE,
                            text=True
                        )
                        if response == '':
                            continue
                        process_piper = subprocess.Popen(
                            ['./piper/piper', '--model', 'en-us-amy-low.onnx', '--output_file', 'welcome.wav'],
                            stdin=process_echo.stdout,
                            stdout=subprocess.PIPE,
                            text=True
                        )

                        # Print the output of the piper process (for demonstration purposes)
                        output_piper = process_piper.communicate()[0]
                        print(output_piper)

                        subprocess.run(['paplay', 'welcome.wav'])
                        
                    data_decoded = ""
                    
                
                

if __name__ == "__main__":
    receive_data(12345) 