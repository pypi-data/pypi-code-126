import pathlib
from .cofan import *
import re
import sys
import argparse
from .utils.misc import tree_patterner
from .utils.tfman import TFMan

parser = argparse.ArgumentParser(description='Serve files over http.')
parser.add_argument(
  '-a', '--addr', type=str, action='store', default='localhost:8000',
  help='http bind address in the form <ip>:<port>'
)
parser.add_argument(
  '-u', '--upload_password', action='store', default='',
  help='upload password. defaults to empty string which disables uploads'
)
parser.add_argument(
        'root', action='store', nargs='?', default='.',
        help='root directory to serve through http'
    )


args = parser.parse_args()

addr = args.addr.split(':')
addr[1] = int(addr[1])
root = args.root
upload_password = args.upload_password

main_tree = pathlib.Path(__file__).parent / 'main_tree'
env = {'root': root}
env['upload_password'] = upload_password
env['tfman'] = TFMan

localhost_checker = IPPatterner()
localhost_checker.add(re.compile(r'localhost|127.0.0.1'),
  tree_patterner(main_tree / 'localhost_tree', env))
localhost_checker.add(re.compile(r'.*'),
  tree_patterner(main_tree / 'others_tree', env))

handler = BaseHandler(localhost_checker)

srv = Server(tuple(addr), handler)
print('serving {} at {}:{}'.format(pathlib.Path(root).resolve(), *addr))
if addr[0] in ['', '0.0.0.0']:
    try:
        import netifaces
    except ImportError:
        pass
    else:
        ifaces = netifaces.interfaces()
        addrs = [netifaces.ifaddresses(c) for c in ifaces]
        family_addrs = []
        for c in addrs:
            if srv.address_family.value in c:
                family_addrs.extend(c[srv.address_family.value])
        final_addrs = [c['addr'] for c in family_addrs]
        
        print('serving at the following addresses:')
        for c in final_addrs:
            print(c)

try:
    srv.serve_forever()
except KeyboardInterrupt:
    pass

