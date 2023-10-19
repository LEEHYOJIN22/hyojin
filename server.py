import cv2
import socket
import threading
from UI import VideoChatUI
import tkinter as tk

class VideoChatServer:
    def __init__(self):
        self.ui = VideoChatUI(tk.Tk(), "화상 채팅 서버")
        self.ui.on_send_message = self.send_message_to_clients
        self.clients = []
#웹캠초기화
        self.cap = cv2.VideoCapture(0)
#소켓초기화
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 2323))
        self.server_socket.listen(5)
#웹캠영상전송스레드시작
        self.webcam_thread = threading.Thread(target=self.send_webcam)
        self.webcam_thread.daemon = True
        self.webcam_thread.start()
#클라이언트연결을처리하는스레드시작
        self.receive_thread = threading.Thread(target=self.receive_clients)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        tk.mainloop()

    def show_frame(self, frame):
        self.ui.show_frame(frame)
