from setuptools import setup,find_packages

setup(
    name="Openkst",

    version="0.0.1",

    author="imamts",

    author_email="zjutzzy@126.com",

    maintainer="imamts",

    maintainer_email="zjutzzy@126.com",

    license="MIT",

    description="通过BiLSTM-CRF的文本实体提取",

    platforms=["Windows", "Linux"],

    install_requires=[  'gensim==3.8.3',
                        'gensim==3.8.3',
                        'jieba==0.42.1',
                        'matplotlib==3.1.3',
                        'networkx==2.4',
                        'numpy==1.19.5',
                        'onnx==1.7.0',
                        'onnxruntime==1.10.0',
                        'paddle2onnx==0.5.1',
                        'paddlehub==2.1.0',
                        'paddlenlp==2.0.0rc18',
                        'paddlepaddle-gpu==2.0.2.post110',
                        'pgl==2.1.5',
                        'py2neo==2020.7b8',
                        'pyOpenSSL==19.1.0',
                        'ray==1.0.0',
                        'scikit-learn==0.24.0',
                        'scipy==1.3.1',
                        'tensorboard==1.14.0',
                        'tensorboard-plugin-wit==1.7.0',
                        'tensorflow==2.5.2',
                        'tensorflow-estimator==1.14.0',
                        'torch==1.7.1+cu110',
                        'torchvision==0.8.2+cu110',
                        'torchaudio==0.7.2',
                        'dgl==0.6.1',
                        'yacs==0.1.8',
                        'torch_geometric==2.0.4',
                        'pycocotools==2.0.4',
                        'sentencepiece==0.1.96',
                        'torch_cluster==1.5.8',
                        'torch_scatter==2.0.5',
                        'torch_sparse==0.6.8',
                        'torch-spline-conv==1.2.0',
                      ],

    python_requires='==3.7',

    packages=find_packages(),
)


