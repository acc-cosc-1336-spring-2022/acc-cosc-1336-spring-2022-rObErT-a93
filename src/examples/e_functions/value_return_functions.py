def test_config():
    return True

def local_variable(val0):
    val = val0
    val0 = 100
    return val    

def main():
    val = 0 # example
    local_variable()

val3 = 10
def use_global():       # Global Variable
    val3 = 5
    print(val3)