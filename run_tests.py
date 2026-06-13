import sys, runpy, os
root = os.path.abspath(os.path.dirname(__file__))
if root not in sys.path:
    sys.path.insert(0, root)
runpy.run_path(os.path.join('Scripts', 'test_body_type.py'), run_name='__main__')
print('runner finished')
