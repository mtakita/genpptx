
import os

def handle_uploaded_file(f):

	f.seek(0, os.SEEK_SET)
	byteArray = bytearray()

	byte = f.read(1)
	while byte:
		byteArray+=byte
		byte = f.read(1)

	return byteArray

