import random
import socket
import subprocess
from inference import process_input
from datetime import datetime, timedelta

def receive_data(port):
    is_receiving = False
    jake_detection_time = None
    speaking_start_time = None
    response = ""

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
                decoded_data = data.decode('utf-8')
                #print(f"Received data: {decoded_data}")

                if "jake" in decoded_data.lower():
                    jake_detection_time = datetime.now()
                    print(f"Jake detected at: {jake_detection_time}")
                    respond_to_call()
                    continue

                if is_receiving:
                    response += decoded_data if decoded_data != "[BLANK_AUDIO]" or decoded_data != "[ Silence ]" else " "
                    print(f"Received: {decoded_data}")
                    print(f"Response SO FAR: {response}")

                if jake_detection_time is not None:
                    elapsed_time = datetime.now() - jake_detection_time
                    if elapsed_time >= timedelta(seconds=2):
                        is_receiving = True
                        print("Just started receiving...")
                        speaking_start_time = datetime.now()
                        jake_detection_time = None
                    else:
                        print("Not receiving yet...")
                        continue

                if speaking_start_time is not None:
                    speaking_time_elapsed = datetime.now() - speaking_start_time
                    if speaking_time_elapsed <= timedelta(seconds=10):
                        continue
                    else:
                        is_receiving = False
                        speaking_start_time = None
                        print("No more receiving. Final response is:", response)
                        response = process_input(response)
                        play_response_audio(response)
                        response = ""

                # if not is_receiving and response != "":
                #     print(f"Message caught is: {response}")
                #     play_response_audio(response)
                #     response = ""

def respond_to_call():
    greetings = ['g1.wav', 'g2.wav', 'g3.wav', 'g4.wav']
    subprocess.run(['paplay', greetings[random.randint(0, len(greetings) - 1)]])

def play_response_audio(response):
    print(f"Building audio for response: {response}")
    process_echo = subprocess.Popen(
        ['echo', '-n', response],
        stdout=subprocess.PIPE,
        text=True
    )
    if 
    process_piper = subprocess.Popen(
        ['./piper/piper', '--model', 'en-us-amy-low.onnx', '--output_file', 'welcome.wav'],
        stdin=process_echo.stdout,
        stdout=subprocess.PIPE,
        text=True
    )
    output_piper = process_piper.communicate()[0]
    print(output_piper)
    subprocess.run(['paplay', 'welcome.wav'])

if __name__ == "__main__":
    receive_data(12346)  # Use the port you choose for communication
