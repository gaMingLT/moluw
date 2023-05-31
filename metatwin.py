import argparse, os
# import pefile
# import sigvalidator

def extract_resources(rsc_hckr: str, src_bin:str, rsc_name: str):
    print("=== Extracting resources === ")
 
    cmd = "xvfb-run wine {0} -open ./{1} -action extract -mask ,,, -save ./{2}.res -log ./{2}.log".format(rsc_hckr, src_bin,rsc_name)

    res = os.system(cmd)

    if (res != 0):
       print("Resource extraction unsuccessful!")
       exit(1)

    # Check log file exists and for "failed" word
    if os.path.exists("./{}.log".format(rsc_name)):
        log_file = open("./{}.log".format(rsc_name), "r")
        data = log_file.read()

        if 'Failed' in data:
            print('Unable to extract resources from source binary')
            exit(1)

    else:
        print("No log file found!")
        exit(1)


def write_resources(rsc_hckr: str, rsc_name: str, trg_bin: str):
    print("=== Writing resources ===")

    cmd = "xvfb-run wine {0} -open ./{1}, -save './executable_written.exe' -resource {2}.res -action addoverwrite".format(rsc_hckr, trg_bin,rsc_name)

    res = os.system(cmd)

    if (res != 0):
       print("Resource writing unsuccessful!")
       exit(1) 


def sign_binary(src_bin: str, trg_bin: str):
    print("=== Signing binary === ")

    sigh_thief_src = './sigthief.py'

    cmd = "python3 {0} -i ./{1} -t './executable_written.exe' -o ./{2}_signed".format(sigh_thief_src, src_bin, trg_bin)

    res = os.system(cmd)

    if (res != 0):
       print("Signing unsuccessful!")
       exit(1) 

# TODO: Add extract signature information feature
# def extract_signature_information(src_bin: str, trg_bin: str):
#     print("=== Extracting signature information ===")

#     sigv = sigvalidator.SigValidator()

#     for path in [trg_bin]:
#         pe = pefile.PE(path, fast_load=True)
#         result = sigv.verify_pe(pe)
#         print("{0}: {1}".format(path, result))



def metatwin(args):
    rsc_hckr = "./ResourceHacker.exe "

    src_bin = args.source
    trg_bin = args.target

    print(
    """  
     __  __           _               __          __ 
    |  \/  |         | |              \ \        / /
    | \  / |   ___   | |       _   _   \ \  /\  / / 
    | |\/| |  / _ \  | |      | | | |   \ \/  \/ /  
    | |  | | | (_) | | |____  | |_| |    \  /\  /   
    |_|  |_|  \___/  |______|  \__,_|     \/  \/ 
    """)

    # Program settings
    print("[x] - Extracting and writings resources")
    if args.sign:
       print("[x] - Extracting and writings signature")
    else:
      print("[-] - Extracting and writings signature")  

    rsc_name = "exRscBin"

    # Extract resources
    extract_resources(rsc_hckr=rsc_hckr, src_bin=src_bin, rsc_name=rsc_name)

    # Write resources to target binary
    write_resources(rsc_hckr=rsc_hckr, rsc_name=rsc_name, trg_bin=trg_bin)

    # Sign
    if (args.sign):
        sign_binary(src_bin=src_bin, trg_bin=trg_bin)
        # extract_signature_information(src_bin=src_bin, trg_bin=trg_bin)

    print("=== Script finished! ===")

def main():
    parser = argparse.ArgumentParser(
                    prog='Metatwin Linux',
                    description='',
                    epilog='')
    
    parser.add_argument('-s', '--source', type=str, help='Source (binary) of where to extract resources and signature from.', required=True)
    parser.add_argument('-t', '--target', type=str, help='Target of where to copy resources and signature to.', required=True)
    parser.add_argument('-si', '--sign', action='store_true', help='Sign the target binary.')

    args = parser.parse_args()
    metatwin(args=args)

if __name__ == "__main__":
    main()
