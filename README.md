## llama2.c

First, clone and open the repository folder:

```bash
git clone https://github.com/karpathy/llama2.c.git
cd llama2.c
```




## Huggingface LLAMA-2

We can load any huggingface models that use the Llama 2 architecture. See the script [export.py](export.py) and the `--hf` flag to export the model .bin file.

```bash
python export.py llama2_7b.bin --hf path/to/llama/model/7B
```

The export will take ~10 minutes or so and generate a 26GB file (the weights of the 7B model in float32) called `llama2_7b.bin` in the current directory. It has been [reported](https://github.com/karpathy/llama2.c/pull/85) that despite efforts. I would not attempt to run anything above 7B right now for two reasons: first, 13B+ currently doesn't work because of integer flow in pointer arithmetic, which is yet to be fixed, and second, even if it were fixed, this repo is doing float32 inference right now, so it would be fairly unusably slow. Once the export is done, we can run it:

```bash
make run
./run llama2_7b.bin
```

Multi-thread acceleration
```bash
make runomp
OMP_NUM_THREADS=32 ./run llama2_7b.bin
```