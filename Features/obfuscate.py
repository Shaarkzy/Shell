#------------------------------------------------------------------------------------------------------------------------------

import sys, zlib, base64

#------------------------------------------------------------------------------------------------------------------------------

def obfuscator(file, output_file):
    src = open(file, "r", encoding="utf-8").read()
    blob = base64.b85encode(zlib.compress(src.encode("utf-8"), 9))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(
            "import zlib,base64\n"
            "exec(zlib.decompress(base64.b85decode(%r)))\n" % blob
        )

#------------------------------------------------------------------------------------------------------------------------------
#end line 17