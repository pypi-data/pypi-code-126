import json, os, sys
import fire

from .py_ext import json2dic, copy_dir
# 提取 gene的相对位置
# 提取 TF的 tfbs
# 提取 enhancer 的 交联 sites
# 构建 .ini 文件
# pyGenomeTrack

def get_gene_region(gene_name):
  try:
    gene_dic = json2dic('./') # 按照服务器路径
    return gene_dic[gene_name]
  except:
    return None

def get_specie_info(specie):
  # 输出 gtf, 调控文件 路径
  dic_specie_gtf = {
    'human': './data/a.gtf',
    'mouse': './data/b.gtf'
  }
  try:
    return dic_specie_gtf[specie]
  except:
    return None


def construct_genome_track_ini(specie, region, forward_bw, reverse_bw):
  gtf = get_specie_info[specie]
  if not gtf:
    print( 'Error, no specie', specie)
    os.sys.exit(0)
  copy_dir('./data/template.ini', './tmp.ini')
  with open( './tmp.ini', 'w') as f:
    f.replace('{gtf}', gtf)
    specie_title = gtf.split('/')[-1].replace('.gtf', '')
    f.replace('{specie_title}', specie_title )
    f.replace( '{forward_bw}', forward_bw )
    f.replace( '{reverse_bw}', reverse_bw )



def main():
  fire.Fire()

  region = get_gene_region()




