class A:
  a=10
  def disp(self):
    print('disp in A')
class B(A):
  b=20
  def disp(self):
    print('disp in B')
ob=B()
super(B,ob).disp()
