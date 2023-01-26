def bob_key(Ya,Xb,q):
	return Ya**Xb%q

def alice_key(Yb,Xa,q):
	return Yb**Xa%q
	
	
def main():
	q = int(input("Enter the prime number: "))
	alpha = int(input("Enter the generator: "))

	Xa = int(input("Enter Alice Secret Key: "))
	Xb = int(input("Enter Bob secret Key: "))

	Ya = alpha ** Xa % q
	Yb = alpha ** Xb % q

	print("Bob Common Key :", bob_key(Ya,Xb,q))
	print("Alice Common Key : ", alice_key(Yb,Xa,q))
	
main()