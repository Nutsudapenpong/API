## Running the code

### Floking this project to your device

```
git clone 

```
### Running API

Here is an example code of running API, run

```
cd data
wget https://www.dropbox.com/s/avgm2u562itwpkl/Imagenet.tar.gz
tar -xvzf Imagenet.tar.gz
cd ..
```

### Downloading Neural Network Models

We provide download links of four pre-trained models.

* **[DenseNet-BC trained on CIFAR-10](https://www.dropbox.com/s/wr4kjintq1tmorr/densenet10.pth.tar.gz)**
* **[DenseNet-BC trained on CIFAR-100](https://www.dropbox.com/s/vxuv11jjg8bw2v9/densenet100.pth.tar.gz)**
* **[Wide ResNet trained on CIFAR-10](https://www.dropbox.com/s/uiye5nw0uj6ie53/wideresnet10.pth.tar.gz)**
* **[Wide ResNet trained on CIFAR-100](https://www.dropbox.com/s/uiye5nw0uj6ie53/wideresnet100.pth.tar.gz)**

Here is an example code of downloading DenseNet-BC trained on CIFAR-10. In the **root** directory, run

```
mkdir models
cd models
wget https://www.dropbox.com/s/wr4kjintq1tmorr/densenet10.pth.tar.gz
tar -xvzf densenet10.pth.tar.gz
cd ..
```


### Running

Here is an example code reproducing the results of DenseNet-BC trained on CIFAR-10 where TinyImageNet (crop) is the out-of-distribution dataset. The temperature is set as 1000, and perturbation magnitude is set as 0.0014. In the **root** directory, run

```
cd code
# model: DenseNet-BC, in-distribution: CIFAR-10, out-distribution: TinyImageNet (crop)
# magnitude: 0.0014, temperature 1000, gpu: 0
python main.py --nn densenet10 --out_dataset Imagenet --magnitude 0.0014 --temperature 1000 --gpu 0
```
**Note:** Please choose arguments according to the following.

#### args
* **args.nn**: the arguments of neural networks are shown as follows

	Nerual Network Models | args.nn
	----------------------|--------
	DenseNet-BC trained on CIFAR-10| densenet10
	DenseNet-BC trained on CIFAR-100| densenet100
* **args.out_dataset**: the arguments of out-of-distribution datasets are shown as follows

	Out-of-Distribution Datasets     | args.out_dataset
	------------------------------------|-----------------
	Tiny-ImageNet (crop)                | Imagenet
	Tiny-ImageNet (resize)              | Imagenet_resize
	LSUN (crop)                         | LSUN
	LSUN (resize)                       | LSUN_resize
	iSUN                                | iSUN
	Uniform random noise                | Uniform
	Gaussian random noise               | Gaussian

* **args.magnitude**: the optimal noise magnitude can be found below. In practice, the optimal choices of noise magnitude are model-specific and need to be tuned accordingly.

	Out-of-Distribution Datasets        |   densenet10     |  densenet100  | wideresnet10   | wideresnet100
	------------------------------------|------------------|-------------  | -------------- |--------------
	Tiny-ImageNet (crop)                | 0.0014           | 0.0014        | 0.0005           | 0.0028
	Tiny-ImageNet (resize)              | 0.0014           | 0.0028        | 0.0011           | 0.0028
	LSUN (crop)                         | 0                | 0.0028        | 0                | 0.0048
	LSUN (resize)                       | 0.0014           | 0.0028        | 0.0006           | 0.002
	iSUN                                | 0.0014           | 0.0028        | 0.0008           | 0.0028
	Uniform random noise                | 0.0014           | 0.0028        | 0.0014           | 0.0028
	Gaussian random noise               | 0.0014           |0.0028         | 0.0014           | 0.0028

* **args.temperature**: temperature is set to 1000 in all cases.
* **args.gpu**: make sure you use the following gpu when running the code:

	Neural Network Models |  args.gpu
	----------------------|----------
	densenet10            | 0
	densenet100           | 0
	wideresnet10          | 1
	wideresnet100         | 2

### Outputs
Here is an example of output.

```
Neural network architecture:          DenseNet-BC-100
In-distribution dataset:                     CIFAR-10
Out-of-distribution dataset:     Tiny-ImageNet (crop)

                          Baseline         Our Method
FPR at TPR 95%:              34.8%               4.3%
Detection error:              9.9%               4.6%
AUROC:                       95.3%              99.1%
AUPR In:                     96.4%              99.2%
AUPR Out:                    93.8%              99.1%
```

### License
Please refer to the [LICENSE](https://github.com/facebookresearch/odin/blob/master/LICENSE).
