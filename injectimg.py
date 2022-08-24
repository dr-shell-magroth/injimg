import getopt
import sys

input_user= ''
data_input = ''


def usge():
    print("[*] injectimg is a tool for hiddin data in img")

usge()

def main():
    global input_user
    global data_input

    try:
        opt , arg = getopt.getopt(sys.argv[1:],'h:i:d',['help','input','data'])
    except:
        print('error! in argement!!!')

    for o , a in opt:
        if o in ('-h','--help'):
            usge()
        elif o in ('-i','--input'):
            input_user = a
        elif o in ('-d','--data'):
            data_input = a
        else:
            print("un none command or error argement")

    appendData(input_user,data_input)

    read_file_byte(input_user)


def appendData(inputx , data: str):
    global input_user
    global data_input

    with open(inputx,'ab') as jpg:
        bdata = data.encode
        jpg.write(bdata)
        

def read_file_byte(file):
    global input_user
    global data_input

    with open(file, 'rb') as jpg:
        f = jpg.read()
        print(f)

main()