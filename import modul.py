import modul

def main():
	waktu = 20
	jarak = 120
	
	kecepatan = modul.kecepatan (jarak, waktu)
	
	print("KECEPATAN")
	print("Jarak\t: ", jarak)
	print("Waktu\t: ", waktu)
	print("Hasil\t: ", jarak / waktu)
	
	waktu = modul.waktu (jarak, kecepatan)

	print("WAKTU")
	print("Jarak\t: ", jarak)
	print("Kecepatan\t: ", kecepatan)
	print("Hasil\t: ", jarak * kecepatan)
	
	jarak = modul.jarak (waktu, kecepatan)
	
	print("JARAK")
	print("waktu\t: ", waktu)
	print("Kecepatan\t: ", kecepatan)
	print("Hasil\t: ", waktu / kecepatan)
	
if __name__ == "__main__":
	main()
