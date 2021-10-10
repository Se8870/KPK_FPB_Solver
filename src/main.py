from math import GCF, LCM

def main():
	factor = []

	try:
		factor.append(int(input("Please input first number: ")))
		factor.append(int(input("Please input second number: ")))
	except:
		print("Invalid input.")
		exit()

	while True:
		try:
			ret = int(input("Please input extra number (if available): "))
		except:
			ret = 0
			
		if ret == 0:
			break
		else:
			factor.append(ret)

	result_fpb = GCF (*factor)
	result_kpk = LCM (*factor)

	print(f"Result from {factor} is:\nGCF: {result_fpb}\nLCM: {result_kpk}")


if __name__ == "__main__":
	main()
