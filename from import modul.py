from modul import kecepatan

def main():
	waktu = 20
	jarak = 120
	
	kec = kecepatan(jarak, waktu)
	
	print("KECEPATAN")
	print("Jarak\t: ", jarak)
	print("Waktu\t: ", waktu)
	print("Hasil\t: ", jarak / waktu)

if __name__ == "__main__":
	main()
