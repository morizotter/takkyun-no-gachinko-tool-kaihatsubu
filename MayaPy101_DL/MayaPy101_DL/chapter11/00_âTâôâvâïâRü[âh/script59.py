class A(object):
    def output(self):
        print 'A'

class B(object):
    def output(self):
        print 'B'

class C(A, B):
    pass

obj = C()
obj.output()
# >> A
