import syamsir.modul

def main():
	kecepatan = 30
	jarak = 120

	waktu = syamsir.modul.waktu(jarak, kecepatan)

	print("WAKTU")
	print("Jarak\t: ", jarak)
	print("Kecepatan\t: ", kecepatan)
	print("Hasil\t: ", jarak * kecepatan)
	
if __name__ == "__main__":
	main()
