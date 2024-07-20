import time
import random

def sender(packets):
    for frame_to_send in range(packets):
        print("Sender: Sending frame", frame_to_send)
        ack_received = receiver(frame_to_send)
        if ack_received:
            print("Sender: Acknowledgment received for frame", frame_to_send)
        else:
            print("Sender: Timeout occurred for frame", frame_to_send)
        time.sleep(0.0001)  # Simulating transmission time

def receiver(expected_frame):
    # Simulating transmission errors (frame loss)
    if random.random() < 0.2:  # 20% chance of frame loss
        print("Receiver: Frame", expected_frame, "lost")
        return False
    
    # Simulating ACK loss
    if random.random() < 0.2:  # 20% chance of ACK loss
        print("Receiver: ACK for frame", expected_frame, "lost")
        return False
    
    # Simulating ACK delay
    time.sleep(random.uniform(0.02))  # Random ACK delay
    
    # Simulating successful reception
    print("Receiver: Received frame", expected_frame)
    return True

# Start sender with 10 packets
packets = 10
sender(packets)
