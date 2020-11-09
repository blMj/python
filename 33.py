//Diamond shape problem in multiple inheritance
//diamond shape problem =means some programming language doesn't support multiple inheritance but python support inheritance. 
class A:
	pass
class B(A):
	pass
class C(A):
	pass
class D(B,C):
	pass
//here we can see we have inherit B to A ,C to A,D to B,C or C,A
//here when inherit D to B,C output will differ and C,A output will            differ
