import wave
import struct
import socket
import time
import websocket
import threading
import json
import ssl
from random import randint
from time import sleep

def threadRecv(ws, asr, utt, err):
	while 1:
		data = ws.recv()
		data = json.loads(data)
		if (data["cmd"] == "asrfull"):
			asr.append(data)
			break
		elif (data["cmd"] == "err"):
			err.append(data["msg"])
			break

def HLTASRStreamVAD(url, wavFile, utt):
	asr = []
	while 1:
		ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
		ws.connect(url)

		asr = []
		err = []

		recvThread = threading.Thread(target=threadRecv, args=(ws, asr, utt, err))
		recvThread.start()

		msgVADStart = bytearray(10);
		x = utt.to_bytes(8, byteorder='big', signed=False);
		for i in range(0, 8):
			msgVADStart[i + 2] = x[i]
		ws.send_binary(msgVADStart)

		obj = wave.open(wavFile, 'r')

		while 1:
			audio = obj.readframes(1024);
			if (len(audio) == 0):
				break
			channelSamples = int(len(audio) / 2)
			audio = struct.unpack(str(channelSamples) + 'H', audio)

			buf = []
			buf = struct.pack('!b' + str(channelSamples) + 'H', 2, *audio)
			ws.send(buf)
		obj.close()

		msgVADEnd = bytearray(1);
		msgVADEnd[0] = 1;
		ws.send_binary(msgVADEnd)

		recvThread.join()
		ws.close()

		if (len(err) == 0):
			break
		else:
			print(err[0])
			sleep(randint(1, 3))

#	print(asr)
	return asr
