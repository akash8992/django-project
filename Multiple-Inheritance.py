class A:
    def speak(self):
        print("A speaks.")

class B(A):
    def speak(self):
        print("B speaks.")

class C(B):
    def speak(self):
        print("C speaks.")

obj = C()
obj.speak()
