

import logging
from conf.setting import current_date
from conf.setting import BaseDir


def get_logger(log_type):
    # 创建日志对象
    log_obj = logging.getLogger(log_type)

    # 设置日志水平
    log_obj.setLevel(logging.DEBUG)

    # 创建控制台句柄
    sh = logging.StreamHandler()

    # 创建文件句柄
    log_file = BaseDir + '/log/' + current_date() + '.log'
    fh = logging.FileHandler(log_file)


    # 创建格式对象
    log_format = logging.Formatter('%(asctime)s>%(name)s>%(levelname)s>%(message)s')

    # 设置句柄格式
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)

    # 添加句柄到日志对象
    log_obj.addHandler(sh)
    log_obj.addHandler(fh)

    # 返回日志对象
    return log_obj



if __name__ == "__main__":
    log = get_logger()
    log.info('test')
    log.info('test1')
    log.info('test2')
    log.info('test3')