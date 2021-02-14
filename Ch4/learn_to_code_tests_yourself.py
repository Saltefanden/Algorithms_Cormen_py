class Test():

    def test(func):
        def inner():
                try:
                    func()
                except Exception as ex:
                    print(ex.args[0])
                    print(*ex.args, 'at') 
                else:
                    print("Code executed with return value 0")
        return inner
    

    @test
    def tstfun():
        assert 5+8 == 13, "Dillermand"
        assert 3+2 == 5, "Dollermand"
        assert myList([1,4,2,1]).insertion_sort() == [1,1,2,4,1]



class myList(list):
    def __init__(self, the_list):
        super().__init__(the_list)
    
    def insertion_sort(self, reverse = False):
        for i in range(1,len(self)):
            key = self[i]
            j = i-1
            if not reverse:
                while j>=0 and self[j]>key:
                    self[j+1] = self[j]
                    j -= 1
            else:
                while j>=0 and self[j]<key:
                    self[j+1] = self[j]
                    j -= 1
            self[j+1] = key
        return self



def main():
    Test.tstfun() 


if __name__ == '__main__':
    main()