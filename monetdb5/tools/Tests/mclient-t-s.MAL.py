import os, sys
try:
    from MonetDBtesting import process
except ImportError:
    import process

def client(args):
    clt = process.client('mal', args = args,
                         stdout = process.PIPE, stderr = process.PIPE)
    out, err = clt.communicate()
    sys.stderr.write(err)

client(['-s', 'io.print(123);'])
