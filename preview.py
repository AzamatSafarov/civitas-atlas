from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
import os
os.chdir(Path(__file__).parent/'portal')
print('Contribution portal: http://127.0.0.1:8850',flush=True)
ThreadingHTTPServer(('127.0.0.1',8850),SimpleHTTPRequestHandler).serve_forever()
