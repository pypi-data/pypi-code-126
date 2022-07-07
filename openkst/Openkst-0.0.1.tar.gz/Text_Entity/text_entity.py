# Copyright (c) 2021 OpenKS Authors, DCD Research Lab, Zhejiang University.
# All Rights Reserved.
def Trainrun(source_uris,args={
		'gpu': False,
		'word_dim': 32,
		'hidden_size': 512,
		'depth': 8,
		'mix_hidden_lr': 1e-3,
		'hidden_lr': 1e-3,
		'epoch': 300,
		'batch_size': 20,
		'model_dir': './ner_model'}
		,platform = 'Paddle',executor = 'KELearn',model = 'entity-extract'):
	from Text_Entity.openks.loaders import loader_config, SourceType, FileType, Loader
	from Text_Entity.openks.models import OpenKSModel

	''' 文本载入与MMD数据结构生成 '''
	# 载入参数配置与数据集载入
	loader_config.source_type = SourceType.LOCAL_FILE
	loader_config.file_type = FileType.OPENKS
	loader_config.source_uris = source_uris
	loader_config.data_name = 'my-data-set'
	loader = Loader(loader_config)
	dataset = loader.dataset
	dataset.info_display()

	''' 文本信息抽取模型训练 '''
	# 列出已加载模型
	OpenKSModel.list_modules()
	# 算法模型选择配置
	print("根据配置，使用 {} 框架，{} 执行器训练 {} 模型。".format(platform, executor, model))
	print("-----------------------------------------------")
	# 模型训练
	executor = OpenKSModel.get_module(platform, executor)
	text_ner = executor(dataset=dataset, model=OpenKSModel.get_module(platform, model), args=args)
	text_ner.run()
	print("-----------------------------------------------")
