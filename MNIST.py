import struct


def read(fn, size):
	# meeded >I for endianness for my computer
	if size == 4:
		return struct.unpack('>I', fn.read(size))[0]
	else:
		my_int = struct.unpack('>H', b'\x00' + fn.read(1))[0]
		return my_int

def load_labels(fn):
	f = open(fn, "rb")
	labels = []
	magic_number = read(f, 4) 
	num_labels = read(f, 4)
	for i in range(0, num_labels):
		labels.append(read(f, 1))
	return labels

def load_features(fn):
	f = open(fn, "rb")
	features = []
	magic_number = read(f, 4)
	num_images = read(f, 4)
	for i in range(0, num_images):
		feature = []
		for j in range(0, 255):
			feature.append(read(f,1))
		features.append(feature)
	return features

def print_formatted_data(features,labels,label1, label2):
	if not(len(features) == len(labels)):
		print "Something went wrong"
		return
	wstar = [0] * 255
	wstarconfig = "//w* is " + str(wstar)
	wstarconfig = wstarconfig.replace("\n", "")
	wstarconfig = wstarconfig.replace(",", "")
	print wstarconfig
	for i in range(0, len(features)):
		data = ""
		label = labels[i]
		if not(label == label1 or label == label2):
			continue
		feature = features[i]
		for f in feature:
			data += str(f/255.0) + " "
		if label == label1:
			data += str(-1)
		if label == label2:
			data += str(1)
		print data
def main():
	labels = load_labels("train-labels-idx1-ubyte")
	features = load_features("train-images-idx3-ubyte")
	print_formatted_data(features, labels, 1, 8)

main()