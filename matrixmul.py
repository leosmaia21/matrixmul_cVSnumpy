import numpy as np
import time

N = 2048
def main():
    A = np.random.randn(N, N).astype(np.float32)
    B = np.random.randn(N, N).astype(np.float32)

    flop = N*N*2*N
    print(f"{flop / 1e9:.2f} GFLOP")
    start = time.monotonic()
    C = A @ B
    end = time.monotonic()
    t = end - start
    print(f"{flop/t * 1e-9:.2f} GFLOPS")


    with open("/tmp/matmul", "wb") as f:
        f.write(A.data)
        f.write(B.data)
        f.write(C.data)


if __name__ == "__main__":
    main()
