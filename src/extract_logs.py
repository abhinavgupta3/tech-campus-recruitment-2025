import sys
import mmap
import os

def get_logs(d):
    print("Started...")

    in_file = 'path_to_log_file.log'
    out_dir = 'output'
    os.makedirs(out_dir, exist_ok=True)
    out_file = f'{out_dir}/out_{d}.txt'

    print(f"Searching for {d}...")

    try:
        with open(in_file, 'r') as f, open(out_file, 'w') as out:
            m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

            for line in iter(m.readline, b""):
                if line.startswith(d.encode()):
                    out.write(line.decode())

        print(f"Saved to {out_file}")

    except FileNotFoundError:
        print(f"File '{in_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "_main_":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    get_logs(sys.argv[1])